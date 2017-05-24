from collections import defaultdict

def walk(s, k=2):
    for i in range(len(s) - (k - 1)):
        yield s[i:i+k]

def rel_freq(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read() # preberi besedilo, dodaj se pravilne replace() in lower()
        text = defaultdict(int)
        # TODO

def main():
    print(list(walk("tralalalahopsasa")))

if __name__ == "__main__":
    main()
