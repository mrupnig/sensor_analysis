# Sensor Analysis – Mini-Projekt für IDE-Usability-Studie

Dieses kleine Python-Projekt dient dazu, typische IDE-Funktionalitäten in einer empirischen Untersuchung zu testen:

- Projektverwaltung
- Navigation
- Debugging
- Refactoring
- Code-Vervollständigung
- Profiling
- Git-Integration / Versionierung
- Testausführung

## Inhalt

Das Projekt simuliert eine einfache Analyse von Sensordaten:

- `data/readings.csv`: Beispiel-Messwerte
- `sensor/data_loader.py`: Laden der Messdaten aus CSV
- `sensor/analysis.py`: Konvertierung, Ausreißer-Filterung, gleitender Mittelwert
- `sensor/reporting.py`: Berichtserstellung als Text
- `main.py`: Skript, das alles zusammen ausführt
- `tests/test_analysis.py`: Unit-Tests für zentrale Analysefunktionen

Es ist bewusst mindestens ein Bug in `moving_average` eingebaut
(Tests schlagen zunächst fehl), und es gibt Code, der sich gut für
Refactoring-Aufgaben eignet.

## Voraussetzungen

- Python 3.10+
- `pip` für Paketinstallation

Installation der Test-Abhängigkeit:

```bash
pip install -r requirements.txt
```

## Aufgaben

die Aufgabenstellungen liegen hier:
- [Aufgaben A](task_A.md)
- [Aufgaben B](task_B.md)