import requests
import base64

def getCard(cardLocation): 
    cookies = {
        'easylogin_locale': 'en',
        '_ga': 'GA1.1.1482918017.1679946151',
        '_ga_YGZ758F8B0': 'GS1.1.1679946151.1.0.1679946151.0.0.0',
        'easylogin_session': 'r43usdullvf59m1squqa4m1s46',
    }

    headers = {
        'authority': 'www.mtgstand.com',
        'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="88"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.mtgstand.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
    }

    with open(cardLocation, "rb") as image_file:
        data = base64.b64encode(image_file.read())

    json_data = {
        'data': 'data:image/jpeg;base64,' + data.decode('utf-8'),
        'api': 'findcard',
    }

    response = requests.post('https://www.mtgstand.com/cardscanner/cardapi.php', cookies=cookies, headers=headers, json=json_data)

    print(response.content)
