import threading
import requests
from bs4 import BeautifulSoup


urls = ['https://vietnamnet.vn/mua-ban-vang-tu-20-trieu-phai-chuyen-khoan-tinh-theo-ngay-hay-theo-luot-2421143.html',
        'https://vietnamnet.vn/chung-cu-ha-noi-tang-phi-ma-nha-dau-tu-om-tien-vao-sieu-do-thi-tphcm-2420977.html']


def fetch_cotent(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched: {len(soup.text)} characters from {url}')


thread_manage = []

for url in urls:
    thread_fetch_content = threading.Thread(
        target=fetch_cotent,
        args=[url]
    )
    thread_manage.append(thread_fetch_content)
    thread_fetch_content.start()

# Wait for all content fetch success
for thread in thread_manage:
    thread.join()

print('All page fetch successfully !')
