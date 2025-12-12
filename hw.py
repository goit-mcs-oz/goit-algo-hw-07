

# Двійкове дерево пошуку
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = " " * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# Завдання 1. Знаходить найбільше значення
def searchMax(root, maxValue=None):
    if root:
        if maxValue is None or maxValue < root.val:
            maxValue = root.val
        return searchMax(root.right, maxValue)
    else:
        return maxValue


# Завдання 2. Знаходить найменше значення
def searchMin(root, minValue=None):
    if root:
        if minValue is None or minValue > root.val:
            minValue = root.val
        return searchMin(root.left, minValue)
    else:
        return minValue


# Завдання 3. Знаходить суму всіх значень
def calculateSum(root, sumValue=0):
    if root:
        return root.val + calculateSum(root.left, sumValue) + calculateSum(root.right, sumValue)
    else:
        return sumValue


root = Node(5)
root = insert(root, 9)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 8)

print(root)
print(f'Найбільше значення: {searchMax(root)}')
print(f'Найменше значення: {searchMin(root)}')
print(f'Сумма всіх значень: {calculateSum(root)}')
