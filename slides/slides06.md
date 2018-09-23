<!-- $theme: gaia -->
<!-- page_number: true -->

# Python-Schulung (6)

![](images/python-verwirrt.png)

# Objektorientierte Programmierung (OOP)

(cc) 2018: Jörg Kantel


---

### Python ist eine **objektorientierte** Programmiersprache.

- Das heißt, Python kennt **Klassen**, **Objekte** und **Methoden**
- Objekte können Eigenschaften an Unterobjekte **vererben**
- Und leider kennt Python auch die **Mehrfach-Vererbung**

---

### Klassen und Methoden

- Eine **Klasse** ist eine Objektdefinition. Sie definiert die Datenstrukturen und Methoden eines Objektes
- Eine Klasse »lebt« erst, wenn sie einem Objekt zugewiesen wurde
- Eine **Methode** ist einer Funktion   ähnlich, jedoch
    - werden Methoden *innerhalb* einer Klasse definiert und
    - die Syntax für den Aufruf einer Methode unterscheidet sich von der Syntax für den Aufruf einer Funktion

---

**Beispiel**: Die aus Processing bekannte Klasse *PVector* in Python (Auszug):

```python
import math

class PVector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y
        
    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
```

---

- Mit `class Klassenname()` wird eine Klassendefinition eingeleitet
- Wann `class Klassenname(object)` in Python 2.7 wirklich nötig ist, hat sich mir bisher nicht erschlossen. Es scheint so, daß es notwendig ist, wenn die Klasse einer *Oberklasse* sein soll
- Klassennamen werden per Konvention mit (mindestens) einem Großbuchstaben am Anfang geschrieben
- Die Methode `__init__(parameter)`  ist der *Konstruktor* einer Klasse (zwei Unterstriche rechts und links)

---

- Der Parameter `self` macht aus einer Funktion eine Methode. Er muß immer als *erster* Parameter übergeben werden.

Ein Objekt wird aus einer Klasse wie folgt erzeugt:

```python
location = PVector(100, 100)
velocity = PVector(1.0, 3.3)

location.add(velocity)
print(location.x, location.y)
```

- Im Gegenssatz zu einer Funktion werden Methoden durch die Punkt-Notation, zum Beispiel `location.add()` aufgerufen. 

---

- Das gilt auch für alle anderen Eigenschaften eines Objektes, sofern sie mit `self`  zur Objekteigenschaft erklärt wurden:

```python
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

* Der erste Parameter `self` wird also beim Aufruf mithilfe der Punktnotation vor dem Aufruf geschoben, aus *self* wird daher der Objektname:
   - `self.x`  -> `location.x`
   - `add(self)`  -> `location.add()`