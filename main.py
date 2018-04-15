from PIL import Image

width = 400
height = 300

picI = Image.open("images/I.png")
picE = Image.open("images/E.png")
picEP = Image.open("images/EP.png")
picK1 = Image.open("images/k1.png")
picK2 = Image.open("images/k2.png")

SEN = 1
epoch = 1
rate = 0.00001

def mseGD():
    nowEpoch = 1
    wNow = [1, 1, 1]
    while nowEpoch==1 || nowEpoch<epoch &&:
        for k in (width * height):
            
