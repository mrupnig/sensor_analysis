from typing import List, Tuple


def to_float_values(readings: List[Tuple[str, str]]) -> List[float]:
    """
    Extrahiert die Messwerte (value) aus den Messungen als float-Liste.

    Parameter:
        readings: Liste von (timestamp, value)-Tupeln, value als str.

    Rückgabe:
        Liste von float-Werten.
    """
    values: List[float] = []
    for ts, v in readings:
        # Potentielle Fehlerquelle (ValueError), wenn das CSV unpassende Werte enthält.
        values.append(float(v))
    return values


def moving_average(values: List[float], window_size: int = 3) -> List[float]:
    """
    Berechnet eine einfache gleitende Durchschnittskurve.

    Aktuell ist hier bewusst ein Bug / Code-Smell eingebaut, so dass
    die Berechnung nicht dem üblichen gleitenden Fenster entspricht.

    Erwartetes Verhalten (z. B. im Test):
        Bei window_size = 2 und values = [1, 2, 3, 4]
        sollte das Ergebnis [1.0, 1.5, 2.5, 3.5] sein.

    Der aktuelle Code verwendet jedoch immer das Fenster ab Index 0.
    """
    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    result: List[float] = []
    for i in range(len(values)):
        # BUG: das Fenster startet immer bei 0, anstatt nur die letzten 'window_size' Werte zu nehmen
        window = values[0 : i + 1]
        avg = sum(window) / len(window)
        result.append(avg)
    return result


def remove_outliers(values: List[float], threshold: float = 100.0) -> List[float]:
    """
    Filtert Ausreißer heraus (sehr einfache Implementierung).

    Alle Werte >= threshold werden entfernt.

    Parameter:
        values: Liste von float-Werten
        threshold: Grenzwert, ab dem ein Wert als Ausreißer gilt

    Rückgabe:
        Liste von Werten < threshold.
    """
    filtered: List[float] = []
    for v in values:
        if v < threshold:
            filtered.append(v)
    return filtered
