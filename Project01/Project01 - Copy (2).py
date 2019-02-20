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
    my_read = [read.strip() for read in islice(fq, 4)]

    # print(my_read)

    if my_read:
        print("extracting read....")
        sequence_id = my_read[0]
        #print(sequence_id)
        nucleotide_sequence = my_read[1]
        # print(nucleotide_sequence)
        second_id = my_read[2]
        # print(second_id)
        quality_score = my_read[3]
        # print(quality_score)
    else:
        return False
    return [sequence_id, nucleotide_sequence, second_id, quality_score]

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
    print("trimming read.......")
    nucl_sequence = read[1]
    nucl_seq_list = list(nucl_sequence)
    nucl_seq_list_copy = nucl_seq_list
    #print(nucl_seq_list)

    nucl_score = read[3]
    nucl_score_list = list(nucl_score)
    #print(nucl_score_list)

    # for i in range(len(nucl_seq_list)):
    #     nucl_seq_list_element = nucl_seq_list[i]
    #     nucl_seq_list_element = nucl_seq_list_element_copy
    #     print(nucl_seq_list_element_copy)
    #     print(nucl_seq_list_element_copy)
    #     nucl_score_list_element = nucl_score_list[i]
    #     true_nucl_score_list_element = (ord(nucl_score_list_element) - 33)
    #     print(true_nucl_score_list_element)
    #     if true_nucl_score_list_element < min_q:

    for i, j in zip(nucl_seq_list, nucl_score_list):
        print(i)
        print(j)
        nucl_score_list_element = j
        true_nucl_score_list_element = (ord(nucl_score_list_element) - 33)
        print(true_nucl_score_list_element)

        if true_nucl_score_list_element < min_q:
            print(true_nucl_score_list_element)
            del nucl_seq_list_copy[0]
            print(nucl_seq_list_copy)
            # del qual_read_list[0]
        else:
            raise StopIteration

        length_trimmed_read = len(nucl_seq_list_copy)

        length_untrimmed_read = len(nucl_seq_list_copy)






        #     print(true_score)
        #     seq_read_list.remove(i)
        #     qual_read_list.remove(j)
        #
        # print(seq_read_list)
        # print(qual_read_list)
        #
        # if len(seq_read_list) < 30:
        #     del seq_read_list
        #     del qual_read_list
    # print(seq_read_list)
    # print(qual_read_list)


    #
    #
    #
    # if i == 1 and i == j:
    #     do(x
    #
    #
    #
    #
    #
    # for i in range(len(seq_read_list)):
    #     nucl = seq_read_list[i]
    #     true_score = (ord(y) - 33)
    #
    #
    #     if seq_read_list[i]==list2[i]:
    #
    #
    #
    #
    #
    #
    #
    #
    # for nucl in seq_read_list:
    #
    #
    #
    #     print(nucl)
    #     for y in qual_read_list:
    #         true_score = (ord(y) - 33)
    #         print(true_score)
    #         if true_score > 30:
    #             #print(true_score)
    #             seq_read_list_trimmed.append(nucl)
    #             qual_read_list_trimmed.append(y)
    #         else:
    #             pass
    # if len(seq_read_list) < 30:
    #     del seq_read_list
    #     del qual_read_list
    # # print(seq_read_list)
    # # print(qual_read_list)




























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

    print("Opening SP1.fq file for reading...")

    with open (fq_in, "r") as file_handle:
        read = get_read(file_handle)

        while read:
# readcount = 0
#             readcount += 1

            trim_read = trim_read_front(read, quality_limit, min_size)

            with open (fq_out, "w") as output_file:
                output.write(sequence_id)
                output.write('\n')
                output.write(nucleotide_sequence) #edit to include the trimmed read
                output.write('\n')
                output.write(second_id)
                output.write('\n')
                output.write(quality_score) #edit to include the Q trimmed read
                output.write('\n')

            # print("total reads")
            # print("total short reads removed")
            # print("")

# Begin the program by calling the main function.
main(argv)
