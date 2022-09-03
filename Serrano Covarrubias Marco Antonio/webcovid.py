from re import U


import requests

url="https://datos.cdmx.gob.mx/dataset/capacidad-hospitalaria"

resp=requests.get(url)
print(resp)

path='E:/Python/'
with open(path+'covicho.csv','wb') as output:
    output.write(resp.content)