"""
This script is used to compare the RF distance between the monte carlo trees and the nextstrain trees.
"""


class Node:
    def __init__(self, name='', length=0.0):
        self.name = name
        self.length = length
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def parse_newick(newick):
    stack, i, ln = [], 0, len(newick)
    root = Node()
    current_node = root

    while i < ln:
        if newick[i] == '(':
            new_node = Node()
            current_node.add_child(new_node)
            stack.append(current_node)
            current_node = new_node
        elif newick[i] == ',':
            current_node = stack[-1]
        elif newick[i] == ')':
            current_node = stack.pop()
        elif newick[i] not in ';':
            start = i
            while i < ln and newick[i] not in [',', ')', ':']:
                i += 1
            current_node.name = newick[start:i]
            if i < ln and newick[i] == ':':  # handle branch length
                start = i + 1
                while i < ln and newick[i] not in [',', ')', ';']:
                    i += 1
                branch_length_str = newick[start:i]
                if branch_length_str[-1] == ';':
                    branch_length_str = branch_length_str[:-1]
                current_node.length = float(branch_length_str)
                i -= 1
        i += 1

    return root


def extract_clades(node, clades):
    if node.children:
        clade = ','.join(sorted([child.name for child in node.children]))
        clades.add(clade)
        for child in node.children:
            extract_clades(child, clades)
    return clades


def robinson_foulds_distance(tree1, tree2):
    clades1 = extract_clades(tree1, set())
    clades2 = extract_clades(tree2, set())

    return len(clades1.symmetric_difference(clades2))


# substitute using all of our monte carlo vs. next strain ground truth trees
newick1 = "((3:0.0013155685372809494,(2:4.895425914735705E-4,1:4.895425914735705E-4):8.260259458073789E-4):4.828227370447637E-4,4:0.001798391274325713):0.0;"
newick2 = "(1:0,(((((((((((((((((((2:6):2):1):0):3):3):8):6):1):0):0):0):0):0):0):0,(((((((((((((3:0):1):0):1):0):0):0):0):2):1):13,((((((((((((4:21):0):3):3):1):2):8):4):3):1):4):17):6):29):1):3):1):1):2):0):0;"

tree1 = parse_newick(newick1)
tree2 = parse_newick(newick2)

distance = robinson_foulds_distance(tree1, tree2)
print(f"Robinson-Foulds distance: {distance}")
