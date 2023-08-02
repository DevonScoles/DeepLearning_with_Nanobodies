import gzip
# ***
# This file decompresses the tsv.gz files abd then outputs the tsv files
# ***

input_file = 'manual_meta.tsv.gz'
output_file = 'manual_meta.tsv'

with gzip.open(input_file, 'rb') as gz_file:
    with open(output_file, 'wb') as out_file:
        out_file.write(gz_file.read())

input_file = 'manual_sequence.tsv.gz'
output_file = 'manual_sequence.tsv'

with gzip.open(input_file, 'rb') as gz_file:
    with open(output_file, 'wb') as out_file:
        out_file.write(gz_file.read())

print("Decompression complete.")