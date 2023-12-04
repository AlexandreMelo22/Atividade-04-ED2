import random
import time
from sortedcontainers import SortedDict  # Para AVL e Rubro-Negra

# Função para ler os primeiros 100.000 números do arquivo
def read_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[:100000]
        numbers = [int(num.strip()) for line in lines for num in line.split(',')]
    return numbers

# Função para preencher a árvore com os números e medir o tempo
def fill_tree(tree, numbers):
    start_time = time.time()
    for num in numbers:
        tree[num] = True  # Para AVL e Rubro-Negra
    end_time = time.time()
    return end_time - start_time

# Função para realizar operações aleatórias
def random_operations(tree, numbers):
    for _ in range(50000):
        random_num = random.randint(-9999, 9999)

        if random_num % 3 == 0:
            tree[random_num] = True  # Para AVL e Rubro-Negra
        elif random_num % 5 == 0:
            if random_num in tree:  # Para AVL e Rubro-Negra
                del tree[random_num]
        else:
            count = tree.get(random_num, 0)  # Para AVL e Rubro-Negra
            print(f'O número {random_num} aparece {count} vezes na árvore.')

# Execução
avl_tree = SortedDict()
rb_tree = SortedDict()

numbers = read_numbers('numeros.txt')

avl_time = fill_tree(avl_tree, numbers)
rb_time = fill_tree(rb_tree, numbers)

print(f'Tempo de inserção AVL: {avl_time} segundos')
print(f'Tempo de inserção Rubro-Negra: {rb_time} segundos')

random_operations(avl_tree, numbers)
random_operations(rb_tree, numbers)
