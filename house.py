from key import *
from house import *
import random
import time
import pygame

class House:

    def __init__(self, bpm=128, key="Amin", seed = -1):

        # the basics 
        self.bpm = bpm
        self.key = Key(key)
        self.number_of_tracks = 1
        self.sections = 64
        self.bar_chunks = 4

        # sounds
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        
        # Load sound
        self.choose_sounds()

        # track
        self.sub_count = 0
        self.bar_count = 0

        
        # data
        self.track_names = ["kicks", "hats", "claps"]
        self.interface = {}
        for track_name in self.track_names:

            subsection = [None] * self.sections
            section = [subsection] * self.bar_chunks
            self.interface[track_name] = (section)

        # to save song
        self.randomness_seed = seed
        if self.randomness_seed == -1:
            self.randomness_seed = random.randint(1, 10000)

    def choose_sounds(self):
        
        #choose kicks
        kick_num = random.randint(1,4)
        file_name1 = "sounds/drums/kicks/" + str(kick_num) + ".wav"
        self.kick1 = pygame.mixer.Sound(file_name1)

        #choose hats
        hat_num = random.randint(1,3)
        file_name2 = "sounds/drums/hats/" + str(hat_num) + ".wav"
        self.hat1 = pygame.mixer.Sound(file_name2)

        #choose claps
        clap_num = random.randint(1,3)
        file_name3 = "sounds/drums/claps/" + str(hat_num) + ".wav"
        self.clap1 = pygame.mixer.Sound(file_name3)



    def generate_bars(self):
        
        #drums
        for bar in range(self.bar_chunks):

            for section in range(self.sections):

                if(section % 16 == 0):

                    self.interface["kicks"][bar][section] = "p"

                if((section+8)%16 == 0):

                    self.interface["hats"][bar][section] = "p"

                if((section+16)%32==0):

                    self.interface["claps"][bar][section] = "p"

    def play(self):

        print_out = False
        clock = pygame.time.Clock()

        while(True):

            if self.sub_count % 16 == 0 and print_out:
                print(str(self.bar_count + 1) + ":" + str(self.sub_count / 16 + 1))

            init_time = time.time()
            #### perform actions ####
    

            if(self.interface["kicks"][self.bar_count][self.sub_count] == "p"):
                self.kick1.play()

            if(self.interface["hats"][self.bar_count][self.sub_count] == "p"):
                self.hat1.play()

            if(self.interface["claps"][self.bar_count][self.sub_count] == "p"):
                self.clap1.play()
     
            #########################
            final_time = time.time()

            clock.tick(self.bpm / self.sections * 16)
            self.sub_count += 1

            if self.sub_count == 64:
                self.sub_count = 0
                self.bar_count += 1