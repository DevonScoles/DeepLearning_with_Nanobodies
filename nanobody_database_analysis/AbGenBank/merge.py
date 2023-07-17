import pandas as pd

metaData = pd.read_csv('modified_abgenbank_metadata.tsv', delimiter='\t')
sequence = pd.read_csv('modified_abgenbank_sequence.tsv', delimiter='\t')

metaData['id'] = metaData['id'].astype(str)
sequence['id'] = sequence['id'].astype(str)

merge = pd.merge(metaData, sequence, on='id', how='outer')

merge.to_csv('abgenbank_merged.csv', index=False)