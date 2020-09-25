import wget
import requests
import numpy as np

ENDPOINTS = 1468
f_url = "https://marknad.sgsstudentbostader.se/sgs/files/gif/"

f_prefix = "file"
f_suffix = ".gif"

g_url = "https://marknad.sgsstudentbostader.se/sgs/files/gif/file"

file_name = "file.gif"


url = 'https://marknad.sgsstudentbostader.se/sgs/files/gif/file1467.gif'

# check which index that is 200, (not 404)

fileAvailableList = np.zeros(ENDPOINTS, dtype=bool)

for i in range(ENDPOINTS):
    url = g_url + str(i) + f_suffix
    r = requests.get(url)
    fileAvailableList[i] = r.status_code == 200
    


for idx, available in enumerate(fileAvailableList):
    if(available):
        url = g_url + str(idx) + f_suffix
        wget.download(url, 'downloads/file' + str(idx) + '.png',)

