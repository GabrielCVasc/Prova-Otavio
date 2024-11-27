clube_de_vantagens = []

def validar_data(data):
    try:
        dia, mes, ano = map(int, data.split("/"))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0:
            return dia, mes, ano
        else:
            raise ValueError
    except ValueError:
        return None

def inserir_socio():
    print("\n--- Inserir Sócio ---")
    nome = input("Digite o nome do sócio: ").strip()
    while True:
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
        data = validar_data(data_nascimento)
        if data:
            dia, mes, ano = data
            break
        else:
            print("Data inválida. Tente novamente no formato DD/MM/AAAA.")
    
    socio = {"nome": nome, "data_nascimento": {"dia": dia, "mes": mes, "ano": ano}}
    clube_de_vantagens.append(socio)
    print("Sócio cadastrado com sucesso!")

def exibir_veteranos():
    print("\n--- Exibir Veteranos do Clube ---")
    while True:
        try:
            ano_limite = int(input("Digite um ano (inferior a 1998) para filtrar os veteranos: "))
            if ano_limite >= 1998:
                print("O ano deve ser inferior a 1998.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Insira um ano válido.")
    
    print("\n--- Lista de Veteranos ---")
    veteranos = [socio for socio in clube_de_vantagens if socio["data_nascimento"]["ano"] < ano_limite]
    if not veteranos:
        print("Nenhum veterano encontrado com o filtro fornecido.")
    else:
        for idx, socio in enumerate(veteranos, start=1):
            nome = socio["nome"]
            dia = socio["data_nascimento"]["dia"]
            mes = socio["data_nascimento"]["mes"]
            ano = socio["data_nascimento"]["ano"]
            print(f"{idx}. Nome: {nome}, Data de Nascimento: {dia:02d}/{mes:02d}/{ano}")

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
