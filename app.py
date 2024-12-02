import streamlit as st
from apscheduler.schedulers.background import BackgroundScheduler
import http.client
import json
from datetime import datetime, timedelta
import time

# Function to run daily at midnight
def scheduled_task():
    tm = 0
    while tm < 30:
        conn = http.client.HTTPSConnection("id.gettactic.com")
        payload = '__RequestVerificationToken=CfDJ8LUl0kpA_aJHpAUnUR4ngFKX6lCeBjwVUAOs1kN6VcQLKCCkgeCv_j6HJkKEAYGrhnguryjLQmqP-GFxc41OBbLYeaffVPwo0s25lGYebyIYnszBTBLaVtl48nWW_MmtXd0xOwV8X8OFvVtDYUo9zUI&clientId=tactic_web&slug=www&returnUrl=%2Fconnect%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dtactic_web%26redirect_uri%3Dhttps%253A%252F%252Funion.gettactic.com%252Fauth%252Fcallback%26scope%3Dopenid%2520api%2520offline_access%26state%3D8Ag5beWzTQQIp91Ppvud5hjH%252FrXAk5K0b84XDbfDJHs%253D%26code_challenge_method%3DS256%26code_challenge%3DljQvKHWX_LP9BPNRqB1t0MQWVSGGWOGQ0FvQmhVtxD0%26slug%3Dwww&hint=&email=darko.bundoski%40rldatix.com'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '.AspNetCore.Antiforgery.pWFFJwzms74=CfDJ8LUl0kpA_aJHpAUnUR4ngFKXoxOxclm7SiCQ3iJm3ZsgWfwtTSL2o5vhjfUbnZqaTu69dzXG1jITk-Rg2xAJvuAC-2iwl2E7VMYMQNEWU9Wss62tE0S41Thx6QzOtNkk64A4w8AyD7hOPO5PybWFgKc; union_auth=WaSlnqTpzafZN_ewmYxmZLq2bqTf8mLDu-c6Xt3AizE; intercom-id-vvac201d=50f858c9-6cf3-41d6-aa5d-b272255d9dbb; intercom-device-id-vvac201d=3465aaa7-3b9d-4f5c-858b-891e3e5858fc; _ga=GA1.1.785056214.1730710666; _gcl_au=1.1.1009297620.1730710666; _hjSession_3887589=eyJpZCI6IjY0Y2FkMTBmLTBiYTctNGViYS1hZjk2LWNmYWRkNzQ1NjNiNyIsImMiOjE3MzA3MTA2NjY3MTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __hstc=29959136.5b0f1c613e9f8c6c62843c985792e108.1730710667306.1730710667306.1730710667306.1; hubspotutk=5b0f1c613e9f8c6c62843c985792e108; __hssrc=1; _hjSessionUser_3887589=eyJpZCI6IjIyM2JlOWEzLTVmMjgtNWI5MC1hOTc0LWFiNDI1MWVhNTE1MSIsImNyZWF0ZWQiOjE3MzA3MTA2NjY3MTgsImV4aXN0aW5nIjp0cnVlfQ==; intercom-session-vvac201d=L3YyVHFOYWxtbG5rTW5vbTNRUHQ2THMrdkZPVitNUFN0WHpNVmN1LzJ0UTdUT1NsWTUrVTFRcHY3NXBZS3hoOC0tOFVpNkU1RGU2UEw3Zjc4cDJUUHVXZz09--6f7efb7eea3202647563c65bfff6c3a42bbfd77f; __hssc=29959136.3.1730710667307; _ga_HXS7M5JC7C=GS1.1.1730710665.1.1.1730710762.56.0.0',
            'origin': 'https://id.gettactic.com',
            'priority': 'u=0, i',
            'referer': 'https://id.gettactic.com/login?ReturnUrl=%2fconnect%2fauthorize%3fresponse_type%3dcode%26client_id%3dtactic_web%26redirect_uri%3dhttps%253A%252F%252Funion.gettactic.com%252Fauth%252Fcallback%26scope%3dopenid%2520api%2520offline_access%26state%3d8Ag5beWzTQQIp91Ppvud5hjH%252FrXAk5K0b84XDbfDJHs%253D%26code_challenge_method%3dS256%26code_challenge%3dljQvKHWX_LP9BPNRqB1t0MQWVSGGWOGQ0FvQmhVtxD0%26slug%3dwww&slug=www',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        conn.request("POST", "/login", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print("Login: "+str(res.status))
        
        time.sleep(1)
    
        presentday = datetime.now()
        twoWeeks = presentday + timedelta(13) # 13 days bcs streamlit is 1h behind
        twoWeeks = twoWeeks.date()
        conn2 = http.client.HTTPSConnection("union.gettactic.com")
        payload2 = json.dumps({
            "schedule_slots": [
                {
                    "user_id": "user_f3857b77-b2b9-4c1d-91f0-0f1102bca6f7",
                    "email": None,
                    "resource_id": "reso_14e40913-adc8-4b62-8286-97ebdf571781",
                    "team_id": None,
                    "slots": 1,
                    "start": str(twoWeeks)+"T09:00:00.000Z",
                    "end": str(twoWeeks)+"T17:00:00.000Z",
                    "time_zone": "Europe/Belgrade"
                }
            ]
        })
        headers2 = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'cookie': 'union_auth=WaSlnqTpzafZN_ewmYxmZLq2bqTf8mLDu-c6Xt3AizE; intercom-id-vvac201d=0cd8d7d7-47b8-48de-b0c4-903948961d3d; intercom-device-id-vvac201d=725fc9fc-256c-466f-8019-81afc8bd4f4f; intercom-session-vvac201d=djA5c3Q4TGZEd3YvTUVlbFpPaTl4NHYyTFZuUkRXV0FjWFdQbE42T3RSUHJiRXBwQzRMTEFvcVMveHRQc3NFeC0tb2N1ckI4cW8yNWxpVVdKTlFXeTFudz09--2b4e31b2a5c1d3d24f4881a86b32aff8b5135180',
            'origin': 'https://rldatix.gettactic.com',
            'priority': 'u=1, i',
            'referer': 'https://rldatix.gettactic.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-tactic-orgz': 'rldatix'
        }
        conn2.request("POST", "/api/offices/offi_afeac38d-e010-4204-8241-000e059b937d/schedules", payload2, headers2)
        res2 = conn2.getresponse()
        data2 = res2.read()
        print("["+datetime.datetime.now()+"] "+data2.decode("utf-8"))
        print("Booking: "+str(res2.status))
        if res2.status == 201:
            break
        tm+=1
        time.sleep(1)

# Set up the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_task, 'cron', hour=23, minute=0, second=0)  # Run daily at midnight -1h bcs streamlit is 1h behind
scheduler.start()

# Display the Streamlit app
st.title("Streamlit App with Scheduled Task at Midnight")
st.write("This app runs a scheduled task every day at 00:00:00.")

# Add a control to stop the scheduler if needed
st.button("Stop scheduler", on_click=scheduler.shutdown)
