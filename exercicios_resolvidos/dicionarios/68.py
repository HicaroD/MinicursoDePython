"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa 
pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. 
Seu programa deve ter as seguintes funções:

    incluirNovoNome - essa função acrescenta um novo nome na agenda, com um ou mais 
    telefones. Ela deve receber como argumentos o nome e os telefones.

    incluirTelefone - essa função acrescenta um telefone em um nome existente na agenda. 
    Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. 
    Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 

    excluirTelefone - essa função exclui um telefone de uma pessoa que já está na agenda. 
    Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. 

    excluirNome - essa função exclui uma pessoa da agenda. 

    consultarTelefone - essa função retorna os telefones de uma pessoa na agenda.
"""

agenda_telefonica = dict()

def incluirNovoNome(nome, telefones):
    # Se o nome não estiver na lista, adicione. Caso contrário, não faça nada
    if nome not in agenda_telefonica.keys():
        agenda_telefonica[nome] = telefones

def incluirTelefone(nome, telefones):
    # Se o nome já estiver na lista, adicione os novos telefones junto aos outros 
    if nome in agenda_telefonica.keys():
        agenda_telefonica[nome] += telefones
    # Caso o nome não exista, pergunte se quer adicionar. Caso sim, adicione, caso contrário, faça nada
    else:
        quer_adicionar = input("Esse nome não existe na agenda. Quer adicionar? (S/N)")
        if quer_adicionar == "S":
            agenda_telefonica[nome] = telefones

def excluirTelefone(nome, telefone):
    # Se o nome estiver na lista
    if nome in agenda_telefonica.keys():
        # Se só tiver um telefone e esse telefone é aquele que estamos tentando excluir, apague o nome da lista
        if len(agenda_telefonica[nome]) == 1 and agenda_telefonica[nome][0] == telefone:
            excluirNome(nome)
        else:
            # Para todo nome e telefone agendado
            for telefone_agendado in agenda_telefonica[nome]:
                # Se um dos telefones agendados for aquele que eu quero excluir, apague-o
                if telefone_agendado == telefone:
                    agenda_telefonica[nome].remove(telefone_agendado)


def excluirNome(nome):
    # Se o nome estiver na agenda
    if nome in agenda_telefonica.keys():
        # Delete
        del agenda_telefonica[nome]

def consultarTelefone(nome):
    if nome in agenda_telefonica.keys():
        print("Telefones de " + nome)
        for telefone in agenda_telefonica[nome]:
            print("- " + str(telefone))

def main():
    while True:
        opcao = input("O que você deseja?\n 1) Incluir novo nome\n 2) incluir telefone\n 3) excluir telefone\n 4) excluir nome\n 5) consultar telefone\n")

        if opcao == "1":
            nome = input("Qual nome você deseja adicionar? ")
            telefones = input("Quais os telefones você deseja adicionar? ").split(",")
            incluirNovoNome(nome, telefones)

        elif opcao == "2":
            nome = input("Em qual nome você deseja adicionar um novo número? ")
            telefones = input("Quais os novos telefones? ").split(",")
            incluirTelefone(nome, telefones)
        
        elif opcao == "3":
            nome = input("Em qual nome você deseja remover um número? ")
            telefone = input("Qual o número a ser removido? ")
            excluirTelefone(nome, telefone)

        elif opcao == "4":
            nome = input("Qual nome você deseja remover? ")
            excluirNome(nome)

        elif opcao == "5":
            nome = input("Qual nome você deseja consultar? ")
            consultarTelefone(nome)
main()