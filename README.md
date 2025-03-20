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



## Support & Donations  

If you find this tool useful and would like to support me, consider donating:  

- **PayPal**: [https://www.paypal.me/RonaldsServices]
- **Bitcoin (BTC)**: bc1qpdnu3mcl96g8puru982ndq3kyft7f9srjnx3mt  

Your support is greatly appreciated!



## Examples

![image](https://github.com/user-attachments/assets/893a7502-8f84-4f90-9ec7-c69124cc9ebd)

![image](https://github.com/user-attachments/assets/2ca0f884-5a30-4a50-982b-c61b38e5feb2)



