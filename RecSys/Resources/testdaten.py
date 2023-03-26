import csv

csv.register_dialect('excel_new', 'excel', delimiter=';' )
sprachen = ['Deutsch', 'Englisch']
geschlecht = ['maennlich', 'weiblich', 'divers']
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
                        profiles.append({'userId': id, 'Name': id, 'Alter': age, 'Geschlecht': gender, 'Sprache': language, 'Hoergeraet': hearing, 'Vorkenntnisse': knowledge})
                        configs.append({'userId': id, 'Geschlecht': 'maennlich', 'Tonlage': pitch, 'Klang': 'natuerlich', 'Lautstaerke' : 3, 'Sprache': language, 'Gespraechsorientierung': 'Aufgaben orientiert', 'Anrede': 'Du', 'Satzpause': 'kurz', 'Sprechgeschwindigkeit': rate, 'Satzlaenge': length, 'Ausdruck': expression, 'alternative Keywords': ''})
                        id += 1
                        expression = 'nein'
            pitch = 'normal'
            rate = 'durchschnittlich'
            length = 'normal' 

with open('profile.csv', 'w', newline='') as csvfile:
    headers = ['userId', 'Name', 'Alter', 'Geschlecht', 'Sprache', 'Hoergeraet', 'Vorkenntnisse']
    writer = csv.DictWriter(csvfile, dialect='excel_new', fieldnames=headers)
    writer.writeheader()
    writer.writerows(profiles)

with open('config.csv', 'w', newline='') as csvfile:
    headers = ['userId', 'Geschlecht', 'Tonlage', 'Klang', 'Lautstaerke', 'Sprache', 'Gespraechsorientierung', 'Anrede', 'Satzpause', 'Sprechgeschwindigkeit', 'Satzlaenge', 'Ausdruck', 'alternative Keywords']
    writer = csv.DictWriter(csvfile, dialect='excel_new', fieldnames=headers)
    writer.writeheader()
    writer.writerows(configs)
    
                    
                        
    
