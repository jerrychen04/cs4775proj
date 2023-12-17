"""
Plot a phylogenetic tree from a Newick file.
"""

from Bio import Phylo
import matplotlib.pyplot as plt

# read the Newick tree file
tree = Phylo.read(
    "nwk_tree_analysis\monte_carlo_trees\sample4jc.nwk", "newick")

# prepare the matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# draw the unrooted tree
Phylo.draw(tree, do_show=False, axes=ax)

# customize the plot
ax.axis('on')
plt.tight_layout()

# show or save the plot
plt.savefig("sample4_jc.png")
# plt.show()
