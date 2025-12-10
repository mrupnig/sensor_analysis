from sensor.data_loader import load_readings
from sensor.analysis import to_float_values, moving_average, remove_outliers
from sensor.reporting import format_summary


def main() -> None:
    """
    Einstiegspunkt für die kleine Demo-Anwendung.

    Ablauf:
    - Messwerte laden
    - in floats konvertieren
    - Ausreißer entfernen
    - gleitenden Mittelwert berechnen
    - Bericht erzeugen und ausgeben
    """
    readings = load_readings()
    values = to_float_values(readings)

    # Ausreißer filtern – hier könnte man im Rahmen einer Aufgabe mit dem threshold spielen
    cleaned = remove_outliers(values, threshold=200.0)

    # Gleitender Durchschnitt mit Fenstergröße 3 (aktuell fehlerhafte Implementierung)
    smoothed = moving_average(cleaned, window_size=3)

    report = format_summary(cleaned, smoothed)
    print(report)


if __name__ == "__main__":
    main()
