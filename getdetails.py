import requests

url = 'http://127.0.0.1:5000/download'
data = {'url': 'https://youtu.be/FeUA-0G1p5k?si=aG696NxKKne08NXS'}
response = requests.post(url, json=data)

if response.status_code == 200:
    with open('video.mp4', 'wb') as f:
        f.write(response.content)
    print('Video downloaded successfully.')
else:
    print(f"Error: {response.json().get('error')}")
