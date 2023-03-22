import warnings
import Fit_Data as Fitting
import KNN
import Skill
from warnings import simplefilter


simplefilter(action='ignore', category=FutureWarning)

# SETTINGS
number_of_neighbors = 10
test_size = 0.1

def main():

    KNN.apply_settings(number_of_neighbors, test_size)
    x, y, user_mappings, config_mappings = Fitting.fit_data()
    KNN.trainModel(x, y)

    Skill.Server()

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
