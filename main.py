import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

def read_excel_data(file_path, sheet_name, column_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    file = df[column_name]
    return file.dropna()


def plot_histogram_and_normal_density(file, bins, x_min, x_max):
    plt.hist(file, bins=bins, density=True, alpha=0.4, color='black', label='Выборочные данные')

    average = np.mean(file) #среднее значение
    std = np.std(file) #стандартное отклонение

    x = np.linspace(x_min, x_max, 100)
    p = norm.pdf(x, average, std) # нормальное распределение

    plt.plot(x, p, 'r', linewidth=2, label='Плотность нормального распределения')

    mode = file.mode().values[0]
    plt.axvline(mode, color='c', linestyle='dashed', linewidth=2, label='Оценка моды')
    print(mode)

    plt.xlabel('Значения')
    plt.ylabel('Плотность вероятности')
    plt.title('График гистограммы и подогнанной нормальной ф. плотности')
    plt.legend()
    plt.show()


file_path = r'ZadanMS203.xls'
sheet_name = "Sheet2"
column_name = "Z1-4"
bins = int(18/1)
x_min = 113.2
x_max = 130

file_data = read_excel_data(file_path, sheet_name, column_name)
plot_histogram_and_normal_density(file_data, bins, x_min, x_max)
