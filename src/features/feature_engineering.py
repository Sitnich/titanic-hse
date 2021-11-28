import pandas as pd

def family_group(size):
    a = ''
    if (size <= 1):
        a = 'loner'
    elif (size <= 4):
        a = 'small'
    else:
        a = 'large'
    return a

def age_group_fun(age):
    a = ''
    if age <= 1:
        a = 'infant'
    elif age <= 4:
        a = 'toddler'
    elif age <= 13:
        a = 'child'
    elif age <= 18:
        a = 'teenager'
    elif age <= 35:
        a = 'Young_Adult'
    elif age <= 45:
        a = 'adult'
    elif age <= 55:
        a = 'middle_aged'
    elif age <= 65:
        a = 'senior_citizen'
    else:
        a = 'old'
    return a

def fare_group(fare):
    a = ''
    if fare <= 4:
        a = 'Very_low'
    elif fare <= 10:
        a = 'low'
    elif fare <= 20:
        a = 'mid'
    elif fare <= 45:
        a = 'high'
    else:
        a = "very_high"
    return a

def new_features(train_df, test_df):


    train_df['family_size'] = train_df.SibSp + train_df.Parch + 1
    test_df['family_size'] = test_df.SibSp + test_df.Parch + 1


    train_df['family_group'] = train_df['family_size'].map(family_group)
    test_df['family_group'] = test_df['family_size'].map(family_group)

    train_df['is_alone'] = [1 if i < 2 else 0 for i in train_df.family_size]
    test_df['is_alone'] = [1 if i < 2 else 0 for i in test_df.family_size]

    train_df['child'] = [1 if i < 16 else 0 for i in train_df.Age]
    test_df['child'] = [1 if i < 16 else 0 for i in test_df.Age]
    train_df.child.value_counts()

    train_df['calculated_fare'] = train_df.Fare / train_df.family_size
    test_df['calculated_fare'] = test_df.Fare / test_df.family_size


    train_df['fare_group'] = train_df['calculated_fare'].map(fare_group)
    test_df['fare_group'] = test_df['calculated_fare'].map(fare_group)

    train_df['age_group'] = train_df['Age'].map(age_group_fun)
    test_df['age_group'] = test_df['Age'].map(age_group_fun)

    train_df = pd.get_dummies(train_df, columns=['Title', "Pclass", 'Embarked', 'family_group', 'fare_group'],
                              drop_first=True)
    test_df = pd.get_dummies(test_df, columns=['Title', "Pclass", 'Embarked', 'family_group', 'fare_group'],
                             drop_first=True)
    train_df.drop(['Cabin', 'family_size', 'Ticket', 'Name', 'Fare'], axis=1, inplace=True)
    test_df.drop(['Ticket', 'Name', 'family_size', "Fare", 'Cabin'], axis=1, inplace=True)

    train_df = pd.get_dummies(train_df, columns=['age_group'], drop_first=True)
    test_df = pd.get_dummies(test_df, columns=['age_group'], drop_first=True)

    train_df.drop(['Age', 'calculated_fare'], axis=1, inplace=True)
    test_df.drop(['Age', 'calculated_fare'], axis=1, inplace=True)

    train_df.drop(['Title_Rev', 'age_group_old', 'age_group_teenager', 'age_group_senior_citizen', 'Embarked_Q'],
                  axis=1, inplace=True)
    test_df.drop(['Title_Rev', 'age_group_old', 'age_group_teenager', 'age_group_senior_citizen', 'Embarked_Q'], axis=1,
                 inplace=True)

    return train_df, test_df