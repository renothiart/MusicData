'''song.py'''

class Song:
	'''A class representing a particular song.'''

	def __init__(self, 
			title, 
			album=None,
			featured_artists=None,
			genius_url=None,
			genius_id=None,
			primary_artist=None):
		self.title = title
		self.album = album
		self.featured_artists = featured_artists,
		self.genius_url = genius_url
		self.genius_id = genius_id
		self.primary_artist = primary_artist

	def set_artist(self, artist):
		self.artist = artist

	def add_feature(self, feature):
		self.features.append(feature)

	def add_features(self, features):
		self.features.extend(features)
