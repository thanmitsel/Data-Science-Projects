import pandas as pd
import numpy as np
from scipy import stats
#import math

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

## TODO correlation of features https://data-flair.training/blogs/python-statistics/

def collect_data():
    # converts data in readable format
    df =  pd.read_csv('dataset.txt', sep = ',', header = None)
    df.columns = ["sepal length", "sepal width", "petal length", "petal width", "labels"]
    labels = df["labels"]
    X = df.drop(["labels"], axis = 1)
    Y= pd.DataFrame(data=labels)
    for count, name in enumerate(labels.unique()):
        bin = labels == name
        Y.loc[bin] = count
    return X, Y, df


def describe_data(X):
    # extracts basic statistic
    stat_names = ['max', 'min', 'mean', 'median', 'std']
    summary = pd.DataFrame(data = [X.max(), X.min(), X.mean(), X.median(), X.std()])
    summary['statistics'] = stat_names
    summary = summary.set_index('statistics')
    return summary


def plot_features(df):
    # Plots the flowers by pairs of features
    i=1 # plot counter
    features = ['sepal', 'petal']
    flowers = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    for i, fname in enumerate(features):
        plt.subplot(2, 1, i+1)
        for ftype in flowers:
            plt.scatter(df[fname + ' length'][df['labels']==ftype],
                        df[fname + ' width'][df['labels']==ftype], label= ftype)
        plt.title(fname + ' features')
        plt.ylabel('width')
        plt.xlabel('length')
        plt.legend()
    plt.show()


def plot_histograms(df):
    feature_list = ["sepal length", "sepal width", "petal length", "petal width"]
    for i, feature in enumerate(feature_list):
        plt.subplot(2, 2, i+1)
        for fclass in df['labels'].unique():
            plt.hist(df[feature].loc[df['labels'] == fclass],
                     normed = True, bins = 6, alpha = 0.7, rwidth = 0.85, label = fclass)
        plt.title(feature)
        plt.ylabel('occurance')
        plt.xlabel('feature values')
        plt.legend()
    plt.show()

def confidence_intervals(df, feat_name=None, label_names=None, conf=None):
    '''Petal length for means'''
    g_stats = df.groupby('labels')[feat_name].agg({'mean': 'mean', 'std' : 'std','count' : 'count'})
    deg_free = g_stats['count'].loc[label_names[0]] +g_stats['count'].loc[label_names[0]] -2
    pooled_var = (g_stats['std'].loc[label_names[0]]**2*g_stats['count'].loc[label_names[0]] + \
                      g_stats['std'].loc[label_names[1]]**2*g_stats['count'].loc[label_names[1]])/deg_free
    mean_dif = g_stats['mean'].loc[label_names[0]]-g_stats['mean'].loc[label_names[1]]
    pooled_std = np.sqrt(pooled_var/g_stats['count'].loc[label_names[0]] + \
                         pooled_var/g_stats['count'].loc[label_names[1]])
    t_score = mean_dif/pooled_std
    crit_val = stats.t.ppf(1-conf/2, deg_free)
    conf_int = (mean_dif-crit_val*pooled_std, mean_dif+stats.t.ppf(1-0.025, 98)*pooled_std)
    statistic, pval = stats.ttest_rel(df[feat_name].loc[df['labels'] == label_names[0]],
                    df[feat_name].loc[df['labels'] == label_names[1]])
    return t_score, conf_int, pval*2

[data, labels, dataframe] = collect_data()
stat = describe_data(data)
plot_features(dataframe)
plot_histograms(dataframe)
print(stat)
feature_name = 'petal length'
label_names = ['Iris-versicolor', 'Iris-virginica']
conf = 0.05
print(confidence_intervals(dataframe, feature_name, label_names, conf))