class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keystring):
        res = []
        for track in self.tracks:
            if track.matches(keystring):
                res.append(track)
        return res