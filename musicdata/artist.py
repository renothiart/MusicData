'''artist.py'''

class Artist:
	'''A class representing a particular artist.'''

	def __init__(self, name, albums=[], songs=[]):
		'''Initializes an Artist instance with the given name and optional other attributes.'''
		self.name = name
		self.albums = albums
		self.songs = songs

	def add_song(self, song):
		self.songs.append(song)

	def add_album(self, album):
		self.albums.append(album)
