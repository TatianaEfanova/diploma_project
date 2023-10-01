import sender_stand_request
import requests
import data
import configuration

# Татьяна Ефанова, 8-а когорта — Финальный проект. Инженер по тестированию плюс
#Тест №1. Проверка получения информации о заказе по трэк-номеру заказа.
def test_getting_order_info():
    track_id = {'t': str(sender_stand_request.post_new_order(data.ORDER_BODY))}
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO, params=track_id)
    assert response.status_code == 200, "Expected 200 but got " + str(response.status_code)
