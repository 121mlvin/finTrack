import requests
import json


def get_location():
    try:
        ip_response = requests.get('https://api.ipify.org?format=json')
        ip_data = ip_response.json()
        clean_ip = ip_data['ip']

        res = requests.get(f'http://ip-api.com/json/{clean_ip}')
        res.raise_for_status()
        location_data = res.json()
        return location_data
    except requests.RequestException as e:
        return {'error': str(e)}


def get_currency_info(request):
    loc = get_location()
    if 'error' in loc:
        return 'Unknown', 'Unknown'

    try:
        with open('static/countries.json', encoding="utf8") as f:
            data = json.load(f)
            for country in data:
                if loc['country'] == country['name']:
                    local_currency = country['currency']['name']
                    local_currency_symbol = country['currency']['symbol']
                    return local_currency, local_currency_symbol
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return 'Unknown', 'Unknown'

    return 'Unknown', 'Unknown'
