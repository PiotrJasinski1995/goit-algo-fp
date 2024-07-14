import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue", childlside=False):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Additional argument to store the color of the node
        self.elements = []
        heapq.heappush(self.elements, key)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, color=node.color)  # Saving a node color in a graph
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {(tree_root.val): (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Collect node colors to display

    plt.figure(figsize=(8, 5), num=1)
    nx.draw(tree, pos=pos, with_labels=True, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def add_node(tree_root, key):
    heapq.heappush(tree_root.elements, key)
    heapq.heapify(tree_root.elements)


def create_tree(tree_root):
    tree_root.val = tree_root.elements[0]
    tree_root.left = None
    tree_root.right = None

    for element in tree_root.elements[1:]:
        add_to_tree(tree_root, element)


def add_to_tree(root, element):
    if not root.left:
        root.left = Node(element)
    elif not root.right:
        root.right = Node(element)
    else:
        if root.left.left != None and root.left.right != None:
            if root.right.left != None and root.right.right != None:
                add_to_tree(root.left, element)
            else:
                add_to_tree(root.right, element)
        else:
            add_to_tree(root.left, element)


def visit_dfs(root, node):
    if node:
        node.color = '#1296F0'
        draw_tree(root)
        node.color = '#90EE90'

        visit_dfs(root, node.left)
        visit_dfs(root, node.right)


def visit_bfs(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while(len(queue) > 0):
        node = queue.pop(0)
        node.color = '#1296F0'
        draw_tree(root)
        node.color = '#90EE90'

        while plt.fignum_exists(1):
            pass

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def main():
    while True:
        command = input('Type "dfs" or "bfs" to choose the traversal ("exit" or "close" to leave):\n')

        # Creating the tree
        root = Node(0)
        add_node(root, 4)
        add_node(root, 5)
        add_node(root, 10)
        add_node(root, 1)
        add_node(root, 3)
        add_node(root, 7)
        add_node(root, 64)
        add_node(root, 23)
        add_node(root, 44)
        create_tree(root)

        if command in ['close', 'exit']:
            print('Goodbye!')
            break
        elif command == 'dfs':
            print('You have chosen dfs')
            visit_dfs(root, root)
        elif command == 'bfs':
            print('You have chosen bfs')
            visit_bfs(root)
        else:
            print('Please use commands!')


if __name__ == '__main__':
    main()
