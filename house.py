from key import *

class House:

    def __init__(self, bpm=128, key="Amin"):

        # the basics 
        self.bpm = bpm
        self.key = Key(key)