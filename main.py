import requests
import configuration
import data


def post_new_order(order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=order,
        headers=data.headers)


def get_order_by_tracking(tracking_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK/{tracking_number},
        headers=data.headers)


def test_order_creation_and_tracking():
    # Шаг 1: Создаем заказ
    response = post_new_order(data.order_body)
    assert response.status_code == 201, f'Failed to create order: {response.text}'
    order_id = response.json()['order_id']

    # Шаг 2: Получаем номер трека заказа
    response_t = requests.get(configuration.URL_SERVICE + configuration. GET_ORDER_TRACK,
        headers=data.headers)
    assert response_t.status_code == 200, f'Failed to get order tracking: {response_t.text}'
    tracking_number = response_t.json()['tracking_number']

    # Шаг 3: Получаем заказ по треку заказа и проверяем, что код ответа равен 200
    response_o = get_order_by_tracking(tracking_number)
    assert response_o.status_code == 200, f'Failed to get order by tracking: {response_o.text}'