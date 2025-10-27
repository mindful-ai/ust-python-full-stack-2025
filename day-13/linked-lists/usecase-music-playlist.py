class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None
        self.prev = None


class MusicPlaylist:
    def __init__(self):
        self.current = None

    def add_song(self, title):
        """Add a song at the end of the playlist."""
        new_song = SongNode(title)

        if self.current is None:
            self.current = new_song
            return

        # Find last song
        last = self.current
        while last.next:
            last = last.next
        last.next = new_song
        new_song.prev = last

    def play_next(self):
        """Move to the next song."""
        if self.current and self.current.next:
            print(f"▶ Now playing: {self.current.title}")
            self.current = self.current.next
        else:
            print("🚫 End of playlist.")

    def play_previous(self):
        """Move to the previous song."""
        if self.current and self.current.prev:
            print(f"▶ Now playing: {self.current.title}")
            self.current = self.current.prev
        else:
            print("🚫 Start of playlist.")

    def show_playlist(self):
        """Show all songs in playlist."""
        temp = self.current
        # Move to start
        while temp and temp.prev:
            temp = temp.prev

        print("🎵 Playlist:")
        while temp:
            print("   -", temp.title)
            temp = temp.next


if __name__ == "__main__":

    playlist = MusicPlaylist()

    playlist.add_song("Shape of You")
    playlist.add_song("Believer")
    playlist.add_song("Perfect")

    playlist.show_playlist()

    print("\n▶ Starting playback...")

    playlist.play_next()
    playlist.play_next()
    playlist.play_previous()
    playlist.play_next()
    playlist.play_next()