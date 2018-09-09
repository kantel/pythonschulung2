<!-- $theme: gaia -->
<!-- page_number: true -->


# Python Schulung (3)

![](images/python-verwirrt.png)

## Immer noch ein Parforceritt durch die Sprache

(cc) 2018: Jörg Kantel

---

## Das heutige Programm

- Boolsche Ausdrücke und logische Operatoren
- Verzweigungen
- Schleifen
- Strings (noch einmal, denn Zeichenketten sind sowohl Datentypen wie auch Datenstrukturen)
- Listen (die wichtigsten Datentypen in Python überhaupt)

---

## Boolsche Ausdrücke

Python kennt diese boolschen Operatoren:

- `x == y`: x ist **gleich** y
- `x != y`: x ist **ungleich** y
- `x > y`: x ist **größer** y
- `x < y`: x ist **kleiner** y
- `x >= y`: x ist **größer gleich** y
- `x <= y`: x ist **kleiner gleich** y

---

## Logische Operatoren

- Es gibt drei logische Operatoren, mit denen boolsche Ausdrücke kombiniert werden können, `and`, `or` und `not`.
- Das Ergebnis von boolschen und logischen Operatoren ist immer `True` (wahr) oder `False` (falsch).

---

## Boolsche Funktionen

Funktionen können auch Wahrheitswerte liefern:

    def ist_teilbar(x, y):
        if x%y == 0:
            return(True)
        else:
            return(False)

oder:

    def is_even(x):
        if x%2 == 0:
            return(True)
        else:
            return(False)
    

---

## Verzweigungen

- Mit Hilfe der logischen und boolschen Operatoren können **Verzweigungen** programmiert werden:


    if x > 0:
       print("x ist positiv")
    else:
        print("x ist negativ oder null")

Oder auch:

    if x%2 == 0:
        print("x ist gerade")
    else:
        print("x ist ungerade")


---

## Verkettete Bedingungen

Manchmal gibt es mehr als zwei Möglichkeiten:

    if x < y:
        print("x ist kleiner als y")
    elif x > y:
        print("x ist größer als y")
    elif x == y:
        print("x ist gleich y")
    else:
        print("Das Ende des Universums ist nahe!")

`elif` steht für `else if`.

---

## Rekursion

Eine Funktion darf nicht nur eine andere Funktion, sondern auch sich selber aufrufen. Dies nennt man eine **Rekursion**:

    def countdown(n):
        if n <= 0:
            print("Whammm … 💥💥💥!!")
        else:
            print(n)
            countdown(n-1)

# 💥
       
---

## Schleifen

Die `while`-Schleife ist eigentlich die einzige Schleife, die man braucht. Beispiel:

    def countdown(n):
        while n > 0:
            print(n)
            n -= 1
        print(""Whammm … 💥💥💥!!")
    
    countdown(10)

# 💥

---

## Die Endlos-Schleife

    while True:
        print("From here to internity")
        # Hektische Suche nach dem Kill-Befehl

Die Endlos-Schleife ist aber nicht immer ein Programmfehler, sie wird zum Beispiel benutzt

- bei einem Server (der soll schließlich »immer« laufen)
- bei GUIs und/oder Spielen (warte auf Benutzer-Eingaben)

---

## Callback (Ruf uns nicht an, wir rufen zurück)

    def exit_prog():
        global keepGoing
        keepGoing = False
    
    t.listen()
    t.onkey(exit_prog, "Escape") # Escape beendet Programm
    
    keepGoing = True
    while keepGoing:
        pass  # Mache irgendetwas

(Beispielprogramm: `particle1.py` in `turtlepy`.)
        
---

## Die `for`-Schleife

Python kennt noch die `for`-Schleife:

    for i in range(10):
        print(i)

Der Endwert ist »exklusiv« (mathematisch gesprochen wird das halboffene Intervall `[0 … 10[` abgearbeitet, das heißt die Schleife zählt von Null bis Neun.
 
---

Die `for`-Schleife kann natürlich auch rückwärts zählen:

    for i in range(10, 0, -1):
        print(i)

- Beachtet dabei, daß auch hier der Endwert exklusiv ist, die Schleife also von 10 bis 1 rückwärts zählt.
- Es gibt auch noch eine Abwandlung der `for`-Schleife für Strings und Listen. Dazu später mehr.

---

## Die `range()`-Funktion

    for identifier in range([start, ] stop [, step])

Dabei gilt:

- Alle Parameter sind Integer
- Alle Parameter können positiv oder negativ sein
- Wie alles in Python beginnt der Index mit `0`, daher ist der Stop-Wert »exklusiv«:


    for i in range(5, 10):
        print i

---

## Die `range()`-Funktion (2)

In Python 2.x gab es noch eine `xrange()`-Funktion. Der Unterschied war:

- `range()` gab als Ergebnis eine Liste zurück
- `xrange()` gab als Ergebnis einen `iterator` zurück

In Python 3 wurde `xrange()` zu `range()`  und das originale `range()` als veraltet erklärt *(deprecated)*, das heißt `range()` liefert nun immmer einen `iterator` zurück.

---

## Das war es mit den Grundlagen

Ihr kennt nun die grundlegenden Abläufe eines Programms:

- Sequenzen (werden von oben nach unten abgearbeitet)
- Verzweigung (entweder dies oder das)
- Schleifen (Mehrfachdurchläufe)

---

## Das war es mit den Grundlagen (2)

Und die wichtigsten einfachen Datentypen:

- Zahlen (Integer und Float)
- Zeichenketten in ihrer einfachsten Form (sie werden noch einmal bei den Datenstrukturen behandelt)
- Boolsche Werte und Ausdrücke

Somit seid Ihr in der Lage, einfache Python-Programme selber zu schreiben. 😎

Legen wir mal los …

---

## Ein Template für die Schildkröte

    import turtle as t

	wn = t.Screen()
	wn.colormode(255)
	wn.bgcolor(43, 62, 80)
	wn.setup(width = 600, height = 600)
	wn.title("Ein Super-Duper Turtle-Programm")
    
    alex = t.Turtle()
    
    # Hier kommt jetzt Euer Programm-Code hin
    
    wn.mainloop()

---

# Eine selbstgeschriebene Funktion mit der Turtle

    def quadrat(t):
        for i in range(4):
        	t.forward(100)
            t.left(90)
    
    alex.pensize(2)
    alex.pencolor("red")
    quadrat(alex)

---

Es können aber auch mehrere Schildkröten diese Funktion benutzen:

    berta = t.Turtle()
    berta.pensize(2)
    berta.pencolor("white")
    berta.goto(-100, 0)
    
    quadrat(berta)

---

Und wie wäre es mit einem Polygon?

    def polygon(t, n, length):
        angle = 360.0/n
        for i in range(n):
            t.forward(length)
            t.left(angle)
        
    polygon(alex, 7, 70)


---

Oder mit einem Kreis?

    import math
    
    def circle(t, r):
        circum = 2*math.pi*r
        # n = 50
        n = int(circum/3) + 1
        length = circum/n
        polygon(t, n, length)



---

## Datenstrukturen (1)

- Strings (noch einmal, denn Zeichenketten sind sowohl Datentypen wie auch Datenstrukturen)
- Listen (die wichtigsten Datentypen in Python überhaupt)
- Dictionairies (Hash-Tables) -- nächste Woche
- Tupel -- nächste Woche
- Persistenz (Lesen und Schreiben von Dateien) -- nächste Woche

---

## Strings

Ein String ist eine Folge von Zeichen. Auf die einzelnen Zeichen kann man mit dem (eckigen) Klammer-Operator zugreifen:

    frucht = "Banane"
    zeichen = frucht[1]
    print(zeichen)

Den Ausdruck in den eckigen Klammern nennt man `Index`. Ein Index beginnt immer mit `0`.
Der Indexwert kann berechnet werden, muß aber immer ein `Integer`-Wert sein.

---

`len` liefert die Anzahl der Zeichen eines Strings.

    frucht = "Banane"
    print(len(frucht))
 
 Aber dieses ergibt einen Fehler:
 
     laenge = len(frucht)
     letzter_buchstabe = frucht[laenge]
 
 Richtig ist:
 
     letzter_buchstabe = frucht[laenge - 1]
     print(letzter_buchstabe)
 
 ---
 
 ### Traversierung mit einer Schleife
 
     i = 0
     while i < len(frucht):
         zeichen = frucht[i]
         print(zeichen)
         i += 1
 Oder (einfacher):
 
     for zeichen in frucht:
         print(zeichen)
 
 ---
 
### Enten

In Robert McCloskeys Buch *[Make Way for Ducklings](https://de.wikipedia.org/wiki/Make_Way_for_Ducklings)* gibt es Entchen mit den Namen Jack, Kack, Lack, Mack, Nack, Ouack, Pack und Quack:

    suffix = "ack"
    praefixe = "JKLMNOPQ"
    for praefix in praefixe:
        if praefix == "O" or praefix == "Q":
            print(praefix + "u" + suffix)
        else:
            print(praefix + suffix)
---

### String-Teile

    s = "Monty Python"
    print(s[0:5])
    print(s[6:12])
    
Der Operator `[n:m]` gibt den Teil des Strings vom »n-ten« bis zum »m-ten« Zeichen zurück und zwar einschließlich des ersten, aber ausschließlich des letzten Zeichens. Auch hier gilt wieder das halboffene Intervall `[n, m[`.  

---

### Slices

    frucht = "banane"
    print(frucht[:3])
    print(frucht[3:])
    print(frucht[:])
    print(frucht[-1])
    
Wird der erste Index vor dem Doppelpunkt weggelassen, beginnt das Slice am Anfang des Strings, wird der zweite Index weggelassen, reicht das Slice bis zum Ende des Strings.

Negative Indizes zählen von hinten.

---

### Strings sind unveränderlich (immutable)

Man kann aus »Jörg« kein »Jürg« machen:

    name = "Jörg"
    name[1] = "ü"
    TypeError: 'str' object does not support item assignment

Man muß stattdessen einen neuen String erzeugen:

    neuer_name = name[0] + "ü" + name[2:]
    print(neuer_name)

---

### String-Methoden

Diese Methode spricht für sich:

    frucht = "banane"
    neue_frucht = frucht.upper()

Man kann in Strings auch suchen:

    frucht = "banane"
    i = frucht.find("a")
    print(i)
    
Die Methode find gibt immer die erste Position im String zurück, wo der zu suchende Teilstring gefunden wurde, andernfalls `-1`.

---

Man kann in Strings auch Teilstrings suchen:

    i = frucht.find("na")
    print(i)

Als zweites Argument kann man optional den Startindex angeben:

    i = frucht.find("na", 3)
    print(i)
    
Und als drittes Argument kann man den Index angeben, an dem die Suche beendet werden soll:

    frucht.find("e", 1, 4)
    print(i)

---

### Der in-Operator

Das Wort `in` ist ein Boolscher Operator, der zwei Strings erwartet und `True` zurückliefert, wenn der erste als Teilstring im zweiten vorkommt:

    print("a" in frucht)
    print("samen" in frucht)

Beispiel:

    def in_beiden(wort1, wort2):
        for zeichen in wort1:
            if zeichen in wort2:
                print(zeichen)
                
    in_beiden("apfel", "orange")

---


### Fragen?
 
