from key import *

class Chord:

    def __init__(self, key, type="triad", inversion=0):

        self.key = key
        self.numeric_scale = key.numeric_scale
        self.inversion = inversion
        self.type = type
        self.numeric_notes = []
        self.get_chord()

    def get_letter_notes(self):
        toret = []
        for i in range(len(self.numeric_notes)):
            toret.append(self.key.numeric_conversion[self.numeric_notes[i]])

        return toret

    def get_chord(self):
        pos = self.get_notes()
        self.notes = []

        for p in pos:
            self.numeric_notes.append(self.numeric_scale[p-1])

        #invert
        for i in range(self.inversion):
            rem = self.numeric_notes.pop(0)
            self.numeric_notes.append(rem)

    def get_notes(self):

        #chord types
        if self.type == "triad":
            return [1, 3, 5]
        
        elif self.type == "15":
            return [1, 5]
        
        elif self.type == "37":
            return [3, 7]
        
        elif self.type == "7thtriad":
            return [3, 5, 7]
        
        elif self.type == "note":
            return [1]