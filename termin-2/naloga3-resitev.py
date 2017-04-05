from itertools import zip_longest
from pprint import PrettyPrinter

class Pixel:
    """
    Resitev s pomocjo razreda Pixel
    """
    def __init__(self, data):
        self.r = data[0]
        self.g = data[1]
        self.b = data[2]


    def __str__(self):
        """
        Ce zelimo printati Pixel npr.
        p = Pixel((0, 0, 0))
        print(p) # izpis je enak (0,0,0)
        """
        return "(" + str(self.r) + "," + str(self.g) + "," + str(self.b) + ")"


    def __repr__(self):
        """
        Ce zelimo printati seznam Pixel npr:
        p = Pixel((0,0,0))
        l = [p, p, p]
        print(l) # izpis je [(0,0,0), (0,0,0), (0,0,0)]
        """
        return str(self)


    def sivina(self):
        """
        Vrne sivino enega piksla
        """
        return (self.r + self.g + self.b) / 3


    def sivina_to_ascii(self, sivina=None):
        if sivina is None:
            sivina = self.sivina()
        Z = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
        S = (230, 200, 180, 160, 130, 100, 70, 50, 0)
        for idx, el in enumerate(S):
            if sivina >= el:
                return Z[idx]
        return None


    @staticmethod
    def sivina_to_ascii_static(sivina):
        """
        Primer staticne funkcije, ni vezana na neko instanco Pixel
        """
        Z = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
        S = (230, 200, 180, 160, 130, 100, 70, 50, 0)
        for idx, el in enumerate(S):
            if sivina >= el:
                return Z[idx]
        return None


def grouper(n, iterable):
    """ 
    Iz seznama naredi seznam, v katerem so vsake 3 vrednosti en element seznama
    """
	args = [iter(iterable)] * n
	return list((tuple([e for e in t if e != None]) for t in zip_longest(*args)))

def ascii_code_to_string(l):
	return "".join([chr(i) for i in l])

def okno(pixels, i, j, n):
    sumR, sumG, sumB = 0, 0, 0
    for x in range(i, i+n):
        for y in range(j, j+n):
            sumR += pixels[x][y].r
            sumG += pixels[x][y].g
            sumB += pixels[x][y].b
    # 3*n**2: imamo n*n veliko okno, vsak element okna pa ima tri vrednosti (rgb)
    return (sumR + sumG + sumB) / (3 * (n * n))

def read_file(in_file):
    with open(in_file, "rb") as f:
        indata = f.readlines()

    dimension = ascii_code_to_string(indata[1]).split()

    byte_data = indata[3:]
    data = []
    for line in byte_data:
        for b in line:
            data.append(int(b)) # pretvori byte v nek int
    return dimension, data

def write_file(pixels, out_file, n):
    with open(out_file, "w") as f:
        for x in range(0, len(pixels), n): # len(pixels) = visina
            for y in range(0, len(pixels[0]), n): # len(pixels[0]) = sirina
                o = okno(pixels, x, y, n) # izracunaj sivino okna
                c = Pixel.sivina_to_ascii_static(o) # kateri znak pripada sivini?
                f.write("%s" % c) # zapisi znak v izhodno datoteko
            f.write("\n")

def main():
    in_file = input()
    out_file = input()
    n = int(input())

    dimension, data = read_file(in_file)
    
    # iz dimension = ("123", "456") naredi dve int spremenljivki
    width, height = int(dimension[0]), int(dimension[1])
    # vsake tri vrednosti barve daj v en tuple (piksel) -> vse piksle pa v seznam
    data = grouper(3, data)
    
    # iz data poberi vse piksle in napolni 2d seznam pixels z razredom Pixel
    # na pozicijah x, y
    pixels = []
    i = 0
    for x in range(height):
        pixel_line = []
        for y in range(width):
            new_pixel = Pixel(data[i])
            pixel_line.append(new_pixel)
            i += 1
        pixels.append(pixel_line)
    
    # zapisi piksle v datoteko
    write_file(pixels, out_file, n)

if __name__ == "__main__":
    main()
