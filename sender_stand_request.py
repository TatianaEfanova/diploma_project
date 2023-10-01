import requests
import configuration
import data


def post_new_order(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_URL, json=body, headers=data.HEADERS)
    return response.json()["track"]