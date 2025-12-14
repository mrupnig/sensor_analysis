# Usability- und UX-Studie: Aufgabenstellungen für IDE-Vergleich (PyCharm vs. Spyder)

Grundlage ist das bereitgestellte Python-Projekt `sensor_analysis`.  
Die folgenden Teilaufgaben sollen **in der jeweiligen IDE** bearbeitet werden.  
Die Aufgaben sind **offen formuliert**; es wird **kein konkreter Lösungsweg vorgegeben**.  
Der jeweils beschriebene *Idealpfad* dient ausschließlich der Auswertung und Beobachtung.

---
## Explorationsphase

---

## Teilaufgabe A – Projekt öffnen & Überblick verschaffen

### Kontext
Du arbeitest mit einem bestehenden Python-Projekt, das aus mehreren Dateien und Ordnern besteht.  
Ziel ist es, sich einen ersten Überblick über Struktur und Einstiegspunkt des Projekts zu verschaffen.

### Aufgabenstellung
Öffne das Projekt in der IDE und verschaffe dir einen Überblick über Aufbau und Inhalte.  
Führe anschließend das Programm aus.

### Idealpfad (nicht vorgeben)
- Projektordner als Projekt/Workspace in der IDE öffnen  
- Projektstruktur im Datei-/Projektbrowser erkunden  
- Datei `main.py` als Einstiegspunkt identifizieren  
- `main.py` im Editor öffnen  
- Programm über die IDE ausführen (z. B. Run-Button oder Run-Konfiguration)
- Abhängigkeiten installieren

### Misst
- Projektverwaltung / Projektöffnung
- Orientierung in der Projektstruktur
- Navigation zwischen Dateien
- Auffindbarkeit von Run-Funktionen
- Erstverständnis der IDE-Oberfläche

---

## Teilaufgabe B – Debugging

### Kontext
Das Programm soll die "Sensordaten" aus dem `data` Ordner laden und zu einem Plot verarbeiten. 
Im Projekt sind ein paar Fehler enthalten, die dazu führen, dass das Programm nicht wie erwartet ausgeführt wird. Diese Fehler sollen mithilfe der IDE gefunden und behoben werden. Erst muss der Pfad angepasst werden, damit die richtige csv Datei geladen wird. Dann funktioniert das Programm, aber es wird ein leerer Plot ausgegeben. Es gibt zwei Fehler im Code, die gefunden und behoben werden sollen.

### Aufgabenstellung


### Idealpfad (nicht vorgeben)
- Fehlermeldung identifizieren
- Zur betroffenen Fehlerquelle in `main.py` navigieren
- Pfad anpassen
- Programm erneut ausführen
- leeren Plot identifizieren
- Breakpoints setzen
- Debugger starten
- Variablenwerte inspizieren und Programmausführung schrittweise verfolgen
- Fehlerquelle ausfindig machen
- Codezeilen korrigieren

### Lösungsvorschlag
in `data_loader.py` folgenden Code bearbeiten

vorher:
```python
    df[timestamp_col] = pd.to_datetime(
            df[timestamp_col],
            format="%d.%m.%Y",
            errors="coerce")

            # ...

    df["temp"] = pd.to_numeric(
            df[temperature_col].astype(str).str.replace(".", "", regex=False),
            errors="coerce")
```
nachher:
```python
    df[timestamp_col] = pd.to_datetime(
            df[timestamp_col],
            errors="coerce")
            
            # ...

    df["temp"] = pd.to_numeric(
            df[temperature_col],
            errors="coerce")
```

### Misst
- Darstellung und Verständlichkeit von Fehlermeldungen
- Debugger-Usability (Breakpoints, Step-Funktionen, Variableninspektion)
- Kognitive Belastung beim Debugging

---

## Teilaufgabe C – Refactoring

### Kontext
Der Code enthält Stellen, die funktional korrekt sind, aber strukturell verbessert werden können.  
Diese Änderungen sollen mithilfe der Refactoring-Werkzeuge der IDE durchgeführt werden. In `main.py` gibt es einen Codeabschnitt, der das Tagesmittel berechnet. Das würde in einer Funktion besser aussehen:

- extrahiere eine Funktion
- verschiebe die Funktion in eine andere Datei
- importiere die Funktion und rufe sie an der ursprünglichen Stelle auf.

### Aufgabenstellung
Verbessern Sie die Code-Struktur, indem Sie eine bestehende Funktion sinnvoll umbenennen  
und eine kleine strukturelle Verbesserung im Code vornehmen, ohne das Verhalten zu ändern.
Verschieben einer Funktion in eine andere Datei
Umbenennen einer Funktion


### Lösung

in `main.py` gibt es folgenden Codeabschnitt:

```python
    # Tagesmittel (Kalendertage)
    daily = df["temp"].resample("D").mean()
    daily.dropna()
```
Dieser soll per Refactoring in eine Funktion gepackt werden. Diese Funktion soll in `processing.py` geschoben werden. An der ursprünglichen Stelle soll die Funktion aufgerufen werden.

### Idealpfad (nicht vorgeben)
- markieren des korrekten Codeabschnttes
- Umwandeln in eine Funktion
- Funktionsnamen ändern und Änderungen automatisch anwenden lassen
- Verschieben der Funktion
- Importieren der Funktion
- Aufrufen der Funktion an der richtigen Stelle
- Sicherstellen, dass das Programm weiterhin lauffähig ist

### Misst
- Auffindbarkeit von Refactoring-Funktionen
- Verständlichkeit von Refactoring-Dialogen
- Vertrauen in automatische Code-Änderungen
- Unterstützung bei projektweiten Änderungen
- Rückmeldung der IDE bei potenziellen Problemen

---

## Teilaufgabe D – Autocompletion & Syntax-Highlighting

### Kontext
Das Projekt soll um eine kleine zusätzliche Funktion erweitert werden.  
Die Funktion ist vorgegeben und soll in eine bestehende Datei übernommen werden. Die Funktion soll anschließend in `main.py` importiert und an der richtigen Stelle aufgerufen werden.

### Aufgabenstellung
Erstelle die Funktion an einer passenden Stelle.

```python
def remove_physical_outliers(df, min_temp=-40.0, max_temp=50.0):
    return df[(df["temp"] >= min_temp) & (df["temp"] <= max_temp)]
```

### Idealpfad (nicht vorgeben)
- Datei `visualization.py` öffnen
- Geeignete Stelle im Code finden
- Funktionsdefinition manuell einfügen
- Autovervollständigung für Typannotationen, Variablen und Funktionen nutzen
- Syntax-Highlighting und Hinweise der IDE wahrnehmen
- Datei speichern
- Funktion in `main.py` importieren
- kontrollieren, ob das Programm das gewünschte Ergebnis liefert

### Misst
- Qualität der Autovervollständigung
- Lesbarkeit durch Syntax-Highlighting
- Unterstützung bei Typannotationen
- Fehler- und Warnhinweise während der Eingabe
- Schreibkomfort im Editor

---

## Teilaufgabe E – Versionierung (Git)

### Kontext
Das Projekt ist bereits als Git-Repository vorbereitet.  
Die vorgenommenen Änderungen sollen versioniert werden.

### Aufgabenstellung
Überprüfe den aktuellen Versionsstatus des Projekts und sichere deine Änderungen in einem Commit.  
Betrachte anschließend die vorgenommenen Änderungen.

### Idealpfad (nicht vorgeben)
- Git-Status in der IDE aufrufen
- Geänderte Dateien identifizieren
- Diff-Ansicht für mindestens eine Datei öffnen
- Commit mit aussagekräftiger Commit-Nachricht erstellen
- Optional: eine Änderung verwerfen oder rückgängig machen

### Misst
- Integration von Versionskontrolle in der IDE
- Verständlichkeit von Status- und Diff-Ansichten
- Usability des Commit-Workflows
- Unterstützung bei Revert/Discard-Aktionen
- Transparenz von Code-Änderungen

---
