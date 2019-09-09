import sqlite3

print("""
        1 = criar banco de dados
        2 = ler dados
        3 = inserir dados
        4 = deletando dados
        5 = alterando dados
        """)
opcao = int(input("Escolha sua opcao:"))


while opcao > 5:
    print("Escolha uma opção válida!")
    opcao = int(input("Escolha sua opcao:"))

else:
    #criando db
    if opcao == 1:
        conn = sqlite3.connect('clientes.db')
        # definindo um cursor
        cursor = conn.cursor()
        # criando uma tabela (schema)
        cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            cpf     VARCHAR(11) NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
            cidade TEXT,
            uf VARCHAR(2) NOT NULL,
            criado_em DATE NOT NULL
            );""")

        print('Tabela criada com sucesso')
        # desconectando...
        # encerrando a conecção com o db
        conn.close()


    # ler dados
    elif opcao == 2:
          conn = sqlite3.connect('clientes.db')
          cursor = conn.cursor()
          # lendo os dados
          cursor.execute("""
          SELECT * FROM  clientes;
          """)
          for linha in cursor.fetchall():
              print(linha)
          conn.close()



    #inserir dados
    elif opcao == 3:
          conn = sqlite3.connect('clientes.db')
          cursor = conn.cursor()
          # solicitando os dados do usuário
          p_nome = input('Nome: ')
          p_idade = input('Idade: ')
          p_cpf = input('CPF: ')
          p_email = input('Email: ')
          p_fone = input('Fone: ')
          p_cidade = input('Cidade: ')
          p_uf = input('UF: ')
          p_criado_em = input('Digite a data atual (yyyy-mm-dd): ')
          
          # inserindo os dados na tabela
          cursor.execute("""
          INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
          VALUES (?,?,?,?,?,?,?,?)
          """, (p_nome, p_idade, p_cpf, p_email, p_fone, p_cidade, p_uf, p_criado_em))
          conn.commit()
          print('Dados inseridos com sucesso')
          conn.close

    #deletando dados
    elif opcao == 4:
          conn = sqlite3.connect('clientes.db')
          cursor = conn.cursor()
          id_cliente = 8
          # excluindo um registro da tabela
          cursor.execute("""
          DELETE FROM clientes
          WHERE id = ?
          """, (id_cliente,))
          conn.commit()
          print('Registro excluido com sucesso.')
          conn.close()



    #alterando dados
    elif opcao == 5:
          conn = sqlite3.connect('clientes.db')
          cursor = conn.cursor()
          # idermos definir o id a ser alterado
          id_cliente = 1
          # como usamos o fone como parametro
          # iremos criara um novo fone
          novo_fone = '11-1000-2014'
          novo_criado_em = '2014-06-11'
          # alterando os dados da tabela
          cursor.execute("""
          UPDATE clientes
          SET fone = ?, criado_em = ?
          WHERE id = ?
          """, (novo_fone, novo_criado_em, id_cliente))
          conn.commit()
          print('Dados alterados com sucesso')
          conn.close()
