import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder




# The gender column has been encoded using the LabelEncoder class from scikit-learn, which converts categorical variables into numerical ones. In this case, it has encoded the "gender" column into 0s and 1s, where 0 represents "female" and 1 represents "male".


my_data = pd.read_csv('Pneumonia_Detection.csv')
le = LabelEncoder()
my_data['gender'] = le.fit_transform(my_data['gender'])

X = my_data.drop(columns=['Pneumonia_Infected'])
X.columns = ['gender', 'age_year', 'fever', 'cough', 'Breathing_Difficulty', 'weight_loss', 'Headache', 'Fainting', 'Bronchitis_infection', 'Chest_Pain', 'Tuberculosis_History']
y = my_data['Pneumonia_Infected']

X_train,x_test,y_train,y_test = train_test_split(X,y, test_size=0.2)
Decision_tree_model = DecisionTreeClassifier()
Logistic_regression_model= LogisticRegression(solver='lbfgs', max_iter=10000)
SVM_model=svm.SVC(kernel='linear')
RF_model = RandomForestClassifier(n_estimators=100)

Decision_tree_model.fit(X_train,y_train)
Logistic_regression_model.fit(X_train,y_train)
SVM_model.fit(X_train,y_train)
RF_model.fit(X_train,y_train)

DT_Prediction = Decision_tree_model.predict(x_test)
LR_Prediction = Logistic_regression_model.predict(x_test)
SVM_Prediction = SVM_model.predict(x_test)
RF_Prediction = RF_model.predict(x_test)
 
DT_score =accuracy_score(y_test, DT_Prediction)
LR_score =accuracy_score(y_test, LR_Prediction)
SVM_score =accuracy_score(y_test, SVM_Prediction)
RF_score =accuracy_score(y_test ,   RF_Prediction)


print("DEcision Tree accurancy score :", DT_score*100,"%")
print("Logistic Regressoin accurancy score :", LR_score*100,"%")
print("Support Vertor Machine accurancy score :", SVM_score*100,"%")
print("Random Forest accurancy score :", RF_score*100,"%")