from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_year_doy_heatmap(matrix: pd.DataFrame, title: str = "Temperatur (Tagesmittel) – Jahr × Tag des Jahres") -> None:
    """
    Visualisiert die Jahr×DOY-Matrix als Heatmap.
    matrix: index=Jahr, columns=1..366, values=Temperatur
    """
    years = matrix.index.to_list()
    data = matrix.to_numpy()

    plt.figure(figsize=(12, 9))
    ax = plt.gca()

    # imshow: y=Jahre, x=Tag des Jahres
    im = ax.imshow(
        data,
        aspect="auto",
        interpolation="nearest",
        origin="lower",
    )

    ax.set_title(title)
    ax.set_xlabel("Tag des Jahres")
    ax.set_ylabel("Jahr")

    # y-Achse: Jahre
    ax.set_yticks(np.arange(len(years)))
    ax.set_yticklabels(years)

    # x-Achse: grobe Monatsmarker (ungefähr)
    month_ticks = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    month_labels = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
    ax.set_xticks([t - 1 for t in month_ticks])
    ax.set_xticklabels(month_labels)

    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label("Temperatur (°C)")

    plt.tight_layout()
    plt.show()
