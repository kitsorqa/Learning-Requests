import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import json



#1_Скачка видео
url = "https://parsinger.ru/video_downloads/videoplayback.mp4"
response = requests.get(url, stream=True)
with open('my_file.mp4', 'wb') as video:
    video.write(response.content)


#2_Отправить 200 запросов и суммировать ответы от серверов
codes_sum = 0
for i in range(1, 201):
    url = f'https://parsinger.ru/3.3/2/{i}.html'
    response = requests.get(url)
    codes_sum += int(response.status_code)
print(codes_sum)


#3_Среди 200 страниц найти работающую
for i in range(1, 201):
    url = f'https://parsinger.ru/3.3/1/{i}.html'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        break


#4_Среди изображение найти самое большое
name_img = [
    '1663231240183817644.jpg', '1663231245165469794.jpg',
    '1663231252148267596.jpg', '16632460271311817.jpg',
    '1663260860165832550.jpg', '1663260862112644405.jpg',
    '1663260864114071369.jpg', '1663260869127473152.jpg',
    '1663260874115452216.jpg', '1663260877136512181.jpg',
    '1663260878140464277.jpg', '1663267600193799276.jpg',
    '1663267613117130673.jpg', '1663267619197170483.jpg',
    '1663267626154597739.jpg', '1663267648135114690.jpg',
    '166326765416196421.jpg', '1663267662118079649.jpg',
    '1663267668165066872.jpg', '1663267878176341940.jpg',
    '166326990115068678.jpg', '1663269922185881885.jpg',
    '1663269927127433209.jpg', '1663269942143420441.jpg',
    '1663269946174943071.jpg', '1663269964195277579.jpg',
    '1663269970148058649.jpg', '1663269974197750992.jpg',
    '166326997917397750.jpg', '1663270039138442380.jpg',
    '1663388012194470737.jpg', '166342371029995280.jpg',
    '1663423712288242036.jpg', '1663423715255612089.jpg',
    '1663423720221155166.jpg', '1663423722211139858.jpg',
    '1663423724211218483.jpg', '1663423728215479371.jpg',
    '1663423729298828299.jpg', '1663423732225964403.jpg',
    '1663424198111663025.jpg', '1663424199157537861.jpg',
    '1663424200184778832.jpg', '166342420214123494.jpg',
    '166342420317539591.jpg', '1663424204161674559.jpg',
    '1663424206188873432.jpg', '166342420813193185.jpg',
    '1663424209187179962.jpg', '1663424212162573102.jpg'
]

current = {1: 1,
           'ind': 0}

for i in range(0, len(name_img)):
    url = f"https://parsinger.ru/3.3/3/img/{name_img[i]}"
    response = requests.get(url)
    img_size = response.headers.get('Content-Length')
    if int(img_size) > current[1]:
        current[1] = int(img_size)
        current['ind'] = name_img[i]


#5_Первая и последняя доступная страница
count = 0
first_available_page, last_available_page = 0, 0
for i in range(1, 101):
    url = f'https://parsinger.ru/3.3/4/{i}.html'
    response = requests.get(url)
    if response.status_code == 200:
        if count == 0:
            first_available_page = url
            count += 1
    if response.status_code == 200 and count >= 1:
        last_available_page = url


print(f"Первая доступная страница: {first_available_page}")
print(f"Последняя доступная страница: {last_available_page}")