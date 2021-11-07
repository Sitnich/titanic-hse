def new_features(train_df, test_df):
    train_df['family_size'] = train_df.SibSp + train_df.Parch + 1
    test_df['family_size'] = test_df.SibSp + test_df.Parch + 1

    def family_group(size):
        a = ''
        if (size <= 1):
            a = 'loner'
        elif (size <= 4):
            a = 'small'
        else:
            a = 'large'
        return a

    train_df['family_group'] = train_df['family_size'].map(family_group)
    test_df['family_group'] = test_df['family_size'].map(family_group)

    train_df['is_alone'] = [1 if i < 2 else 0 for i in train_df.family_size]
    test_df['is_alone'] = [1 if i < 2 else 0 for i in test_df.family_size]

    train_df['child'] = [1 if i < 16 else 0 for i in train_df.Age]
    test_df['child'] = [1 if i < 16 else 0 for i in test_df.Age]
    train_df.child.value_counts()

    train_df['calculated_fare'] = train_df.Fare / train_df.family_size
    test_df['calculated_fare'] = test_df.Fare / test_df.family_size

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

    train_df['fare_group'] = train_df['calculated_fare'].map(fare_group)
    test_df['fare_group'] = test_df['calculated_fare'].map(fare_group)

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

    train_df['age_group'] = train_df['Age'].map(age_group_fun)
    test_df['age_group'] = test_df['Age'].map(age_group_fun)