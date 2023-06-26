import os
import io
import cv2
from google.cloud import vision
from config import *
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
from logger import logger


def new_screen():
    # cap = cv2.VideoCapture(0) #default camera
    cap = cv2.VideoCapture(RTSP_CONN)  # IP Camera

    ret, frame = cap.read()
    cv2.imwrite("images/capture.png", frame)
    croop = frame[620:709, 685:935] # [start_row:end_row, start_col:end_col]
    rotate = cv2.rotate(croop, cv2.ROTATE_180)

    cv2.imwrite("images/capturee.png", rotate)



new_screen()

def detect_text(path):
    """Detects text in the file."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './practical-robot-381309-1d818c812f41.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    logger.info(int(texts[0].description))

    if response.error.message:
        logger.error("")
        if response.error.message:
            raise Exception(logger.error(
                "For more info on error messages, check: ' 'https://cloud.google.com/apis/design/errors'".format(
                    response.error.message)))

    return int(texts[0].description)

detect_text("images/capturee.png")