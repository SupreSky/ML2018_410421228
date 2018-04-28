from PIL import Image

width = 400
height = 300

picI = Image.open("images/I.png")
picE = Image.open("images/E.png")
picEP = Image.open("images/Eprime.png")
picK1 = Image.open("images/k1.png")
picK2 = Image.open("images/k2.png")

SEN = 1
epoch = 1
rate = 1e-6
w = [1e9, 1e9, 1e9]

def mseGD():
    nowEpoch = 1
    wNow = [1, 1, 1]
    while nowEpoch==1 or nowEpoch<epoch &&:
        for i in range(0, 400):
            for j in range(0, 300):
                a = w[0] * picK1.getpixel((i, j)) +
                    w[1] * picK2.getpixel((i, j)) +
                    w[2] * picI.getpixel((i, j))
                error = (picE.getpixel((i, j)) - a)
