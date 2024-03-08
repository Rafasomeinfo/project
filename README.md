# project
Projeto final cs50 - gerenciador de peças 
Desenvolvimento de Software para Estoque de Peças multi-plataforma, Tecnologia usada Python.
 Autor: Rafael da Silva Ribas
Professor e Desenvolvedor de sistemas eletrônicos,Web e Banco de Dados
Data: 10/09/23


Licença
Esta obra e seus personagens são licenciados sob a licença Creative Commons
Atribuição-Uso Não-Comercial-Vedada a Criação de Obras Derivadas 2.5
Brasil ( http://creativecommons.org/licenses/by-nc-nd/2.5/br/ ).
As premissas básicas desta licença são que:
Você pode
• copiar, distribuir, exibir e executar a obra 
Sob as seguintes condições
• Atribuição. Você deve dar crédito ao autor original, da forma
especificada pelo autor ou licenciante. 
• Uso Não-Comercial. Você não pode utilizar esta obra com finalidades
comerciais. 
• Vedada a Criação de Obras Derivadas. Você não pode alterar,
transformar ou criar outra obra com base nesta. 
Observações
• Para cada novo uso ou distribuição, você deve deixar claro para outros
os termos da licença desta obra. 
• Qualquer uma destas condições podem ser renunciadas, desde que Você
obtenha permissão do autor. 
• Nada nesta licença atrapalha ou restringe os direitos morais do autor. 
O autor desta obra e de seus personagens é Rafael da Silva Ribas
(codinome "Rafael Ribas").
A autoria das ilustrações é de Rafael da Silva Ribas.
A revisão e edição do texto é de Rafael da Silva Ribas.

Agradecimentos

"Dedico este projeto à Gestora Thamires Durão , minha família, pelo apoio constante e incentivo."
"A Deus que me permite  trabalhar incansavelmente para tornar este projeto uma realidade."
"Dedico este projeto à causa da educação e ao desejo de compartilhar conhecimento."

                                                   
                                                




Processo de engenharia

1 Levantamento de requisitos
Cliente pede um aplicativo de “controle de estoque de peças” para gerenciar produtos, listar estoque, cadastrar nova peça, exibir histórico, registrar entrada e saída,.etc…

Atentar ao que o cliente escolheu

2 Criando o documento de requisitos
Cliente pede um aplicativo que de “controle de estoque de peças” para gerenciar produtos, listar estoque, cadastrar nova peça, exibir histórico, registrar entrada e saída,.etc…
Fica decidido que a escolha das tecnologias, incluindo a linguagem de programação e o formato de armazenamento de dados, optou por usar Python e o formato JSON para armazenamento de dados, aqui está uma breve explicação das vantagens e considerações:
Linguagem de Programação: Python
Python é uma excelente escolha para desenvolver sistemas de gerenciamento de assistência técnica. Algumas razões pelas quais Python é uma linguagem popular para esse tipo de aplicativo incluem:
Facilidade de Aprendizado e Uso: Python é conhecido por sua sintaxe limpa e legível, o que torna mais fácil para os desenvolvedores criar e manter código.
Ampla Comunidade e Recursos: Python possui uma vasta comunidade de desenvolvedores e uma grande variedade de bibliotecas e frameworks que podem acelerar o desenvolvimento.
Versatilidade: Python é uma linguagem versátil que pode ser usada para desenvolver aplicativos de desktop, aplicativos web e muito mais. Isso o torna uma escolha adequada para diferentes partes de um sistema de gerenciamento de assistência técnica.
Formato de Armazenamento de Dados: JSON
Usar JSON para armazenar dados tem algumas vantagens, especialmente para sistemas mais simples ou pequenas empresas. Algumas considerações incluem:
Simplicidade: O formato JSON é simples e fácil de entender. Não requer um sistema de gerenciamento de banco de dados (DBMS) complexo para armazenar dados.
Portabilidade: Os dados em formato JSON são facilmente transportáveis entre sistemas. Você pode importar e exportar dados JSON com relativa facilidade.
Leveza: JSON é um formato de dados leve, o que significa que é eficiente em termos de armazenamento e transferência de dados pela rede.
No entanto, é importante notar que, à medida que o sistema cresce e se torna mais complexo, você pode encontrar limitações no uso do JSON. Bancos de dados relacionais ou não relacionais podem ser mais apropriados para sistemas maiores que exigem consultas complexas, transações e alta concorrência de acesso aos dados.
Se você optar por continuar usando Python e JSON, certifique-se de implementar um sistema de backup robusto e medidas de segurança para proteger os dados do cliente e da empresa. Além disso, considere a escalabilidade futura e como você pode migrar para um sistema de gerenciamento de dados mais avançado, como um banco de dados relacional, conforme seu sistema cresce.


O programa tera  A classe Sistema de Estoque,  que  representa o sistema em si e contém métodos para carregar, salvar dados, encontrar local disponível, gerenciar produtos, listar estoque, cadastrar nova peça, exibir histórico, registrar entrada e saída.

Imagem 1(interface de usuario front end)

Entendido! Vou criar um diagrama UML simplificado para representar a estrutura geral do sistema de gerenciamento de estoque em Python que foi desenvolvido. Note que o diagrama a seguir será uma representação simplificada e não abrangerá todos os detalhes do código.
Início

Crie um dicionário vazio para representar o estoque (estoque)

Enquanto Verdadeiro:
    Exiba o menu de opções:
    1. Adicionar Produto
    2. Listar Estoque
    3. Sair
etc,,,
    Leia a opção escolhida pelo usuário (opcao)

    Se opcao for igual a 1:
        Leia o nome do produto (nome)
        Leia a quantidade do produto (quantidade)
        Se o produto já existir no estoque:
            Adicione a quantidade informada à quantidade existente
        Senão:
            Adicione o produto ao estoque com a quantidade informada

    Se opcao for igual a 2:
        Se o estoque estiver vazio:
            Exiba "O estoque está vazio."
        Senão:
            Para cada produto no estoque:
                Exiba o nome do produto e sua quantidade

    Se opcao for igual a 3:
        Exiba "Saindo do programa."
        Encerre o loop

    Se opcao não for igual a 1, 2 ou 3:
        Exiba "Opção inválida. Tente novamente."

Fim


As instruções fundamentais usadas neste código são relacionadas a manipulação de dados em um sistema de estoque. Abaixo, descrevo as principais instruções e conceitos fundamentais aplicados:

1. **Carregando e Salvando Dados em Arquivo JSON**:
   - `carregar_estoque()`: Essa função carrega os dados do estoque a partir de um arquivo JSON chamado "estoque.json" ou cria um novo estoque vazio se o arquivo não existir.
Exemplo;

      # Função para carregar dados do arquivo JSON
def carregar_dados():
#Nesta linha, uma função chamada carregar_dados() está sendo definida. Essa função será responsável por carregar os dados do estoque a partir de um arquivo JSON.
    try:
        with open("sistema_assistencia.json", "r") as arquivo:
#Aqui, um bloco try é iniciado, indicando que o código dentro dele será executado, e qualquer exceção que ocorra será tratada no bloco except subsequente. O código está tentando abrir o arquivo "estoque.json" para leitura ("r" indica leitura).

            dados = json.load(arquivo)
#Dentro do bloco try, o código está lendo o conteúdo do arquivo JSON usando a função json.load(). Isso carrega os dados do arquivo JSON e os armazena na variável dados. Essa variável dados será um dicionário Python contendo os dados do arquivo JSON

    except FileNotFoundError:
#Aqui, está sendo especificada a exceção que o código vai capturar, que é FileNotFoundError. Isso significa que o código no bloco except será executado apenas se o arquivo "sistema _assitencia.json" não for encontrado.
        dados = {
            "clientes": [],
            "estoque": {},
            "vendas": [],
            "servicos": [],
            "historico_entrada": [],
            "historico_saida": [],
            "ordem_servico": 0,
            "modelos_aparelho": []  # Lista de modelos de aparelho
        }
#Dentro do bloco except, o código está criando um dicionário chamado estoque. Esse dicionário é uma representação do estoque e possui dois campos: "produtos" (que será um dicionário vazio representando os produtos) e "historico_saida" (que será uma lista vazia representando o histórico de saída de produtos).
Essa criação de dicionário é feita porque, se o arquivo "estoque.json" não for encontrado, é assumido que o estoque está vazio, e, portanto, um estoque vazio é criado.

    return dados
#Finalmente, a função retorna o dicionário dados, que conterá os dados carregados do arquivo JSON ou um estoque vazio, dependendo se o arquivo foi encontrado ou não.
Resumindo, essa função tenta carregar os dados do estoque a partir de um arquivo JSON chamado "assistencia tecnica.json". Se o arquivo não for encontrado, ela cria um estoque ”dados’ vazio e retorna esse dados. Em qualquer caso, a função retorna o dados(que pode estar vazio ou conter dados carregados do arquivo JSON) como um dicionário Python.
. Se não existir, ele será criado automaticamente. Certifique-se também de que todas as bibliotecas necessárias, como json e datetime, estejam importadas no seu ambiente de execução.


   - `salvar_estoque(estoque)`: Esta função salva os dados do estoque em um arquivo JSON para persistência.

2. **Encontrar o Próximo Local Disponível**:
   - `encontrar_proximo_local(estoque)`: Essa função verifica o próximo local disponível na sequência (local1, local2, local3, ...) com base nas localizações existentes no estoque.

3. **Registrar Entrada de Peças**:
   - `registrar_entrada(estoque)`: Permite registrar a entrada de peças no estoque, atualizando a quantidade e registrando a data e hora da entrada.

4. **Registrar Saída de Peças**:
   - `registrar_saida(estoque)`: Permite registrar a saída de peças do estoque, atualizando a quantidade e registrando a data e hora da saída.

5. **Cadastrar Nova Peça**:
   - `cadastrar_nova_peca(estoque)`: Permite adicionar um novo produto ao estoque, especificando o nome, a quantidade e a localização.

6. **Listar Estoque**:
   - `listar_estoque(estoque)`: Exibe uma lista de todos os produtos no estoque, incluindo nome, localização e quantidade.

7. **Exibir Histórico de Saída**:
   - `exibir_historico(estoque)`: Exibe um histórico das entradas e saídas de produtos, incluindo nome, tipo (entrada ou saída), quantidade e data e hora.

8. **Menu Principal**:
   - A função `main()` implementa um menu principal que permite ao usuário escolher entre várias operações, como registrar entradas/saídas, listar o estoque, exibir histórico, cadastrar novas peças ou sair do programa.

Essas instruções fundamentais são usadas para criar um sistema de gerenciamento de estoque simples, onde o usuário pode realizar ações básicas de entrada, saída, consulta e manutenção de produtos em um estoque, com registro de histórico de operações.














**Diagrama de Classes UML**:

+-----------------------------------------+
|             Sistema de Estoque         |
+-----------------------------------------+
| - estoque: Dict[str, Produto]          |
|-----------------------------------------|
| + carregar_estoque(): Dict[str, Produto] |
| + salvar_estoque(estoque: Dict[str, Produto]): void |
| + encontrar_proximo_local(estoque: Dict[str, Produto]): str |
| + gerenciar_produto(nome: str): void   |
| + listar_estoque(): void               |
| + cadastrar_nova_peca(nome: str, quantidade: int): void |
| + exibir_historico(): void             |
| - registrar_entrada(produto: Produto): void |
| - registrar_saida(produto: Produto): void   |
+-----------------------------------------+

+-----------------------------------------+
|              Produto                    |
+-----------------------------------------+
| - nome: str                            |
| - localizacao: str                     |
| - quantidade: int                      |
| - historico: List[Operacao]            |
+-----------------------------------------+
| + get_nome(): str                      |
| + set_nome(nome: str): void            |
| + get_localizacao(): str               |
| + set_localizacao(localizacao: str): void |
| + get_quantidade(): int                |
| + set_quantidade(quantidade: int): void |
| + adicionar_operacao(operacao: Operacao): void |
| + obter_historico(): List[Operacao]    |
+-----------------------------------------+

+-----------------------------------------+
|              Operacao                   |
+-----------------------------------------+
| - tipo: str                            |
| - quantidade: int                      |
| - data_hora: str                       |
+-----------------------------------------+
| + get_tipo(): str                      |
| + get_quantidade(): int                |
| + get_data_hora(): str                 |
+-----------------------------------------+
```

**Descrição**:

- A classe `Sistema de Estoque` representa o sistema em si e contém métodos para carregar, salvar dados, encontrar local disponível, gerenciar produtos, listar estoque, cadastrar nova peça, exibir histórico, registrar entrada e saída.

- A classe `Produto` representa um item no estoque com atributos como nome, localização, quantidade e histórico de operações. Os métodos permitem obter e definir esses atributos, bem como adicionar operações ao histórico.

- A classe `Operacao` representa uma operação de entrada ou saída de um produto, incluindo informações sobre o tipo (entrada ou saída), quantidade e data/hora.

Este diagrama UML descreve as classes e suas relações simplificadas no sistema de gerenciamento de estoque. Lembre-se de que um sistema completo pode ter mais detalhes e métodos específicos, mas este é um modelo básico para representar a estrutura geral do sistema.

3 Reunindo hardware

Roda em qualquer maquina, Windows, smartphone

4 Configurando Hardware

Roda em qualquer maquina, inclui instalar IDE ou Terminal

5 Escrevendo Software

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

6 Depurando O software OK!!!

As instruções fundamentais usadas neste código são relacionadas a manipulação de dados em um sistema de estoque. Abaixo, descrevo as principais instruções e conceitos fundamentais aplicados:
Menu Principal:
A função main() implementa um menu principal que permite ao usuário escolher entre várias operações, como registrar entradas/saídas, listar o estoque, exibir histórico, cadastrar novas peças ou sair do programa.




Carregando e Salvando Dados em Arquivo JSON:
carregar_estoque(): Essa função carrega os dados do estoque a partir de um arquivo JSON chamado "estoque.json" ou cria um novo estoque vazio se o arquivo não existir.
salvar_estoque(estoque): Esta função salva os dados do estoque em um arquivo JSON para persistência.
Encontrar o Próximo Local Disponível:
encontrar_proximo_local(estoque): Essa função verifica o próximo local disponível na sequência (local1, local2, local3, ...) com base nas localizações existentes no estoque.
Registrar Entrada de Peças:
registrar_entrada(estoque): Permite registrar a entrada de peças no estoque, atualizando a quantidade e registrando a data e hora da entrada.
Registrar Saída de Peças:
registrar_saida(estoque): Permite registrar a saída de peças do estoque, atualizando a quantidade e registrando a data e hora da saída.
Cadastrar Nova Peça:
cadastrar_nova_peca(estoque): Permite adicionar um novo produto ao estoque, especificando o nome, a quantidade e a localização.
Listar Estoque:
listar_estoque(estoque): Exibe uma lista de todos os produtos no estoque, incluindo nome, localização e quantidade.
Exibir Histórico de Saída:
exibir_historico(estoque): Exibe um histórico das entradas e saídas de produtos, incluindo nome, tipo (entrada ou saída), quantidade e data e hora.
Essas instruções fundamentais são usadas para criar um sistema de gerenciamento de estoque simples, onde o usuário pode realizar ações básicas de entrada, saída, consulta e manutenção de produtos em um estoque, com registro de histórico de operações.


7 Solucionando Problemas
Durante o teste foram apresentados e corrigidos erros de duplicatas etc, apagar aquivo json antigo, etc

8 Protótipo finalizado

OK.


Imagens do programa funcionando, momento de registro de saida de peças.







