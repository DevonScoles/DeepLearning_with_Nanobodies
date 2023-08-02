import pandas as pd

# open files for reading/writing
metaData = pd.read_csv('structure_meta.tsv', delimiter='\t')
sequence = pd.read_csv('structure_sequence.tsv', delimiter='\t')


sequence = sequence.rename(columns={'Comma-separated db-specific IDS': 'id'}) #rename column to just id
sequence = sequence[ ['id'] + [col for col in sequence.columns if col != 'id'] ] # sort left to right starting from id column

