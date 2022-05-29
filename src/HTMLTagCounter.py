#Ecenur Atıgan

from bs4 import BeautifulSoup as bs
import os 
import requests 
import json

domain = input("Please enter a domain name: ")

# HTML file from Domain 
html = requests.get(domain) 
	
# Parse HTML file 
soup = bs(html.content, 'html.parser') 

print("Number of HTML tags:")

# Calculate and print the tag count with json file format
tag_dict = {
	'a' : len(soup.find_all("a")),
	'script' : len(soup.find_all("script")),
	'div' : len(soup.find_all("div")),
	'img' : len(soup.find_all("img")),
	'br' : len(soup.find_all("br")),
	'p' : len(soup.find_all("p"))
}

tag_json = json.dumps(tag_dict)
print(tag_json)
