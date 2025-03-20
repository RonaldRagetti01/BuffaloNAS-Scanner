# BuffaloNAS-Scanner  
Scan Shodan for open Buffalo NAS devices and identify accessible folders.  

## Features  

- Scans for open Buffalo NAS devices via Shodan  
- Extracts folder names from each NAS device  
- Filters out empty NAS devices  
- Saves results to:  
  - `hits.txt` → NAS devices with useful folders  
  - `no_hits.txt` → NAS devices with no useful content  
  - `output.html` → Clickable links for NAS devices  

## Requirements  

Before running the script, ensure you have:  

- Python 3 installed  
- Dependencies installed (`requirements.txt`):  
  ```sh
  pip install -r requirements.txt
  ```
- A Shodan account with an API key  
- Shodan CLI initialized using:  
  ```sh
  shodan init YOUR_API_KEY
  ```  

## Usage  

```sh
git clone https://github.com/RonaldRagetti01/BuffaloNAS-Scanner
cd BuffaloNAS-Scanner
python BuffaloNAS-Scanner.py
```

To change the Shodan search limit (set to **10** by default), modify the following line in `script.py`:  
```python
["shodan", "search", "--fields", "ip_str,port", "--limit", "10", query]
```
## Disclaimer  

**This tool is for research purposes only.** Unauthorized access to systems without permission may be illegal. **Use responsibly.**  
