from house import *

def main():
    h = House()
    t = h.key

    print(t.numeric)
    print(t.letter)
    print(t.maj)
    print(t.min)

    print(t.letter_scale)
    print(t.numeric_scale)

if __name__ == "__main__":
    main()
