class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Saque efetuado!")
        else:
            print("Limite não disponível.")

    def deposito(self, valor):
        self.__saldo += valor

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
