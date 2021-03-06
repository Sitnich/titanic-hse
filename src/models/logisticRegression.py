import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score,recall_score,confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

logreg = LogisticRegression(solver='liblinear', penalty='l1')

ROOT_DIR = os.path.abspath(os.curdir)

def build_logReg(train_df, test_df):
    X = train_df.drop(columns='Survived')
    y = train_df['Survived']

    std_scaler = StandardScaler()
    X = std_scaler.fit_transform(X)
    testframe = std_scaler.fit_transform(test_df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1000)

    def logReg(X_train,y_train, X_test, y_test):
        logreg.fit(X_train,y_train)
        predict=logreg.predict(X_test)
        print(accuracy_score(y_test,predict))
        print(confusion_matrix(y_test,predict))
        print(precision_score(y_test,predict))
        print(recall_score(y_test,predict))

        def grid_search():
            C_vals = [0.0001, 0.001, 0.01, 0.1, 0.13, 0.2, .15, .25, .275, .33, 0.5, .66, 0.75, 1.0, 2.5, 4.0, 4.5, 5.0, 5.1,
                      5.5, 6.0, 10.0, 100.0, 1000.0]
            penalties = ['l1', 'l2']

            param = {'penalty': penalties, 'C': C_vals, }
            grid = GridSearchCV(logreg, param, verbose=False, cv=StratifiedKFold(n_splits=5, random_state=10, shuffle=True),
                                n_jobs=1, scoring='accuracy')
            grid.fit(X_train, y_train)
            print(grid.best_params_)
            print(grid.best_score_)
            print(grid.best_estimator_)

            logreg_grid = LogisticRegression(penalty=grid.best_params_['penalty'], C=grid.best_params_['C'])
            logreg_grid.fit(X_train, y_train)
            y_pred = logreg_grid.predict(X_test)
            logreg_accy = round(accuracy_score(y_test, y_pred), 3)
            print(logreg_accy)
            print(confusion_matrix(y_test, y_pred))
            print(precision_score(y_test, y_pred))
            print(recall_score(y_test, y_pred))

    logReg(X_train, y_train, X_test, y_test)
    return(testframe)

def submit(testframe, passenger_id):
    y_predict = logreg.predict(testframe)
    print(y_predict)

    temp = pd.DataFrame(pd.DataFrame({
        "PassengerId": passenger_id,
        "Survived": y_predict
    }))
    temp.to_csv(ROOT_DIR + r"\..\data\result\res.csv", index=False)