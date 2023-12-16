from ete3 import Tree
from ete3 import TreeStyle, NodeStyle, AttrFace, faces


def load_tree(file_path):
    # Load a tree from a Newick file
    with open(file_path, 'r') as file:
        newick_str = file.read().strip()
    return Tree(newick_str, format=1)


def calculate_similarity(tree1, tree2):
    # Calculate the Robinson-Foulds distance
    rf_distance, _, _, _ = tree1.robinson_foulds(tree2)

    # Calculate the branch length score
    branch_length_score = tree1.compare(tree2, unrooted=True)[
        'branch_length_score']

    return rf_distance, branch_length_score


def main(tree_path1, tree_path2):
    # Load the trees
    tree1 = load_tree(tree_path1)
    tree2 = load_tree(tree_path2)

    # Calculate the similarity
    rf_distance, branch_length_score = calculate_similarity(tree1, tree2)

    print(f"Robinson-Foulds Distance: {rf_distance}")
    print(f"Branch Length Score: {branch_length_score}")


# Example usage
# Replace 'tree1.nwk' and 'tree2.nwk' with your file paths
main('sample2.nwk', 'sample2gtr.nwk')
