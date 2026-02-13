class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        print(f"🔌 Connessione a '{self.db_name}' aperta")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"⚠️  Errore durante connessione: {exc_val}")

        print(f"🔌 Connessione a '{self.db_name}' chiusa")
        self.connected = False

        return False  # Propaga eccezione (non sopprime)

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Connessione non aperta")
        print(f"Esecuzione query: {sql}")
        return [{'id': 1, 'nome': 'Test'}]

    def execute(self, sql):
        if not self.connected:
            raise RuntimeError("Connessione non aperta")
        print(f"Esecuzione comando: {sql}")
        return True


if __name__ == "__main__":
    # Uso corretto
    with DatabaseConnection("mydb") as db:
        risultato = db.query("SELECT * FROM users")
        print(f"Risultati: {risultato}")
        db.execute("INSERT INTO users VALUES (...)")

    print()

    # Uso con eccezione
    try:
        with DatabaseConnection("mydb") as db:
            db.query("SELECT * FROM users")
            raise ValueError("Errore simulato")
            db.query("Non eseguita")
    except ValueError:
        print("Eccezione gestita, ma DB chiuso correttamente")
