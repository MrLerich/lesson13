import pytest

from day_night import get_period

grade_parameters = [
    (6, "ночь"),
    (11, "утро"),
    (13, "день"),
    (19, "вечер"),
]

@pytest.mark.parametrize("hour, daytime", grade_parameters)
def test_get_period(hour, daytime):
    assert get_period(hour) == daytime


grade_exceptions = [
    (25, ValueError),
    (-4, ValueError),
    ("12", TypeError),
]


@pytest.mark.parametrize("hour, exception", grade_exceptions)
def test_get_period_exceptions(hour, exception):
    with pytest.raises(exception):
        get_period(hour)