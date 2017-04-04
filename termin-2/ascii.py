from pprint import PrettyPrinter
from itertools import zip_longest

def grouper(n, iterable):
	args = [iter(iterable)] * n
	return (tuple([e for e in t if e != None]) for t in zip_longest(*args))

def ascii_code_to_string(l):
	return "".join([chr(i) for i in l])

with open("ChessBoard.ppm", "rb") as f:
	indata = f.readlines()
	outdata = []
	for line in indata:
		outdata.append(line)
		
pp = PrettyPrinter(indent=2)
for i in outdata[:3]: 
	print(ascii_code_to_string(i), end="") # podatki o sliki, nas zanima samo dimenzija

out = list(grouper(3, outdata[3]))
pp.pprint(out) # (r,g,b) vseh pikslev
#print(out)