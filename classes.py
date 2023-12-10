from abc import ABC, abstractmethod
from datetime import datetime

class Transacao:
    @abstractmethod
    def saque(self, valor):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        pass
    
    def __str__(self):
        pass

    @property
    def contas(self):
        saida = []
        for conta in self._contas:
            saida.append(conta.numero)
        
        return saida
    

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def realizar_transacao(self, numConta, transacao):
        for conta in self._contas:
            if conta.numero == numConta:
                if transacao['transacao'] == 'saque':
                    indexConta = self._contas.index(conta)
                    self._contas[indexConta].sacar(transacao['valor'])

                elif transacao['transacao'] == 'deposito':
                    indexConta = self._contas.index(conta)
                    self._contas[indexConta].depositar(transacao['valor'])

                elif transacao['transacao'] == 'extrato':
                    indexConta = self._contas.index(conta)
                    self._contas[indexConta].extrato()
                else:
                    print('Transacao nao reconhecida !')  

    def saldo(self, numConta):
        for conta in self._contas:
            if conta.numero == numConta:
                return conta.saldo
    
    def saques(self, numConta):
        for conta in self._contas:
            if conta.numero == numConta:
                return conta.saques
    
    def limiteSaques(self, numConta):
        for conta in self._contas:
            if conta.numero == numConta:
                return conta.limiteSaques
            
    


class Conta(Transacao):
    def __init__(self,numero=None, agencia='0001', cliente=None):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = []
        self._saques = 0


    @property
    def saldo(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def saques(self):
        return self._saques

    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero=numero, cliente=cliente)
    

    def sacar(self, valor):
        self._saldo -= valor
        transacao = {
            'transacao' : 'saque',
            'valor' : valor
        }
        self._historico.append(transacao)
        self._saques += 1

    def depositar(self, valor):
        self._saldo += valor
        transacao = {
            'transacao' : 'deposito',
            'valor' : valor
        }
        self._historico.append(transacao)

    def extrato(self):
        for transacao in self._historico:
            if transacao['transacao'] == 'saque':
                print(f"{str(transacao['transacao']) + 3*' '}: - R$ {round(float(transacao['valor']), 2)}")

            elif transacao['transacao'] == 'extrato':
                print(f"{str(transacao['transacao']) + ' '}:   -")

            else:
                print(f"{str(transacao['transacao'])}:   R$ {round(float(transacao['valor']), 2)}")
        transacao = {
            'transacao': 'extrato'
        }

        self._historico.append(transacao)
        

  
class ContaCorrente(Conta):

    def __init__(self, numero=None, agencia='0001', cliente=None):
        super().__init__(numero, agencia, cliente)
        self._limite = self.saldo
        self._limiteSaques = 3

    def __str__(self):
        self._atualizarLimite()
        saida = f"""
    Agencia:            {self._agencia}
    Numero da conta:    {self._numero}
    Saldo:              {self._limite}
"""        
        return saida
    

    @property
    def limite(self):
        return self._limite

    @property
    def limiteSaques(self):
        return self._limiteSaques
    
    def _atualizarLimite(self):
        self._limite = self.saldo
        

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, ano, mes, dia, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = datetime(ano, mes, dia)
        super().__init__(endereco)
    
    def __str__(self):
        pass

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def data_nascimento(self):
        strData = f'{self._data_nascimento.day}/{self._data_nascimento.month}/{self.data_nascimento.year}'
        return strData
    

