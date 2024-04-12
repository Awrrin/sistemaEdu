import sqlite3
from getpass import getpass

# Conecta ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Cria a tabela 'users' (execute apenas uma vez)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')

def register_user(username, password):
    cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))
    conn.commit()

def authenticate_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    return cursor.fetchone() is not None

def main():
    print("=== Sistema de Autenticação ===")
    username = input("Digite seu nome de usuário: ")
    password = getpass("Digite sua senha: ")

    if authenticate_user(username, password):
        print("Bem-vindo ao sistema!")
    else:
        print("Erro de login. Tente novamente.")

if __name__ == "__main__":
    main()

# Feche a conexão com o banco de dados
conn.close()