# BuffaloNAS-Scanner
Scan shodan for open Buffalo NAS devices and identify accessible folders

#Features  
  - Scans for open Buffalo NAS devices via Shodan
  - Extracts folder names from each NAS device 
  - Filters out empty NAS devices
    
  Saves results to:  
   - `hits.txt` → NAS devices with useful folders  
   - `no_hits.txt` → NAS devices with no useful content  
   - `output.html` → Clickable links for NAS devices  

#Requirements  
  Before running the script, ensure you have:
    - Python 3 installed
    - Requirements.txt installed
    - A Shodan account with an API key  
      - Shodan CLI initialized using:  
          shodan init YOUR_API_KEY
