import numpy as np
import pandas as pd
from scipy.stats import kstest



def gen_normal_distribution_data(start,end,num):
    return np.random.normal(start,end,num)


def is_normal_distribution(data):
    res=kstest(data,'norm')
    return res.pvalue<0.03


def three_sigma_valid(data,suspect):
    series=pd.Series(data)
    mean=series.mean()
    std=series.std()
    return abs(suspect-mean)<3*std


def grubbs_valid(data,suspect):
    pass


if __name__=="__main__":
    data=gen_normal_distribution_data(0,100,100)
    print data
    print is_normal_distribution(data)
    print three_sigma_valid(data,1000)
    print three_sigma_valid(data,50)
