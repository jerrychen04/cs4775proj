from Bio import Phylo
import matplotlib.pyplot as plt

# read the Newick tree file
tree = Phylo.read("new_four_taxa_tree.nwk", "newick")

# prepare the matplotlib figure and axis
fig, ax = plt.subplots(figsize=(8, 8))  # Adjust the figure size as needed

# draw the unrooted tree
Phylo.draw(tree, do_show=False, axes=ax)

# customize the plot
ax.axis('off')  # Turn off the axis
plt.tight_layout()

# show or save the plot
plt.savefig("unrooted_tree_plot.png")  # Save the plot as a PNG file
plt.show()  # Show the plot
