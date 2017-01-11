# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

def compute(strand_a, strand_b):

    if check_strand_length(strand_a,strand_b) == False:
        raise ValueError

    difference = 0
    nucleotide = 0
    while(nucleotide < len(strand_a)):
        if strand_a[nucleotide] != strand_b[nucleotide]:
            difference = difference + 1
        nucleotide = nucleotide + 1

    return difference

def check_strand_length(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        return False
