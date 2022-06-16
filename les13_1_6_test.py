import points as points
import pytest

from les13_1_6 import get_grade

grade_parameters = [
    (15, 2),
    (35, 3),
    (77, 4),
    (88, 5),
]

@pytest.mark.parametrize("points, grade", grade_parameters)
def test_get_grade(points, grade):
    assert get_grade(points) == grade


grade_exceptions = [
    (100500, ValueError),
    ("100500", TypeError),
]


@pytest.mark.parametrize("points, exception", grade_exceptions)
def test_get_grade_exceptions(points, exception):
    with pytest.raises(exception):
        get_grade(points)