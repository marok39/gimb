from pprint import PrettyPrinter
from itertools import zip_longest
from math import ceil
import argparse


def grouper(n, iterable):
    "Group a list into a tuples of n elements"
    args = [iter(iterable)] * n
    return list(tuple([e for e in t if e != None]) for t in zip_longest(*args))


def ascii_code_to_string(l):
    "Change list of ascii codes into a string of characters"
    return "".join([chr(i) for i in l])


def read_file(ppm_file):
    "Open a PPM file and return tuple with size of picture and list of pixel values"
    with open(ppm_file, "rb") as f:
        indata = f.readlines()

    dimension = str(indata[1]).split(" ") # kje je dimenzija v indata?

    byte_data = indata[3:] # kje so podatki o pikslih v indata oz. od kje naprej?
    data = []
    for line in byte_data:
        for b in line:
            data.append(int(b))
    #print(data)
    return dimension, data


'''
def average_pixels():
    avg_pix = []
    f = input("What file do you want to open?")
    if not f.endswith(".ppm"):
        f += ".ppm"
    (width, height), data = read_file(f)
    width, height = int(width.strip("b'")), int(height.strip("b'"))
    print(width, height)
    for line in range(height):
        line_out = []
        current_line = data[line*width:(line+1)*width]
        for pixel in current_line:
            line_out.append(sum(pixel)/3)
        avg_pix.append(line_out)
    return avg_pix
'''


def make_list(filename, ratio):
    """
    Make list of lists of pixels, each inner list is a row in original picture.
    If ratio is specified, shrink the picture by it and return smaller one.
    """
    f = filename
    make_smaller = ratio
    if not f.endswith(".ppm"):
        f += ".ppm"
    (width, height), data = read_file(f)
    width, height = int(width.strip("b'")), int(height.strip("b'").strip("\\\\n"))
    final_list = []
    final_small = []
    print(width, height)

    data = grouper(3, data)

    for i, line in enumerate(range(height)):
        line_out = []
        current_line = data[line*width:(line+1)*width]
        for j, pixel in enumerate(current_line):
            #print(pixel)
            line_out.append(Pixel(pixel, (i, j)))
        final_list.append(line_out)

    if make_smaller:
        if len(make_smaller) == 1:
            ratio_x = int(make_smaller[0])
            ratio_y = ratio_x
        elif len(make_smaller) == 2:
            ratio_x = int(make_smaller[0])
            ratio_y = int(make_smaller[1])
        else:
            raise ZeroDivisionError("One or two argumets only!")
        for x in range(ceil(height/ratio_x)):
            small_line = []
            for y in range(ceil(width/ratio_y)):
                a = BigPixel()
                small_line.append(a)
            final_small.append(small_line)

        for line in final_list:
            for pixel in line:
                x, y = pixel.get_big_coord(ratio_x, ratio_y)
                final_small[x][y] += pixel

        return final_small

    return final_list


def make_pic(filename, ratio):
    "Join inner lists with empty string, then join lists together with newline - create final picture"
    grayscale_pix = []
    pixels = make_list(filename, ratio)
    for line in pixels:
        gray_line = []
        for pixel in line:
            gray_line.append(str(pixel))
        grayscale_pix.append(gray_line)
    for line in range(len(grayscale_pix)):
        grayscale_pix[line] = "".join(grayscale_pix[line])
    grayscale_pix = "\n".join(grayscale_pix)
    return grayscale_pix


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Which file to open", type=str)
    parser.add_argument("height", help="How many times do you want the picture to be shorter", type=int)
    parser.add_argument("width", help="How many times do you want the picture to be thinner", type=int)
    parser.add_argument("-o", "--output", help="In what file do you want to store your output", type=str, default="result")
    args = parser.parse_args()
    if not args.output.endswith(".txt"):
        args.output += ".txt"
    with open(args.output, "w") as f:
        f.write(str(make_pic(args.filename, (args.height, args.width))))


class Pixel:
    "Class with pixel values"
    def __init__(self, pixel, coords):
        self.gray = sum(pixel)/3 #pixel value -> average value of Red, Green and Blue values
        self.x, self.y = coords


    def pix_gray(self):
        "Changes self.value to grayscale symbol"
        chars = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
        grayscale = (230, 200, 180, 160, 130, 100, 70 , 50, 0)
        for index, gray_iter in enumerate(grayscale):
            if self.gray >= gray_iter:
                gray_char = chars[index]
                break
        return gray_char


    def get_big_coord(self, num_x, num_y): #num is amount of pixels to be grouped together.
        "Get coordinates of pixel in smaller picture to which this pixel will contribute its value."
        return (self.x//num_x, self.y//num_y)


    def __str__(self):
        return self.pix_gray()


class BigPixel(Pixel):
    "Class for small picture (multiple pixels joined into one)."
    def __init__(self):
        self.total = 0
        self.count = 0
        self.gray = 255

    def __iadd__(self, other):
        self.total += other.gray
        self.count += 1
        self.gray = self.total/self.count
        return self


if __name__ == "__main__":
    main()
