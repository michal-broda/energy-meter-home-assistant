import os
import io
import cv2
from google.cloud import vision
from config import *
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from logger import logger
import time


def new_screen():
    # cap = cv2.VideoCapture(0) #default camera
    cap = cv2.VideoCapture(RTSP_CONN)  # IP Camera
    ret, frame = cap.read()
    cv2.imwrite("images/test1.png", frame)
    croop = frame[630:810, 360:980]  # [start_row:end_row, start_col:end_col]
    rotate = cv2.rotate(croop, cv2.ROTATE_180)

    cv2.imwrite("images/test2.png", rotate)


def detect_text(path):
    """Detects text in the file."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './practical-robot-381309-8ef5504be52d.json'
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    text_detection_params = vision.TextDetectionParams(enable_text_detection_confidence_score=True)
    image_context = vision.ImageContext(text_detection_params=text_detection_params)
    response = client.text_detection(image=image, image_context=image_context)
    print("ressss", response)

    texts = response.text_annotations

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    words = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Words: {} (confidence: {})'.format(
                        words, word.confidence))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    # print(texts[0].description)
    if response and word.confidence > 0.80:
        return float(texts[0].description)
    else:
        logger.error("Confidence is not high")
        return False


