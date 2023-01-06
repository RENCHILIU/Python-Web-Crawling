import requests
import os

url = "https://renchiliu.com/upload/IMG_5822.JPG"
root = "/home/pics/"   # be careful about the last / 
path = root + url.split('/')[-1]


try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("saved pic")
    else:
        print("file exists")
except:
    print("error")
