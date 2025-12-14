from __future__ import annotations

import pandas as pd

def year_doy_heatmap_matrix(daily: pd.Series) -> pd.DataFrame:
    """
    Baut eine Matrix: Zeilen=Jahr, Spalten=Tag des Jahres (1..366),
    Werte=Tagesmitteltemperatur.

    Vorteil: Sehr visuelle Darstellung von Saisonverläufen + Anomalien.
    """
    s = daily.copy()
    idx = s.index

    years = idx.year
    doy = idx.dayofyear

    mat = pd.DataFrame({"year": years, "doy": doy, "temp": s.values})
    pivot = mat.pivot_table(index="year", columns="doy", values="temp", aggfunc="mean")

    # Spalten lückenlos 1..366, damit Heatmap stabil ist
    pivot = pivot.reindex(columns=range(1, 367))

    return pivot


def rolling_mean(series: pd.Series, days: int = 7) -> pd.Series:
    """Gleitender Mittelwert über 'days' Tage (für Glättung)."""
    return series.rolling(window=days, min_periods=max(1, days // 2)).mean()
