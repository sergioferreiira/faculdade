import pyodbc

# clientes
# ('Ana Silva', 1500.00, '1990-05-15'),
# ('Carlos Pereira', 2500.50, '1985-08-22'),
# ('Fernanda Lima', 3200.75, '1992-12-01'),
# ('Ricardo Gomes', 800.00, '1978-03-10'),
# ('Juliana Santos', 1200.30, '1988-07-19'),
# ('Marcos Oliveira', 3000.00, '1980-11-30'),
# ('Luana Costa', 4500.80, '1995-02-25'),
# ('Pedro Almeida', 600.20, '1993-04-12');

#  aqui e o formato solicitado pelo pyodbc para uma conexao local
dados_conexao = (
    "Driver={SQL Server};"
    "Server={DESKTOP-1STOELQ};"
    "Database=Estudos;"
)

# aqui e como e feita a conexao seria um : pyodbc se conecte aos dados passados
conexao = pyodbc.connect(dados_conexao)
print("Conexao bem sucedida")

# aqui e como é executado no caso : conexao e ele se ligando ao db, 
# cursor e como se voce fosse guiar a partir de agora voce vai cursar o rumo exemplo "cursor.faça algo" cursor.execute()
cursor = conexao.cursor()

# cursor.commit e para dar o apply após as alterações,
#  em buscas apenas nao se usa o commit apenas faz a busca, o commit e para alterações
cursor.commit()


def criaCliente(nome,saldo,anoNascimento):
    comando = """
        INSERT INTO Clientes (nome, saldo_conta, ano_nascimento) 
        VALUES(?, ?, ?)"""
    # cursor.faça(esse comando, (os valores passados com o marcador ? são como as F"strings" ))
    cursor.execute(comando, (nome, saldo, anoNascimento))
    # confirmando a alteração do db use o COMMIT
    conexao.commit() 

# utilização da função
# criaCliente("Sergio", 2000, "2000-04-20")





