from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
print(dataset.shape)
print(dataset)
# print(dataset.describe())
# print(dataset.groupby('class').size())
# histograms
# dataset.hist()
# pyplot.show()

# Split-out validation dataset
array = dataset.values

X = array[:, 0:4]
# print(X)
Y = array[:, 4]
# print(Y)
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1)

# print("X", len(X))
# print(X[0], X[1], X[2], X[3])
# print(Y[0], Y[1], Y[2], Y[3])
# print("Y", len(Y))
# print("X_length", len(X_train))
# print("Y_length", len(Y_train))

# print("X_validation", X_validation)
# print("X_train", X_train)
# print("Y_validation", Y_validation)
# print("Y_train", Y_train)

# Make predictions on validation dataset
model = LinearDiscriminantAnalysis()
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
predictions2 = model.predict(Y_validation)
# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

