import requests
city =input('input the city name:')
print(city)
print('displaying weather report :')
url='https://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)