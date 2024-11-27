# Lista para armazenar os funcionários da empresa
empresa = []

# Função para inserir um funcionário
def inserir_funcionario():
    print("\n--- Inserir Funcionário ---")
    while True:
        try:
            matricula = int(input("Digite a matrícula (3 dígitos entre 100 e 999): "))
            if 100 <= matricula <= 999:
                break
            else:
                print("Erro: A matrícula deve ser um número de 3 dígitos (100 a 999).")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número de 3 dígitos.")
    
    nome = input("Digite o nome do funcionário: ").strip()
    
    while True:
        try:
            salario_bruto = float(input("Digite o salário bruto (mínimo R$1412,55): "))
            if salario_bruto >= 1412.55:
                break
            else:
                print("Erro: O salário bruto deve ser maior ou igual a R$1412,55.")
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")
    
    while True:
        try:
            plano_saude = int(input("Possui plano de saúde? Sim(1) Não(0): "))
            if plano_saude in [0, 1]:
                break
            else:
                print("Erro: Digite 1 para Sim ou 0 para Não.")
        except ValueError:
            print("Erro: Entrada inválida. Digite 1 para Sim ou 0 para Não.")
    
    funcionario = {
        "matricula": matricula,
        "nome": nome,
        "salario_bruto": salario_bruto,
        "plano_saude": bool(plano_saude)
    }
    empresa.append(funcionario)
    print(f"Funcionário {nome} inserido com sucesso!")

# Função para exibir as médias salariais
def exibir_medias_salariais():
    print("\n--- Exibir Médias Salariais ---")
    if not empresa:
        print("Nenhum funcionário cadastrado ainda.")
        return
    
    salarios_com_plano = [f["salario_bruto"] for f in empresa if f["plano_saude"]]
    salarios_sem_plano = [f["salario_bruto"] for f in empresa if not f["plano_saude"]]
    
    media_com_plano = sum(salarios_com_plano) / len(salarios_com_plano) if salarios_com_plano else 0
    media_sem_plano = sum(salarios_sem_plano) / len(salarios_sem_plano) if salarios_sem_plano else 0
    
    print(f"Média Salarial dos Funcionários com Plano de Saúde: R${media_com_plano:.2f}")
    print(f"Média Salarial dos Funcionários sem Plano de Saúde: R${media_sem_plano:.2f}")

# Função principal do menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Inserir Funcionário")
        print("2. Exibir Médias Salariais")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            inserir_funcionario()
        elif opcao == "2":
            exibir_medias_salariais()
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa
menu()
