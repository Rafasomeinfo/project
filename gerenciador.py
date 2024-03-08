import json
from datetime import datetime

# Função para carregar dados do arquivo JSON
def carregar_estoque():
    try:
        with open("estoque.json", "r") as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        estoque = {"produtos": {}, "historico_saida": []}
    return estoque

# Função para salvar dados no arquivo JSON
def salvar_estoque(estoque):
    with open("estoque.json", "w") as arquivo:
        json.dump(estoque, arquivo)

# Função para encontrar o próximo local disponível na sequência (local1, local2, local3, ...)
def encontrar_proximo_local(estoque):
    i = 1
    while True:
        local = f"local{i}"
        if not any(produto['Localização'] == local for produto in estoque["produtos"].values()):
            return local
        i += 1

# Função para registrar entrada de peças
def registrar_entrada(estoque):
    nome = input("Informe o nome do produto que está entrando: ")
    quantidade_entrada = int(input("Informe a quantidade que está entrando: "))
    if nome in estoque["produtos"]:
        estoque["produtos"][nome]["Quantidade"] += quantidade_entrada
    else:
        local = encontrar_proximo_local(estoque)
        estoque["produtos"][nome] = {"Nome": nome, "Localização": local, "Quantidade": quantidade_entrada}

    # Registra data e hora da entrada
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    estoque["historico_saida"].append({"Produto": nome, "Tipo": "Entrada", "Quantidade": quantidade_entrada, "DataHora": data_hora})

    salvar_estoque(estoque)
    print("Entrada registrada com sucesso!")

# Função para registrar saída de peças
def registrar_saida(estoque):
    nome = input("Informe o nome do produto que está saindo: ")
    if nome in estoque["produtos"]:
        quantidade_saida = int(input("Informe a quantidade que está saindo: "))
        if estoque["produtos"][nome]["Quantidade"] >= quantidade_saida:
            estoque["produtos"][nome]["Quantidade"] -= quantidade_saida
            # Registra data e hora da saída
            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            estoque["historico_saida"].append({"Produto": nome, "Tipo": "Saída", "Quantidade": quantidade_saida, "DataHora": data_hora})
            salvar_estoque(estoque)
            print("Saída registrada com sucesso!")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado no estoque.")

# Função para cadastrar uma nova peça no estoque
def cadastrar_nova_peca(estoque):
    nome = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade do produto: "))
    local = encontrar_proximo_local(estoque)
    estoque["produtos"][nome] = {"Nome": nome, "Localização": local, "Quantidade": quantidade}
    salvar_estoque(estoque)
    print("Nova peça cadastrada com sucesso!")

# Função para listar todos os produtos no estoque
def listar_estoque(estoque):
    if not estoque["produtos"]:
        print("O estoque está vazio.")
    else:
        print("Lista de Produtos no Estoque:")
        for nome, produto in estoque["produtos"].items():
            print(f"Nome: {nome}, Localização: {produto['Localização']}, Quantidade: {produto['Quantidade']}")

# Função para exibir o histórico de saída
def exibir_historico(estoque):
    historico = estoque["historico_saida"]
    if not historico:
        print("O histórico de saída está vazio.")
    else:
        print("Histórico de Saída:")
        for registro in historico:
            print(f"Produto: {registro['Produto']}, Tipo: {registro['Tipo']}, Quantidade: {registro['Quantidade']}, Data e Hora: {registro['DataHora']}")

# Função principal
def main():
    estoque = carregar_estoque()

    while True:
        print("=====================================")
        print("\nSistema de Estoque de Peças Thamires|")
        print("Desenvolvido por Rafael Ribas  |")
        print("======================================")
        print("1. Registrar Entrada de Peças")
        print("2. Registrar Saída de Peças")
        print("3. Listar Estoque")
        print("4. Exibir Histórico de Saída")
        print("5. Cadastrar Nova Peça")
        print("6. Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_entrada(estoque)
        elif opcao == "2":
            registrar_saida(estoque)
        elif opcao == "3":
            listar_estoque(estoque)
        elif opcao == "4":
            exibir_historico(estoque)
        elif opcao == "5":
            cadastrar_nova_peca(estoque)
        elif opcao == "6":
            print("Saindo do programa. Salvando dados...")
            salvar_estoque(estoque)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

