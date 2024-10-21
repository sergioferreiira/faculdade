import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server={DESKTOP-1STOELQ};"
    "Database=Estudos;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")

cursor = conexao.cursor()

def criar_tabelas(nomeTabela, **kwargs):
    colunas =' , '.join([f"{coluna}{tipo}" for coluna, tipo in kwargs.items()])
    comando = f"CREATE TABLE {nomeTabela } \n ({(colunas)})"
    cursor.execute(comando)
    cursor.commit()


def criar_alunos(id_aluno, nome_aluno, email_aluno):
    add_aluno = """
        INSERT INTO Aluno (id,nome,email)
         VALUES (?,?,?);
        """
    cursor.execute(add_aluno,(id_aluno, nome_aluno,email_aluno))
    cursor.commit()


def criar_livros(id,aluno,descri):
    add_livro = """
        INSERT INTO Livro (id_livro, id_aluno, descricao)  
        VALUES (?,?,?)"""
    cursor.execute(add_livro,(id, aluno,descri))
    cursor.commit()


criar_alunos()




#1b) Crie uma função todos_alunos que retorna um lista com um dicionario
# para cada aluno

def todos_alunos():
    alunosLista = []
    while True:
        comando = """ 
        SELECT * FROM Aluno """   
        if cursor.fetchone() == None:
            break
        alunosLista.append(comando)
    return alunosLista
todos_alunos()
#1c) Crie uma função todos_livros que retorna um lista com um dicionario
# para cada livro

# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição)
# e o adiciona no banco de dados

# 3) Crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno
# e marca o livro como emprestado pelo aluno

# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro
# como disponível

# 5) Crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados
# por ninguém (uma lista de dicionários, um para cada livro)

# 6) Crie uma função livros_do_aluno, recebe o nome do aluno e devolve a lista de todos
# os livros que estão com o aluno no momento

