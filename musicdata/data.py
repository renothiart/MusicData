
class Data:

	def __init__():
		self.artists = {}
		self.artists['unmatched'] = []

	def add_artist(self, artist):
		if artist not in artists:
			self.artists.put(artist, artist.songs)
			return True
		return False

	def add_song(self, song):
		if song.primary_artist in artists:
