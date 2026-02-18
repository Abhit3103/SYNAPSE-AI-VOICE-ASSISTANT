class MusicLibrary:
    def __init__(self, file_path="songs.txt"):
        self.songs = []          # list of (name, link)
        self.index = -1          # current position
        self.load(file_path)

    def load(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "|" in line:
                    name, link = line.strip().split("|", 1)
                    self.songs.append((name.lower(), link))

    def play_by_name(self, name):
        name = name.lower()
        for i, (song_name, link) in enumerate(self.songs):
            if song_name in name:

                self.index = i
                return link
        return None

    def next(self):
        if not self.songs:
            return None
        if self.index < len(self.songs) - 1:
            self.index += 1
        return self.songs[self.index][1]

    def previous(self):
        if not self.songs:
            return None
        if self.index > 0:
            self.index -= 1
        return self.songs[self.index][1]
