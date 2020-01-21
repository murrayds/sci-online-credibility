# maybe script for downloading images



# import random
# import urllib.request

# def download_image(url):
    # name = random.randrange(1,100)
    # fullname = str(name)+".jpg"
    # urllib.request.urlretrieve(url,fullname)     
# download_image("http://ella.ils.indiana.edu/~atsou/Tweets/Article 1/art1.10.1.jpg")

import requests
import csv

filename = "../codebook/tweetsGuide.csv"

with open(filename, "r") as csvfile:
    fileraw = csv.reader(csvfile, delimiter = ",")
    list = [row for row in fileraw]
file = list[1:]

print('Beginning file download with requests')
id = 0

for line in file:
    id += 1
    url = line[0]
    # url = 'http://ella.ils.indiana.edu/~atsou/Tweets/Article 1/art1.10.1.jpg'
    r = requests.get(url)
    with open(str(id) + '.jpg', 'wb') as f:
        f.write(r.content)

# Retrieve HTTP meta-data
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)