import pandas as pd
import Fit_Data as Fitting
import KNN
from flask import Flask, jsonify, request, redirect, render_template, url_for


ip = "" #eigene IP-Adresse angeben
port = 8080
profiles = "./Resources/profile_created.csv"
configfile_created = "./Resources/config_created.csv"
   

def Server():
    app = Flask(__name__)
    app.static_folder = 'static'

    @app.route('/MCI/<int:uid>/', methods=['GET', 'POST'])
    def change_config(uid):

        userdata, configdata = getUser(uid)
        recdata = KNN.predictConfig(userdata)
        recdata = Fitting.retranslate_configMapping(list(recdata))
        print(configdata)
        
        if request.method == 'POST':
            return redirect(url_for('index'))
        return render_template('config.html', c=configdata , r=recdata, u=userdata)
    
    
    @app.route('/save_config/', methods=['POST'])
    def save_config():
        data = request.get_json()
        store_config(data)
        return jsonify(data)


    @app.route('/MCI/newUser/', methods=['GET', 'POST'])
    def newUser_form():
        if request.method == 'POST':
            return redirect(url_for('index'))
        return render_template('createProfile.html')
    

    @app.route('/get_new_user/', methods=['POST'])
    def get_new_user():
        data = request.get_json()
        id = storeUser(data)
        create_default_config(id)
        print("\n#### Added new user ####")
        print("Username:", data["userName"])
        print("Config:", data)
        print("ID:", id, "\n")
        data['userId'] = id
        return jsonify(data)

    app.run(host=ip, port=port)

    
def getUser(id): 
    config = get_csvconfig_created(id)
    user = get_csvuser_created(id)
    return user, config 

def storeUser(data): #Profil abspeichern
    userId = 901 + pd.read_csv(Fitting.userfile_created, sep=";")["userId"].size
    with open(profiles, 'a') as csv:
        csv.write("\n" + str(userId) + ";" + data['userName'] + ";" + data['age'] + ";" + data['gender_p'] + ";" + data['language_p'] + ";" + data['hearing_aid'] + ";" + data['prior_knowledge'])
    return userId

def store_config(data): #Konfigurationen abspeichern
    print(data)
    csv = pd.read_csv(configfile_created, sep=';')
    id = int(data["userId"])

    csv.loc[csv["userId"] == id, "Geschlecht"] = data["gender"]
    csv.loc[csv["userId"] == id, "Tonlage"] = data["pitch"]
    csv.loc[csv["userId"] == id, "Klang"] = data["tone"]
    csv.loc[csv["userId"] == id, "Lautstaerke"] = data["volume"]
    csv.loc[csv["userId"] == id, "Sprache"] = data["language"]
    csv.loc[csv["userId"] == id, "Gespraechsorientierung"] = data["topics"]
    csv.loc[csv["userId"] == id, "Anrede"] = data["form_of_address"]       
    csv.loc[csv["userId"] == id, "Satzpause"] = data["pause"]
    csv.loc[csv["userId"] == id, "Sprechgeschwindigkeit"] = data["speed"]
    csv.loc[csv["userId"] == id, "Satzlaenge"] = data["length"]
    csv.loc[csv["userId"] == id, "Ausdruck"] = data["expression"]
    csv.loc[csv["userId"] == id, "alternative Keywords"] = data["alternate_keywords"]

    csv.to_csv(configfile_created, index=False, sep=';')

def create_default_config(id):
    with open(configfile_created, 'a') as csv:
        csv.write("\n" + str(id) + ";" + "maennlich" + ";" + "normal" + ";" + "natuerlich" + ";" + "3" + ";" + "Deutsch" + ";" + "Aufgaben orientiert" + ";" + "Du" + ";" + "kurz" + ";" + "durchschnittlich" + ";" + "normal" + ";" + "nein" + ";" )


def get_csvuser(uid): #Trainingdaten auslesen
    i = 0
    flag = False
    for x in Fitting.profiles["userId"]:
        i = i + 1
        if x == uid:
            flag = True
            break
    if flag:
        data = Fitting.profiles.iloc[i - 1]
        data = list([data[0], data[1], data[2], data[3], data[4], data[5], data[6]])
    else:
        data = None
    return data

def get_csvuser_created(uid): #Profile auslesen
    i = 0
    flag = False
    profiles_created = pd.read_csv(profiles, sep=';')
    for x in profiles_created["userId"]:
        i = i + 1
        if x == uid:
            flag = True
            break
    if flag:
        data = profiles_created.iloc[i - 1]
        data = list([data[0], data[1], data[2], data[3], data[4], data[5], data[6]])
    else:
        data = None
    return data    

def get_csvconfig(uid): #Trainingsdaten auslesen
    i = 0
    flag = False
    for x in Fitting.configs["userId"]:
        i = i + 1
        if x == uid:
            flag = True
            break
    if flag:
        data = Fitting.configs.iloc[i - 1]
        data = list([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]])
    else:
        data = None
    return data

def get_csvconfig_created(uid): #Konfigurationen auslesen
    i = 0
    flag = False
    configs_created = pd.read_csv(configfile_created, sep=';')
    for x in configs_created["userId"]:
        i = i + 1
        if x == uid:
            flag = True
            break
    if flag:
        data = configs_created.iloc[i - 1]
        data = list([data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12]])
    else:
        data = None
    return data    
