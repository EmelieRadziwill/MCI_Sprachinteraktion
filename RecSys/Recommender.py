import warnings
import Fit_Data as Fitting
import KNN
import Skill
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

# SETTINGS
do_test = False
print_probability = False
number_of_neighbors = 10
test_size = 0.1

do_recommendation = True
recommendation_ids = [3, 7]
config_translate = True

best_of_n = False  # only for test purpose
min_score = 0.88


def main():
    """"
    if not best_of_n:
        KNN.apply_settings(print_probability, config_translate, number_of_neighbors, test_size)
        x, y, user_mappings, config_mappings = Fitting.fit_data()
        x_test, y_test = KNN.trainModel(x, y)

        # debug purpose
        if do_test:
            KNN.testModel(x_test, y_test, 0)
        if do_recommendation:
            user, user_config = Skill.getUser(recommendation_ids)
            for x in range(len(user)):
                KNN.config_rating(user[x], user_config[x])

    else:
        acc = 0
        while acc < min_score:
            KNN.apply_settings(print_probability, config_translate, number_of_neighbors, test_size)
            x, y, user_mappings, config_mappings = Fitting.fit_data()
            x_test, y_test = KNN.trainModel(x, y)
            acc = KNN.testModel(x_test, y_test, min_score)

        if do_recommendation:
            user, user_config = Skill.getUser(recommendation_ids)
            for x in range(len(user)):
                KNN.config_rating(user[x], user_config[x])
    Skill.Server()
    """
    KNN.apply_settings(print_probability, config_translate, number_of_neighbors, test_size)
    x, y, user_mappings, config_mappings = Fitting.fit_data()
    x_test, y_test = KNN.trainModel(x, y)

    Skill.Server()
    

    '''
    t = True
    f = False
    choice = ""
    while (choice not in ["n", "j"]):
        choice = input("Haben Sie bereits ein Profil? (j/n)" + "\n")
    if choice == "n": 
        id = [Skill.UserStartup()]
        user, user_config = Skill.getNewUser(id)
        for x in range(len(user)):
            prediction = KNN.config_rating(user[x], user_config[x], f)
            choice = ""
            while (choice not in ["n", "j"]):
                choice = input("Wollen Sie die Konfiguration übernehmen? (j/n)" + "\n")
            if choice == "j":
                predict_translate = (Fitting.retranslate_configMapping(list(prediction)))
                Skill.save_configs(id, predict_translate)
                

    else:
        id = [int(input("Bitte geben Sie Ihre ID an" + "\n"))]
        user, config = Skill.getNewUser(id)
        if user == [None]:
            print("Es existiert kein Profil mit dieser ID")
        else:
            print("\n Ihr Profil:\n")
            print(user[0])
            print("\nIhre Einstellungen:\n")
            print(config[0])

            choice = ""
            while (choice not in ["n", "j"]):
                choice = input("\nMöchten sie eine andere Konfiguration vorgeschlagen bekommen? (j/n)" + "\n")
            if choice == "j":
                for x in range(len(user)):
                    prediction = KNN.config_rating(user[x], config[x], t)
                choice = ""
                while (choice not in ["n", "j"]):
                    choice = input("Möchten sie die Konfiguration übernehmen? (j/n)" + "\n")
                if choice == "j":
                    predict_translate = (Fitting.retranslate_configMapping(list(prediction)))
                    Skill.save_configs(id, predict_translate)
    '''

    """    
    for x in range(len(user)):
        KNN.config_rating(user[x], user_config[x])
    """
        



    

if __name__ == '__main__':
    print(
        "\n\n██████╗░███████╗░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗███╗░░██╗██████╗░███████╗██████╗░░░░░░░░"
        "██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗")
    print(
        "██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗░░░░░░██╔══"
        "══╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║")
    print(
        "██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝█████╗╚████"
        "█╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║")
    print(
        "██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗╚════╝░╚═══"
        "██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║")
    print(
        "██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║███████╗██║░╚███║██████╔╝███████╗██║░░██║░░░░░░█████"
        "█╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║")
    print(
        "╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚════"
        "═╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝")
    print("http://127.0.0.1:8080/MCI/newUser\n")
    with warnings.catch_warnings():
        # ignore all caught warnings
        warnings.filterwarnings("ignore")
        # execute code that will generate warnings
        main()
