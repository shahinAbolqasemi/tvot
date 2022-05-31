import re
import time
import threading
import random
import requests

def vote():
    cookies = {
        'tp_eebee97cadceb9cae9bc1f079b63248c': '1',
    }

    headers = {
        'authority': 'turkishtvlife.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryC5e2NHK9k8vBuDfb',
        # 'cookie': 'tp_eebee97cadceb9cae9bc1f079b63248c=1',
        'origin': 'https://turkishtvlife.com',
        'referer': 'https://turkishtvlife.com/turkish-tv-series-universe-awards-2022/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'totalpoll',
    }

    proxies = dict(http='socks5://tord-git-8:9050', https='socks5://tord-git-8:9050')

    data = '------WebKitFormBoundaryC5e2NHK9k8vBuDfb\r\nContent-Disposition: form-data; name="totalpoll[choices][f70621ea-7908-47ef-a93a-23320548f35b][]"\r\n\r\n33ae8d29-7d9f-4cc4-b5f6-0285940f2fa0\r\n------WebKitFormBoundaryC5e2NHK9k8vBuDfb\r\nContent-Disposition: form-data; name="totalpoll[screen]"\r\n\r\nvote\r\n------WebKitFormBoundaryC5e2NHK9k8vBuDfb\r\nContent-Disposition: form-data; name="totalpoll[pollId]"\r\n\r\n391\r\n------WebKitFormBoundaryC5e2NHK9k8vBuDfb\r\nContent-Disposition: form-data; name="totalpoll[action]"\r\n\r\nvote\r\n------WebKitFormBoundaryC5e2NHK9k8vBuDfb--\r\n'
    while True:
        try:
            response = requests.post('https://turkishtvlife.com/wp-admin/admin-ajax.php', params=params, cookies=cookies,
                                     headers=headers, data=data, proxies=proxies)
            response.raise_for_status()
            if response.status_code == 200:
                result = re.findall(
                    r'>.+ Votes  .*%',
                    response.text
                )
                result = result[:2]
                vote_diff = int(result[0][1:].split()[0].strip().replace(',', '')) - int(result[1][1:].split()[0].strip().replace(',', ''))
                print("\t".join([res[1:] for res in result]), f'diff= {vote_diff}')
            time.sleep(random.randint(1, 5))
            # int('2,553,262 Votes  39.70%'.split()[0].strip().replace(',', ''))
        except Exception:
            print('error')
        except KeyboardInterrupt:
            print('exit')
            break

if __name__ == '__main__':
    for i in range(1, 100):
        t = threading.Thread(target=vote)
        t.start()

