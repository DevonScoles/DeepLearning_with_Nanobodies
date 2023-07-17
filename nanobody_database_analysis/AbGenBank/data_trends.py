import pandas as pd

merge = pd.read_csv('abgenbank_merged.csv')

occurrencesOfOrgs = merge['organism'].value_counts()
humans = occurrencesOfOrgs['Homo sapiens']
total_occurrences = occurrencesOfOrgs.sum()
probability_of_human = (humans / total_occurrences) * 100

print(f"Probability of human from Abgenbank: {round(probability_of_human, 3)}%\n"
f"Probability of non-human: {round(1-probability_of_human, 3)}%")