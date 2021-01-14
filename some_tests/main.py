import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


from test_pic_b64 import b64_encoded_pic, b64_encoded_pic_2

def is_valid_media(b64_encoded):
    b64_buf = b64_encoded # to generate byte type of instead str type => b'hello'

    # Convert image as thermal image
    # convert image to RGB matrix
    nparr = np.frombuffer(base64.b64decode(b64_buf), dtype=int)
    img = cv2.imdecode(nparr, cv2.COLOR_BGR2HSV)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #scale_percent = 100  # percent of original size
    #width = int(img.shape[1] * scale_percent / 100)
    #height = int(img.shape[0] * scale_percent / 100)

    width = 300
    height = 300
    dim = (width, height)

    # resize image 300 * 300
    resized_img = cv2.resize(gray_img, dim, interpolation=cv2.INTER_AREA)
    heatmap_img = cv2.applyColorMap(resized_img, cv2.COLORMAP_JET)


    # https://stackoverflow.com/questions/61979855/changing-colours-of-an-area-in-an-image-using-opencv-in-python

    #(A)RGB pixels are usually saved as intergers (32 bit).
    # Thereby, each channel is represented by 8 bit (giving you a range between 0 and 255).
    # The first 8 bits(32-24) of the number represent the alpha channel, the next 8 bit the red channel (24-16),
    # the next 8 bit the green channel (16-8) and the last 8 bit the blue channel.
    # So each number in the array actually represents the transparency (alpha) and the 3 intensity values of the respective color channels and thus can also be viewed as a vector. M-by-N-by3 describes a MxN matrix containing the vector (the integer) for each pixel to describe its color.


    # To understand
    # https://stackoverflow.com/questions/37060788/python-numpy-array-with-multiple-conditions-to-iterate-over-image

    print(heatmap_img.shape)
    #print(heatmap_img)
    #pprint(heatmap_img.tolist())
    pixels = 0

    # 2D height / width
    # channels color
    h, w, channels = heatmap_img.shape
    for x in range(0,h):
        for y in range(0, w):
            b,g,r = heatmap_img[x, y] # b, g, r
            print(f"RED : {r}")

            # Remove red too dark
            if heatmap_img[x, y][2] == 255 :
                heatmap_img[x, y][2] = 0

            #heatmap_img[x, y][0] = 0


    cv2.imshow('TEST', heatmap_img)

    cv2.waitKey()
    return "wip"

if __name__ == "__main__":
    # execute only if run as a script
    is_valid_media(b64_encoded=b64_encoded_pic_2)