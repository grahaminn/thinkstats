import survey
table = survey.Pregnancies()
table.ReadRecords()

first_births = 0
first_birth_pregnancy_lengths = 0.0
later_births = 0
later_birth_pregnancy_lengths = 0.0

for record in table.records:
    if record.outcome != 1:
        continue

    if record.birthord == 1:
        first_births += 1
        first_birth_pregnancy_lengths += record.prglength
    else:
        later_births += 1
        later_birth_pregnancy_lengths += record.prglength

print 'live first births:',  first_births
print 'live subsequent births:', later_births         

print 'average first birth pregnancy length:', first_birth_pregnancy_lengths / first_births
print 'average later birth pregnancy length:', later_birth_pregnancy_lengths / later_births
