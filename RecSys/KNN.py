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

def apply_settings(neighbors, test):
    global print_probability
    global test_size
    global knn
    global model
    test_size = test
    knn = KNeighborsClassifier(n_neighbors=neighbors)  # number of neighbors
    model = MultiOutputClassifier(knn, n_jobs=-1)


def trainModel(X, y):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=test_size)  # choose testsize
    x_train = list(x_train)
    y_train = list(y_train)

    model.fit(x_train, y_train)


def predictConfig(data):
    data = Fitting.translate_userMapping(data)
    predict = model.predict([data[2:]])
    final_predict = list(predict[0])

    return final_predict
