import pyodbc

server = "localhost,1433"  # Substitua pela porta correta, se necessário
database = "dev"
username = "sa"
password = "1984Icm000"
driver = "ODBC Driver 17 for SQL Server"

try:
    conn = pyodbc.connect(
        f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro: {e}")
