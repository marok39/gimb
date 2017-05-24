from collections import Counter
from itertools import combinations
import os

from unidecode import unidecode
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import numpy as np


def walk(s, k=2):
    for i in range(len(s) - (k - 1)):
        yield s[i:i+k]


def language_distance(l1, l2):
    """ Cosine distance between languages. """
    intersection = set(l1.keys()).intersection(l2.keys())
    dist = sum([l1[i] * l2[i] for i in intersection])
    l1_length = np.sqrt(sum([x**2 for x in l1.values()]))
    l2_length = np.sqrt(sum([x**2 for x in l2.values()]))

    cos = dist / (l1_length * l2_length)
    return 1 - cos


def language_similarity(path, print_pair=False):
    """ Return distances between all languages for clustering. """
    languages = []
    texts = []
    distances = []

    for filename in os.listdir(path):
        full_path = path + filename
        with open(full_path, "r", encoding="utf-8") as f:
            languages.append(filename.split(".")[0])

            data = f.read().replace("\n", " ").replace("  ", " ")
            data = unidecode(data).lower()
            text = Counter(walk(data))

            texts.append(text)

    for l in combinations(range(len(languages)), 2):
        dist = language_distance(texts[l[0]], texts[l[1]])
        distances.append(dist)
        if (print_pair):
            print(languages[l[0]] + " : " + languages[l[1]] + " = ", dist)

    return languages, distances


def plot_dendrogram(ids, data):
    """ Plot dendrogram with given data. """
    Z = hierarchy.linkage(data, method="average")
    hierarchy.dendrogram(Z, orientation="right", labels=ids)
    plt.title("Language similarity")
    plt.xlabel("Cosine Distance")
    plt.ylabel("Language")
    plt.show()


def main():
    ids, data = language_similarity("./human_rights/")
    plot_dendrogram(ids, data)

if __name__ == "__main__":
    main()
