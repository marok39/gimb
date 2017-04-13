from pprint import PrettyPrinter
from itertools import zip_longest


def grouper(n, iterable):
    "Groups a list into a tuples of n elements"
    args = [iter(iterable)] * n
    return list(tuple([e for e in t if e != None]) for t in zip_longest(*args))


def ascii_code_to_string(l):
    "Changes list of ascii codes into a string of characters"
    return "".join([chr(i) for i in l])


def read_file(ppm_file):
    "Opens a PPM file and returns tuple with size of picture and list of pixel values"
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



def make_list():
    "Makes list of lists of pixels, each inner list is a row in original picture"
    f = input("What file do you want to open?")
    if not f.endswith(".ppm"):
        f += ".ppm"
    (width, height), data = read_file(f)
    width, height = int(width.strip("b'")), int(height.strip("b'").strip("\\\\n"))
    final_list = []
    print(width, height)

    data = grouper(3, data)

    for line in range(height):
        line_out = []
        current_line = data[line*width:(line+1)*width]
        for pixel in current_line:
            #print(pixel)
            line_out.append(Pixel(pixel))
        final_list.append(line_out)
    return final_list


def make_pic():
    "Joins iner lists with empty string, then joins lists together with newline - creates final picture"
    grayscale_pix = []
    pixels = make_list()
    for line in pixels:
        gray_line = []
        for pixel in line:
            gray_line.append(pixel.pix_gray())
        grayscale_pix.append(gray_line)
    for line in range(len(grayscale_pix)):
        grayscale_pix[line] = "".join(grayscale_pix[line])
    grayscale_pix = "\n".join(grayscale_pix)
    return grayscale_pix


def join_pixels(n, orig):
    ret_str = []
    for x in range(int(len(orig)/n)):
        large_pix = 


def main():
    with open("result.txt", "w") as f:
        f.write(str(make_pic()))


class Pixel:
    "Class with pixel values"
    def __init__(self, pixel):
        self.avg = sum(pixel)/3 #pixel value -> average value of Red, Green ansd Blue values


    def pix_gray(self):
        "Changes self.value to grayscale symbol"
        chars = (' ', '.', '\'', ':',  'o', '&', '8', '#', '@')
        grayscale = (230, 200, 180, 160, 130, 100, 70 , 50, 0)
        for index, gray_iter in enumerate(grayscale):
            if self.avg >= gray_iter:
                gray = chars[index]
                break
        return gray




if __name__ == "__main__":
    main()
