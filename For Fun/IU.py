import requests
from bs4 import BeautifulSoup

# send an HTTP request to the album page
url = 'https://kprofiles.com/iu-discography/'
response = requests.get(url).text

# create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response, 'lxml')

# find the album name tag and extract its text
album_name = soup.find('div', {'class':'entry-content herald-entry-content'})

print(soup.prettify())
