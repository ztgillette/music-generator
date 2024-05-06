from house import *
from chord import *

def main():
    
    h = House()
    h.generate_bars()
    #print(h.interface)
    h.play()

if __name__ == "__main__":
    main()
