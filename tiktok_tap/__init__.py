import singer
import requests
import time
import hashlib
import os

LOGGER = singer.get_logger()


def generate_signature(app_secret, params):
    sorted_params = sorted(params.items())
    base_string = app_secret + ''.join([f'{k}{v}' for k, v in sorted_params]) + app_secret
    signature = hashlib.md5(base_string.encode('utf-8')).hexdigest().upper()
    return signature


def fetch_authorized_shops(config):
    app_key = config.app_key
    app_secret = config.app_secret
    access_token = config.access_token

    endpoint = 'https://open-api.tiktokglobalshop.com/api/shop/get_authorized_shops'
    params = {
        'app_key': app_key,
        'access_token': access_token,
        'timestamp': int(time.time())
    }
    params['sign'] = generate_signature(app_secret, params)

    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()


def main():
    args = singer.utils.parse_args(required_config_keys=['app_key', 'app_secret', 'access_token', 'start_date'])
    config = args.config

    data = fetch_authorized_shops(config)

    schema = {
        "properties": {
            "shop_id": {"type": "string"},
            "shop_name": {"type": "string"},
            "authorized": {"type": "boolean"}
        }
    }
    singer.write_schema('authorized_shops', schema, 'shop_id')

    for record in data.get('data', {}).get('shops', []):
        singer.write_record('authorized_shops', record)


if __name__ == '__main__':
    main()
