<!-- $theme: gaia -->
<!-- page_number: true -->


# Python Schulung (2)

![](images/python-verwirrt.png)

## Ein Parforceritt durch die Sprache

(cc) 2018: Jörg Kantel

---


## Das heutige Programm

- Werte und Datentypen
- Variablen und Operatoren
- Kommentare
- Funktionen mit und ohne Parameter
- Boolsche Ausdrücke und logische Operatoren
- Verzweigungen
- Schleifen

---

## Werte und Datentypen

- Ein **Wert** ist das grundlegende Ding, mit denen ein Programm arbeitet, etwa **Buchstaben** (Zeichenketten) oder **Zahlen**.
- Diese Werte gehören **Datentypen** an, Zeichenketten sind vom Typ `string`, Zahlen können zum Beispiel vom Typ `int` (Integer, ganze Zahl) oder `float` (Fließkommazahl) sein.
- Mit dem Befehl `type` gibt der Interpreter den Typen aus.

---

    type("Hallo Welt!")
<class 'str'>

    type(17)
<class 'int'>

    type(1.414)
<class 'float'>

---

**Aber**:

    type("17")
<class 'str'>

**Und**:

    type('Hallo Welt!')
<class 'str'>

`Strings`  können entweder in einfachen (' ') oder doppelten (" ") Hochkommata eingeschlossen sein.

---

## Variablen

- Eine **Variable** ist ein »Container«, der sich auf einen Wert bezieht
- Durch die **Zuweisung** wird eine neue Variable erstellt, ihr wird ein Wert zugewiesen:

 
     meldung = "Und nun etwas ganz anderes"
     print(meldung)
     n = 17
     print(n)
     n = 3.14159
     print(n)
 
 ---
 
 ## Doch Vorsicht:
 
     plz = 02492
 
 gibt eine Fehlermeldung! Aber probiert mal
 
    oct = 0o235
    print(oct)
    hex = 0xff
    print(hex)
    bin = 0b110011
    print(bin)
    
---

## Type- Casting

    a = "17"
    b = int(a) + 4
    print(b)
    
Folgende Casting-Kommandos stehen zur Verfügung:

- `int()` macht aus einem String oder einem Float einen Integer-Wert
- `float()` macht aus einem String oder einem Integer eine Fließkommazahl
- `string()` versucht aus allem, was ihm unter die Finger kommt, eine Zeichenkette zu machen

---

#### Beispiele
    a = 17
    b = float(a) + 2
    print(b)

Hier greift das *Duck-Typing*, aus `2` wird ein *float*.

    a = "4711"
    b = int(a)*2
    print(b)

Aber:

    a = "4711"
    b = a*2
    print(b)

---
 
## Gültige Variablennamen

Ein **Bezeichner** in Python ist ein Name um Variablen, Module, Klassen, Funktionen oder andere Objekte eindeutig zu benennen. Ein Bezeichner kann aus folgenden Zeichen bestehen:

- Großbuchstaben A-Z
- Kleinbuchstaben a-z
- Unterstrich _
- Die Zahlen 0 bis 9 (jedoch nicht an erster Stelle)

---

- **Groß- und Kleinschreibung** zählt, das heißt `myNumber`und `Mynumber` sind verschiedene Namen.

- Seit Python 3 wird **Unicode** unterstützt. Somit kann der Bezeichner auch Unicode-Zeichen enthalten. Die Länge eines Bezeichners ist nicht begrenzt. Das heißt, daß dies gültige Bezeichner sind:


    maximum_height_from_january_1920_to_december_2017 = 100
    υψος = 10
    μεγιστη_υψος = 100



---

## Konventionen

Im **PEP8** *(Python Enhancement Proposal 8)* gibt es einen *Style Guide* für Python-Code. Der empfiehlt (unter anderem):

- Den Unterstrich als Worttrenner: `maximum_height`
- Also kein CamelCase: `maximumHeight`
- Variablen und Funktions-/Methodennamen beginnen mit einem Kleinbuchstaben und Klassen mit einem Großbuchstaben
- Konstanten werden komplett großgeschrieben: `HEIGHT`

---

## Operatoren

- Die Operatoren `+`, `-`, `*`, `/` und `**` stehen für Addition, Substraktion, Multiplikation, Division und Potenzen. Doch Vorsicht in Python 2, dort ergibt


    minute = 59
    minute/60

nicht unbedingt das, was Ihr erwartet, besser ist

    minute = 59
    minute/60.0

---

## Ganzzahl-Division und der Modulo-Operator

- In Python 3 wird dieses Verhalten der Integer-Division durch diesen Operator `//` erreicht:


    minute = 59
    minute//60

- Als Gegenstück gibt es in Python 2 *und* Python 3 den Modulo-Operator `%`


    minute = 59
    minute%60
    
---

## Rangfolge von Operatoren

- Klammern `()` haben den höchsten Rang
- Danach Exponenten `**`
- Danach Multiplikation `*` und Division `/`
- Danach Addition `+` und Subtraktion `-`
- Operatoren gleichen Ranges werden von links nach rechts abgearbeitet.
- Ich mache mir darüber aber selten Gedanken, im Zweifel verwende ich »Sicherheitsklammern«.

---

## String-Operatoren

- Python-Strings können mit `+` und `*` umgehen, *nicht* jedoch mit `-` und `/`:


    erster = "pangalaktischer "
    zweiter = "Donnergurgler"
    print(erster + zweiter)


    print("Spam"*3)

---

## Kommentare

**Kommentare** beginnen mit einem Doppelkreuz `#`, alles was hinter `#` steht, wird vom Interpreter ignoriert:

    # Das ist ein ganzzeiliger Kommentar
    y = math.cos(x)  # Hier wird der Cosinus von x berechnet


Einige Kommentare zu Beginn einer Programmdatei haben eine besondere Bedeutung:


    #!/usr/local/bin/python
    # coding=utf-8
    
---

## Funktionen

- Funktionen können *mit* und/oder *ohne* Parameter aufgerufen werden.
- Mehrere Parameter werden durch Kommata getrennt.


    import turtle
    import math
    tess = turtle.Turtle()
    tess.penup()
    x = 2.5
    y = math.cos(x)
    print("I got it, Babe, the cosine from x is ", y)

---

## Funktionen erstellen

(Selbstgeschriebene) Funktionen werden mit `def` definiert:


    def search_spring():
        print("Veronika, der Lenz ist da.")
        print("Die Mädchen singen trallala.")
    
    search_spring()
    
Der Doppelpunkt `:` am Ende der ersten Zeile ist genau so wichtig, wie die Einrückungen darunter!

---

Funktionen können andere Funktionen aufrufen:


    def sing_twice():
        search_spring()
        search_spring()
    
    sing_twice()

---

## Parameter

Stellt Euch diese Funktion vor:


    def print_twice(peter):
        print(peter)
        print(peter)

Und versucht dann folgendes:

    print_twice("Spam")
    print_twice(127)
    import math
    print_twice(math.pi)
    
---

### Funktionen mit mehreren Parametern

    def mult3(a, b, c):
        ergebnis = a*b*c
        print("Die Multiplikation ergibt: ", ergebnis)
    
    mult3(2, 3, 4)
Oder:

    def mult_word(s, a):
        print(s*a)
    
    mult_word("SPAM", 3)

---

### Funktionen mit optionalen Parametern

    def print_vektor(x, y, z=0):
        if z == 0:
            print(x, y)
        else:
            print(x, y, z)
    
    print_vektor(3, 5)
    print_vektor(6, 6, 6)

---

Innerhalb einer Funktion sind Variablen und Paramter **lokal**:

    my_supernumber = 333
    
    def add_number(my_supernumber):
        print(my_supernumber)
        my_supernumber += my_supernumber
        print("The number of the beast is ", my_supernumber)
    
    add_number(my_supernumber)
    print("But my Supernumber is still ", my_supernumber)

**Anmerkung**

- `x += n` ist eine Abkürtzung für `x = x + n`.
- Das gilt auch für `x -= n`,  `x *= n` und `x /= n`.

---

# Funktionen mit Rückgabewert

    def double(x):
        return(2*x)
        
    x = 10
    y = double(x)
    print(y)

- `return()` ist die Schlüsselfunktion!
- Ähnlich wie `print` konnte in Python 2.x auch `return` ohne Klammern aufgerufen werden.


---

## Import von Modulen

Erlaubt sind:

    import math
    import numpy as np
    from mygames_framework import Sprite
    

Verboten ist:

    from numpy import *

Auch wenn Ihr das häufig in der Literatur seht, das verschmutzt nur den Namensraum!!!

---

# Fragen?




    

    