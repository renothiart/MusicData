# MusicData
Python package allowing easy access to music data from major music websites.

## Classes
One of the central features of MusicData is the capability to collect and collate data from multiple major sources. There are several classes that MusicData uses to encapsulate retrieved information, namely Artist, Song and Album. Both Artist and Song handle core data from Genius. Album is currently unused due to limitations of the Genius API.

## Genius
MusicData is fully integrated with the Genius.com API. Look up your favorite artists, songs and lyrics easily and programatically. Songs and artists can be retrieved both by Genius ID (get_song_from_id(), get_artist_from_id(), get_artist_songs_from_id()) and by title/artist name (get_song(), get_artist(), get_artist_songs()). You can also use Genius' search functionality to search for songs (search_songs()). Most importantly, lyrics can be retrieved through the get_lyrics_from_song() and the get_lyrics_from_artist() methods.

## Spotify
API integration in progress. Coming soon.