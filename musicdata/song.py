
class Song(object):
	"""Represents the data for a song."""

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

