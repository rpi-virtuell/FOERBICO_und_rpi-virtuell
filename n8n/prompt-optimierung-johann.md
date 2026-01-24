# Analyse & Verbesserungsvorschläge für deinen Prompt
(mit Claude Haiku 4.5)

Dein Prompt hat eine **solide Grundstruktur**, aber es gibt mehrere Punkte, wo präzisere Anweisungen bessere Ergebnisse bringen würden:

## 🔴 Kritische Schwachstellen

### 1. **Zu vage Persona-Definition**
**Problem:** Die Personas sind zu kurz und zu undifferenziert. Eine Erzieher*in mit 10 Jahren Erfahrung hat andere Bedürfnisse als eine Quereinsteiger*in.

**Lösung:** Erweitere jede Persona um:
- **Erfahrungslevel** (Anfänger, Praktiker, Experte)
- **Konkrete Constraints** (Zeit, Ressourcen, Gruppengröße)
- **Sprachliche Marker** (Was sagt die Person zu sich selbst? Was sind ihre Pain Points?)

**Beispiel für "Religionslehrer*in GS":**
```
- Unterrichtet 2–3 Klassen parallel
- Hat 45–90 Min. Zeit pro Unterrichtseinheit
- Sucht schnell umsetzbare Ideen ohne lange Vorbereitung
- Möchte theologische Tiefe, aber für 8–10 Jährige verständlich
- Nervt: zu akademische Vorschläge, unrealistische Ressourcenangaben
```

### 2. **Unklare Bedingungslogik in "Praktische Umsetzung"**
**Problem:** Die FALLS-Bedingungen sind zu schwammig. Was ist eine "Anleitung"? Wie unterscheidest du zwischen vollständig und teilweise?

**Lösung:**
```
FALLS material.verlaufsplan UND material.verlaufsplan.length > 200:
  → Nutze den vorhandenen Plan, ergänze um 1-2 Reflexionsfragen

FALLS material.methodische_hinweise existiert:
  → Strukturiere diese in 5 aufeinanderfolgende Phasen

SONST:
  → Generiere eine Ideenbox basierend auf:
     - material.zielgruppe → passende Methoden
     - material.themen → thematische Ankerpunkte
     - material.content → konkrete Schnittstellen identifizieren
```

### 3. **"Ideenbox" ist unterkonzeptualisiert**
**Problem:** 3–5 Methoden ist viel für die Hand einer Fachkraft. Zu viel Auswahl = Entscheidungsparalyse.

**Lösung:**
- Gib **eine Primärmethode** (für Standardfall)
- + **2 Alternativmethoden** (für unterschiedliche Gruppentypen: heterogen, online, mit Trauma-Sensibilität)
- Mache **explizit**, welche Methode wie lange dauert und welche Ressourcen nötig sind

### 4. **Differenzierung ist zu generisch**
**Problem:** "Leichte Sprache" oder "alternative Materialien" sagen wenig aus. Jede*r weiß das.

**Lösung:** Verlange **konkrete Differenzierungsbeispiele** für JEDE vorgeschlagene Methode:
```
**Methode X – Differenzierungsvarianten:**
- Für Kinder mit Lese-/Schreibschwierigkeiten: [konkrete Alternative]
- Für sehr stille/zurückhaltende Kinder: [Rollenvariante oder Einzelarbeit]
- Für Hochbegabte/Schnellere: [Tiefergehende Frage/Extension]
```

### 5. **"Material-Check" hat keine klare Gewichtung**
**Problem:** Alle Qualitätskriterien werden gleich behandelt, aber nicht alle sind gleich wichtig.

**Lösung:**
- Definiere **Knockout-Kriterien** (z.B. „Ist das Material diskriminierungsfrei?")
- Unterscheide **Must-haves** (z.B. theologische Korrektheit) von **Nice-to-haves** (z.B. ästhetische Aufbereitung)

### 6. **Fehlende Kontextinformation**
**Problem:** Der Prompt ignoriert, dass `material.bildungsstufen` und `material.zielgruppen` **unterschiedliche Logiken erfordern**:
- Eine Kita-Gruppe hat Gemeinsamkeiten (Altersgruppe), aber auch **unterschiedliche Förderbedarfe**
- Eine Förderschule braucht ganz andere Zugänge als ein Gymnasium

**Lösung:** Füge dieser Logik hinzu:
```
Wenn altersstufen = [3–6] UND zielgruppen = ["Kinder mit Behinderungen"]:
  → Nutze sensorische Zugänge, verkürze Konzentrationsphasen,
     ergänze Gebärdensprache-Hinweise
```

## 🟡 Mittlere Verbesserungen

### 7. **Überschriften sind zu starr**
Die Struktur ist gut, aber es könnten **aussagekräftigere, dynamischere Titel** sein:
```
Statt:  "Praktische Umsetzung"
Besser: "Stundenentwurf im 2er-Format: Einstieg (10 Min) → Erarbeitung (25 Min) → Abschluss (10 Min)"
```

### 8. **Fehlende "Vorab-Checkliste"**
Eine schnelle Frage wie *"Habe ich alle Materialien? Passt die Zeit?"* am Anfang hilft.

### 9. **"Weiterführende Ressourcen"** könnten **annotiert** sein
Statt nur Links: erkläre kurz, **warum** diese Ressource konkret hilft (z.B. „für Lehrkräfte ohne theologischen Hintergrund", „für die Vor- und Nachbereitung zuhause").

## ✅ Was funktioniert gut

- ✓ Persona-Ansatz ist richtig (Ton anpassen)
- ✓ Qualitätskriterien-Check ist ein plus
- ✓ Fokus auf "Fallstricke & Chancen" ist pädagogisch wertvoll
- ✓ Markdown-Nutzung ist übersichtlich

---

## 📋 Konkrete Rewrite-Empfehlungen

**Würde ich so adjustieren:**

```markdown
### Neue Struktur:

1. **Vorab-Checkliste** (30 Sekunden)
   - Materialien verfügbar? Zeit verfügbar? Gruppenkonstellation?

2. **Kurzüberblick & Relevanz** (wie jetzt, aber prägnanter)

3. **Theologische Verankerung** (wie jetzt)

4. **Praktische Umsetzung – mit Falllogik**
   - IF vollständiger Plan → Fasse + ergänze
   - ELSE → Primärmethode + 2 Alternativen (mit Zeitangaben!)

5. **Detaillierte Differenzierung** (nicht generisch)
   - Pro Methode: 2–3 konkrete Varianten

6. **Gewichteter Material-Check**
   - Knockout-Kriterien zuerst
   - Dann: Must-haves / Nice-to-haves

7. **Fallstricke & Chancen** (wie jetzt)

8. **Annotierte Ressourcen** (mit Begründungen)
```

---

## 🎯 **Warum diese Verbesserungen besser funktionieren**

| Problem | Warum es jetzt suboptimal ist | Wie Verbesserung hilft |
|---------|------|---------|
| Vage Personas | Fachkraft weiß nicht, ob Vorschlag zu ihr passt | Konkrete Realitätsabgleichung ist möglich |
| Zu viele Methoden | Auswahl-Paralysis, Unsicherheit | Fokus auf die beste Option + Alternativen |
| Generische Differenzierung | Nicht konkret umsetzbar | Handlungsanweisungen für reale Situationen |
| Alle Qualitätskriterien gleichgewichtig | Wichtiges wird übersehen | Priorisierung macht schnelle Entscheidungen möglich |
| Fehlende Zeitangaben | Unrealistische Erwartungen | Zeitbudget wird realistisch geplant |

Möchtest du, dass ich dir eine **vollständig überarbeitete Version** deines Prompts schreibe?