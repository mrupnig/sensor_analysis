## Aufgabenblatt: IDE-Usability – Weather Monitor Projekt

Dieses Aufgabenblatt dient der Erhebung von Usability- und Effizienzmerkmalen verschiedener IDEs anhand eines gemeinsamen Python-Projekts. Jede Teilaufgabe misst bestimmte Interaktionsaspekte wie Navigation, Debugging, Refactoring oder Git-Workflows.

---

### Explorationsphase:

Öffnen Sie die IDE und machen Sie sich mit der Nutzeroberfläche vertraut. Explorieren Sie die Oberfläche, um sich einen Überlick zu verschaffen.

---

### Teilaufgabe A – Projekt öffnen & Überblick

**Instruktion**

1. Öffnen Sie das Projekt `weather_monitor` als Projekt/Workspace in der IDE.  
2. Finden Sie die Datei `processor.py` und führen Sie das Skript `run.py` aus.  
3. Navigieren Sie von `run()` zur Funktion, die den Medianfilter für Sensordaten berechnet.

**Misst**

- Projektverwaltung und Orientierung  
- Navigation (Go to Definition)  
- Run-Konfigurationen  

---

### Teilaufgabe B – Debugging

**Kontext:** Die Funktion `median_filter` in `processor.py` liefert fehlerhafte Werte.

**Instruktion**

1. Führen Sie die Tests aus (z. B. `test_filters.py`).  
2. Identifizieren Sie die Ursache des Fehlschlags von `test_median_filter_basic`.  
3. Verwenden Sie Breakpoints, Step-Over, Step-Into und den Variablen-Inspector.  
4. Beheben Sie den Fehler.

**Misst**

- Testausführung und Testintegration  
- Effizienz und Verständlichkeit des Debuggers  
- Qualität der Stacktrace-Darstellung  

---

### Teilaufgabe C – Refactoring

**Kontext:** Eine Funktion soll IDE-gestützt umbenannt werden, ohne manuelle Such-/Ersetzvorgänge.

**Instruktion**

Benennen Sie in `data_utils.py` die Funktion `smooth_values` um in:

> `smooth_signal`

Stellen Sie sicher, dass alle Verwendungen in anderen Modulen automatisch aktualisiert werden.

**Misst**

- Präzision und Zuverlässigkeit des Rename-Refactorings  
- Korrekte Aktualisierung von Imports und Funktionsaufrufen  

---

### Teilaufgabe D – Autocomplete & Syntax-Highlighting

**Instruktion**

Fügen Sie in `stats.py` folgende neue Funktion hinzu:

```python
def z_scores(values: List[float]) -> List[float]:
    if not values:
        return []
    mean_val = sum(values) / len(values)
    std_val = (sum((v - mean_val) * 2 for v in values) / len(values)) * 0.5
    if std_val == 0:
        return [0.0 for _ in values]
    return [(v - mean_val) / std_val for v in values]
```

**Misst**

- Qualität der Code Completion  
- Syntax Highlighting & Fehlermeldungen  
- Unterstützung bei Typannotationen  

---

### Teilaufgabe E – Versionierung (Git)

Das Projekt ist bereits als Git-Repository mit einem Start-Commit vorbereitet.

**Instruktion**

1. Prüfen Sie den aktuellen Git-Status.  
2. Führen Sie nach Debugging & Refactoring einen Commit durch:

   **Commit-Message:**  
   `Fix median_filter bug & rename smooth_values`

3. Zeigen Sie den Diff für `processor.py` an.  
4. Optional: Machen Sie die letzte Änderung in `visualization.py` rückgängig (Revert/Discard).

**Misst**

- Git-Status-Ansichten  
- Diff-Darstellungen  
- Commit-Dialoge  
- Revert/Discard-Usability  
