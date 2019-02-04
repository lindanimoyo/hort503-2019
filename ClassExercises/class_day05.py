from sys import argv

script, in_file, outfile = argv

#normalized_expression count data

normalized_expression_data = open(in_file)

normalized_expression_data_read = normalized_expression_data.read()

normalized_expression_data_read_split = normalized_expression_data_read.split(' ')

print(normalized_expression_data_read_split)

output_split = open(outfile, 'w')

output_split.write(normalized_expression_data_read_split)


output.close()
normalized_expression_data.close()
