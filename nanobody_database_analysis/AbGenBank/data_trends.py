import pandas as pd

merge = pd.read_csv('abgenbank_merged.csv')

occurrencesOfOrgs = merge['organism'].value_counts()
humans = occurrencesOfOrgs['Homo sapiens']
total_occurrences = occurrencesOfOrgs.sum()
probability_of_human = (humans / total_occurrences)

sequences_num = merge['sequence'].duplicated()
id_num = merge['id'].count()

# print(f"There are {id_num} nanobody IDs. {humans} of them are humans while {id_num-humans} are nonhuman."
# f"\nProbability of human from Abgenbank: {round(probability_of_human * 100, 3)}%\n"
# f"Probability of non-human: {round((1-probability_of_human) * 100, 3)}%")

cdr1_mask = merge['CDR1'].notna()
cdr1_nut_null = merge['CDR1'][cdr1_mask]
cdr2_mask = merge['CDR2'].notna()
cdr2_nut_null = merge['CDR2'][cdr2_mask]
cdr3_mask = merge['CDR3'].notna()
cdr3_nut_null = merge['CDR3'][cdr3_mask]

# print("There's",len(cdr1_nut_null.unique()), "unique regions in Complementarity-determining region 1")
# print(len(cdr2_nut_null.unique()), "unique regions in Complementarity-determining region 2\nand",
# len(cdr3_nut_null.unique()), "unique regions in Complementarity-determining region 3 ")

print(merge[cdr1_mask][merge['CDR1'] == nand]) # finding humans and non-humans in CDR1