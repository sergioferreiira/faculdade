import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server={DESKTOP-1STOELQ};"
    "Database=Estudos;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")

cursor = conexao.cursor()

def criar_tabelas():
    create_tabela_aluno = """
    USE Estudos
    CREATE TABLE Aluno (
        id INTEGER PRIMARY KEY,
        nome varchar(50) NOT NULL,
        email varchar(50) NOT NULL UNIQUE
    )"""    
    create_tabela_livro = """
    USE Estudos
    CREATE TABLE Livro (
        id_livro INTEGER PRIMARY KEY,
        id_aluno INTEGER,
        descricao TEXT NOT NULL,
        FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  
    ) """   

    cursor.execute(create_tabela_aluno)
    cursor.execute(create_tabela_livro)
    cursor.commit()
        

def criar_alunos():
    add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com');"
    cursor.execute(add_aluno)
    add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com');"
    cursor.execute(add_aluno)
    add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com');"
    cursor.execute(add_aluno)

def criar_livros():
    add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python completo e total')"
    cursor.execute(add_livro)
    add_livro = "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias póstumas de brás cubas')"
    cursor.execute(add_livro)
    add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')"
    cursor.execute(add_livro)

criar_tabelas()