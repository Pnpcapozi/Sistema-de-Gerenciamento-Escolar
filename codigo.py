import pandas as pd
import os

arquivo_csv = 'escola_dados.csv'

def carregar_dados():
    if os.path.exists(arquivo_csv):
        df = pd.read_csv(arquivo_csv)
        df['Código'] = df['Código'].astype(int)
        codigo = df['Código'].max() + 1
    else:
        colunas = ['Código', 'Nome', 'Rua', 'Número', 'Bairro',
                   'Cidade', 'UF', 'Telefone', 'E-mail']
        df = pd.DataFrame(columns=colunas)
        codigo = 1
    return df, codigo

def salvar_dados(df):
    df.to_csv(arquivo_csv, index=False)

def nome_escola():
    print('\n ESCOLA TERÊ \n')

def menu_escolha():
    print("1-INSERIR", "2-PESQUISAR", "3-REMOVER", "4-SAIR", sep="\n")

def escolher(df, codigo):
    escolha = 0
    while escolha != 4:
        menu_escolha()
        try:
            escolha = int(input('\nEscolha uma das opções: '))
            if escolha == 1:
                df, codigo = inserir(df, codigo)
            elif escolha == 2:
                pesquisar(df)
            elif escolha == 3:
                df = remover(df)
            elif escolha == 4:
                print("Saindo do sistema...")
                salvar_dados(df)
            else:
                print('Essa escolha não existe.')
        except ValueError:
            print("Insira um número válido.")
    return df, codigo

def inserir(df, codigo):
    while True:
        print("\nInsira os dados do aluno:")
        nome = input('Nome: ')
        rua = input('Rua: ')
        numero = input('Número: ')
        bairro = input('Bairro: ')
        cidade = input('Cidade: ')
        uf = input('UF: ')
        telefone = input('Telefone: ')
        email = input('E-mail: ')
        novo_registro = {
            'Código': codigo,
            'Nome': nome,
            'Rua': rua,
            'Número': numero,
            'Bairro': bairro,
            'Cidade': cidade,
            'UF': uf,
            'Telefone': telefone,
            'E-mail': email
        }
        df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
        salvar_dados(df)
        codigo += 1
        continuar = input("\nDeseja continuar inserindo? (s/n): ").lower()
        if continuar != 's':
            break
    return df, codigo

def pesquisar(df):
    while True:
        try:
            cod = int(input('Digite o código: '))
            linha = df.loc[df['Código'] == cod]
            if linha.empty:
                print("Código não encontrado!")
            else:
                print(linha.to_string(index=False))
        except ValueError:
            print("Insira um número válido.")
        continuar = input("\nDeseja continuar pesquisando? (s/n): ").lower()
        if continuar != 's':
            break

def remover(df):
    while True:
        try:
            cod = int(input('Digite o código: '))
            linha = df.loc[df['Código'] == cod]
            if not linha.empty:
                df = df[df['Código'] != cod]
                print(f"Aluno {cod} removido com sucesso.")
                salvar_dados(df)
            else:
                print("Código não encontrado.")
        except ValueError:
            print("Insira um número válido.")
        continuar = input("\nDeseja continuar removendo? (s/n): ").lower()
        if continuar != 's':
            break
    return df

def main():
    nome_escola()
    df, codigo = carregar_dados()
    df, codigo = escolher(df, codigo)

if __name__ == "__main__":
    main()
