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


# Example usage
input_fasta = "your_input_file.fasta"  # Replace with your input file path
output_fasta = "aligned_sequences.fasta"  # Output file

multiple_sequence_alignment(input_fasta, output_fasta)
