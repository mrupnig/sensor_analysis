from pathlib import Path

from sensorlib.data_loader import load_readings
from sensorlib.processing import extract_values, filter_outliers, moving_average
from sensorlib.visualization import plot_series


def main() -> None:
    project_root = Path(__file__).resolve().parent
    csv_path = project_root / "data" / "sensor_readings.csv"

    readings = load_readings(csv_path)
    raw_values = extract_values(readings)

    cleaned = filter_outliers(raw_values, upper_threshold=100.0)
    smoothed = moving_average(cleaned, window_size=3)

    plot_series(raw_values, cleaned, smoothed)


if __name__ == "__main__":
    main()
