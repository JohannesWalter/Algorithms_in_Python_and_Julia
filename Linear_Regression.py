# 11.08.2020
# Linear Regression
# Taken from: https://github.com/TheAlgorithms/Python/blob/master/machine_learning/linear_regression.py


"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

import numpy as np
import requests
import matplotlib.pyplot as plt


data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_y = [1.1, 1.94, 2, 3.8, 5.2, 6.1, 7.8, 7.9, 9.5, 10.8]
plt.plot(data_x, data_y)
theta = np.zeros((1, no_features))

def sum_of_squared_error(data_x, data_y, len_data, theta):
    """
    Return sum of square error for error calculation
    :param data_x : contains our dataset
    :param data_y : contains the output (result vector)
    :param len_data : lenght of dataset
    :param theta    : contains the feature vector
    :return         : sum of square error computed from given features
    """

    prod = np.dot(theta, data_x.transpose())
    prod -= data_y.transpose()

    sum_elem = np.sum(np.square(prod))
    error = sum_elem / (2 * len_data)
    return error






def main():
    """ Driver function """
    data = collect_dataset()

    len_data = data.shape[0]
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    data_y = data[:, -1].astype(float)

    theta = run_linear_regression(data_x, data_y)
    len_result = theta.shape[1]
    print("Resultant Feature vector : ")
    for i in range(0, len_result):
        print("%.5f" % (theta[0, i]))


if __name__ == "__main__":
    main()