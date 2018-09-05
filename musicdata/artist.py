
class Artist(object):
	"""Represents the data for a singer, musician or band."""

	def __init__(self,
				 albums=[],
				 alternate_names=None,
				 genius_follower_count=None,
				 genius_id=None,
				 genius_image_url=None,
				 genius_url=None,
				 name=None,
				 songs=[]):
		"""Initializes an Artist instance with the given name and optional other attributes."""
		
		self.albums = albums
		self.alternate_names = alternate_names
		self.genius_follower_count = genius_follower_count
		self.genius_id = genius_id
		self.genius_image_url = genius_image_url
		self.genius_url = genius_url
		self.name = name
		self.songs = songs

	def add_song(self, song):
		self.songs.append(song)

	def add_album(self, album):
		self.albums.append(album)
