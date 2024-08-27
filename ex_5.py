# H0 - среднее значение параметра не изменится или увеличится
# H1 - cреднее значение параметра уменьшится
import math

import pandas as pd
import numpy as np
from scipy import stats

#Путь к файлу
excel_file_path = "ZadanMS203.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_before = "Z5A"
column_name_after = "Z5B"

df_before = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_after = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_before = df_before[column_name_before]
data_before = data_before.dropna()

data_after = df_after[column_name_after]
data_after = data_after.dropna()

u = data_before - data_after
print(u)
# Объем выборок
def data_size(data_before, data_after):
    result = []
    size_before = len(data_before)
    size_after = len(data_after)
    difference_of_size = size_after

    result.append(size_before)
    result.append(size_after)
    result.append(difference_of_size)

    return result

# Среднее выборок
def avarage_value(data_before, data_after):
    result = []
    average_before = np.mean(data_before)
    average_after = np.mean(data_after)
    difference_of_average = np.mean(u)

    result.append(average_before)
    result.append(average_after)
    result.append(difference_of_average)

    return result

#Стандартные отклонения
def std_deviation(data_before, data_after):
    result = []
    std_before = np.std(data_before)
    std_after = np.std(data_after)
    difference_of_std = np.std(u)

    result.append(std_before)
    result.append(std_after)
    result.append(difference_of_std)

    return result

# Стандартная ошибка среднего
def std_error_of_mean(data_before, data_after):
    result = []
    std_error_before = np.std(data_before) / np.sqrt(len(data_before) - 1)
    std_error_after = np.std(data_after) / np.sqrt(len(data_after) - 1)
    difference_of_std_error = np.std(u) / np.sqrt(len(u) - 1)


    result.append(std_error_before)
    result.append(std_error_after)
    result.append(difference_of_std_error)

    return result

# Статистика Стьюдента и p-value (уровень значимости для конкретного случая)
size = data_size(data_before, data_after)
mean = avarage_value(data_before, data_after)
std = std_deviation(data_before, data_after)
std_error = std_error_of_mean(data_before, data_after)

t_value = mean[2] / std[2] * math.sqrt(size[0] - 1)
p_value = stats.t.cdf(t_value, size[0] - 1)

c_kr = stats.t.ppf(1 - 0.1,56)

print("                               До                После                Разность" )
print(f"Объем выборки:                 {size[0]}                 {size[1]}                      {size[2]}")
print(f"Среднее:                  {mean[0]}         {mean[1]}        {mean[2]}")
print(f"Станд. отклонение:        {std[0]}          {std[1]}          {std[2]}")
print(f"Станд.ошибка среднего:    {std_error[0]}        {std_error[1]}       {std_error[2]}\n")

print(f"Статистика Стьюдента: T = {t_value}")
print(f"10%-критическая область: {c_kr}")
print(f"p-значение: {p_value}")

if p_value < 0.1:
    print("Гипотеза отвергается")
else:
    print("Гипотеза принимается")

if t_value > c_kr:
    print("Гипотеза принимается")
else:
    print("Гипотеза отвергается")

print("Вывод: данные подтверждают предположение об изменении давления после лечения.")