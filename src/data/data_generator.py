import os

import numpy as np
import pandas as pd

ROOT_DIR = os.path.abspath(os.curdir)


def gen():
    for i in range(20):
        rand_x = np.random.randint(1, 10)
        rand_y = np.random.randint(1, 10)
        df = pd.DataFrame(np.random.randint(-100, 100, size=(rand_x, rand_y)))
        df.to_csv(ROOT_DIR +
                  "\\..\\..\\data\\test\\" + "{}.csv".format(i), index=False)


if __name__ == '__main__':
    gen()
