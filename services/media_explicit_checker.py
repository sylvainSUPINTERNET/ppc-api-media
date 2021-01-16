import base64
import cv2
import numpy as np

def is_valid_media(b64_encoded):
    b64_buf = b64_encoded # to generate byte type of instead str type => b'hello'

    # Convert image as thermal image
    # convert image to RGB matrix
    nparr = np.frombuffer(b64_buf, dtype=int)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('TEST', img)

    cv2.waitKey()
    return "wip"