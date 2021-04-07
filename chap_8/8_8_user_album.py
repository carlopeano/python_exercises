# Write a while loop that allows users to enter an album's artist and title

def make_album(artist_name, album_title):
    """Return info about an album"""
    album = {'artist': artist_name, 'title': album_title}
    return album

while True:
    print("\nPlease, tell me what is your favorite album")
    print("(Type 'q' if you want to quit)")

    a_name = input("\nWho is the artist? ")
    if a_name == 'q':
        break

    a_title = input("\nWhat is the album? ")
    if a_title == 'q':
        break

    album_info = make_album(a_name, a_title)
    print(album_info)