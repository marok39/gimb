from collections import defaultdict

def walk(s, k=2):
    for i in range(len(s) - (k - 1)):
        yield s[i:i+k]

def rel_freq(path):
    with open(path, "r", encoding="utf-8") as f:
        data = f.read().replace("\n", " ").replace("  ", " ").lower()

        text = defaultdict(int)
        for key in walk(data):
            text[key] += 1

        s = sum(text.values())
        for key, value in text.items():
            text[key] = value/s

        text = sorted(text.items(), key=lambda v: (v[1], v[0]), reverse=True)

        for key, value in text:
            print(key, value)

def main():
    rel_freq(input())

if __name__ == "__main__":
    main()
