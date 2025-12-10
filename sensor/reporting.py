from typing import List


def format_summary(values: List[float], smoothed: List[float]) -> str:
    """
    Erstellt einen Textbericht über die Messwerte.

    Hinweise:
    - Dieser Code enthält leichte Redundanzen bei der Durchschnittsberechnung
      und eignet sich daher gut für Refactoring-Aufgaben (z. B. Extract Function).
    """
    if not values:
        return "Keine Werte vorhanden."

    lines: List[str] = []
    lines.append(f"Anzahl Werte: {len(values)}")
    lines.append(f"Erster Wert: {values[0]}")
    lines.append(f"Letzter Wert: {values[-1]}")

    # Potentielle Stelle für das Extrahieren einer Hilfsfunktion, z. B. compute_average(...)
    raw_avg = sum(values) / len(values)
    lines.append(f"Durchschnitt (ungerundet): {raw_avg}")

    smoothed_avg = sum(smoothed) / len(smoothed)
    lines.append(f"Durchschnitt (geglättet, ungerundet): {smoothed_avg}")

    return "\n".join(lines)
