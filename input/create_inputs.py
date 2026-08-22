import csv

pseudo_one = set()
pseudo_two = set()
real_one = set()
real_two = set()

# in theory including all 4 counterbalances doesn't do anything because they all contain the same words,
# but since the script needs to do multiple files anyway, I included them as a safety redundancy
files = ['Counterbalance 1.csv', 'Counterbalance 2.csv', 'Counterbalance 3.csv', 'Counterbalance 4.csv', 'Identical Trials.csv', 'Practice Trials.csv']

for file in files:
    with open(f'input/Study Trials/{file}', newline='') as rf:
        for row in csv.DictReader(rf):
            
            target_is_real = row['Target Type'] == 'real'
            target_syllables = int(row['Target Syllables'])
            prime_syllables = int(row['Prime Syllables'])
            
            # handle the prime
            if (prime_syllables == 1):
                real_one.add(row['Prime'])
            elif (prime_syllables == 2):
                real_two.add(row['Prime'])
            else:
                raise ValueError(f"detected prime word {row['Prime']} has wrong number of syllables at {prime_syllables}")
                
            # handle the real word
            # there is certainly a more pretty way to do this, but this works
            if (target_syllables == 1):
                real_one.add(row['Target']) if target_is_real else pseudo_one.add(row['Target']) 
            elif (target_syllables == 2):
                real_two.add(row['Target']) if target_is_real else pseudo_two.add(row['Target'])
            else:
                raise ValueError(f"detected target word {row['Target']} has wrong number of syllables at {target_syllables}")
                
# Sanity Check
print(f"""
    One Syllable Pseudos - {len(pseudo_one)}
    Two Syllable Pseudos - {len(pseudo_two)}
    One Syllable Reals - {len(real_one)}
    Two Syllable Reals - {len(real_two)}
    """)


# output them to files
def output_csv(file_name, set, is_pseudo):
    with open(f'input/{file_name}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for item in set:
            writer.writerow([item])
        
output_csv('One Syllable Real', real_one, False)
output_csv('Two Syllable Real', real_two, False)
output_csv('One Syllable Pseudo', pseudo_one, True)
output_csv('Two Syllable Pseudo', pseudo_two, True)