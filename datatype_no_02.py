#binary type data byte

Numbers = [12, 13, 14, 15, 16, 17, 18, 19, 20]

bytes(Numbers)
b = bytes(Numbers)

#byte change kora jai na

print(type(b))

#binary type data bytearray

Allnumbers = [12, 13, 14, 15, 16, 17, 18,36, 37, 38, 39]

b1 = bytearray(Allnumbers)

#bytearray change kora jai 

b1[1] = 200

print(b1[1])