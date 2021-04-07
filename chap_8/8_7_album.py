# def make_album(artist_name, album_title):
#     """Return a dictionary describing a music album"""
#     album = {'artist': artist_name, 'title': album_title}
#     return album

# album_info = make_album('pink floyd', 'the dark side of the moon')
# print (album_info)

# album_info = make_album('aimee mann', 'magnolia')
# print(album_info)

# album_info = make_album('alabama shakes', 'boys & girls')
# print(album_info)

def make_album(artist_name, album_title, number_songs = None):
    """Return a dictionary describing a music album"""
    if number_songs:
        album = {'artist': artist_name, 'title': album_title, 
        'songs': number_songs}
        return album
    else:
        album = {'artist': artist_name, 'title': album_title}
        return album

album_info = make_album('pink floyd', 'the division bell', 11)
print(album_info)

album_info = make_album('alabama shakes', 'boys & girls')
print(album_info)