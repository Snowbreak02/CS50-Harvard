import requests
from bs4 import BeautifulSoup

# send an HTTP request to the album page
url = 'https://www.melon.com/album/detail.htm?albumId=10827816'
response = requests.get(url).text

# create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(response, 'lxml')
"""
# find the album name tag and extract its text
album_name = soup.find('div', class_= 'service_list_song d_song_list').text.strip()
"""
print(soup.prettify())
