import artist
import bs4
import re
import requests
import song

api_url = 'https://api.genius.com/'
access_token = 'T1YF5Byobkda1VFZxn7NJLtU74e89wGnQyopOpX-vfcVCy6QplLfGvEqi86eC_Cw'

class GeniusConnection(object):
	"""Handles the HTTP connection to the Genius API and JSON parsing.
	"""

	def __init__(self):
		self.session = requests.Session()
		headers = {}
		headers['User-Agent'] = 'MusicData'
		headers['Authorization'] = 'Bearer {}'.format(access_token)
		self.session.headers = headers

	# API CALLS

	def make_api_request(self, endpoint, params=None):
		"""Retrieves the HTTP response from a given Genius API endpoint.

		Args:
			endpoint: the API endpoint at which to direct the request.
			params: a dict of parameters for the request.

		Returns:
			A dictionary containing the JSON contents of the API response,
			or None if there was an error.
		"""
		request_url = api_url + endpoint
		response = self.session.request('GET', request_url, params=params)

		if(not response.ok):
			print("error")
			return None
		else:
			return response.json()['response']

	def get_song_json(self, id):
		"""Calls make_api_request() with the endpoint for a given song.

		Args:
			id: the desired song's Genius ID.

		Returns:
			A dict containing the song's JSON data. 
		"""
		endpoint = 'songs/{}'.format(id)
		params = {'text_format' : 'plain'}
		return self.make_api_request(endpoint, params=params)['song']

	def get_artist_json(self, id):
		"""Calls make_api_request() with the endpoint for a given artist.

		Args:
			id: the desired artist's Genius ID.

		Returns:
			A dict containing the artist's JSON data. 
		"""
		endpoint = 'artists/{}'.format(id)
		params = {'text_format' : 'plain'}
		return self.make_api_request(endpoint, params=params)['artist']

	def get_artist_songs_json(self, id, sort='title', per_page=10, page=1):
		"""Calls make_api_request() with the endpoint for a given artist's songs.

		Args:
			id: the desired artist's Genius ID.
			sort: the sorting method for songs by the given artist ('title' or 'popularity')
			per_page: the number of songs to load for a 'page'
			page: the page to start loading songs from (first page is 1)

		Returns:
			A dict containing a list of individual songs' JSON data. 
		"""
		endpoint = 'artists/{}/songs'.format(id)
		params = {'sort' : sort, 'per_page' : per_page, 'page' : page}
		return self.make_api_request(endpoint, params=params)['songs']

	def search_json(self, search_term):
		"""Calls make_api_request() with the endpoint for a given search term.

		Args:
			search_term: the queried term

		Returns:
			A list of dicts containing the JSON query results.
		"""
		endpoint = 'search/'
		params = {'q' : search_term}
		return self.make_api_request(endpoint, params=params)['hits']

	# URL SCRAPING

	def get_lyrics_from_url(self, url, plain=True, formatted=False):
		"""Uses BeautifulSoup to scrape lyrics from a given url.

		Args:
			url: 
			plain: 
			formatted:

		Returns:
			If plain is true, a string representing the text of the lyrics at the given URL.
			If formatted is true, tags and section separating new lines are preserved in
			the returned string (eg. [Produced by Metro Boomin], [Chorus] or [Bridge]).
			If both plain and formatted are true, a tuple is returned containing both strings.
		"""
		page = requests.get(url)
		soup = bs4.BeautifulSoup(page.text, 'html.parser')
		
		lyrics_formatted = soup.find('div', class_='lyrics').get_text()
		lyrics = re.sub(r'\[.*\]', '', lyrics_formatted)
		lyrics = re.sub(r'\n{2,}', '\n', lyrics)

		if plain and formatted:
			return lyrics, lyrics_formatted
		else:
			return lyrics if plain else lyrics_formatted

	def get_artist_id_from_url(self, url):
		"""Uses BeautifulSoup to scrape an artist's id from a given url.

		Args:
			url: the url from which to scrape the artist id

		Returns:
			A string representing the artist id 
		"""
		page = requests.get(url)
		soup = bs4.BeautifulSoup(page.text, 'html.parser')
		
		# retrieves artist id from the html
		artist_attr = soup.find('meta', attrs={'name':'newrelic-resource-path'}).get('content')
		artist_id = re.sub('/artists/', '', artist_attr)
		return artist_id

	def get_song_id_from_url(self, url):
		"""Uses BeautifulSoup to scrape a song's id from a given url.

		Args:
			url: the url from which to scrape the song id

		Returns:
			A string representing song id
		"""
		page = requests.get(url)
		soup = bs4.BeautifulSoup(page.text, 'html.parser')
		
		# retrieves song id from the html
		song_attr = soup.find('meta', attrs={'name':'newrelic-resource-path'}).get('content')
		song_id = re.sub('/songs/', '', song_attr)
		return song_id

	# JSON PARSING

	def song_from_genius_json(self, json):
		return song.Song(title=json['title'],
					genius_id=json['id'],
					genius_pageviews=json['stats']['pageviews'],
					genius_url=json['url'],
					primary_artist=json['primary_artist']['name'])

	def artist_from_genius_json(self, json):
		return artist.Artist(name=json['name'],
					  alternate_names=json['alternate_names'],
					  genius_id=json['id'],
					  genius_url=json['url'],
					  genius_image_url=json['image_url'],
					  genius_follower_count=json['followers_count'])
