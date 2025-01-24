import requests
import json
import socket

HOST = "127.0.1.1"
PORT = 5000
URL = f"http://{HOST}:{PORT}"

def send_get_request():
    try:
        print("Sending GET request...")
        response = requests.get(URL)
        if response.status_code == 200:
            print("Response received:")
            print(response.text)
        else:
            print(f"Failed GET request with status code {response.status_code}")
    except Exception as e:
        print(f"Error during GET request: {e}")

def send_post_request(data):
    try:
        print("Sending POST request...")
        headers = {"Content-Type": "application/json"}
        response = requests.post(URL, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Response received:")
            print(response.text)
        else:
            print(f"Failed POST request with status code {response.status_code}")
    except Exception as e:
        print(f"Error during POST request: {e}")

if __name__ == "__main__":
    for i in range(5000):
        send_get_request()

        sample_data = {"name": "Test", "value": 42}
        send_post_request(sample_data)
        print(i)