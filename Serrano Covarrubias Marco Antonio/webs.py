from re import U


import requests

url="http://www.mambiente.munimadrid.es/opendata/horario.txt"

resp=requests.get(url)
print(resp)

path='E:/Python/'
with open(path+'horario.csv','wb') as output:
    output.write(resp.content)