class Key:

    def __init__(self, key="Amin"):

        self.valid_keys = {
            "Amaj" : 9, "Bmaj" : 11, "Cmaj" : 0, "Dmaj" : 2, "Emaj" : 4, "Fmaj" : 5, "Gmaj" : 7,
            "A#maj" : 10, "B#maj" : 0, "C#maj" : 1, "D#maj" : 3, "E#maj" : 5, "F#maj" : 6, "G#maj" : 8,
            "Abmaj" : 8, "Bbmaj" : 10, "Cbmaj" : 11, "Dbmaj" : 1, "Ebmaj" : 3, "Fbmaj" : 4, "Gbmaj" : 6,

            "Amin" : 0, "Bmin" : 2, "Cmin" : 3, "Dmin" : 5, "Emin" : 7, "Fmin" : 8, "Gmin" : 10,
            "A#min" : 1, "B#min" : 3, "C#min" : 4, "D#min" : 6, "E#min" : 8, "F#min" : 9, "G#min" : 11,
            "Abmin" : 11, "Bbmin" : 1, "Cbmin" : 2, "Dbmin" : 4, "Ebmin" : 6, "Fbmin" : 7, "Gbmin" : 9,
        }

        self.numeric_conversion = {
            0 : "C",
            1 : "C# / Db",
            2 : "D",
            3 : "D# / Eb",
            4 : "E",
            5 : "F",
            6 : "F# / Gb",
            7 : "G",
            8 : "G# / Ab",
            9 : "A",
            10 : "A# / Bb",
            11 : "B"
        }


        if key in self.valid_keys.keys():
            self.key = key
            self.numeric = self.valid_keys[key]

            self.maj = False
            self.min = False
            self.letter = ""

            self.set_major_minor()
            if self.min:
                self.numeric = (self.numeric + 9) % 12
            self.set_letter()

            self.set_scale()
        else:
            print("Error: Invalid Key. (1)")
            return

    def set_major_minor(self):

        if self.key[-3:] == "maj":
            self.maj = True
            self.min = False
        elif self.key[-3:] == "min":
            self.min = True
            self.maj = False
        else:
            print("Error: Invalid key. (2)")

    def set_letter(self):

        self.letter = self.key[:-3]

    def equals(self, key2):
        return self.numeric == key2.numeric and self.maj == key2.maj
    
    def relative(self, key2):
        return self.numeric == key2.numeric and self.maj != key2.maj

    def set_scale(self):

        if self.maj:
            self.numeric_scale = [self.numeric, self.numeric + 2, self.numeric + 4, self.numeric + 5, self.numeric + 7, self.numeric + 9, self.numeric + 11]
        else:
            self.numeric_scale = [self.numeric, self.numeric + 2, self.numeric + 3, self.numeric + 5, self.numeric + 7, self.numeric + 9, self.numeric + 10]

        self.letter_scale = []

        for i in range(len(self.numeric_scale)):
            self.numeric_scale[i] %= 12
            self.letter_scale.append(self.numeric_conversion[self.numeric_scale[i]])



    def test(self):

        k1 = Key("Cmaj")
        print(k1.key == "Cmaj" and k1.numeric == 0 and k1.maj is True and k1.min is False and k1.letter == 'C')  # True

        k2 = Key("Amin")
        print(k2.key == "Amin" and k2.numeric == 0 and k2.maj is False and k2.min is True and k2.letter == 'A')  # True

        k3 = Key("F#maj")
        print(k3.key == "F#maj" and k3.numeric == 6 and k3.maj is True and k3.min is False and k3.letter == 'F#')  # True

        k4 = Key("Ebmin")
        print(k4.key == "Ebmin" and k4.numeric == 6 and k4.maj is False and k4.min is True and k4.letter == 'Eb')  # True

        # Test enharmonic equivalents that should be true
        k5 = Key("B#maj")
        k6 = Key("Cmaj")
        print(k5.equals(k6))  # True

        k7 = Key("Cbmaj")
        k8 = Key("Bmaj")
        print(k7.equals(k8))  # True

        k9 = Key("G#min")
        k10 = Key("Abmin")
        print(k9.equals(k10))  # True

        # Test same numeric values with different major/minor status
        k11 = Key("Cmaj")
        k12 = Key("Amin")
        print(not k11.equals(k12))  # True

        # Additional checks
        k13 = Key("Fmaj")
        print(k13.key == "Fmaj" and k13.numeric == 5 and k13.maj is True and k13.letter == 'F')  # True

        k14 = Key("D#min")
        k15 = Key("Emin")
        print(not k14.equals(k15))  # True, these are not enharmonic equivalents


    

                

