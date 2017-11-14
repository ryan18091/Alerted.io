import random



alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']

order = []

def in_order():
    global alpl
    global order

    while len(alpl) != 0:
        x = alpl[0]
        order.append(x)
        alpl.remove(x)
    return order


def backwards(alpl):
    i = alpl[-1]
    return i

def random_gen():
    global alpl
    global order


    while len(alpl) != 0:
        x = random.choice(alpl)
        order.append(x)
        alpl.remove(x)
        # return order

# random_gen()
# print(order)

#

# for _ in range(3):
    random_gen()
    print(order)
    alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
    order = []

def random_order():
    global order
    random_gen()
    alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']
    order = []