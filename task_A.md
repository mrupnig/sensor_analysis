## Aufgabenstellung:

### Explorationsphase:

Öffnen Sie die IDE und machen Sie sich mit der Nutzeroberfläche vertraut. Explorieren Sie die Oberfläche, um sich einen Überlick zu verschaffen.

### Teilaufgabe A – Projekt öffnen & Überblick (Projektverwaltung, Navigation)

Instruktion an Proband:innen:

- Öffnen Sie das Projekt `sensor_analysis` als Projekt/Workspace in der IDE.
- Finden Sie die Datei, `main.py`, und führen Sie das Programm aus.
- Navigieren Sie von `main()` zu der Funktion, die den gleitenden Durchschnitt berechnet.

→ Misst: Projektverwaltung, Projekt-Öffnen, Navigation (Go to Definition), Run-Konfiguration.

### Teilaufgabe B – Debugging

Ziel: Sie sollen den Bug in `moving_average` finden und beheben.

Instruktion:

- Führen Sie die Tests aus und prüfen Sie, ob alle Tests bestehen.
- Finden Sie den Fehler, der zum Fehlschlag von `test_moving_average_simple` führt.
- Nutzen Sie dabei den Debugger der IDE (Breakpoints setzen, Schritt-für-Schritt-Ausführung, Variablen inspizieren).

→ Misst:

Testausführung (Run/Debug-Konfiguration, Test-Integration)
Debugger-Usability (Breakpoints, Step into/over, Variable Inspector)
Darstellung von Stacktrace/Syntax-Highlighting von Fehlern

### Teilaufgabe C – Refactoring

Ziel: Nutzung der Refactoring-Funktionen (nicht „suchen/ersetzen“ per Hand).

- Rename Refactoring

    - Benennen Sie die Funktion `remove_outliers` in `filter_outliers` um. Verwenden Sie dafür die Refactoring-Funktion der IDE (kein manuelles Suchen/Ersetzen). Achten Sie darauf, dass Tests und `main.py` weiterhin funktionieren.

### Teilaufgabe D – Autocomplete & Syntax-Highlighting (kleine Funktionserweiterung)

Ziel: Die Personen sollen eine kleine Erweiterung programmieren und dabei stark von Code Completion profitieren.

- Fügen Sie in `analysis.py` eine neue Funktion hinzu:
```

def normalize(values: List[float]) -> List[float]:

    if not values:
        return []

    min_val = min(values)
    max_val = max(values)

    if max_val == min_val:
        return [0.0 for _ in values]

    return [(v - min_val) / (max_val - min_val) for v in values]
```
→ Misst:

- Qualität der Code Completion
- Lesbarkeit (Syntax-Highlighting, Fehleranzeigen)
- Unterstützung bei Typannotationen / Imports

### Teilaufgabe E – Profiling


### Teilaufgabe F – Versionierung (Git)

Das Projekt liegt als Git-Repo vor (mit einem initialen Commit).

Aufgabe:

- Prüfen Sie den aktuellen Git-Status des Projekts in der IDE.“
- Führen Sie nach Behebung des Bugs und nach dem Refactoring einen Commit durch mit der Nachricht *"Fix moving_average“*
- Zeigen Sie sich den Unterschied (Diff) zur vorherigen Version für `analysis.py` an.“

Optional: 
- Machen Sie die letzte Änderung in reporting.py rückgängig (Revert/Discard).“

→ Misst:

Integrierte Git-Unterstützung (Status, Diff, Commit)
Transparenz von Änderungen (Diff-View)
Bedienbarkeit von Revert/Discard