# LEZIONE 30 - ESERCITAZIONI
## Magic Methods e Operatori Speciali

**Modalità:** Individuale | **Durata:** 2 ore (60 min guidate + 60 min autonome)

---

## 📋 ESERCITAZIONI GUIDATE (60 minuti)

### Esercizio 1 - Classe Frazione con Operatori (20 minuti)

#### Descrizione
Creare una classe `Frazione` che rappresenta frazioni matematiche con operatori aritmetici.

#### Requisiti

**Classe Frazione:**
- `__init__(self, numeratore, denominatore)`
  - Valida denominatore != 0
  - Semplifica frazione (usa MCD)

- `__str__(self)` e `__repr__(self)`
  - `__str__`: "3/4"
  - `__repr__`: "Frazione(3, 4)"

- `__add__(self, other)` per +
  - a/b + c/d = (ad + bc) / bd
  - Semplifica risultato

- `__sub__(self, other)` per -
  - a/b - c/d = (ad - bc) / bd

- `__mul__(self, other)` per *
  - a/b * c/d = ac / bd

- `__truediv__(self, other)` per /
  - a/b / c/d = ad / bc

- `__eq__(self, other)` per ==
  - Confronta frazioni semplificate

- `to_float(self)`
  - Converte in decimale

#### Esempio di Utilizzo
```python
f1 = Frazione(1, 2)
f2 = Frazione(1, 3)

print(f1 + f2)  # 5/6
print(f1 - f2)  # 1/6
print(f1 * f2)  # 1/6
print(f1 / f2)  # 3/2

print(f1 == Frazione(2, 4))  # True (semplificate uguali)
print(f1.to_float())  # 0.5
```

#### Output Atteso
```
5/6
1/6
1/6
3/2
True
0.5
```

#### Hint MCD (Massimo Comun Divisore)
```python
import math

def mcd(a, b):
    return math.gcd(abs(a), abs(b))

# Semplificazione
def semplifica(num, den):
    divisore = mcd(num, den)
    return num // divisore, den // divisore
```

---

### Esercizio 2 - Matrice con Accesso [i][j] (20 minuti)

#### Descrizione
Creare classe `Matrice` che supporta accesso elementi con notazione `mat[i][j]`.

#### Requisiti

**Classe Matrice:**
- `__init__(self, righe, colonne, valore_default=0)`
  - Crea matrice righe × colonne
  - Inizializza con valore_default

- `__getitem__(self, index)`
  - Restituisce riga (che supporta a sua volta [j])
  - Supporta mat[i][j]

- `__setitem__(self, index, valore)`
  - Imposta intera riga
  - mat[i] = [1, 2, 3]

- `__str__(self)`
  - Visualizzazione formattata
  - Una riga per line

- `__len__(self)`
  - Restituisce numero righe

- `dimensioni(self)`
  - Restituisce tupla (righe, colonne)

- `trasposta(self)`
  - Restituisce matrice trasposta

#### Esempio di Utilizzo
```python
mat = Matrice(3, 3)

# Imposta valori
mat[0][0] = 1
mat[0][1] = 2
mat[0][2] = 3
mat[1] = [4, 5, 6]
mat[2] = [7, 8, 9]

print(mat)
print(f"Elemento [1][1]: {mat[1][1]}")  # 5
print(f"Dimensioni: {mat.dimensioni()}")  # (3, 3)

# Trasposta
mat_t = mat.trasposta()
print("Trasposta:")
print(mat_t)
```

#### Output Atteso
```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

Elemento [1][1]: 5
Dimensioni: (3, 3)

Trasposta:
[1, 4, 7]
[2, 5, 8]
[3, 6, 9]
```

#### Hint Implementazione
- Usa lista di liste internamente: `self._data = [[0]*cols for _ in range(rows)]`
- `__getitem__` restituisce `self._data[index]` (che è lista, quindi supporta [j])
- Per trasposta: `[[self._data[j][i] for j in range(righe)] for i in range(colonne)]`

---

### Esercizio 3 - DatabaseConnection Context Manager (20 minuti)

#### Descrizione
Creare context manager per simulare connessione database con gestione automatica apertura/chiusura.

#### Requisiti

**Classe DatabaseConnection:**
- `__init__(self, db_name)`
  - Salva nome database
  - `connected = False`

- `__enter__(self)`
  - Simula apertura connessione
  - Stampa messaggio
  - Imposta `connected = True`
  - Restituisce self

- `__exit__(self, exc_type, exc_val, exc_tb)`
  - Simula chiusura connessione
  - Stampa messaggio (anche se errore)
  - Imposta `connected = False`
  - Se eccezione: log e propaga

- `query(self, sql)`
  - Verifica `connected == True`
  - Simula esecuzione query
  - Restituisce risultato fake

- `execute(self, sql)`
  - Simula comando (INSERT, UPDATE, DELETE)

#### Esempio di Utilizzo
```python
# Uso corretto
with DatabaseConnection("mydb") as db:
    risultato = db.query("SELECT * FROM users")
    print(f"Risultati: {risultato}")
    db.execute("INSERT INTO users VALUES (...)")

# Connessione chiusa automaticamente

# Uso con eccezione
try:
    with DatabaseConnection("mydb") as db:
        db.query("SELECT * FROM users")
        raise ValueError("Errore simulato")
        db.query("Non eseguita")
except ValueError:
    print("Eccezione gestita, ma DB chiuso correttamente")
```

#### Output Atteso
```
🔌 Connessione a 'mydb' aperta
Esecuzione query: SELECT * FROM users
Risultati: [{'id': 1, 'nome': 'Test'}]
Esecuzione comando: INSERT INTO users VALUES (...)
🔌 Connessione a 'mydb' chiusa

🔌 Connessione a 'mydb' aperta
Esecuzione query: SELECT * FROM users
⚠️ Errore durante connessione: Errore simulato
🔌 Connessione a 'mydb' chiusa
Eccezione gestita, ma DB chiuso correttamente
```

#### Hint __exit__
```python
def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is not None:
        print(f"⚠️ Errore durante connessione: {exc_val}")
    
    print(f"🔌 Connessione a '{self.db_name}' chiusa")
    self.connected = False
    
    return False  # Propaga eccezione (non sopprime)
```

---

## 🎯 ESERCITAZIONI AUTONOME (60 minuti)

### Esercizio 4 - Classe Money con Operazioni (20 minuti)

#### Descrizione
Creare classe per gestire valori monetari con operatori e conversioni valute.

#### Requisiti

**Classe Money:**
- `__init__(self, importo, valuta="EUR")`
  - importo: float
  - valuta: stringa (EUR, USD, GBP)

- `__str__(self)` → "€25.50", "$100.00", "£50.00"

- `__repr__(self)` → "Money(25.5, 'EUR')"

- `__add__(self, other)` 
  - Somma solo se stessa valuta
  - Altrimenti raise ValueError

- `__sub__(self, other)`
  - Sottrazione (stessa valuta)

- `__mul__(self, scalar)`
  - Moltiplicazione per numero
  - Money(10, 'EUR') * 2 = Money(20, 'EUR')

- `__eq__(self, other)`, `__lt__(self, other)`
  - Confronto (stessa valuta)

- `__bool__(self)`
  - False se importo == 0

- `converti_in(self, nuova_valuta, tassi)`
  - Converte usando dizionario tassi
  - Restituisce nuovo Money

#### Test
```python
m1 = Money(100, "EUR")
m2 = Money(50, "EUR")
m3 = Money(75, "USD")

print(m1 + m2)  # €150.00
print(m1 - m2)  # €50.00
print(m1 * 1.5)  # €150.00

print(m1 > m2)  # True
print(bool(Money(0, "EUR")))  # False

tassi = {"EUR": 1.0, "USD": 1.1, "GBP": 0.85}
m_usd = m1.converti_in("USD", tassi)
print(m_usd)  # $110.00
```

---

### Esercizio 5 - Custom List Ordinabile (20 minuti)

#### Descrizione
Creare lista custom con operazioni lista e ordinamento.

#### Requisiti

**Classe SortedList:**
- `__init__(self, items=None)`
  - Inizializza con lista opzionale

- `__len__(self)`, `__getitem__(self, index)`, `__setitem__(self, index, value)`
  - Comportamento lista base

- `__contains__(self, item)`
  - Supporta `item in lista`

- `__iter__(self)`
  - Supporta for loop

- `__str__(self)` e `__repr__(self)`

- `append(self, item)`
  - Aggiunge elemento

- `remove(self, item)`
  - Rimuove elemento

- `sort(self, reverse=False)`
  - Ordina lista in-place

- `__add__(self, other)`
  - Concatena due SortedList

- `filter(self, predicate)`
  - Restituisce nuova lista con elementi che soddisfano predicate

#### Test
```python
sl = SortedList([3, 1, 4, 1, 5])

print(len(sl))  # 5
print(sl[0])    # 3
print(2 in sl)  # False

sl.sort()
print(sl)  # [1, 1, 3, 4, 5]

sl.append(2)
print(sl)  # [1, 1, 3, 4, 5, 2]

# Filtro
pari = sl.filter(lambda x: x % 2 == 0)
print(pari)  # [4, 2]

# Concatenazione
sl2 = SortedList([6, 7])
sl3 = sl + sl2
print(sl3)
```

---

### Esercizio 6 - Challenge: Vector Matematico Completo (20 minuti)

#### Descrizione
Creare classe `Vector` con tutte le operazioni vettoriali matematiche.

#### Requisiti

**Classe Vector:**
- `__init__(self, *componenti)` o `__init__(self, componenti_list)`
  - Vector(1, 2, 3) o Vector([1, 2, 3])

- **Rappresentazione:**
  - `__str__()` → "<1, 2, 3>"
  - `__repr__()` → "Vector(1, 2, 3)"
  - `__len__()` → dimensione vettore

- **Accesso elementi:**
  - `__getitem__(self, index)` → v[0]
  - `__setitem__(self, index, value)` → v[0] = 5
  - `__iter__(self)` → for comp in v:

- **Operatori aritmetici:**
  - `__add__(self, other)` → somma vettoriale
  - `__sub__(self, other)` → differenza
  - `__mul__(self, scalar)` → prodotto scalare
  - `__rmul__(self, scalar)` → 3 * v
  - `__truediv__(self, scalar)` → divisione per scalare

- **Confronto:**
  - `__eq__(self, other)` → uguaglianza
  - `__abs__(self)` → modulo/lunghezza vettore

- **Operazioni matematiche:**
  - `dot(self, other)` → prodotto scalare (numero)
  - `cross(self, other)` → prodotto vettoriale (solo 3D)
  - `normalize(self)` → vettore unitario
  - `distanza(self, other)` → distanza euclidea

- **Utilità:**
  - `__bool__(self)` → False se vettore nullo
  - `angolo_con(self, other)` → angolo in radianti

#### Test
```python
import math

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(1, 0, 0)
v4 = Vector(0, 1, 0)

# Operazioni base
print(v1 + v2)  # <4, 6>
print(v1 - v2)  # <2, 2>
print(v1 * 2)   # <6, 8>
print(3 * v1)   # <9, 12>

# Accesso
print(v1[0])    # 3
v1[0] = 5
print(v1)       # <5, 4>

# Proprietà
print(len(v1))  # 2
print(abs(v1))  # sqrt(25 + 16) = 6.4...

# Prodotti
print(v1.dot(v2))  # 5*1 + 4*2 = 13
print(v3.cross(v4))  # <0, 0, 1>

# Normalizzazione
v_norm = v1.normalize()
print(abs(v_norm))  # 1.0

# Distanza
print(v1.distanza(v2))

# Angolo
angolo = v3.angolo_con(v4)
print(f"Angolo: {math.degrees(angolo)}°")  # 90°
```

#### Output Atteso
```
<4, 6>
<2, 2>
<6, 8>
<9, 12>
3
<5, 4>
2
6.4031...
13
<0, 0, 1>
1.0
4.123...
Angolo: 90.0°
```

#### Hint Formule
```python
# Modulo
import math
modulo = math.sqrt(sum(c**2 for c in componenti))

# Prodotto scalare
dot = sum(a*b for a, b in zip(v1, v2))

# Prodotto vettoriale (solo 3D)
# v1 × v2 = (v1.y*v2.z - v1.z*v2.y,
#            v1.z*v2.x - v1.x*v2.z,
#            v1.x*v2.y - v1.y*v2.x)

# Normalizzazione
mod = abs(self)
normalized = Vector(*(c/mod for c in self))

# Angolo
cos_angle = v1.dot(v2) / (abs(v1) * abs(v2))
angle = math.acos(cos_angle)
```

---

## 📝 NOTE PER LO STUDENTE

### Concetti Chiave

1. **Magic Methods Naming**
   - Sempre doppio underscore: `__metodo__`
   - Non inventare: usa quelli standard Python

2. **__str__ vs __repr__**
   - `__str__`: human-readable, per utente
   - `__repr__`: unambiguous, per debug
   - Se solo uno: implementa `__repr__`

3. **Operatori Binari**
   - Primo operando: self
   - Secondo operando: other
   - Restituisci nuovo oggetto (immutabile)

4. **Type Checking**
   ```python
   def __add__(self, other):
       if not isinstance(other, TipoCorretto):
           return NotImplemented  # Non raise!
       # ... logica
   ```

5. **Context Manager Pattern**
   ```python
   def __enter__(self):
       # Setup
       return resource
   
   def __exit__(self, exc_type, exc_val, exc_tb):
       # Cleanup (sempre eseguito)
       return False  # False = propaga eccezioni
   ```

### Errori da Evitare

1. **Modificare self in operatori**
   ```python
   # SBAGLIATO
   def __add__(self, other):
       self.x += other.x  # Modifica self!
       return self
   
   # CORRETTO
   def __add__(self, other):
       return Classe(self.x + other.x)  # Nuovo oggetto
   ```

2. **Dimenticare __hash__ con __eq__**
   ```python
   # Se implementi __eq__, implementa anche __hash__
   # per usare in set/dict
   ```

3. **Usare raise in __exit__**
   ```python
   # SBAGLIATO
   def __exit__(self, ...):
       if self.file:
           self.file.close()
       raise Exception()  # Non usare raise
   
   # CORRETTO
   def __exit__(self, ...):
       if self.file:
           self.file.close()
       return False  # Restituisci False per propagare
   ```

4. **__repr__ non valido**
   ```python
   # SBAGLIATO
   def __repr__(self):
       return "Un oggetto bello"  # Non ricostruibile
   
   # CORRETTO
   def __repr__(self):
       return f"Classe({self.x}, {self.y})"  # eval(repr(obj)) funziona
   ```

### Pattern Comuni

**Classe Numerica Completa:**
```python
class Numero:
    def __init__(self, valore):
        self.valore = valore
    
    def __str__(self):
        return str(self.valore)
    
    def __repr__(self):
        return f"Numero({self.valore})"
    
    def __add__(self, other):
        if isinstance(other, Numero):
            return Numero(self.valore + other.valore)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Numero):
            return self.valore == other.valore
        return NotImplemented
    
    def __hash__(self):
        return hash(self.valore)
```

**Container Base:**
```python
class Container:
    def __init__(self):
        self._items = []
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __contains__(self, item):
        return item in self._items
    
    def __iter__(self):
        return iter(self._items)
```

---

## ✅ CHECKLIST COMPLETAMENTO

- [ ] __str__ e __repr__ implementati
- [ ] Operatori aritmetici funzionanti
- [ ] Operatori confronto coerenti
- [ ] Type checking con isinstance()
- [ ] Restituisci NotImplemented per tipi non supportati
- [ ] Context manager cleanup garantito
- [ ] __hash__ coerente con __eq__
- [ ] Documentazione (docstring) presente

---

**Buon lavoro con i magic methods! 🪄✨**
