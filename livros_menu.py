import sqlite3


def criar_tabela():
    bd = sqlite3.connect('livros.db')
    try:        
        cur = bd.cursor()
        comandoSQL = '''create table livros 
                        (nome_livro text (50) primary key,
                        autora text (30) not null);'''
        cur.execute(comandoSQL)
        print ('Tabela de livros criada com sucesso')        
    except sqlite3.Error as erro:
        print("Erro na operação:",erro)
        bd.rollback()
    bd.close()

def inserir():
    bd = sqlite3.connect('livros.db')
    comandoSQL = '''insert into livros 
                    (nome_livro , autora) values(?,?);'''
    nomeInp = input("Informe o nome do livro: ")
    autoralInp = input("Informe do autor do livro: ")  
    try:
        cur = bd.cursor()
        cur.execute(comandoSQL,(nomeInp,autoralInp))
        bd.commit()
        print ("Um livro foi incluido com sucesso")
    except sqlite3.Error as erro:
        print("Erro na operação:",erro)
        bd.rollback()
    bd.close()

def excluir():
    bd = sqlite3.connect('livros.db')
    nomeInp = input("Informe o nome do livro a ser excluido: ")
    cur=bd.cursor()
    comandoSQL="select nome_livro, autora from livros where nome_livro=?;"
    cur.execute(comandoSQL,(nomeInp,))
    linhas_resposta = cur.fetchall()
    for resp in linhas_resposta:
        print("Este é o livro que será excluído:",resp)
    # ---- excluir o livro
    comandoSQL = "delete from livros where nome_livro=?;"
    try:
        cur=bd.cursor()
        cur.execute(comandoSQL, (nomeInp,))
        bd.commit()
        print("Livro excluído com sucesso")
    except sqlite3.Error as erro:
        print("Erro na operação:",erro)
        bd.rollback()
    bd.close()

def consultar_todos():
    bd=sqlite3.connect('livros.db')
    cur=bd.cursor()
    comandoSQL="select nome_livro, autora from livros;"
    cur.execute(comandoSQL)


    linhas_resposta = cur.fetchall()
    for livro in linhas_resposta:
        print(livro)
    bd.close()


while True:
    print("-------------------------------------")
    print("1- Para criar a lista com os livros")
    print("2- Inculuir um novo livro")
    print("3- Excluir um livro")
    print("4- Listar todos os livros")
    print("5- Sair da aplicação")
    print("-------------------------------------")
    op = (input("Entre com a opção desejada: "))
    print()


    if op == '1':
        print("\nVocê escolheu a opção 1")
        print("Vamos criar a tabela.")
        criar_tabela()
    elif op == '2':
        print("\nVocê escolheu a opção 2")
        print("Vamos inserir um novo livro.")
        inserir()
    elif op == '3':
        print("\nVocê escolheu a opção 3")
        print("Vamos excluir um livro.")
        excluir()
    elif op == '4':
        print("\nVocê escolheu a opção 4")
        print("Vamos consultar todos os livros.")
        consultar_todos()
    elif op == '5':
        print("\nTchau.")
        break
    else:
        print("\nOpção inválida. Tente ontra vez.")