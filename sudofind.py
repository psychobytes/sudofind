banner = """Simple Subdomain Finder & Port Scanner
________      _________     ______________       _________
__  ___/___  _______  /________  ____/__(_)____________  /
_____ \_  / / /  __  /_  __ \_  /_   __  /__  __ \  __  / 
____/ // /_/ // /_/ / / /_/ /  __/   _  / _  / / / /_/ /  
/____/ \__,_/ \__,_/  \____//_/      /_/  /_/ /_/\__,_/   
                                                          """
print(banner)

import requests
import socket

domain = str(input("input domain name : "))
ip_add = socket.gethostbyname(domain)
print('IP Address : ', ip_add)

while True :
    run = (input("run port scanning using nmap ? y/n : "))
    if run == "y" or run == "n" :
        if run == "y" :
            print("scanning open port using nmap...")
            import nmap
            scanner = nmap.PortScanner()
            begin = 1
            end = 500
            for i in range(begin,end+1):
                res = scanner.scan(ip_add,str(i))
                res = res['scan'][ip_add]['tcp'][i]['state']
                print(f'port {i} is {res}.')

        else :
            print("scanning subdomain...")
            file = open("subdomain1.txt")
            content = file.read()
            subdomains = content.splitlines()
            
            for subdomain in subdomains:
                # construct the url
                url = f"https://{subdomain}.{domain}"
                try:
                    # if this raises an ERROR, that means the subdomain does not exist
                    r=requests.get(url)
                except requests.ConnectionError:
                    # if the subdomain does not exist, just pass, print nothing
                    pass
                except requests.ReadTimeout:
                    print ("Timeout occurred")
                else:
                    print("[+]", r.status_code, "Discovered subdomain:", url)

    else :
        print ("wrong input.")