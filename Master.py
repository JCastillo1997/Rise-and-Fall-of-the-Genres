def create_playlist_dataframe(playlist_id):
    import pandas as pd
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials


    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8aaea3fe61404b23aa07c9f760df3985",
                                                           client_secret="e6670aad9bc94f1ba66f382abe39394c"))

    client_credentials_manager = SpotifyClientCredentials(client_id="8aaea3fe61404b23aa07c9f760df3985", client_secret="e6670aad9bc94f1ba66f382abe39394c")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


    playlist = sp.playlist(playlist_id)


  
    data = {
        'cancion':[],
        'cantante': [],
        'año': [],
        'duracion_minutos': [],
        'album': [],
        'explicito': [],
    }

    for track in playlist['tracks']['items']:
        data['cancion'].append(track['track']['name'])
        data['cantante'].append(track['track']['artists'][0]['name'])
        data['año'].append(track['track']['album']['release_date'][:4])
        data['duracion_minutos'].append(track['track']['duration_ms'] / 60000)
        data['album'].append(track['track']['album']['name'])
        data['explicito'].append(track['track']['explicit'])

    df = pd.DataFrame(data)
    return df