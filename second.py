import survey
table = survey.Pregnancies()
table.ReadRecords()
live_births = 0
for record in table.records:
       if record.outcome == 1:
           live_births += record.nbrnaliv

print 'live births:',  live_births         
