import csv
import spotipy

james_token  = '... redacted and expired ...'
rachel_token = '... redacted and expired ...'

james  = spotipy.Spotify(auth=james_token)
rachel = spotipy.Spotify(auth=rachel_token)

# print('James',  james.current_user())
# print('Rachel', rachel.current_user())

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])

# number = 3
#
# for x in [james, rachel, number]:
#   print(x, type(x))
#   print(x.current_user())
#   print('')

spotify = james

recent = spotify.current_user_top_tracks(limit=50)

song_ids = []
for item in recent['items']:
  song_ids.append(item['id'])

audio_info = spotify.audio_features(song_ids)

# import pdb; pdb.set_trace() - start interactive session on a line
# type(object) - what kind of thing is object?
# dir(object) - what methods does this object have?
# Ctrl-D - exit interactive session

# x = { 'a': 1, 'b': 2 } - dictionary
# x['a'] - get key
# x['b'] = 5 - set key
# x.keys() - list all keys

# for index in range(0, 50):
#   item = recent['items'][index]
#   print(item['name'])

# for item in recent['items']:
#   print(item['id'])
#   print(item['name'])
#   print(item['album']['name'])
#   print(item['artists'][0]['name'])
#   print('')

# with open('test.csv', 'w') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['a','b,extra','c'])
#   writer.writerow([1,2,3])
#   writer.writerow([4,5,'a,b,c'])

# import pdb; pdb.set_trace()

audio_lookup = {} # keys = ids => values = danceability
for info in audio_info:
  key = info['id']
  audio_lookup[key] = info

with open('songs.csv', 'w') as songfile:
  writer = csv.writer(songfile)
  writer.writerow([
    'ID',
    'Name',
    'Album',
    'Artist',
    'Danceability',
    'Energy',
    'Key',
    'Loudness'
  ])

  for item in recent['items']:
    item_id = item['id']
    info = audio_lookup[item_id]

    writer.writerow([
      item_id,
      item['name'],
      item['album']['name'],
      item['artists'][0]['name'],
      info['danceability'],
      info['energy'],
      info['key'],
      info['loudness']
    ])
