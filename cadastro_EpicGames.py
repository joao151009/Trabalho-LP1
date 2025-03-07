import json
print('Bem vindo ao cadastro da epic games!!')
def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Digite o {nome_variavel}: ')
    while valor_lido == '': 
        print(f'{nome_variavel} não pode ficar vazio!')
        valor_lido = input(f'Digite o {nome_variavel}:')
    return valor_lido

def confirmaSenha(senha):
    senha = input(f'Digite sua senha: ')
    while senha == '':
        print(f'Senha não pode ser vazio!')
        senha = input(f'Digite sua senha: ')
    while len(senha) < 8:
        print("A senha tem que ter no mínimo 8 caracteres!!!!")
        senha = input(f'Digite sua senha: ')
    confirmacaoSenha = input(f'Confirme sua senha: ')
    while confirmacaoSenha != senha:
        print("As senhas não coincidem!")
        confirmacaoSenha = input(f'Confirme sua senha: ')
    return senha

def lerPlataforma(plataforma):
    plataforma_lida = input('Digite a plataforma: ')
    while plataforma_lida.lower() != 'pc' and plataforma_lida.lower() != 'xbox' and plataforma_lida.lower() != 'playstation':
        print('Digite uma plataforma válida!')
        plataforma_lida = input('Digite a plataforma: ')
    return plataforma_lida


def cadastroEpicGames():
    nome = ler_valor_nao_vazio('nome')
    plataforma = lerPlataforma('plataforma')
    senha = confirmaSenha('senha')
    email = ler_valor_nao_vazio('email')

    cadastro = {
        'nome': nome,
        'plataforma': plataforma,
        'senha': senha,
        'email': email
    }

    return cadastro

def imprimir_cadastro(cadastro):
    print(f"Nome:\t\t{cadastro['nome']}")
    print(f"Plataforma:\t{cadastro['plataforma']}")
    print(f"Email:\t\t{cadastro['email']}")
    print(f"senha:\t\t{cadastro['senha']}")

def lerJson():
    with open('cadastros.json', 'r') as arquivo:
        registro = json.load(arquivo)
    return registro

def salvarJson(registro):
    dados = json.dumps(registro, indent=2)
    with open('cadastros.json', 'w') as arquivo:
        arquivo.write(dados)

def mostrarCadastros():
                print("Cadastros:\n ")
                for i, item in enumerate(registro):
                    print(f'Cadastro {i + 1}')
                    print(f"Nome:\t\t{item['nome']}")
                    print(f"Plataforma:\t{item['plataforma']}")
                    print(f"Email:\t\t{item['email']}")
                    print(f"senha:\t\t{item['senha']}")
                    print('\n')

def removerCadastros():
        removedor = int(input("Qual cadastro você deseja apagar? (Ex.: 1, 2, 3...): "))
        removedor -= 1
        registro.pop(removedor)
        print('Cadastro removido com sucesso!!!!')

def editarCadastros():
        editor = int(input("Qual cadastro você deseja editar? (Ex.: 1, 2, 3...): "))
        editor -= 1
        modificarDados = int(input("Qual dado você quer editar?\n 1-Nome \n 2-Plataforma \n 3-Email \n 4-Senha: \n"))
        if modificarDados == 1:
            novo_nome = ler_valor_nao_vazio('nome')
            registro[editor]['nome'] = novo_nome
            print('Cadastro alterado com sucesso!')
            salvarJson(registro)
        elif modificarDados == 2:
            nova_plataforma = lerPlataforma('plataforma')
            registro[editor]['plataforma'] = nova_plataforma
            print('Cadastro alterado com sucesso!')
            salvarJson(registro)
        elif modificarDados == 3:
            novo_email = ler_valor_nao_vazio('email')
            registro[editor]['email'] = novo_email
            print('Cadastro alterado com sucesso!')
            salvarJson(registro)
        elif modificarDados == 4:
            nova_senha = confirmaSenha('senha')
            registro[editor]['senha'] = nova_senha
            print('Cadastro alterado com sucesso!')
            salvarJson(registro)
        print('Digite um valor válido!')
registro = lerJson()

while True:
        try:
            menu = int(input("Digite:\n 1 para mostrar os cadastros, 2 para criar um novo cadastro, 3 para excluir um cadastro, 4 para editar algum cadastro e 0 para sair: "))
            if menu == 1:
                mostrarCadastros()
            elif menu == 2:
                item = cadastroEpicGames()
                registro.append(item)
                print("Cadastro feito com sucesso!!! YAY!!!")
            elif menu == 3:
                mostrarCadastros()
                while True:
                    try:
                        removerCadastros()
                    except:
                        print('Esse cadastro não existe!!')
            elif menu == 4:
                mostrarCadastros()
                while True:
                    try:
                        editarCadastros()
                    except:
                        print('Insira um valor válido!')
            elif menu == 0:
                break
        except:
            print('Digite um valor válido!')