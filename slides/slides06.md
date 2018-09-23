<!-- $theme: gaia -->
<!-- page_number: true -->

# Python-Schulung (6)

![](images/python-verwirrt.png)

# Objektorientierte Programmierung (OOP)

(cc) 2018: Jörg Kantel


---

## Python ist eine **objektorientierte** Programmiersprache.

- Das heißt, Python kennt **Klassen**, **Objekte** und **Methoden**
- Objekte können Eigenschaften an Unterobjekte **vererben**
- Und leider kennt Python auch die **Mehrfach-Vererbung**

---

## Benutzerdefinierte Typen

- Eine **Klasse** ist ein **benutzerdefinierter** Datentyp. Sie definiert die Datenstrukturen und Methoden eines Objektes
- Eine Klasse kann **Attribute** und **Methoden** besitzen
- Eine Klasse ist eine Fabrik zur Herstellung von Objekten, sie »lebt« erst, wenn sie einem Objekt zugewiesen wurde
- Eine Klasse benötigt einen **Konstruktur**

---

### Beispiel: Klasse »Punkt«

```python
class Punkt():

    # Konstruktor
    def __init__(self):
        self.x = 0
        self.y = 0

p = Punkt()
print(p.x)
print(p.y)
```
`p` ist ein Objekt, eine **Instanz** der Klasse `Punkt()`.

---

- Mit `class Klassenname()` wird eine Klassendefinition eingeleitet
- Wann `class Klassenname(object)` in Python 2.7 wirklich nötig ist, hat sich mir bisher nicht erschlossen. Es scheint so, daß es notwendig ist, wenn die Klasse einer *Oberklasse* sein soll
- Klassennamen werden per Konvention mit (mindestens) einem Großbuchstaben am Anfang geschrieben (hier ist auch der *CamelCase* üblich
- Die Methode `__init__(parameter)`  ist der *Konstruktor* einer Klasse (zwei Unterstriche rechts und links)

---

### Objekte sind veränderbar!

Der Zustand eines Objektes kann verändert werden, in dem zum Beispiel seinen Elmenten Werte zuweist:

```python
p.x = 4.0
p.y = 7.0

print(p.x)
print(p.y)
```
Diese Punktschreibweise ist der Auswahl einer Variablen aus einem Modul ähnlich, allerdings wird hier einem Element eines Objektes ein Wert zugewiesen. Diese Elemente bezeichnet man als **Attribute**.

---

## Objekte als Rückgabewerte

Objekte können als Rückgabewerte einer Funktion genutzt werden:

```python
def bewege_punkt(x, y):
    p = Punkt()
    p.x = x
    p.y = y
    return(p)

np = bewege_punkt(7.5, 3.0)
print(np.x)
print(np.y)
```
---

## Methoden

- Eine **Methode** ist einer Funktion   ähnlich, jedoch
    - werden Methoden *innerhalb* einer Klasse definiert und
    - die Syntax für den Aufruf einer Methode unterscheidet sich ebenfalls durch die Punktschreibweise von der Syntax für den Aufruf einer Funktion
- Auch der Konstruktur ist eine Methode

---

## Der Parameter `self`

Standardmäßig heitß der erste Parameter einer Methode `self`. Damit wird der Instanz der Klasse der Name des Objektes zugewiesen:

```python

erster_punkt = Punkt()   # self ist jetzt "erster_punkt"
print(erster_punkt.x)    # self.x

zweiter_punkt = Punkt()  # self ist jetzt "zweiter_punkt"
print(zweiter_punkt.x)   # self.x

```
---

## Methoden und `self`

- Der Parameter `self` macht aus einer Funktion eine Methode. Er muß immer als *erster* Parameter übergeben werden.

- Im Gegenssatz zu einer Funktion werden Methoden durch die Punktschreibweise aufgerufen.

---

```python

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, v):
        self.x += v.x
        self.y += v.y
    
    def print_vector(self):
        print("(" + str(self.x) + ", " + str(self.y) + ")")

p1 = Vector(3, 4)
p2 = Vector(5.0, 7.3)
p1.add(p2)
p1.print_vector()

```

---

- Das gilt auch für alle anderen Eigenschaften eines Objektes, sofern sie mit `self`  zur Objekteigenschaft erklärt wurden:

* Der erste Parameter `self` wird also beim Aufruf mithilfe der Punktnotation vor dem Aufruf geschoben, aus *self* wird daher der Objektname:
   - `self.x`  -> `p1.x`
   - `add(self, v)`  -> `p1.add(p2)`

---

## Die Methode `__str__()`

`__str__()` ist wie `__init__()` eine besondere Methode und soll die String-Repräsentation eines Objektes zurückgeben.

Damit können wir das obige Beispiel vereinfachen:

---

```python

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, v):
        self.x += v.x
        self.y += v.y
    
    def __str__(self):
        return("(" + str(self.x) + ", " + str(self.y) + ")")

p1 = Vector(3, 4)
p2 = Vector(5.0, 7.3)
p1.add(p2)
print(p1)

```
---

## Operator-Überladung

Nun stört an dem Beispiel nur noch die Methode `add()`. Es wäre doch viel einleuchtender, hier `p1 + p2` schreiben zu können. Durch die Definition zusätzlicher, spezieller Methoden, kann das Verhalten von Operatoren mit benutzerdefinierten Typen (Klassen) bestimmt werden.

Wenn also für die Klasse Vektor die spezielle Methode `__add__()` definiert wird:

---

```python

class Vector():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return(self)
    
    def __str__(self):
        return("(" + str(self.x) + ", " + str(self.y) + ")")
```
---

Kann man schreiben:
```python
p1 = Vector(3, 4)
p2 = Vector(5.0, 7.3)
p3 = p1 + p2
print(p3)
print(type(p3))

```

Wenn das Verhalten eines Operators so verändert wird, daß es mit benutzerdefinierten Objekten funktioniert, spricht man von **Operator-Überladung**.

---

Für jeden Operator gibt es in Python eine entsprechende spezielle Funktion. Sie sind in der Dokumentation unter <https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types> zu finden. Die wichtigsten (mathematischen) sind:

```python
object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
```
---

## Vererbung

Unter **Vererbung** versteht man die Möglichkeit