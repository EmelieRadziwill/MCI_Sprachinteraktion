import sklearn
import Fit_Data as Fitting
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier

print_probability = False
config_translate = True
user_mappings = []
config_mappings = []
knn = KNeighborsClassifier
model = MultiOutputClassifier
test_size = 0

def apply_settings(print_prob, config_trans, neighbors, test):
    global print_probability
    global config_translate
    global test_size
    global knn
    global model
    print_probability = print_prob
    config_translate = config_trans
    test_size = test
    knn = KNeighborsClassifier(n_neighbors=neighbors)  # number of neighbors
    model = MultiOutputClassifier(knn, n_jobs=-1)


def trainModel(X, y):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=test_size)  # choose testsize
    x_train = list(x_train)
    y_train = list(y_train)

    '''
    for obj in range(len(x_train)):
        x_train[obj] = x_train[obj][2:]
        y_train[obj] = y_train[obj][2:]
    '''
    model.fit(x_train, y_train)

    return x_test, y_test


def testModel(x_test, y_test, min_score):
    print("\n\033[92m###START TESTING MODEL###\033[0m")
    x_temp_test = list(x_test)
    for obj in range(len(x_temp_test)):
        x_temp_test[obj] = x_temp_test[obj][2:]

    predicted = model.predict(x_temp_test)
    proba = model.predict_proba(x_temp_test)

    predicted_final = []
    for i in range(len(predicted)):
        temp_obj = list(predicted[i])
        temp_obj.insert(0, x_test[i][0])
        temp_obj.insert(1, x_test[i][1])
        predicted_final.append(temp_obj)

    accuracy_total = 0
    for x in range(len(x_test)):
        hit = 0
        if print_probability and x < len(proba):
            print(proba[x])
        for y in range(len(predicted_final[x])):
            if predicted_final[x][y] == y_test[x][y]:
                hit = hit + 1
        accuracy = hit / len(predicted_final[x])
        accuracy_total = accuracy_total + accuracy
        print("\nAcc:", accuracy)
        print("Predicted:", predicted_final[x], " --> Data: ", x_test[x], " --> Actual: ", y_test[x])
    accuracy_total = accuracy_total / len(predicted_final)
    if accuracy_total >= min_score:
        print("\n\033[92m#####################################\033[0m")
        print("\033[93m Total Accuracy:", accuracy_total, "\033[0m")
        print("\033[92m#####################################\033[0m\n")
    return accuracy_total


def predictConfig(data):
    data = Fitting.translate_userMapping(data)
    predict = model.predict([data[2:]])
    final_predict = list(predict[0])
    #final_predict.insert(0, data[3])
    #final_predict.insert(1, data[4])
    #print("\033[94m###", data[1], "U_ID:", data[0], "###\033[0m")
    #print("Vorgeschlagene Konfiguration:\n", final_predict)
    #if config_translate:
        #print(str(Fitting.retranslate_configMapping(list(final_predict))) + "\n")

    return final_predict

    #return predict[0], final_predict


def config_rating(user, config, bool):
    predicted_config, predict= predictConfig(user)
    final_predicted_config = list(predicted_config)
    final_predicted_config.insert(0, user[3])
    final_predicted_config.insert(1, user[4])
    hit = 0
    config = Fitting.translate_configMapping(config)
    for x in range(len(final_predicted_config)):
        if final_predicted_config[x] == config[x]:
            hit = hit + 1
    #accuracy = hit / len(final_predicted_config)
    if bool:
        print("Momentane Konfiguration:\n", config)
        if config_translate:
            print(str(Fitting.retranslate_configMapping(config)))
    #print("\nCurrent config has an recommondation of\033[93m", round(accuracy * 100, 2), "%\033[0m\n\n")

    return predict

