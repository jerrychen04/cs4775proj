# Note: make sure to install muscle.exe on your PC with a path to it in order to run this script.
"""
This script performs multiple sequence alignment using MUSCLE.
Input: FASTA file
Output: FASTA file with aligned sequences

Alternatively, we used the MEGA MSA Alignment software to do some of our analyses. Take a look at that software if you have issues running this script, as it also runs MUSCLE without needing to provide a path to an .exe
"""


from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO
from io import StringIO


def multiple_sequence_alignment(input_file, output_file):
    # load muscle command line
    muscle_cline = MuscleCommandline(input=input_file)
    stdout, stderr = muscle_cline()

    # parse the alignment
    align = AlignIO.read(StringIO(stdout), "fasta")

    # writing the alignment to a file
    with open(output_file, "w") as f:
        AlignIO.write(align, f, "fasta")

    print("Alignment completed. Output file created:", output_file)


# usage example
input_fasta = "your_input_file.fasta"
output_fasta = "aligned_sequences.fasta"

multiple_sequence_alignment(input_fasta, output_fasta)
