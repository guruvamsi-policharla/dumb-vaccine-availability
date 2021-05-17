import requests
import json
import time
from playsound import playsound
import datetime

browser_header = {'User-Agent': 'browser'}

flag = False
i = 0
while(True):
    DIST_LIST=[294] #Add districts here.
    today = datetime.date.today()
    #INP_DATE=today.strftime("%d-%m-%Y")
    INP_DATE="17-05-2021" #Change query date here. API request checks for next 7 days.

    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_LIST[i], INP_DATE)

    try:
        response = requests.get(URL, headers=browser_header)
        app = json.loads(response.text)
    except:
        print("http GET request error")
    for centers in app["centers"]:
        for sessions in centers["sessions"]:
            if (sessions["available_capacity"] > 0) and (sessions["min_age_limit"]==18) and (sessions["available_capacity_dose1"] > 0): #Change filters here.
                print("Hospital:{}, Appointments:{}, Age:{}, date:{}, vaccine:{}, pincode:{}, dose1:{}, dose2:{}".format(centers["name"],sessions["available_capacity"],sessions["min_age_limit"],sessions["date"],sessions["vaccine"],centers["pincode"],sessions["available_capacity_dose1"],sessions["available_capacity_dose2"]))
                flag = True

    if(flag == True):
        playsound('alarm.wav')

    print("--------",datetime.datetime.now().time(),"--------",INP_DATE,"--------",DIST_LIST[i],"--------")
    time.sleep(3.1)
    flag = False
    i=(i+1)%len(DIST_LIST)
            

#Example reuqest to see JSON formatting in browser
#http://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=15-05-2021
