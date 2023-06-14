import os
import io
import cv2
from google.cloud import vision
from google.cloud import vision_v1
from google.cloud.vision_v1 import types


def new_screen():

    cap = cv2.VideoCapture('rtsp://') #

    ret, frame = cap.read()
    croop = frame[80:280, 150:330]

    cv2.imwrite("images/cc.png", croop)


def detect_text(path):
    """Detects text in the file."""

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './practical-robot-381309-1d818c812f41.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    print(int(texts[0].description))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: ' 'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return int(texts[0].description)



