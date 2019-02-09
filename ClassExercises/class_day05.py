from sys import argv

import numpy as np

script, in_file, outfile = argv

#normalized_expression count data

normalized_expression_data = open(in_file, 'r')

output_split = open(outfile, 'w')

# def my_x(value):
    # x_value = math.log2(value)
    # if value == 0.000000 or value == 0:
    #     return x_value == 0.000000
    # else:
    #     return x_value

def split_count(open_file):
    #open file with normalized_expression_data
    normalized_expression_data_read = open_file.readlines()
    # print(normalized_expression_data_read)
    lines = normalized_expression_data_read


    for line in lines:
        split_file = line.split()

        # split_file[1]

        # print(split_file[0])

        float_expression = float((split_file[1]))

        log_float_expr = np.log2(float_expression)

        if log_float_expr == 0:
            log_float_expr = 0

        output_split.write(split_file[0])

        output_split.write("\t")

        output_split.write(split_file[1])

        output_split.write('\t')

        output_split.write(str(log_float_expr))

        output_split.write('\n')

        # normalized_expression_data_read_split.append(line)
        # print(normalized_expression_data_read_split)

split_count(normalized_expression_data)

output_split.close()
normalized_expression_data.close()
