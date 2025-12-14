import csv
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class Reading:
    timestamp: str
    value: float  # semantisch "float", aber der Loader macht gleich den Bug (siehe unten)


def load_readings(csv_path: Path) -> List[Reading]:
    """
    Lädt Sensorwerte aus einer CSV-Datei.

    Erwartete Spalten:
      - timestamp
      - value
    """
    readings: List[Reading] = []
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # BUG: value wird NICHT in float umgewandelt (bleibt str).
            # Das führt später in processing.py zu einem Fehler beim Rechnen.
            readings.append(Reading(timestamp=row["timestamp"], value=row["value"]))  # type: ignore[arg-type]
    return readings
