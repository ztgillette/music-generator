from key import *
from house import *
import random
import time

class House:

    def __init__(self, bpm=128, key="Amin", seed = -1):

        # the basics 
        self.bpm = bpm
        self.key = Key(key)
        self.number_of_tracks = 10
        self.sections = 64

        # track
        self.sub_count = 0
        self.bar_count = 0

        
        # data
        self.interface = []
        for i in range(self.number_of_tracks):
            section = [None] * 64
            self.interface.append(section)

        # to save song
        self.randomness_seed = seed
        if self.randomness_seed == -1:
            self.randomness_seed = random.randint(1, 10000)

    def play(self):

        print_out = False

        prev = time.time()

        while(True):

            if self.sub_count % 16 == 0 and print_out:
                print(str(self.bar_count + 1) + ":" + str(self.sub_count / 16 + 1))

            init_time = time.time()
            #### perform actions ####

            #########################
            final_time = time.time()

            time.sleep(max(0, (60 / self.bpm / self.sections * 4) - (final_time-init_time)))
            self.sub_count += 1

            if self.sub_count == 64:
                self.sub_count = 0
                self.bar_count += 1