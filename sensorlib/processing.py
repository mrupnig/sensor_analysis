from typing import List, Sequence
from .data_loader import Reading


def filter_outliers(values: Sequence[float], upper_threshold: float) -> List[float]:
    """Entfernt Werte oberhalb eines Schwellwerts (sehr einfache Outlier-Logik)."""
    return [v for v in values if v <= upper_threshold]


def moving_average(values: Sequence[float], window_size: int = 3) -> List[float]:
    """
    Einfache gleitende Mittelwerte über die letzten window_size Werte.
    """
    if window_size <= 0:
        raise ValueError("window_size must be > 0")

    result: List[float] = []
    for i in range(len(values)):
        start = max(0, i - window_size + 1)
        window = values[start : i + 1]
        # Wenn values Strings sind, knallt sum(window) im Debugging sehr gut nachvollziehbar.
        result.append(sum(window) / len(window))
    return result


def extract_values(readings: Sequence[Reading]) -> List[float]:
    """Extrahiert die numerischen Werte aus den Messungen."""
    return [r.value for r in readings]
