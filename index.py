from datetime import datetime

# Lista para armazenar os sócios do Clube de Vantagens
clube_de_vantagens = []

# Função para inserir um novo sócio
def inserir_socio():
    print("\n--- Inserir Sócio ---")
    nome = input("Digite o nome do sócio: ").strip()
    while True:
        try:
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
            data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Tente novamente no formato DD/MM/AAAA.")
    
    socio = {"nome": nome, "data_nascimento": data_nascimento}
    clube_de_vantagens.append(socio)
    print("Sócio cadastrado com sucesso!")

# Função para exibir os veteranos
def exibir_veteranos():
    print("\n--- Exibir Veteranos do Clube ---")
    while True:
        try:
            ano = int(input("Digite um ano (inferior a 1998) para filtrar os veteranos: "))
            if ano >= 1998:
                raise ValueError("O ano deve ser inferior a 1998.")
            break
        except ValueError as e:
            print(e)

    print("\n--- Lista de Veteranos ---")
    veteranos = [socio for socio in clube_de_vantagens if socio["data_nascimento"].year < ano]
    if not veteranos:
        print("Nenhum veterano encontrado com o filtro fornecido.")
    else:
        for idx, socio in enumerate(veteranos, start=1):
            nome = socio["nome"]
            data_nasc = socio["data_nascimento"].strftime("%d/%m/%Y")
            print(f"{idx}. Nome: {nome}, Data de Nascimento: {data_nasc}")

# Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Inserir Sócio")
        print("2. Exibir os Veteranos do Clube")
        print("0. Sair do Programa")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            inserir_socio()
        elif opcao == "2":
            exibir_veteranos()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
menu()
