import pytest
from les13_1_5 import ticket_price

param = [
    (0, "Бесплатно"),
    (1, "Бесплатно"),
    (7, "100 рублей"),
    (18, "200 рублей"),
    (25, "300 рублей"),
    (60, "Бесплатно"),
    (0.5, "Бесплатно"),
    (-1, "Ошибка")
]


@pytest.mark.parametrize(
    "age, expected", param
    # [
    #     (0, "Бесплатно"),
    #     (1, "Бесплатно"),
    #     (7, "100 рублей"),
    #     (18, "200 рублей"),
    #     (25, "300 рублей"),
    #     (60, "Бесплатно"),
    #     (0.5, "Бесплатно"),
    #     (-1,"Ошибка")]
)  # param )
def test_ticket_price(age, expected):
    assert ticket_price(age) == expected

    # assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"
    # assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"
    # assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"
    # assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"
    # assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"
    # assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"
    # assert ticket_price(0.5) == "Бесплатно", "Ошибка для 0.5 лет"
    # assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"
