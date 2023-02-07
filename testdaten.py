import csv

csv.register_dialect('excel_new', 'excel', delimiter=';' )
sprachen = ['Deutsch', 'Englisch']
geschlecht = ['m', 'w']
bool = ['ja', 'nein']
id = 1
profiles = []
configs = []
pitch = 'normal'
rate = 'durchschnittlich'
length = 'normal' 
expression = 'nein'

for knowledge in bool:
        for hearing in bool: 
            if hearing == 'ja':
                pitch = 'tief'
                rate = 'langsam'
                length = 'vereinfacht' 
            for language in sprachen:
                for gender in geschlecht:
                    for age in range(65,101):
                        if age > 80:
                            expression = 'ja'
                        profiles.append({'ID': id, 'Name': id, 'Alter': age, 'Geschlecht': gender, 'Sprache': language, 'Hörgerät': hearing, 'Vorkenntnisse': knowledge, 'alternative Keywords': ''})
                        configs.append({'ID': id, 'Geschlecht': 'männlich', 'Tonlage': pitch, 'Art': 'natürlich', 'Lautstärke' : 3, 'Sprache': language, 'Gesprächsorientierung': 'Aufgaben orientiert', 'Anrede': 'Du', 'alternative Keywords': '', 'Satzpause': 'kurz', 'Sprechgeschwindigkeit': rate, 'Satzlänge': length, 'Ausdruck': expression})
                        id += 1
                        expression = 'nein'
            pitch = 'normal'
            rate = 'durchschnittlich'
            length = 'normal' 

with open('Profil.csv', 'w', newline='') as csvfile:
    headers = ['ID', 'Name', 'Alter', 'Geschlecht', 'Sprache', 'Hörgerät', 'Vorkenntnisse', 'alternative Keywords']
    writer = csv.DictWriter(csvfile, dialect='excel_new', fieldnames=headers)
    writer.writeheader()
    writer.writerows(profiles)

with open('Config.csv', 'w', newline='') as csvfile:
    headers = ['ID', 'Geschlecht', 'Tonlage', 'Art', 'Lautstärke', 'Sprache', 'Gesprächsorientierung', 'Anrede', 'alternative Keywords', 'Satzpause', 'Sprechgeschwindigkeit', 'Satzlänge', 'Ausdruck']
    writer = csv.DictWriter(csvfile, dialect='excel_new', fieldnames=headers)
    writer.writeheader()
    writer.writerows(configs)
    
                    
                        
    
