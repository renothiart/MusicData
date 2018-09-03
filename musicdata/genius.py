import requests
import json
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
	return make_api_request(endpoint, params=params)

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

