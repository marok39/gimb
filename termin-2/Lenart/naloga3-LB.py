from pprint import PrettyPrinter
from itertools import zip_longest


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return (tuple([e for e in t if e != None]) for t in zip_longest(*args))


def ascii_code_to_string(l):
    return "".join([chr(i) for i in l])


def read_file(ppm_file):
    with open(ppm_file, "rb") as f:
        indata = f.readlines()
        outdata = []
        for line in indata:
            outdata.append(line)

    pp = PrettyPrinter(indent=2)
    for i in outdata[:3]:
        print(ascii_code_to_string(i), end="") # podatki o sliki, nas zanima samo dimenzija

    out = list(grouper(3, outdata[3]))
    #pp.pprint(out) # (r,g,b) vseh pikslev
    #print(out)
    return outdata[1], outdata[2], out

def average_pixels():
    avg_pix = []
    width, height, data = read_file(input("What file do you want to open?"))
    for line in range(height):
        line_out = []
        current_line = data[line*width:(line+1)*width]
        for pixel in current_line:
            line_out.append(sum(pixel)/3)
        avg_pix.append(line_out)
    return avg_pix


def pix_to_grayscale():
    chars = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
    grayscale = (230, 200, 180, 160, 130, 100, 70 , 50)
    grayscale_pix = []
    pixels = average_pixels()
    for line in pixels:
        gray_line = []
        for pixel in line:
            for index, gray_iter in enumerate(grayscale):
                if pixel >= gray_iter:
                    gray_line.append(chars[index])
        grayscale_pix.append(gray_line)
    for line in len(grayscale_pix):
        grayscale_pix[line] = "".join(grayscale_pix[line])
    "\n".join(grayscale_pix)
    return grayscale_pix


def main():
    print(pix_to_grayscale())


if __name__ == "__main__":
    main()
