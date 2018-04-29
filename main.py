from PIL import Image

width = 400
height = 300

picI = Image.open("images/I.png")
picE = Image.open("images/E.png")
picEP = Image.open("images/Eprime.png")
picK1 = Image.open("images/key1.png")
picK2 = Image.open("images/key2.png")

SEN = 1
epoch = 25
rate = 1e-8


def mseGD():
    nowEpoch = 1
    w = [0, 0, 0]
    while nowEpoch==1 or nowEpoch<epoch:
        print ("epoch: ", nowEpoch)
        for i in range(0, 400):
            for j in range(0, 300):
                a = w[0] * picK1.getpixel((i, j)) + \
                    w[1] * picK2.getpixel((i, j)) + \
                    w[2] * picI.getpixel((i, j))
                error = (picE.getpixel((i, j)) - a)
                w[0] += rate * error * picK1.getpixel((i, j))
                w[1] += rate * error * picK2.getpixel((i, j))
                w[2] += rate * error * picE.getpixel((i, j))

        nowEpoch += 1
        print ("error: ", error)

    return w

print (mseGD())
