from pathlib import Path

from sensorlib.data_loader import load_weather_csv
from sensorlib.processing import year_doy_heatmap_matrix
from sensorlib.visualization import plot_year_doy_heatmap

def main() -> None:
    project_root = Path(__file__).resolve().parent
    csv_path = project_root / "data" / "metadata.txt"

    # Passe Spaltennamen an deine CSV an:
    df = load_weather_csv(
        csv_path,
        timestamp_col="timestamp",
        temperature_col="temperature",
        tz=None,  # z.B. "Europe/Berlin" falls nötig
    )

    #df = remove_physical_outliers(df)
    
    if "temp" not in df.columns:
        raise KeyError("Spalte 'temp' fehlt. Verwende load_weather_csv().")

    # Tagesmittel (Kalendertage)
    daily = df["temp"].resample("D").mean()
    daily.dropna()
    
    mat = year_doy_heatmap_matrix(daily)

    plot_year_doy_heatmap(mat)


if __name__ == "__main__":
    main()
