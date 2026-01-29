class Track:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
    
    def matches(self, keystring):
        keystring = keystring.lower()
        return keystring in self.artist.lower() or keystring in self.title.lower()