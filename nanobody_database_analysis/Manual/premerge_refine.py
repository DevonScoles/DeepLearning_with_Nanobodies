import pandas as pd

# open files for reading/writing
metaData = pd.read_csv('manual_meta.tsv', delimiter='\t')
sequence = pd.read_csv('manual_sequence.tsv', delimiter='\t')


sequence = sequence.rename(columns={'Comma-separated db-specific IDS': 'id'}) #rename column to just id
sequence = sequence[ ['id'] + [col for col in sequence.columns if col != 'id'] ] # sort left to right starting from id column


# Convert the "id" column to numeric values
sequence = sequence.sort_values('id')
metaData = metaData.sort_values('id')

# adds binary human non-human column to metaData
# defaults to 0 for non-humn 1 for human.

num_rows = metaData.shape[0]
human_column_data = [0] * num_rows
human_column = "Human"
metaData[human_column] = human_column_data

print(metaData.head())

# merge = pd.merge(metaData, sequence, on='id', how='outer')

# # ***
# # When multiple instances or rows of id exist
# # loop appends -instance# onto the end e.g. 8731642-1 then 8731642-2 then 8731642-3...
# # ***
# merge_dups = merge['id'].duplicated()
# suffixes = {}
# for i,row in merge.iterrows():
#     id_value = row['id'] # id value = random num in 'id' column
#     if merge_dups[i]: # i = line from sequence file so here we check if that line is in the duplicated series
#         if id_value in suffixes:
#             suffixes[id_value] += 1
#             merge.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"
        
#         else:
#             suffixes[id_value] = 1
#             merge.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"



# merge.to_csv('manual_merged.csv', index=False)