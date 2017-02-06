import numpy as np
import pandas as pd
from scipy.stats import kstest



def gen_normal_distribution_data(start,end,num):
    return np.random.normal(start,end,num)


def is_normal_distribution(data):
    res=kstest(data,'norm')
    return res.pvalue<0.03


def k_sigma_valid(data,suspect,k=3):
    series=pd.Series(data)
    mean=series.mean()
    std=series.std()
    return abs(suspect-mean)<3*std


def grubbs_valid(data,suspect):
    pass


def histogram_valid(data,suspect):
    hist=np.histogram(data,bins=15)
    bins=hist[1]
    for i,size in enumerate(hist[0]):
        if size<=20 and suspect>=bins[i] and suspect<bins[i+1]:
                return True
    return False



def median_absolute_deviation(data,suspect):
    series=pd.Series(data)
    median=series.median()
    demedians=np.abs(series-median)
    demedian=demedians.median()
    if demedian==0:
        return False
    test=demedians.iget(-1)/demedian
    if test>6:
        return True
    return False


if __name__=="__main__":
    data=gen_normal_distribution_data(0,100,100)
    print data
    print is_normal_distribution(data)
    print k_sigma_valid(data,1000)
    print k_sigma_valid(data,50)
    print histogram_valid(data,50)
    print histogram_valid(data,1000)
    print median_absolute_deviation(data,1000)
    print median_absolute_deviation(data,50)
