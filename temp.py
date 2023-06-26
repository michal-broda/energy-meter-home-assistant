"""from requests import get, post

url = "http://192.168.12.110:8079/api/states/input_number.tempv"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhN2NjNzJjY2VhNzc0ZTFiODMzNWU1OTdlZTJhYWI3YiIsImlhdCI6MTY4NjYwMTcxMCwiZXhwIjoyMDAxOTYxNzEwfQ.lQ6SZOpIFcNKki6rYIUgsQQK98e0boDOILI6qvBbqMA",
    "content-type": "application/json",
}

response = get(url, headers=headers)

print(response.text)
"""
import time

"""from requests import post

url = "http://192.168.12.110:8079/api/states/input_number.tempv"
headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhN2NjNzJjY2VhNzc0ZTFiODMzNWU1OTdlZTJhYWI3YiIsImlhdCI6MTY4NjYwMTcxMCwiZXhwIjoyMDAxOTYxNzEwfQ.lQ6SZOpIFcNKki6rYIUgsQQK98e0boDOILI6qvBbqMA",
    "content-type": "application/json",
}
x = "14"
data = {"state": x, "attributes": {"unit_of_measurement": "°C"}}

response = post(url, headers=headers, json=data)
print(response.text)"""

"""
import datetime



while True:
    x = datetime.datetime.now()
    y = x.strftime("%H:%M:%S")
    print(y)

    if y == '12:44:21':
        print("jest")
        time.sleep(5)"""

"""import cv2


# cap = cv2.VideoCapture(0) #default camera
cap = cv2.VideoCapture('rtsp://admin:astrum18@192.168.12.111:554')  # IP Camera


ret, frame = cap.read()
croop = frame[80:280, 150:330]
# [start_row:end_row, start_col:end_col]
# frame = cv2.resize(frame, (960, 540))
cv2.imwrite("GefdeksFfdorGeeks.png", frame)

raise Exception(
    '{}\nFor more info on error messages, check: ' 'https://cloud.google.com/apis/design/errors'.format(
        response.error.message))


BASE_URL = "http://192.168.12.110:8079/api/states/input_number.tempv"
AUTHORIZATION = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhN2NjNzJjY2VhNzc0ZTFiODMzNWU1OTdlZTJhYWI3Y" \
                "iIsImlhdCI6MTY4NjYwMTcxMCwiZXhwIjoyMDAxOTYxNzEwfQ.lQ6SZOpIFcNKki6rYIUgsQQK98e0boDOILI6qvBbqMA"
HOUR = "07:00:00"
RTSP_CONN = "rtsp://admin:astrum18@192.168.12.103:554"""



import cv2

# RTSP info -- change these 4 values according to your RTSP URL
username = 'USERNAME'
password = 'PASSWORD'
endpoint = 'ENDPOINT'
ip = 'IPADDRESS'

# Stream
stream = cv2.VideoCapture(f'rtsp://192.168.12.57:8554/mjpeg/1')

try:
    while True:
        # Read the input live stream
        ret, frame = stream.read()
        height, width, layers = frame.shape
        frame = cv2.resize(frame, (width // 2, height // 2))

        # Show video frame
        cv2.imshow("Wyze v2 camera", frame)

        # Quit when 'x' is pressed
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
except Exception as e:
    print("ERROR:", e)

# Main function
if __name__ == "__main__":
    # Release and close stream
    stream.release()
    cv2.destroyAllWindows()