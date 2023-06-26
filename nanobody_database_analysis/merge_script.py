import csv

meta_file = open('patent_meta.tsv', 'r')
seq_file = open('patent_sequence.tsv', 'r')
meta_reader = csv.reader(meta_file, delimiter='\t')
seq_reader = csv.reader(seq_file, delimiter='\t')

print(next(meta_reader))
next(seq_reader)
print(next(seq_reader))

meta_file.close()
seq_file.close()
