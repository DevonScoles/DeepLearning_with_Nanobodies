import pandas as pd

metaData = pd.read_csv('modified_pat_metadata.tsv', delimiter='\t')
sequence = pd.read_csv('modified_pat_sequence.tsv', delimiter='\t')

metaData['id'] = metaData['id'].astype(str)
sequence['id'] = sequence['id'].astype(str)

merge = pd.merge(metaData, sequence, on='id', how='outer')

# ***
# When multiple instances or rows of id exist
# loop appends -instance# onto the end e.g. 8731642-1 then 8731642-2 then 8731642-3...
# ***
merge_dups = merge['id'].duplicated()
suffixes = {}
for i,row in merge.iterrows():
    id_value = row['id'] # id value = random num in 'id' column
    if merge_dups[i]: # i = line from sequence file so here we check if that line is in the duplicated series
        if id_value in suffixes:
            suffixes[id_value] += 1
            merge.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"
        
        else:
            suffixes[id_value] = 1
            merge.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"

merge.to_csv('patent_merged.csv', index=False)