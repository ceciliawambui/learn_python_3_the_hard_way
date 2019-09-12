class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So i'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With POckets full of shells"])

blessed_soul = Song(["Bless my soul",
                     "oh my Lord",
                     "ooh my soul"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

blessed_soul.sing_me_a_song()
