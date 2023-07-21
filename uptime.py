import requests
import colorama

def check_uptime(url):
    api_url1 = f"https://caiditmemay.team-1479445.repl.co/addlink?link={url}"
    api_url2 = f"https://api-uptime.susmoere.repl.co/addlink?link={url}"

    response1 = requests.get(api_url1)
    response2 = requests.get(api_url2)

    if response1.status_code == 200:
        print("API 1 - Uptime check successful!")
        # Perform additional actions or display a banner related to API 1

    if response2.status_code == 200:
        print("API 2 - Uptime check successful!")
        # Perform additional actions or display a banner related to API 2

def print_banner():
    banner = '''
    
\x1b[31m██╗   \x1b[38;5;208m██╗\x1b[93m██████╗ \x1b[38;5;46m████████╗\x1b[36m██╗\x1b[38;5;91m███╗   \x1b[38;5;91m███╗\x1b[35m███████╗
\x1b[31m██║   \x1b[38;5;208m██║\x1b[93m██╔══██╗\x1b[38;5;46m╚══██╔══╝\x1b[36m██║\x1b[38;5;91m████╗ \x1b[38;5;91m████║\x1b[35m██╔════╝
\x1b[31m██║   \x1b[38;5;208m██║\x1b[93m██████╔╝   \x1b[38;5;46m██║   \x1b[36m██║\x1b[38;5;91m██╔██\x1b[38;5;91m██╔██║\x1b[35m█████╗  
\x1b[31m██║   \x1b[38;5;208m██║\x1b[93m██╔═══╝    \x1b[38;5;46m██║   \x1b[36m██║\x1b[38;5;91m██║╚█\x1b[38;5;91m█╔╝██║\x1b[35m██╔══╝  
\x1b[31m╚███\x1b[38;5;208m███╔╝\x1b[93m██║        \x1b[38;5;46m██║   \x1b[36m██║\x1b[38;5;91m██║ ╚\x1b[38;5;91m═╝ ██║\x1b[35m███████╗
 \x1b[31m╚══\x1b[38;5;208m═══╝ \x1b[93m╚═╝        \x1b[38;5;46m╚═╝   \x1b[36m╚═╝\x1b[38;5;91m╚═╝     \x1b[38;5;91m╚═╝\x1b[35m╚══════╝ \x1b[38;5;255m
                                                
                                                 
                                                 
                                                 
'''
    print(banner)

def main():
    print_banner()
    # Get user input for the URL to check
    url = input("> Enter the URL to check uptime: ")
    check_uptime(url)

main()