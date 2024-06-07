# Proxy Data Scraper

This simple script scrapes proxy data from Scamalytics and stores the results in a CSV file. It uses multiple threads for faster processing and random user agents to avoid being blocked by the target site.

## Features

- Scrapes detailed proxy information from Scamalytics
- Uses random user agents to avoid detection
- Multithreaded for faster processing
- Stores results in a CSV file

## Requirements

Ensure you have the following Python libraries installed:

- `requests`
- `beautifulsoup4`
- `random_user_agent`

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 random_user_agent
```

# Usage

- Place your list of proxies in a file named proxies.txt in the same directory as the script.
- Run the script.

```sh
<python path variable> main.py
```
