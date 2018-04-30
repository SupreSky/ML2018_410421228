from PIL import Image
import random

width = 400
height = 300

picI = Image.open("images/I.png")
picE = Image.open("images/E.png")
picEP = Image.open("images/Eprime.png")
picK1 = Image.open("images/key1.png")
picK2 = Image.open("images/key2.png")

output = Image.new("L", (width, height), 0)

epoch = 10
rate = 1e-7

def mseGD():
    nowEpoch = 1
    w = [random.random(), random.random(), random.random()]
    while nowEpoch==1 or nowEpoch<=epoch:

        for i in range(0, width):
            for j in range(0, height):
                a = w[0] * picK1.getpixel((i, j)) + \
                    w[1] * picK2.getpixel((i, j)) + \
                    w[2] * picI.getpixel((i, j))
                error = (picE.getpixel((i, j)) - a)
                w[0] += rate * error * picK1.getpixel((i, j))
                w[1] += rate * error * picK2.getpixel((i, j))
                w[2] += rate * error * picE.getpixel((i, j))
        print ("Epoch ", nowEpoch, "/", epoch, "\terror: ", error, "\tW: ", w)
        nowEpoch += 1

    return w

wFound = mseGD()

for i in range(0, width):
    for j in range(0, height):
        output.putpixel((i, j), int(round((picEP.getpixel((i, j))-wFound[0]*picK1.getpixel((i, j))-wFound[1]*picK2.getpixel((i, j)))/wFound[2])))

output.save("de-Eprime.png")
