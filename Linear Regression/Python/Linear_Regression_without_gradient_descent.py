import numpy as np
import requests
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def collect_dataset():
    """
    Collect dataset of Counterstrike Go (CSGO).
    The dataset of CSGO contains Average Damage per Round
    (ADR) vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    response = requests.get(
        "https://raw.githubusercontent.com/yashLadha/"
        + "The_Math_of_Intelligence/master/Week1/ADRvs"
        + "Rating.csv"
    )
    lines = response.text.splitlines()
    data = []

    for item in lines:
        item = item.split(",")
        data.append(item)
    data.pop(0)  # to remove the label from the list
    dataset = np.matrix(data)
    return data


data = collect_dataset()
len_data = data.shape[0]
x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
y = data[:, -1].astype(float)

# OLS formula: beta_hat = ((X'X)^-1)X'Y

x_prime_x = np.dot(x.transpose(), x)
xx_to_minusone = np.linalg.inv(x_prime_x)
x_prime_y = np.dot(x.transpose(), y)
beta_hat = np.dot(xx_to_minusone, x_prime_y)

reg = LinearRegression().fit(x, y)
reg.coef_  # 1.6076036
reg.intercept_  # -15.54790166
