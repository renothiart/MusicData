
class Album(object):
	"""Represents the data for an album, mixtape, EP, etc."""

	def __init__(self, name, artist=None, songs=[]):
		self.name = name
		self.artist = artist
		self.songs = songs

	def set_artist(self, artist):
		self.artist = artist

	def add_song(self, song):
		self.songs.append(song)

	def add_songs(self, songs)
		self.songs.extend(songs)
