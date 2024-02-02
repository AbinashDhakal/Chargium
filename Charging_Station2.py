# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:14:41 2024

@author: abudh
"""

import requests
from bs4 import BeautifulSoup
import re

# URL of the website containing charging station information
url = 'https://example.com/charging_stations'

https://openchargemap.org/site/poi
# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Define regular expressions
address_pattern = re.compile(r"(.*?)\n(.*?)\n(.*?)\n(.*?)\n.*?Level (\d+).*?(\w+ \(\w+ \d+kW\)).*?(\w+ \(Type \d\))", re.DOTALL | re.MULTILINE)

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find relevant text containing charging station information
text_content = soup.get_text()

# Find matches
matches = re.findall(address_pattern, text_content)

# List to store charging stations
charging_stations_list = []

# Process matches and append to the list
for match in matches:
    title = match[0].strip().title()  # Convert to title case
    address = f"{match[1]}, {match[2]}, {match[3]}"
    
    # Search for postcode within the specific match
    postcode_match = re.search(r"\b([A-Z0-9]+ \d[A-Z0-9]*)\b", match[4])
    postcode = postcode_match.group() if postcode_match else None
    
    level = match[5]
    connection_type = match[6]
    
    # Create a dictionary for each charging station
    charging_station_dict = {
        "Title": title,
        "Address": address,
        "Postcode": postcode,
        "Level": level,
        "Connection Type": connection_type
    }
    
    # Append the dictionary to the list
    charging_stations_list.append(charging_station_dict)

# Display the list
for station in charging_stations_list:
    print(station)
    print("\n")
