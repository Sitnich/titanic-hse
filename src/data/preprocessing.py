import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from definition import ROOT_DIR


from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
label=LabelEncoder()
def loading():
    def print_info(train_df, test_df):
        print('Number of Training Examples = {}'.format(train_df.shape[0]))
        print('Number of Test Examples = {}\n'.format(test_df.shape[0]))
        print('Training X Shape = {}'.format(train_df.shape))
        print('Training y Shape = {}\n'.format(train_df['Survived'].shape[0]))
        print('Test X Shape = {}'.format(test_df.shape))
        print('Test y Shape = {}\n'.format(test_df.shape[0]))
        print(train_df.columns)
        print(test_df.columns)

    train_df = pd.read_csv(os.path.join(ROOT_DIR, "data/raw/train.csv"))
    test_df = pd.read_csv(os.path.join(ROOT_DIR, "data/raw/test.csv"))

    train_df.name = 'Training Set'
    test_df.name = 'Test Set'
    return (train_df, test_df)


def preparing(train_df, test_df):

    ## всего одно пропущенное значение - заполним средним
    test_df.Fare.fillna(test_df.Fare.mean(), inplace=True)
    data_df = train_df.append(test_df)

    ## фича PassengerID бесполезна для дальнейшего анализа, выбросим
    train_df.drop(['PassengerId'], axis=1, inplace=True)
    test_df.drop(['PassengerId'], axis=1, inplace=True)

    train_df=train_df[train_df['Fare']<400]

    train_df['Sex'] = train_df.Sex.apply(lambda x: 0 if x == "female" else 1)
    test_df['Sex'] = test_df.Sex.apply(lambda x: 0 if x == "female" else 1)

    test_df['Fare'].fillna(test_df['Fare'].mean(), inplace=True)

    ## заполним пропуски в возрасте средним по классифицированным Titles
    for name_string in data_df['Name']:
        data_df['Title'] = data_df['Name'].str.extract('([A-Za-z]+)\.', expand=True)

    mapping = {'Mlle': 'Miss', 'Major': 'Mr', 'Col': 'Mr',
               'Sir': 'Mr', 'Don': 'Mr', 'Mme': 'Miss',
               'Jonkheer': 'Mr', 'Lady': 'Mrs', 'Capt': 'Mr',
               'Countess': 'Mrs', 'Ms': 'Miss', 'Dona': 'Mrs'}
    data_df.replace({'Title': mapping}, inplace=True)

    data_df['Title'].value_counts()
    train_df['Title'] = data_df['Title'][:891]
    test_df['Title'] = data_df['Title'][891:]

    titles = ['Mr', 'Miss', 'Mrs', 'Master', 'Rev', 'Dr']
    for title in titles:
        age_to_impute = data_df.groupby('Title')['Age'].mean()[titles.index(title)]
        data_df.loc[(data_df['Age'].isnull()) & (data_df['Title'] == title), 'Age'] = age_to_impute
    data_df.isnull().sum()

    train_df['Age'] = data_df['Age'][:891]
    test_df['Age'] = data_df['Age'][891:]
    test_df.isnull().sum()

    train_df.to_csv(os.path.join(ROOT_DIR, "data/processed/train.csv"))
    test_df.to_csv(os.path.join(ROOT_DIR, "data/processed/test.csv"))