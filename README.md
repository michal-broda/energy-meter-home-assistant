# energy-meter-home-assistant

Script converting photo to integer by googleVisionAPI. Saves the value in Home Assistant. Thus, I have a consumption energy graph.

1. Once a day take photo with ESP32
2. Extract only number
   
![Screenshot from 2023-08-03 23-00-00](https://github.com/michal-broda/energy-meter-home-assistant/assets/95285280/79fe12ec-4358-4cdb-980b-5aece9b4777f)

4. By Google Vision API, save number as integer
5. Send value to HomeAssistant with API
6. Enjoy the beautiful energy consumption graph
   
![Zrzut ekranu 2023-08-23 171934](https://github.com/michal-broda/energy-meter-home-assistant/assets/95285280/d352a95d-adb1-4404-8205-fe49f9a2b834)
