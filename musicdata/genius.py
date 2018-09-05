import artist
import geniusconnection
import song
import re

class Genius(object):

	def __init__(self):
		self.gc = geniusconnection.GeniusConnection()

	# RETRIEVAL FROM ID

	def get_song_from_id(self, id):
		"""Retrieves song info and returns a Song instance from the data."""
		return self.gc.song_from_genius_json(self.gc.get_song_json(id))

	def get_artist_from_id(self, id):
		"""Retrieves artist info and returns an Artist instance from the data."""
		return self.gc.artist_from_genius_json(self.gc.get_artist_json(id))

	def get_artist_songs_from_id(self, id):
		"""Retrieves an artist's song info and returns a list of Song instances from the data."""
		songs_json = self.gc.get_artist_songs_json(id)
		songs = []
		for s in songs_json:
			songs.append(self.gc.song_from_genius_json(s))
		return songs

	# LYRIC RETRIEVAL

	def get_lyrics_from_song(self, song, plain=True, formatted=False):
		if(song.lyrics is None and song.genius_url is not None):
			song.lyrics, song.lyrics_formatted = self.gc.get_lyrics_from_url(
				song.genius_url, plain=True, formatted=True)
		if plain and formatted:
			return song.lyrics, song.lyrics_formatted
		else:
			return song.lyrics if plain else song.lyrics_formatted

	def get_lyrics_from_artist(self, artist, plain=True, formatted=False):
		lyrics = []
		for s in artist.songs:
			lyrics.append(self.get_lyrics_from_song(s, plain, formatted))
		return lyrics

	# ID RETRIEVAL

	def get_artist_id(self, name):
		name = re.sub(' ', '-', name.strip())
		return self.gc.get_artist_id_from_url('http://genius.com/artists/{}'.format(name))

	def get_song_id(self, title, name):
		full_title = re.sub(' ', '-', '{}-{}-lyrics'.format(name.strip(), title.strip()))
		return self.gc.get_song_id_from_url('http://genius.com/{}'.format(full_title))

	# RETRIEVAL FROM NAME

	def get_song(self, title, artist_name):
		song_id = self.get_song_id(title, artist_name)
		json = self.gc.get_song_json(song_id)
		return self.gc.song_from_genius_json(json)

	def get_artist(self, artist_name, num_songs=0):
		artist_id = self.get_artist_id(artist_name)
		json = self.gc.get_artist_json(artist_id)
		a = self.gc.artist_from_genius_json(json)

		if(num_songs > 0):
			songs = self.gc.get_artist_songs_json(artist_id, sort='popularity', per_page=num_songs)
			for s in songs:
				a.add_song(self.gc.song_from_genius_json(s))
		return a

	def get_artist_songs(self, artist_name, num_songs=5):
		"""Fetches and returns a list of the desired artist's top songs."""
		artist_id = self.get_artist_id(artist_name)
		json = self.gc.get_artist_songs_json(artist_id, sort='popularity', per_page=num_songs)

		songs = []
		for s in json:
			songs.append(self.gc.song_from_genius_json(s))
		return songs

	def search_songs(self, song_title, artist_name=None, num_songs=1):
		if(artist_name):
			json = self.gc.search_json('{} {}'.format(song_title, artist_name))
		else:
			json = self.gc.search_json(song_title)

		i = 0
		songs = []
		while i < num_songs and i < len(json):
			songs.append(self.gc.song_from_genius_json(json[i]['result']))
			i += 1
		return songs if num_songs > 1 else songs[0]

	############################################################

def example():
	g = Genius()
	print('Getting "Lil Yachty"...')
	yachty = g.get_artist('lil yachty', num_songs=4)
	print('Artist found! Another name is {}.'.format(yachty.alternate_names[0]))
	g.get_lyrics_from_artist(yachty)
	print('Lyrics received.')
	for s in yachty.songs:
		print('Song: {}'.format(s.title))
		print(s.lyrics)
	print('Getting "Family Feud" by "Lil Wayne"...')
	family_feud = g.get_song('Family Feud', 'Lil Wayne')
	print('Retrieved {} by {}.'.format(family_feud.title, family_feud.primary_artist))
	print('Searching for Family Feud by Lil Wayne...')
	ff = g.search_songs('Family Feud', artist_name='Lil Wayne')
	print('Found {} by {}.'.format(ff.title, ff.primary_artist))
	print(g.get_lyrics_from_song(ff))
example()