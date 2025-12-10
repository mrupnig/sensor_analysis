from sensor.analysis import to_float_values, moving_average, remove_outliers


def test_to_float_values():
    readings = [("t1", "1.0"), ("t2", "2.5"), ("t3", "3.5")]
    values = to_float_values(readings)
    assert values == [1.0, 2.5, 3.5]


def test_moving_average_simple():
    values = [1, 2, 3, 4]
    mav = moving_average(values, window_size=2)
    # Erwartung: Durchschnitt über jeweils die letzten 2 Werte:
    # [1.0, (1+2)/2, (2+3)/2, (3+4)/2] = [1.0, 1.5, 2.5, 3.5]
    assert mav == [1.0, 1.5, 2.5, 3.5]


def test_remove_outliers():
    values = [1, 2, 1000, 3]
    filtered = remove_outliers(values, threshold=100)
    assert filtered == [1, 2, 3]
