import requests
import time

server1_url = "http://127.0.0.1:7000/message/"
server2_url = "http://127.0.0.1:7001/message/"

data = {'message': 'hello'}


while True:
    try:
        response1 = requests.post(server1_url, data=data)
        print(f"Server 1 Response: {response1.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Server 1: {e}")

    try:
        response2 = requests.post(server2_url, data=data)
        print(f"Server 2 Response: {response2.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Server 2: {e}")

    time.sleep(1)