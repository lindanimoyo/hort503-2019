"""A Python script that performs simple read trimming of a FASTQ file.

.. module:: Project01
   :platform: Unix, Windows
   :synopsis: This script receives as input a FASTQ file and a set of arguments
      that control trimming. A new FASTQ file is generated containing only
      trimmed reads that meet the given requirements.

.. moduleauthor:: Lindani Moyo

"""
#python Project01.py SP1.fq SP1.trim.fq 30 30 SP1.fasta

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

    if my_read:
        # print("extracting read....")
        sequence_id = my_read[0]
        nucleotide_sequence = my_read[1]
        second_id = my_read[2]
        quality_score = my_read[3]
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
    # print("trimming read.......")
    nucl_sequence = read[1]
    nucl_seq_list = list(nucl_sequence)
    nucl_seq_list_copy = nucl_seq_list

    nucl_score = read[3]
    nucl_score_list = list(nucl_score)

    sequence_id = read[0]
    second_id =read[2]
    counter = 0

    for nucl_score_list_element in nucl_score:
        true_nucl_score_element = (ord(nucl_score_list_element) - 33)

        if true_nucl_score_element < min_q:
            counter += 1
        else:
            break

    trimmed_sequence = nucl_sequence[counter:]
    trimmed_quality_score = nucl_score[counter:]

    if len(trimmed_sequence) < min_size:
        return False
    else:
        return [sequence_id, trimmed_sequence, second_id, trimmed_quality_score]

# The main function for the script.
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
    script, fq_in, fq_out, quality, size, fasta = argv

    quality_limit = int(quality)
    min_size = int(size)
    read_count = 0
    read_removed_count = 0

    print(f"Opening {fq_in} file for reading...")
    with open (fq_in, "r") as file_handle:
        print(f"Opening {fq_out} file for writing...")
        with open (fq_out, "w") as output_file:
            print(f"Opening {fasta} file for writing...")
            with open (fasta, "w") as fasta_outputfile:
                read = get_read(file_handle)

                while read:
                    trim_read = trim_read_front(read, quality_limit, min_size)

                    if trim_read == False:
                        read_removed_count += 1
                        read = get_read(file_handle)
                    else:
                        sequence_id, trimmed_sequence, second_id, trimmed_quality_score = trim_read
                        read_count += 1
                        output_file.write(sequence_id)
                        output_file.write('\n')
                        output_file.write(trimmed_sequence)
                        output_file.write('\n')
                        output_file.write(second_id)
                        output_file.write('\n')
                        output_file.write(trimmed_quality_score)
                        output_file.write('\n')

                        fasta_outputfile.write(f">{sequence_id}")
                        fasta_outputfile.write('\n')
                        fasta_outputfile.write(trimmed_sequence)
                        fasta_outputfile.write('\n')
                        fasta_outputfile.write('\n')

                        read = get_read(file_handle)

    print(f"total number of reads found were {read_removed_count + read_count}")
    print(f"total short reads removed were {read_removed_count}")
    print(f"total number of reads trimmed and kept were {read_count}")

# Begin the program by calling the main function.
main(argv)
