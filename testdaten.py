import csv

csv.register_dialect('excel_new', 'excel', delimiter=';' )
sprachen = ['Deutsch', 'Englisch']
geschlecht = ['m', 'w']
bool = ['ja', 'nein']
wissen = ['ja', 'nein']
id = 1

with open('testdaten.csv', 'w', newline='') as csvfile:
    headers = ['ID', 'Name', 'Alter', 'Geschlecht', 'Sprache', 'Hörgerät', 'Vorkenntnisse']
    writer = csv.DictWriter(csvfile, dialect='excel_new', fieldnames=headers)
    
    writer.writeheader()

    for knowledge in bool:
        for hearing in bool:
            for language in sprachen:
                for gender in geschlecht:
                    for age in range(65,101):
                        writer.writerow({'ID': id, 'Name': id, 'Alter': age, 'Geschlecht': gender, 'Sprache': language, 'Hörgerät': hearing, 'Vorkenntnisse': knowledge})
                        id += 1
                    
                        
    
