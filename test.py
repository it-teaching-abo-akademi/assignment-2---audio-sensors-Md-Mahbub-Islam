#testing purposes

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    mean_file = "tmean.csv"
    var_file = "tvar.csv"

    mean_df = pd.read_csv(mean_file)
    var_df = pd.read_csv(var_file)

    #mean of last 3 columns each row
    means_list = mean_df.iloc[:, -3:].mean(axis=1)

    #plot last 3 columns against 1st column
    mean_df.plot(x=mean_df.columns[0], y=mean_df.columns[-3:])
    plt.plot(mean_df.iloc[:, 0], means_list, color='red', linewidth=2)

    plt.show()

    var_df.plot(x=var_df.columns[0], y=var_df.columns[-3:])
    vars_list = var_df.iloc[:, -3:].mean(axis=1)
    plt.plot(var_df.iloc[:, 0], vars_list, color='red', linewidth=2)
    plt.show()


if __name__ == "__main__":
    main()