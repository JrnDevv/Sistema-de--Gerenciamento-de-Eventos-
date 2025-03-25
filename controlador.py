
eventos = {}

def cadastrar_evento(nome, data, descricao, max_participantes):
    if nome in eventos:
        print ("evento já cadastrado!")
        return
    eventos[nome] = {"data": data, "descricao": descricao, "max_participantes": max_participantes, "inscritos": []}

def visualizar_eventos():
    if not eventos  :
        print("Nenhum evento Disponivel.")
        return
    for nome, detalhes in eventos.items():
        vagas_disponiveis = detalhes["max_participantes"] - len(detalhes["inscritos"])
        print (f"{nome} - {detalhes['data']} - {detalhes['descricao']} - vagas_disponiveis: {vagas_disponiveis}")

def inscrever_aluno(nome_evento, aluno):
    if nome_evento not in eventos:
       print ("evento não encontrado.")
       return
    evento = eventos[nome_evento]   
    if len(evento["inscritos"]) >= evento['max_participantes']:
       print ("Evento Lotado!")
       return
    evento["inscritos"].append(aluno)
    print(f"aluno '{aluno}' inscrito no evento '{nome_evento}'.")

def visualizar_inscritos(nome_evento):
    if nome_evento not in eventos:
       print("evento não Encontrado.")
       return
    inscritos = eventos[nome_evento]["inscritos"]
    print(f"inscritos no evento '{nome_evento}' {','.join(inscritos) if inscritos else 'nenhum inscrito ainda.'}")

def excluir_evento(nome):
    if nome in eventos:
     del eventos[nome]
     print(f"evento '{nome}' excluido com sucesso!") 


def menu():
    while True:
        print("\n===== Menu =====")
        print("1. cadastrar evento")
        print("2. visualizar eventos")
        print("3. inscrever aluno")
        print("4. visualizar inscritos")
        print("5. excluir evento")
        print("6. sair")
        opcao = input("Escolha uma opção:")

        if opcao == "1":
           nome = input("nome do evento:")
           data = input("data do evento:")
           descricao = input("Descrição:")
           max_participantes = int(input("Número Maximo de Participantes:"))
           cadastrar_evento(nome, data, descricao, max_participantes)
       
        elif opcao == "2":
           visualizar_eventos()

        elif opcao == "3":
          nome_evento = input("nome do evento:")
          aluno = input("nome do aluno:")
          inscrever_aluno(nome_evento, aluno)

        elif opcao == "4":
           nome_evento = input("nome do evento:")
           visualizar_inscritos(nome_evento)

        elif opcao == "5":
           nome = input("nome do evento para excluir:")
           excluir_evento(nome)

        elif opcao == "6":
          print("saindo...")
          break
        else:
           print("Opção Invalida, tente novamente.")


menu()         


