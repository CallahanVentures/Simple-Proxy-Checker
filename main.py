import requests
from bs4 import BeautifulSoup
import json
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import concurrent.futures
import csv

# Define params for random_user_agent.get_user_agent
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]       
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# Get list of user agents.
user_agents = user_agent_rotator.get_user_agents()

def get_proxy_data(ip):
    url = f"https://scamalytics.com/ip/{ip.split(':')[0]}"
    user_agent = user_agent_rotator.get_random_user_agent()
    header = {'User-Agent': user_agent,
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 
              'Accept-Language': 'en-US,en;q=0.5', 
              'Accept-Encoding': 'gzip, deflate, br', 
              'Referer': 'https://scamalytics.com/', 
              'Connection': 'keep-alive', 
              'Upgrade-Insecure-Requests': '1',
              'Sec-Fetch-Dest': 'document',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-Site': 'same-origin',
              'Sec-Fetch-User': '?1'}
    resp = requests.get(url, headers=header)

    soup = BeautifulSoup(resp.text, 'html.parser')

    pre = soup.find('pre')
    table = soup.find('table')
    
    pre_text = pre.text.strip()
    basic_data = json.loads(pre_text)
    basic_data = {key.capitalize(): value.title() for key, value in basic_data.items()}
    full_data = {}

    for row in table.find_all('tr'):
        th_element = row.find('th')
        td_element = row.find('td')
    
        if th_element and td_element:
            header = th_element.get_text(strip=True)
            value = td_element.get_text(strip=True)
            full_data[header] = value

    proxy_data = {**basic_data, **full_data}
    return proxy_data

proxies = [ip.strip() for ip in open("proxies.txt", "r")]

output_data_json_list = []

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(get_proxy_data, proxies)
    output_data_json_list.extend(results)

print(f"Finished Checking {len(output_data_json_list)} Proxies...\n\n\n")

# Write the data to a CSV file
csv_file = "proxy_data.csv"
csv_columns = [
    "Ip", "Score", "Risk", "Hostname", "ASN", "ISP Name", "Organization Name",
    "Connection type", "Country Name", "Country Code", "Region", "City",
    "Postal Code", "Metro Code", "Area Code", "Latitude", "Longitude",
    "Anonymizing VPN", "Tor Exit Node", "Server", "Public Proxy", "Web Proxy",
    "Search Engine Robot"
]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in output_data_json_list:
            writer.writerow(data)
except IOError:
    print("I/O error")

print(f"Data has been written to {csv_file}")