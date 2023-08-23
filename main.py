from detect import detect_text, new_screen
from requests import post, get
import datetime
import time
from logger import logger
from config import *


def check():
    headers = {
        "Authorization": AUTHORIZATION,
        "content-type": "application/json",
    }

    response = get("", headers=headers)
    print(response.text)
    old_value = float(response.text[51:56])
    print(old_value)
    return old_value


def run_api(value):
    headers = {
        "Authorization": AUTHORIZATION,
        "content-type": "application/json",
    }

    data = {"state": value}
    response = post(URL_SUM, headers=headers, json=data)
    logger.info("New value send Home Assistant", value)


while True:
    date_now = datetime.datetime.now().strftime("%H:%M:%S")
    # logger.info(date_now)

    if date_now == HOUR:
        logger.info("Now run detect value")
        new_text = False

        tries_number = 0
        while new_text is False:
            for _ in range(2): new_screen()
            new_text = detect_text('images/test2.png')

            if new_text == False:
                if tries_number < 3:
                    logger.error("photo is broken")
                    tries_number += 1
                else:
                    break
            else:
                for _ in range(2):
                    new_value = new_text / 10

                    old_value = check()

                    if new_value and new_value > old_value and new_value < old_value+3 :
                        logger.info("Checking complete")
                        run_api(new_value)
                        break
                    else:
                        logger.error("New value in HA is not available")

                    time.sleep(5)
