import requests
from time import sleep
from logger import get_logger
from mail import send_email

LOGGER = get_logger('vaccin')
SLEEP_INTERVAL = 60*60

def get_results():
    headers = {
        'authority': 'api3.clicsante.ca',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'product': 'clicsante',
        'authorization': 'Basic cHVibGljQHRyaW1vei5jb206MTIzNDU2Nzgh',
        'content-type': 'application/json;charset=UTF-8',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'x-trimoz-role': 'public',
        'origin': 'https://portal3.clicsante.ca',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://portal3.clicsante.ca/',
        'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
        'cookie': '_ga=GA1.2.161867132.1623692589; privacyConsent=1; _gid=GA1.2.2139342216.1624297684',
    }

    data = '{"nam":"WEIN94080619","phone":"2154992107"}'

    response = requests.post('https://api3.clicsante.ca/v3/appointments/jobs', headers=headers, data=data)

    return response.json()


def should_send_alert(results):
    return results['status'] != 404


def main():
    results = get_results()
    if should_send_alert(results):
        LOGGER.info(f'Got non-404 result: f{results}')
        send_email(subject='Vaccine appointment available')
        return
    LOGGER.debug(f'Got 404 result: f{results}')
    sleep(SLEEP_INTERVAL)
    main()


if __name__ == '__main__':
    main()
