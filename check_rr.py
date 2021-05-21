import requests

url = "http://0.0.0.0:80/"

headers = {
    'cache-control': "no-cache",
    'postman-token': "27b3e2ab-815e-f18f-f079-d79b5585ad36"
    }
for i in range(1,40):
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    if i%6==0:
        print("\n")