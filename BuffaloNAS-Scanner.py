import subprocess
import requests
import json

def get_nas_folders(ip, port):
    """Fetch the folder structure from Buffalo NAS using its RPC API."""
    url = f"http://{ip}:{port}/rpc/ls/?_dc=1742363552467"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for request errors
        folders = response.json()
        
        # Extract folder names (excluding "." and "..")
        folder_list = [folder['name'] for folder in folders if folder['name'] not in [".", ".."]]

        # Ignore NAS with only ".webaxs"
        if folder_list == [".webaxs"]:
            return None  # Treat as a non-hit

        return folder_list if folder_list else None  # Return folders or None if empty

    except requests.exceptions.RequestException:
        return None  # Return None if request fails

def generate_html(hits):
    """Generate an HTML file with clickable links for hits."""
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buffalo NAS Hits</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f4f4f4; }
        h2 { color: #333; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .nas-link { margin: 10px 0; padding: 10px; border-bottom: 1px solid #ddd; }
        a { text-decoration: none; color: #007bff; font-weight: bold; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Buffalo NAS Hits</h2>
        <p>Click a link below to access a Buffalo NAS device:</p>
"""

    for entry in hits:
        ip_port, folders = entry.split(" - ", 1)
        html_content += f'<div class="nas-link"><a href="http://{ip_port}/ui#/" target="_blank">{ip_port}</a> - Folders: {folders}</div>\n'

    html_content += """
    </div>
</body>
</html>
"""

    with open("output.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

def main():
    # Prompt for country code
    country_code = input("Enter a two-letter country code (e.g., 'HK' for Hong Kong): ").upper()

    # Shodan search query
    query = f'Redirecting sencha port:9000 country:"{country_code}"'

    # Run Shodan CLI
    shodan_cmd = ["shodan", "search", "--fields", "ip_str,port", "--limit", "10", query]
    result = subprocess.run(shodan_cmd, capture_output=True, text=True)

    # Check for errors
    if result.returncode != 0:
        print(f"Shodan CLI error: {result.stderr}")
        return

    # Parse raw output
    lines = result.stdout.strip().split("\n")
    accessible_ips = []
    no_accessible_ips = []

    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            ip, port = parts
            
            # Fetch NAS folder structure
            folders = get_nas_folders(ip, port)

            if folders:
                print(f"✅ {ip}:{port} - Valid Folders: {folders}")
                accessible_ips.append(f"{ip}:{port} - {folders}")
            else:
                print(f"❌ {ip}:{port} - No useful folders")
                no_accessible_ips.append(f"{ip}:{port}")

    # Save results to files (UTF-8 encoding for special characters)
    with open('hits.txt', 'w', encoding="utf-8") as hits_file:
        for entry in accessible_ips:
            hits_file.write(f'{entry}\n')

    with open('no_hits.txt', 'w', encoding="utf-8") as no_hits_file:
        for entry in no_accessible_ips:
            no_hits_file.write(f'{entry}\n')

    # Generate HTML output
    generate_html(accessible_ips)

    print(f"\nResults saved to 'hits.txt', 'no_hits.txt', and 'output.html'.")

if __name__ == '__main__':
    main()
