import sys

numNode = 0

class NodeAVL:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)

    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()

    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()

    def executaBalanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacaoDireita()
            else:
                self.rotacaoEsquerdaDireita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()

    def add(self, data):
        global numNode
        if data <= self.data:
            if not self.esquerda:
                numNode += 1
                self.esquerda = NodeAVL(data)
            else:
                numNode += 1
                self.esquerda.add(data)
        else:
            if not self.direita:
                numNode += 1
                self.direita = NodeAVL(data)
            else:
                numNode += 1
                self.direita.add(data)
        self.executaBalanco()

    # def PrintTree(self, indent = 0):
    #     # print (" " * indent+ str(self.data))
    #     if self.esquerda:
    #         self.esquerda.PrintTree(indent + 2)
    #     #print (self.data, " ")
    #     sys.stdout.write(str(self.data) + " ")
    #     if self.direita:
    #         self.direita.PrintTree(indent + 2)
    def PrintTree(self):
        # if self.esquerda:
        #     self.esquerda.PrintTree()
        # #print(self.data),
        # sys.stdout.write(str(self.data) + " ")
        # if self.direita:
        #     self.direita.PrintTree()
        print(numNode)
        numNode = 0

# Use the insert method to add nodes
'''
root = NodeAVL()
root.add(3)
root.add(7)
root.add(4)
root.add(20)
root.add(15)

root.PrintTree()
'''