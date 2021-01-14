import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt

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

    cv2.imshow('TEST', heatmap_img)

    cv2.waitKey()
    return "wip"

if __name__ == "__main__":
    # execute only if run as a script
    is_valid_media(b64_encoded=b64_encoded_pic)