import sqlite3

# Função para criar a tabela de pedidos
def criar_tabela():
    conn = sqlite3.connect('pedidos_lanchonete.db')
    cursor = conn.cursor()

    # Criação da tabela de pedidos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lanche TEXT NOT NULL,
            acompanhamento TEXT,
            bebida TEXT,
            valor FLOAT NOT NULL,
            observacao TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Função para mostrar os pedidos
def mostrar():
    conn = sqlite3.connect('pedidos_lanchonete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Função para adicionar um novo pedido
def adicionar_pedido(lanche, acompanhamento, bebida, valor, observacao=''):
    conn = sqlite3.connect('pedidos_lanchonete.db')
    cursor = conn.cursor()

    # Inserção do pedido na tabela
    cursor.execute('''
        INSERT INTO pedidos (lanche, acompanhamento, bebida, valor, observacao)
        VALUES (?, ?, ?, ?, ?)
    ''', (lanche, acompanhamento, bebida, valor, observacao))

    conn.commit()
    conn.close()

# Função para deletar um pedido
def deletar_pedido(id_pedido):
    conn = sqlite3.connect('pedidos_lanchonete.db')
    cursor = conn.cursor()

    # Deleção do pedido na tabela
    cursor.execute('''
        DELETE FROM pedidos
        WHERE id = ?
    ''', (id_pedido,))

    conn.commit()
    conn.close()

# Cria a tabela de pedidos se ela não existir
criar_tabela()
mostrar()

escolha = input("Você deseja deletar[D] ou criar um pedido [C]: ")

if escolha.upper() == 'D' or escolha.upper() == "DELETAR":
    try:
        id_deletado = int(input("Digite o ID do pedido que você quer deletar: "))
        deletar_pedido(id_deletado)
        print("\nPedido deletado com sucesso!")
    except ValueError:
        print("\nErro ao deletar o pedido.")
elif escolha.upper() == 'C' or escolha.upper() == 'CRIAR':
    lanche = input("Me informe qual o lanche: ")
    acompanhamento = input("Qual o acompanhamento: ")
    bebida = input("Qual a bebida: ")
    valor = float(input("Quantos ficou: ").replace(',', '.'))
    observacao = input("Alguma observação: ")
    adicionar_pedido(lanche, acompanhamento, bebida, valor, observacao)
