import src.data.preprocessing as pp
import src.features.feature_engineering as fe
import src.models.logisticRegression as lR
def pip():
    train, test = pp.loading('train.csv', 'test.csv')
    train, test, passenger_id = pp.preparing(train, test)

    train, test = fe.new_features(train, test)

    pp.print_info(train, test)

    testframe=lR.build_logReg(train, test)
    lR.submit(testframe, passenger_id)

if __name__ == '__main__':
    pip()