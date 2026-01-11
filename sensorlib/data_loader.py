from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd

def LoadWeatherCsv(
    csv_path: Path,
    timestamp_col: str = "timestamp",
    temperature_col: str = "temperature",
    tz: Optional[str] = None,
) -> pd.DataFrame:
    """
    Lädt Wetterstationsdaten aus einer CSV.

    Erwartung:
      - Eine Zeitspalte (timestamp_col), die zu datetime parsebar ist
      - Eine Temperaturspalte (temperature_col) in Grad (float)

    Rückgabe:
      DataFrame mit DatetimeIndex und einer Spalte 'temperature'.
    """
    df = pd.read_csv(csv_path)

    if timestamp_col not in df.columns:
        raise KeyError(f"timestamp_col '{timestamp_col}' nicht in CSV-Spalten: {list(df.columns)}")
    if temperature_col not in df.columns:
        raise KeyError(f"temperature_col '{temperature_col}' nicht in CSV-Spalten: {list(df.columns)}")

    df[timestamp_col] = pd.to_datetime(
        df[timestamp_col],
        format="%d.%m.%Y",
        errors="coerce")
        
    df = df.dropna(subset=[timestamp_col])

    # Temperatur robust numerisch
    df["temp"] = pd.to_numeric(
        df[temperature_col].astype(str).str.replace(".", "", regex=False),
        errors="coerce")

    df = df.dropna(subset=["temp"])

    df = df.set_index(timestamp_col).sort_index()

    # Optional: Zeitzone setzen/konvertieren
    if tz is not None:
        if df.index.tz is None:
            df.index = df.index.tz_localize(tz)
        else:
            df.index = df.index.tz_convert(tz)

    return df[["temp"]]
