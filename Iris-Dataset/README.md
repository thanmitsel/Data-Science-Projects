# Iris Data Set Analysis
## Overview
This code is oriented to apply some common analysis techniques in one of the most popular dataset (Iris Dataset). Before any computation it is strongly advised to plot the data, in order to observe any underlying connection. After the two dimensional represenation of the datapoints, I am going apply descriptive statistics, inferential stastics and hypothesis testing on one of the most popular datasets for mahcine learning (Iris Dataset).

## Descriptive Statistics
In this example the following was utilized to kickstart the analysis:
* Scatter plots

![alt text](https://github.com/thanmitsel/Data-Science-Projects/blob/master/Iris-Dataset/images/scatter-plot.png)

* Histograms
* Means
* Standard Deviations

## Assumptions
I am going to use t-student's distribution for independent samples, with unknown variance, but assumed to be equal.
* The samples that are collected are independent of each other within species
* The samples that are collected are independent of each other
* The sample is large enough to compensate for the skew in population distribution.

Tip: Once we have surpassed 50 degrees of freedom, the Student't T distribution converts to Normal Distribution.

## Inferential Statistics

* Degrees of Freedom: 50 + 50 - 2 = 98
* Confidence Interval (alpha): 0.05

Our estimates will be the mean and the standard deviation. The purpose is to obtain the difference in mean of petal lengths of virginica and versicolor.
Our dataset has $50-50-2 = 98 degrees of freedom
Rule of thumb: Reject the null hypothesis when the T-score is bigger than two.

## Hypothesis Testing
We have a two sided test on the average 'petal length'.
* H0 (null): The mean petal-length of Iris-versicolor and Iris-virginica are equal
* H1 (alternate): The mean petal-length of Iris-versicolor and Iris-virginica are not equal

Ways to interpret the results:
* If T-Score > critical-value reject null, if T-Score < critical-value accept null.
* If p-value > alpha accept null, if p-value < alpha reject null.
