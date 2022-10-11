#testing purposes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    mean_file = "mean.csv"
    var_file = "var.csv"

    mean_df = pd.read_csv(mean_file)
    var_df = pd.read_csv(var_file)

    #plot
    plt.plot(mean_df)
    #plt.plot(var_df)
    plt.show()


if __name__ == "__main__":
    main()