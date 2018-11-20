import avl
import bst
import rbt
import random
import sys

#VERIFICAR SE NA PRIMEIRA EXECUÇÃO PODE DIGITAR 3 SEM ENCERRAR

n = int(input())

while (True):
    #ops = [input().split(" ")]
    ops = input().split(' ')

    if (ops[0] == '3'): break

    nAux = [random.randint(1, 100), ]

    ########## PIOR CASO: ORDENADOS ##########
    if(ops[0] == '0'):
        for i in range(1,n):
            num = random.randint(1, 100)
            nAux.insert(i, num)
        nAux.sort() #ordenando

        if (ops[1] == '0'):
            # BST
            print('bst')
            tree = bst.NodeBST(nAux[0])
        elif (ops[1] == '1'):
            # AVL
            print('avl')
            tree = avl.NodeAVL(nAux[0])
        elif (ops[1] == '2'):
            # RBT
            print('rbt')
            tree = rbt.RedBlackTree()
            tree.add(nAux[0])

        for i in range(1,n): tree.add(nAux[i])

    ########## MELHOR CASO: ALEATÓRIOS ##########
    elif(ops[0] == '1'):
        if (ops[1] == '0'):
            # BST
            print('bst')
            tree = bst.NodeBST(nAux[0])
        elif (ops[1] == '1'):
            # AVL
            print('avl')
            tree = avl.NodeAVL(nAux[0])
        elif (ops[1] == '2'):
            # RBT
            print('rbt')
            tree = rbt.RedBlackTree()
            tree.add(nAux[0])
        
        for i in range(1,n):
            num = random.randint(1, 100)
            nAux.insert(i, num)
            #nAux[i].append(num)
            tree.add(nAux[i])

    for i in nAux:
        #print(nAux[i], end=' ')
        sys.stdout.write(str(i) + " ")

    print()
    tree.PrintTree()
    print()

