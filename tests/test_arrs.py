import pytest

from utils import arrs


@pytest.fixture
def data_0():
    return []


@pytest.fixture
def data_1():
    return [1, 2, 3]


@pytest.fixture
def data_2():
    return [1, 2, 3, 4]


def test_get(data_0, data_1):
    assert arrs.get(data_1, 1, "test") == 2
    assert arrs.get(data_1, 5, "test") == "test"
    assert arrs.get(data_0, 0, "test") == "test"
    assert arrs.get(data_1, -1, "test") == "test"


def test_slice(data_0, data_1, data_2):
    assert arrs.my_slice(data_2, 1, 3) == [2, 3]
    assert arrs.my_slice(data_2, -2) == [3, 4]
    assert arrs.my_slice(data_2, -10, 2) == [1, 2]
    assert arrs.my_slice(data_1, 1) == [2, 3]
    assert arrs.my_slice(data_0, 1) == []
