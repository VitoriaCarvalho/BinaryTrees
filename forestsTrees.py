import avl
import bst
import rbt

n = int(input())

while (True):
    ops = input().split()

    if (ops[0] == 3) return

    nAux = [random.random(), ]
    if (ops[1] == 0):
        # BST
        print('bst')
        tree = NodeBST(nAux[0])
    elif (ops[1] == 1):
        # AVL
        print('avl')
        tree = NodeAVL(nAux[0])
    elif (ops[1] == 2):
        # RBT
        print('rbt')
        tree = RedBlackTree()
        tree.add(nAux[0])

    if (ops[0] == 0):
        print('Pior caso!')
    elif (ops[0] == 1):
        for i in range(1, n):
            nAux[i].append(random.random())
            tree.add(nAux[i])

        for i in nAux:
            print(nAux, end=' ')

