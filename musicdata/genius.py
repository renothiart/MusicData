import requests
import re
from song import Song
from bs4 import BeautifulSoup

request_types = ['artist', 'song', 'album', 'search_song', 'search_album', 'search_artist']

api_url = 'https://api.genius.com/'

session = requests.Session()
headers = {}
headers['User-Agent'] = 'MusicData'
headers['Authorization'] = 'Bearer {}'.format(access_token)
session.headers = headers

def make_api_request(endpoint, params=None):
	request_url = api_url + endpoint

	response = session.request('GET', request_url, params=params)

	# print(response.text)
	if(not response.ok):
		print("error")
		return {}
	else:
		return response.json()

def get_artist(id):
	endpoint = 'artists/{}'.format(id)
	params = {'text_format' : 'plain'}
	return make_api_request(endpoint, params=params)

def get_artist_songs(id, sort='title', per_page=10, page=1):
	endpoint = 'artists/{}/songs'.format(id)
	params = {'sort' : sort, 'per_page' : per_page, 'page' : page}

	songs = []
	json = make_api_request(endpoint, params=params)
	songs_json = json['response']['songs']
	for song in songs_json:
		songs.append(Song(title=song['title'], 
						  genius_pageviews=song['stats']['pageviews'],
						  genius_url=song['url'],
						  primary_artist=song['primary_artist']['name']))
	return songs

def get_song(id):
	endpoint = 'songs/{}'.format(id)
	params = {'text_format' : 'plain'}
	return make_api_request(endpoint, params=params)

def search(search_term):
	endpoint = 'search'
	params = {'q' : search_term}
	return make_api_request(endpoint, params=params)

def get_album():
	endpoint = 'albums/{}'.format(id)

def get_lyrics_from_url(url, plain=True, formatted=False):
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	
	lyrics_formatted = soup.find('div', class_='lyrics').get_text()
	lyrics = re.sub(r'\[.*\]', '', lyrics_formatted)
	lyrics = re.sub(r'\n{2,}', '\n', lyrics)
	
	return self.lyrics_formatted if formatted else self.lyrics
			else:
				print('ERROR: No url to retrieve lyrics from')

	if plain and formatted:
		return lyrics, lyrics_formatted
	else:
		return lyrics if plain else lyrics_formatted
