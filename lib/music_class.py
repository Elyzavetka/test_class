class Music():
    def __init__(self):
        self.list_track = []

    def show_songs(self):
        return self.list_track

    def add(self, song):
        return self.list_track.append(song)