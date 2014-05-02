import survey
table = survey.Pregnancies()
table.ReadRecords()
first_births = 0
later_births = 0
for record in table.records:
    if record.outcome != 1: 
        continue

    if record.birthord == 1:
        first_births+=1
    else:
        later_births+=1

print 'live first births:',  first_births
print 'live subsequent births:', later_births         
