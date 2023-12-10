from classes import PessoaFisica, ContaCorrente

usuarios = []
numContaAtual = 1




#EXTRATO
def extratoConta(idUser, numConta):
    print(f'        {str(" EXTRATO ").center(40, "-")}\n')

    transacao = {
        'transacao': 'extrato'
    }

    usuarios[idUser].realizar_transacao(numConta, transacao)

    print('\n\n')

    print(f'Saldo da conta: R$ {round(usuarios[idUser].saldo(numConta), 2)}')
    menuTransacoes(idUser, numConta)

#SACAR
def saqueConta(idUser, numConta):
    limiteValor = 500
    valor = float(input(f"""
            {str(" SAQUE ").center(40, "-")}  
        
    Digite o valor que deseja sacar => R$ """))
    if usuarios[idUser].saldo(numConta) < valor:
        print('Saldo indisponivel')

    elif valor > limiteValor:
        print(f'''
            Valor maximo de R$ {limiteValor} atingido !!
            Tente novamente
            ''')
    elif usuarios[idUser].saques(numConta) >= usuarios[idUser].limiteSaques(numConta):
        print(f'''
            Limite de {usuarios[idUser].limiteSaques(numConta)} saques diarios atingido !!
            Tente novamente amanha
            ''')
    else:
        transacao = {
            'transacao' : 'saque',
            'valor' : valor
        }
        usuarios[idUser].realizar_transacao(numConta, transacao)
        print('Saque realizado com sucesso !!')
        menuTransacoes(idUser, numConta)

#DEPOSITAR 
def depositoConta(idUser, numConta):
    valor = float(input(f"""
    {str(" DEPOSITO ").center(40, "-")}

Digite o valor que deseja depositar => R$ """))
    
    transacao = {
        'transacao' : 'deposito',
        'valor' : valor
    }
    usuarios[idUser].realizar_transacao(numConta,transacao)
       
    print('Deposito realizado com sucesso !!')
    menuTransacoes(idUser, numConta)

#MENU DE TRANSACOES
def menuTransacoes(indexUser, numConta):
    try:
        opcao = input(f"""
            {str(" TRANSACOES ").center(40, "-")}
        
        Opcoes:

        [1] Extrato
        [2] Saque
        [3] Deposito
        [0] Sair

    Digite uma opcao => """)

        
        if int(opcao) == 1:
            extratoConta(indexUser, numConta)
            return True
        

        elif int(opcao) == 2:
            saqueConta(indexUser, numConta)
            return True

        
        elif int(opcao) == 3:
            depositoConta(indexUser, numConta)
            return True

        elif int(opcao) == 0:
            return False
        else:
            print('Digite uma opcao valida !')
    except Exception as error:
        print(f"{error}\n\n")

#CRIAR CONTA 
def menuCriarConta():
    cpf = input(f"""
        {str(" CRIAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', '')
    
    check = False
    attUser = 0
    for user in usuarios:
        if user.cpf == cpf:
            check = True
            attUser = usuarios.index(user)
    
    if check:
        global numContaAtual

        novaConta = ContaCorrente.nova_conta(numero=numContaAtual, cliente=usuarios[attUser].nome)

        usuarios[attUser].adicionar_conta(novaConta)

        numContaAtual+=1
        print('Conta criada com sucesso !!')
    else:
        print('CPF invalido ou nao cadastrado!\nTente novamente')



#CRIAR USUARIO
def menuCriarUsuario():
    nome = input(f"""
        {str(" CRIAR USUARIO ").center(40, "-")}
    

Digite seu nome completo => """)
    
    dataNasc = input("Digite sua data de nascimento (ex : dd/mm/aaaa) => ")

    cpf = input("Digite seu CPF => ").replace('.', '').replace('-', '')

    logradouro = input("Digite o logradouro da sua residencia => ") 

    num = input("Digite o numero da sua residencia => ")

    bairro = input("Digite seu bairro => ")

    cidade = input('Digite sua cidade => ')

    siglaEstado = input("Digite a sigla do seu estado (ex : RJ) =>")

    dataSplit = dataNasc.split('/')
    ano = int(dataSplit[2])
    mes = int(dataSplit[1])
    dia = int(dataSplit[0])

    endereco = f'{logradouro},{num} - {bairro} - {cidade}/{siglaEstado}'

    for user in usuarios:
        if user.cpf == cpf:
            print('Usuario ja cadastrado !!')
            return False
    
    novoCliente = PessoaFisica(cpf=cpf, nome=nome, ano=ano, mes=mes, dia=dia, endereco=endereco)

    usuarios.append(novoCliente)
    print('Usuario criado com sucesso !!\nVoltando para o menu')


#MENU DE ACESSAR A CONTA
def menuAcessarConta():
    cpf = input(f"""
        {str(" ACESSAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', '')
    check = False
    indexUser = 0
    numConta = 0
    for user in usuarios:
        if user.cpf == cpf:
            check = True
            indexUser = usuarios.index(user)
            for conta in usuarios[indexUser]._contas:
                print(conta, end='\n')
            
            nConta = int(input('Digite o numero da conta que deseja acessar => '))

            for conta in usuarios[indexUser].contas:
                if nConta == conta:
                    numConta = usuarios[indexUser].contas[usuarios[indexUser].contas.index(conta)]

                    print('Conta selecionada com sucesso !!')
                    menuTransacoes(indexUser, numConta)
                    return 
        else:
            continue

    print('CPF invalido ou nao cadastrado!\nTente novamente')



#MENU INICIAL
def menuInicial():
    try:
        opcao = input(f"""
            {str(" BANCO INTERNACIONAL ")}
        
        Opcoes:

        [1] Criar usuario
        [2] Criar conta
        [3] Acessar conta
        [0] Sair

    Digite uma opcao => """)
        
        if int(opcao) == 1:
            menuCriarUsuario()
            return True
        

        elif int(opcao) == 2:
            menuCriarConta()
            return True

        
        elif int(opcao) == 3:
            menuAcessarConta()
            return True

        elif int(opcao) == 0:
            return False

    except Exception as error:
        print(f"{error}\n\n")


while True:    
    if menuInicial():
        continue
    else:
        break