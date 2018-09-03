from genius import get_lyrics_from_url

'''song.py'''

class Song:
	'''A class representing a particular song.'''

	def __init__(self, 
			title=None, 
			album=None,
			featured_artists=None,
			genius_id=None,
			genius_pageviews=-1,
			genius_url=None,
			primary_artist=None):
		self.title = title
		self.album = album
		self.featured_artists = featured_artists
		self.genius_id = genius_id
		self.genius_pageviews = genius_pageviews
		self.genius_url = genius_url
		self.primary_artist = primary_artist
		self.lyrics = None
		self.lyrics_formatted = None

	def get_lyrics(self, formatted=False):
		if(self.lyrics is not None):
			if(formatted):
				return self.lyrics
			else:
				return self.lyrics_formatted
		else:
			if(self.genius_url is not None):
				lyrics = get_lyrics_from_url(self.genius_url, plain=True, formatted=True)
				self.lyrics, self.lyrics_formatted = get_lyrics_from_url(
					self.genius_url, plain=True, formatted=True)
			else:
				print('ERROR: No Genius url to retrieve lyrics from')

	def set_artist(self, artist):
		self.artist = artist

	def add_feature(self, feature):
		self.features.append(feature)

	def add_features(self, features):
		self.features.extend(features)
