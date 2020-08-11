import numpy as np
import requests
import matplotlib.pyplot as plt


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
    return dataset


data = collect_dataset())
x=np.c_[np.ones(len_data), data[:, :-1]].astype(float)
y=data[:, -1].astype(float)

# OLS formula: beta_hat = ((X'X)^-1)X'Y

x_prime_x=np.dot(x.transpose(), x)
xx_to_minusone=np.linalg.inv(x_prime_x)
x_prime_y=np.dot(x.transpose(), y)
beta_hat=np.dot(xx_to_minusone, x_prime_y)
