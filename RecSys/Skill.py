import sys
import pandas as pd
import Fit_Data as Fitting
import KNN
from flask import Flask, jsonify, request, redirect, render_template, url_for
import json

import KNN

ip = "192.168.0.108"
port = 8080
profiles = "./Resources/profile_created.csv"
configfile_created = "./Resources/config_created.csv"


def getUser(ids):
    example_config = []
    example_user = []
    for i in ids:
        example_config.append(get_csvconfig(i))
        example_user.append(get_csvuser(i))
    return example_user, example_config

def getNewUser(id):
    config = get_csvconfig_created(id)
    user = get_csvuser_created(id)
    return user, config    


def Server():
    app = Flask(__name__)
    app.static_folder = 'static'

    '''
    @app.route('/MCI/<int:uid>/')
    def return_config(uid):
        data = get_config(uid)
        userName = data[1]
        data = data[0]

        if data is not None:
            return jsonify({'interests': data[1],
                            'language_usage': data[2],
                            'foreign_words': data[3],
                            'slang_words': str(data[4]),
                            'formality': data[5],
                            'conciseness': str(data[6]),
                            'information_density': data[7],
                            'repeat': data[8],
                            'language': data[0],
                            'speed': data[9],
                            'emphasis': data[10],
                            'speech_pauses': str(data[11]),
                            'volume': data[12],
                            'voice_gender': data[13],
                            'voice_age': data[14],
                            'userName': userName})
        else:
            return "No User"
    '''    

    @app.route('/MCI/<int:uid>/', methods=['GET', 'POST'])
    def change_config(uid):

        userdata, configdata = getNewUser(uid)
        recdata = KNN.predictConfig(userdata)
        recdata = Fitting.retranslate_configMapping(list(recdata))
        
        if request.method == 'POST':
            return redirect(url_for('index'))
        return render_template('config.html', c=configdata , r=recdata)
    
    
    @app.route('/save_config/', methods=['POST'])
    def save_config():
        data = request.get_json()
        store_config(data)
        return jsonify(data)


    @app.route('/MCI/newUser', methods=['GET', 'POST'])
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


def storeUser(data):
    userId = 601 + pd.read_csv(Fitting.userfile_created, sep=";")["userId"].size
    with open(profiles, 'a') as csv:
        csv.write("\n" + str(userId) + ";" + data['userName'] + ";" + data['age'] + ";" + data['language_p'] + ";" + data['hearing_aid'] + ";" + data['prior_knowledge'])
    return userId


def create_default_config(id):
    with open(configfile_created, 'a') as csv:
        csv.write("\n" + str(id) + ";" + "maennlich" + ";" + "normal" + ";" + "natuerlich" + ";" + "3" + ";" + "Deutsch" + ";" + "Aufgaben orientiert" + ";" + "du" + ";" + "kurz" + ";" + "durchschnittlich" + ";" + "normal" + ";" + "nein" + ";" )

'''
userId;Name;Alter;Geschlecht;Sprache;Hoergeraet;Vorkenntnisse;alternative Keywords
def storeUserNew(data):
    uID = 201 + pd.read_csv(Fitting.userfile_created)["userId"].size
    with open('./Resources/users_created.csv', 'a') as csv:
        csv.write("\n" + str(uID) + "," + data['userName'] + "," + data['age'] + "," + data['disability'] + "," + data['language'] + "," + data['interests'] + "," + data['education'] + "," + data['formality'] + "," + data['preferred_speaker'])
    return uID    
'''

def get_csvuser(uid):
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

def get_csvuser_created(uid):
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


def get_csvconfig(uid):
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

def get_csvconfig_created(uid):
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


def get_config(uid):
    if(uid <= 200):
        i = 0
        flag = False
        for x in Fitting.profiles["userId"]:
            i = i + 1
            if x == uid:
                flag = True
                break
        if flag:
            data = Fitting.profiles.iloc[i - 1]
            userName = data["userName"]
            data = list([data[0], data[1], data[2], data[4], data[5], data[3], data[6], data[7], data[8]])
            data = list(KNN.predictConfig(data)[1])
            data = Fitting.retranslate_configMapping(data)
        else:
            data = None
            userName = None
    else:
        i = 200
        flag = False
        for x in pd.read_csv(Fitting.userfile_created)["userId"]:
            i = i + 1
            if x == uid:
                flag = True
                break
        if flag:
            data = pd.read_csv(Fitting.userfile_created).iloc[i - 201]
            userName = data["userName"]
            data = list([data[0], data[1], data[2], data[4], data[5], data[3], data[6], data[7], data[8]])
            data = list(KNN.predictConfig(data)[1])
            data = Fitting.retranslate_configMapping(data)
        else:
            data = None
            userName = None
    return data, userName


def store_config(data):
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
