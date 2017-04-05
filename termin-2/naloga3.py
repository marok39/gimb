from itertools import zip_longest

def grouper(n, iterable):
	args = [iter(iterable)] * n
	return list((tuple([e for e in t if e != None]) for t in zip_longest(*args)))

def ascii_code_to_string(l):
	return "".join([chr(i) for i in l])

def read_file(in_file):
    with open(in_file, "rb") as f:
        indata = f.readlines()

    dimension = ("0", "0") # kje je dimenzija v indata?

    byte_data = ("0", "0") # kje so podatki o pikslih v indata oz. od kje naprej?
    data = []
    for line in byte_data:
        for b in line:
            data.append(int(b))
    return dimension, data

def main():
    """
    Ascii art
    """
    pass
    
    
if __name__ == "__main__":
    main()
