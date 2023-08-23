import re
import requests
from bs4 import BeautifulSoup

def get_website_info(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        social_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if re.match(r'^https?://(www\.)?(facebook|linkedin)\.com', href):
                social_links.append(href)
        
        email = None
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        email_match = re.search(email_pattern, response.text)
        if email_match:
            email = email_match.group()
        
        contact = None
        contact_pattern = r'(\+\d{1,3}\s)?\d{3}\s\d{3}\s\d{4}'
        contact_match = re.search(contact_pattern, response.text)
        if contact_match:
            contact = contact_match.group()
        
        return social_links, email, contact
    
    else:
        print("Failed to retrieve website content.")
        return None, None, None

# User input
website_url = input("Enter the website URL: ")

social_links, email, contact = get_website_info(website_url)

if social_links:
    print("Social links:")
    for link in social_links:
        print(link)

if email:
    print("Email:", email)

if contact:
    print("Contact:", contact)
