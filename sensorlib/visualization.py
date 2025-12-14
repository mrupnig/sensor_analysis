from typing import Sequence
import matplotlib.pyplot as plt


def plot_series(
    raw_values: Sequence[float],
    cleaned_values: Sequence[float],
    smoothed_values: Sequence[float],
) -> None:
    """
    Plottet Rohdaten, bereinigte Daten und geglättete Daten als Linien.
    """
    plt.figure()
    plt.plot(raw_values, label="raw")
    plt.plot(cleaned_values, label="cleaned")
    plt.plot(smoothed_values, label="moving_avg")
    plt.title("Sensor readings")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.show()
