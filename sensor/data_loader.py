import csv
from pathlib import Path
from typing import List, Tuple

# Pfad zur CSV-Datei relativ zum Projekt-Root
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "readings.csv"


def load_readings(path: Path = DATA_FILE) -> List[Tuple[str, str]]:
    """
    Lädt Messwerte aus einer CSV-Datei.

    Rückgabe:
        Liste von (timestamp, value)-Tupeln.
        value ist zunächst ein String und wird später konvertiert.
    """
    readings: List[Tuple[str, str]] = []

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # value bleibt hier bewusst als String – Konvertierung später
            readings.append((row["timestamp"], row["value"]))

    return readings
