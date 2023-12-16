from Bio import Phylo
from Bio.Phylo.BaseTree import Clade
from io import StringIO
import itertools


# Read the original tree
tree = Phylo.read("sample2.nwk", "newick")

# Function to find the immediate siblings in a tree, given a sequence name


def find_siblings(tree, sequence_name):
    for clade in tree.find_clades():
        if clade.name == sequence_name:
            # Parent clade should have more than one child for siblings to exist
            if clade.parent and len(clade.parent.clades) > 1:
                siblings = [
                    sibling for sibling in clade.parent if sibling.name != sequence_name]
                return siblings
    return None


# Extract specific sequences and their branch lengths
sequences_to_keep = ['Sequence1', 'Sequence2', 'Sequence3', 'Sequence4']
kept_clades = {seq: None for seq in sequences_to_keep}

for seq in sequences_to_keep:
    siblings = find_siblings(tree, seq)
    if siblings:
        # Choose the first sibling found; in a binary tree, there should be only one sibling
        sibling = siblings[0]
        kept_clades[seq] = sibling

# Determine the pairs of sequences (which sequences are siblings)
pairs = [(seq, sibling.name)
         for seq, sibling in kept_clades.items() if sibling]

# Since we want an unrooted tree, we can just take two pairs to form the topology
# In a four taxa tree, if A is sibling to B, and C to D, the topology is ((A,B),(C,D))
# There should be exactly two pairs, but in case of multiple options, we take the first two
if len(pairs) > 2:
    pairs = pairs[:2]

# Generate the unrooted topology based on the pairs
# We simply put these pairs as clades in the unrooted tree
unrooted_clades = [Clade(branch_length=0.0, clades=[Clade(branch_length=0.0, name=pair[0]),
                                                    Clade(branch_length=0.0, name=pair[1])])
                   for pair in pairs]
unrooted_tree = Clade(branch_length=0.0, clades=unrooted_clades)

# Create tree for the topology
tree = Phylo.BaseTree.Tree(rooted=False, clade=unrooted_tree)

# Print the tree in Newick format
print("Unrooted tree topology:", tree.format("newick"))
