import pandas as pd
from sklearn import preprocessing

userfile = "./Resources/profile.csv"
userfile_created = "./Resources/profile_created.csv"
configfile = "./Resources/config.csv"
configfile_created = "./Resources/config_created.csv"

profiles = pd.read_csv(userfile, sep=";")
profiles_created = pd.read_csv(userfile_created, sep=";")
configs = pd.read_csv(configfile, sep=";")
configs_created = pd.read_csv(configfile_created, sep=";")

# user profiles
user_id = list(profiles["userId"])
name = list(profiles["Name"])
age = list(profiles["Alter"])
alternate_keyword = list(profiles["alternative Keywords"])
user_mappings = []
config_mappings = []

# encode labels in appropriate integer values
le = preprocessing.LabelEncoder()


def fit_data():
    gender_p = le.fit_transform(list(profiles["Geschlecht"]))
    le_gender_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    language_p = le.fit_transform(list(profiles["Sprache"]))
    le_language_p_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    hearing_aid = le.fit_transform(list(profiles["Hoergeraet"]))
    le_hearing_aid_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    prior_knowledge = le.fit_transform(list(profiles["Vorkenntnisse"]))
    le_prior_knowledge_mapping = dict(zip(le.classes_, le.transform(le.classes_)))

    global user_mappings
    user_mappings = [user_id, name, age, le_gender_mapping, le_language_p_mapping, le_hearing_aid_mapping, le_prior_knowledge_mapping, alternate_keyword]

    X = list(zip(gender_p, language_p, hearing_aid, prior_knowledge))

    # user configs
    UserID = list(configs["userId"])
    alternate_keyword_conf = list(configs["alternative Keywords"])
    gender = le.fit_transform(list(configs["Geschlecht"]))
    conf_gender_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    pitch = le.fit_transform(list(configs["Tonlage"]))
    conf_pitch_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    tone = le.fit_transform(list(configs["Klang"]))
    conf_tone_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    volume = le.fit_transform(list(configs["Lautstaerke"]))
    conf_volume_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    language = le.fit_transform(list(configs["Sprache"]))
    conf_language_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    topics = le.fit_transform(list(configs["Gespraechsorientierung"]))
    conf_topics_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    form_of_address = le.fit_transform(list(configs["Anrede"]))
    conf_form_of_address_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    pause = le.fit_transform(list(configs["Satzpause"]))
    conf_pause_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    speed = le.fit_transform(list(configs["Sprechgeschwindigkeit"]))
    conf_speed_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    length = le.fit_transform(list(configs["Satzlaenge"]))
    conf_length_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
    expression = le.fit_transform(list(configs["Ausdruck"]))
    conf_expression_mapping = dict(zip(le.classes_, le.transform(le.classes_)))

    global config_mappings
    config_mappings = [conf_gender_mapping, conf_pitch_mapping, conf_tone_mapping, conf_volume_mapping, conf_language_mapping, conf_topics_mapping,
                        conf_form_of_address_mapping, alternate_keyword_conf, conf_pause_mapping, conf_speed_mapping, conf_length_mapping, conf_expression_mapping]

    
    y = list(zip(gender, pitch, tone, volume, language, topics, form_of_address, pause, speed, length, expression))

    return X, y, user_mappings, config_mappings


def translate_userMapping(data):  # string to int
    for x in range(3, 6):
        data[x] = user_mappings[x].get(data[x])
    return data


def retranslate_configMapping(data):  # int to string
    result = []
    for x in range(len(data)):
        result.append(list(config_mappings[x].keys())[data[x]])
    return result


def translate_configMapping(data):  # string to int
    result = []
    for x in range(12):
        result.append(config_mappings[x].get(data[x]))
    return result
