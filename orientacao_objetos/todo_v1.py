#!python3
from datetime import datetime


class tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + ('(Concluída)' if self.feito else '')

aaasa
def main():
    casa = []
    casa.append(tarefa("passar roupa"))
    casa.append(tarefa('Lavar prato'))
     #Desafio percorrer lista casa e chamar metodo concluir apenas de tarefa lavar prato
    [Tarefa.concluir() for Tarefa in casa if Tarefa.descricao == 'Lavar prato']
    for Tarefa in casa:
        print(f' - {Tarefa}')


if __name__ == '__main__':
    main()
