import pyodbc

# Verbindung zur SQL Server-Datenbank herstellen
server = 'localhost'
database = 'JupiterDB'
username = 'user'
password = 'ciscocisco'
driver = '{SQL Server}'  # Der Treiber für SQL Server

try:
    conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')

    # Erstelle ein Cursor-Objekt, um SQL-Abfragen auszuführen
    cursor = conn.cursor()

    # Beispiel: Eine einfache SQL-Abfrage ausführen
    cursor.execute("SELECT TOP 5 * FROM DeineTabelle")

    # Ergebnisse der Abfrage abrufen und ausgeben
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Verbindung schließen
    conn.close()

except pyodbc.Error as e:
    print(f"Fehler bei der Verbindung zum SQL Server: {str(e)}")