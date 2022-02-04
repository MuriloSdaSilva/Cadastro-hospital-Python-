listaNome = []
listaIdade = []
listaAtendimento = []
contador = 0
somaIdade = 0
contIdade = 0
idadeMaior = 0
nomeMaior = ""



opcao = -1

while opcao != 0:
    print("=-MENU-=")
    print("0 - Sair")
    print("1 - Cadastrar novos pacientes")
    print("2 - Dados dos pacientes")
    print("3 - Atualizar paciente")
    print("4 - Listar paciente por atendimento")
    print("5 - Mostrar quantos pacientes foram atualizados")
    print("6 - Média de idade dos pacientes que usam plano de saúde")
    print("7 - Informar o paciente mais velho")
    opcao = int(input("Digite a opcao: "))


    if opcao == 1:
        if len(listaNome) == 0:
            nome = input("Digite o nome do paciente: ")
            listaNome.append(nome)
            idade = int(input("Digite a idade do paciente: "))
            listaIdade.append(idade)
            print("[1] Plano de Sáude")
            print("[2] SUS")
            print("[3] Particular")
            atendimento = int(input("Digite o tipo de atendimento: "))
            listaAtendimento.append(atendimento)
        elif len(listaNome) > 0:
            nome = input("Digite o nome do paciente: ")
            existe = True
            for i in range(len(listaNome)):
                if listaNome[i].lower() == nome.lower():
                    existe = False
            if existe == True:
                idade = int(input("Digite a idade do paciente: "))
                print("[1] Plano de Sáude")
                print("[2] SUS")
                print("[3] Particular")
                atendimento = int(input("Digite o tipo de atendimento: "))
                listaNome.append(nome)
                listaIdade.append(idade)
                listaAtendimento.append(atendimento)
            if existe == False:
                print("Paciente ja cadastrado")

    elif opcao == 2:
        for i in range(len(listaNome)):
            print("Nome: " + str(listaNome[i]) + " / Idade: " + str(listaIdade[i]) + " / Atendimento: " + str(listaAtendimento[i]))

    elif opcao == 3:
        nomeT = input("Digite o nome do paciente a ser atualizado: ")
        igual = True
        for i in range(len(listaNome)):
            if listaNome[i].lower() == nomeT.lower():
                igual = False
                posicao = i
        if igual == False:
            novaIdade = int(input("Digite a nova idade: "))
            print("[1] Plano de Sáude")
            print("[2] SUS")
            print("[3] Particular")
            novoAtendimento = int(input("Digite o novo atendimento:"))
            listaIdade[posicao] = novaIdade
            listaAtendimento[posicao] = novoAtendimento
            contador = contador + 1
        if igual == True:
            print("Paciente não encontrado")

    elif opcao == 4:
        listaTipoAtendimento = []
        print("[1] Plano de Sáude")
        print("[2] SUS")
        print("[3] Particular")
        tipoAtendimento = int(input("Informa por qual tipo de atendimento voce quer filtrar os pacientes: "))
        if tipoAtendimento == 1:
            for i in range(len(listaAtendimento)):
                if listaAtendimento[i] == tipoAtendimento:
                    listaTipoAtendimento.append(listaNome[i])
        if tipoAtendimento == 2:
            for i in range(len(listaAtendimento)):
                if listaAtendimento[i] == tipoAtendimento:
                    listaTipoAtendimento.append(listaNome[i])
        if tipoAtendimento == 3:
            for i in range(len(listaAtendimento)):
                if listaAtendimento[i] == tipoAtendimento:
                    listaTipoAtendimento.append(listaNome[i])
        print(listaTipoAtendimento)

    elif opcao == 5:
        print("A quantidade de pacientes atualizados é: {}" .format(contador))

    elif opcao == 6:
        for i in range(len(listaAtendimento)):
            if listaAtendimento[i] == 1:
                somaIdade = somaIdade + listaIdade[i]
                contIdade = contIdade + 1
        mediaIdade = somaIdade/contIdade
        print("A média da idade dos pacientes que usam plano de saúde é: {}" .format(mediaIdade))


    elif opcao == 7:
        for i in range(len(listaIdade)):
            if listaIdade[i] > idadeMaior:
                idadeMaior = listaIdade[i]
                nomeMaior = listaNome[i]

        print("O paciente com maior idade é: {}" .format(nomeMaior))





