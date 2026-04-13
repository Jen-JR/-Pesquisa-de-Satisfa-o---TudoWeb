# Variáveis de controle (Configurado para 50 conforme o enunciado. Define minha população pré definida.)
TOTAL_ENTREVISTADOS = 50 
cont_excelente = 0
cont_ruim = 0

print(f"{'='*40}")
print(f"{'SISTEMA PESQUISA DE SATISFAÇÃO TUDOWEB':^40}")
print(f"{'='*40}")

# Estrutura de repetição para coleta de dados
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n| Registro [{i}/{TOTAL_ENTREVISTADOS}]")
    
    nome = input("Olá! Bem vind@ ao TudoWeb! Como foi sua experiência? Nome do cliente: ")
    idade = int(input("Idade: "))
    
    print("-" * 20)
    print("Avaliação do Atendimento:")
    print("[1] EXCELENTE | [2] BOM | [3] RUIM")
    print("-" * 20)
    
    escolha = input("Opinião selecionada: ")

    # Lógica de processamento de dados
    if escolha == "1":
        cont_excelente += 1
    elif escolha == "3":
        cont_ruim += 1
    # Opção 2 (BOM) é ignorada 

# Exibição dos dados consolidados
print("\n" + "="*40)
print(f"{'RELATÓRIO FINAL DE SATISFAÇÃO':^40}")
print(f"{'='*40}")
print(f"Total de respostas EXCELENTE: {cont_excelente}")
print(f"Total de respostas RUIM     : {cont_ruim}")
print("-" * 40)
print("Processamento concluído com sucesso! Respostas computadas!")