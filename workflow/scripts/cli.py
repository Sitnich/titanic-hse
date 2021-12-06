import sys
import os
import numpy as np
import pandas as pd
project_dir=os.path.abspath(os.curdir) + '\..\..'
data_dir=project_dir+'\\data'
sys.path.append(project_dir)

import click
import src.data.preprocessing as pp
import src.features.feature_engineering as fe
import src.models.logisticRegression as lR

@click.group()
def cli():
    pass

@cli.command()
@click.argument("paths", type=click.Path(), nargs=3)
def prepare_data(paths):
    train, test = pp.loading(data_dir+'\\raw\\train.csv', data_dir+'\\raw\\test.csv')
    train, test, passenger_id = pp.preparing(train, test)
    train.to_csv(project_dir + '\\reports\\' + paths[0]+'_prepared.csv', index=False)
    test.to_csv(project_dir + '\\reports\\' + paths[1]+'_prepared.csv', index=False)
    np.savetxt(project_dir + '\\reports\\' + paths[2], passenger_id, delimiter=",")

@cli.command()
@click.argument("paths", type=click.Path(), nargs=2)
def create_features(paths):
    train, test = pp.loading(data_dir+'\\processed\\train.csv', data_dir+'\\processed\\test.csv')
    fe.new_features(train, test)
    train.to_csv(project_dir + '\\reports\\' + paths[0]+'_processed.csv', index=False)
    test.to_csv(project_dir + '\\reports\\' + paths[1]+'_processed.csv', index=False)

@cli.command()
@click.argument("input", type=click.Path())
@click.argument("output", type=click.Path())
def print_info(input, output):
    df = pd.read_csv(data_dir+input)
    pr = pp.print_info(df, file_output=True)
    np.savetxt(project_dir + '\\reports\\' + output, pr, delimiter = " ")

@cli.command()
@click.argument("path", type=click.Path(), nargs=1)
def logReg_result(path):
    train, test = pp.loading(data_dir+'\\processed\\train.csv', data_dir+'\\processed\\test.csv')
    testframe = lR.build_log_reg(train, test, iprint=False)
    passenger_id = np.genfromtxt(data_dir+'\\processed\\passenger_id.csv', delimiter=',')
    res=lR.submit(testframe, passenger_id, output=True)
    res.to_csv(project_dir + '\\reports\\' + path + '_result.csv', index=False)


if __name__ == "__main__":
    cli()