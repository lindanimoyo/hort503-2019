"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: Lindani Moyo

"""

#python Project01.py SP1.fq SP1.trim.fq 30 30

import itertools

from itertools import islice

from sys import argv

def get_read(fq):
    """Extract a single read from a FASTQ file.

    Reads in a FASTQ file are stored in 4 lines that contain the
    sequence_id, nucleotide sequence, a second id, and a series of
    characters represeting quality scores.

    :param fq: A file handle for the FASTQ file
    :type fq: An io.TextIOBase object (created using the open() function).

    :return: a list containing 4 strings: the sequence ID, nucleotide sequence,
        second ID, and the quality score sequence. If there are no more
        sequences in the FASTQ file then this function returns False.
    :rtype: a list with four elements
    """
    my_read = list(itertools.islice(fq, 4)) #reads four lines at a time ot get the read

    print(my_read)

    if my_read:
        sequence_id = my_read[0].strip()
        # print(sequence)
        nucleotide_sequence = my_read[1].strip()
        second_id = my_read[2].strip()
        quality_score = my_read[3].strip()

    else:
        return False

    return [sequence_id, nucleotide_sequence, second_id, quality_score]





    # N = 4
    # y = [read.strip() for read in islice(fq, N)]
    # print(y)

#     reads_fq = fq.readlines()
#     print(reads_fq)
#
# get_read(open_fq)

#     N = 4
#
#     y = [read.strip() for read in islice(fq, N)]
#
#     print(y)
#
# get_readd(open_fq, 4)
#
# get_readd(open_fq, 4)



#     read_fq = fq.readlines()
#
#     for line in read_fq:
#         print(line)
#
# get_read(open_fq)
#


def trim_read_front(read, min_q, min_size):
    """Trims the low quality nucleotides from the front of a reads' sequences.

    This function examines the quality score of each nucleotide sequence
    starting from the first position of the sequence. When it encouters a
    high quality score it stops trimming and returns an updated read.

    :param read: A list containing for elements in this order: the sequence ID,
        the nucleotide sequence string, a secondary identifier string, and a
        quality score string.
    :type read: a list

    :param min_q:  The minimum quality score that a nucleotide must have to
        not be trimmed (e.g. 20).
    :type min_q:  integer

    :param min_size:  The minimum size that the sequence must have after
        trimming to keep the read (e.g. 25).
    :type min_size: integer

    :return: a list just like the the get_read() function returns but with the
       low-quality reads (and corresponding quality scores) trimmed off the
       front of the string. If the remaining trimmed read is smaller than the
       desired minimum read length then this function returns False.
    :rtype: a list with four elements
    """
    idx = 0
    seq_id, nuhc, sec_id, scores = read
    for qauity in scores:
        if ord(quality) < min_score:
            idx += 1
        print(idx)





#
# The main function for the script.
#
def main(argv):
    """The main function of this script.

    After trimming is completed, the fucntion prints out three status lines. The
    first indicates the total number of reads that were found. The second
    indicates how many reads were removed for being too short after trimming and
    the third indicates how many reads were trimmed and kept.

    The script will create a new FASTQ file of just the trimmed reads and name
    it according to the argument provided by the user when running the script.

    :param argv:  The incoming arguments to this script as
       provided by the sys.argv variable.  There must be four total arguments
       provided to the script must be in the following order

       - The filename for the input FASTQ file
       - The filename for the new output FASTQ file that this script creates
       - An integer for the minimum quality score. Anything below this at the
         beginning of each read's nucleotide sequence is trimmed off.
       - An integer indicating how large a read's nucleotide sequence must
         be after trimming in order to keep it.
    """
    script, fq_in, fq_out, quality, size = argv

    quality_limit = int(quality)

    min_size = int(size)

    with open (fq_in, "r") as file_handle:

        with open (fq_out, "w") as output_file:

            read = get_read(file_handle)

        while read:

            trim = trim_read_front(read, quality_limit, min_size)

            read = get_read(file_handle)

# Begin the program by calling the main function.
main(argv)
