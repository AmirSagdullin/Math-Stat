import math

import pandas as pd
import numpy as np
import scipy.stats as stats

# Путь к файлу
excel_file_path = "ZadanMS203.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z12"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

size = len(data)
variance = np.var(data, ddof=1)  # ddof=1 для выборочной дисперсии

Q = 0.95
alpha = 1 - Q

# Вычисляем верхнюю границу доверительного интервала для дисперсии
upper_bound_variance = (size * variance) / stats.chi2.ppf(alpha, df=size - 1)

# Вычисляем верхнюю границу доверительного интервала для стандартного отклонения
upper_bound_std_dev =(size * math.sqrt(variance)) / stats.chi2.ppf(alpha, df=size - 1)
print(math.sqrt(variance))
print(f"Объем выборки: {size}")
print(f"Дисперсия: {variance}")
print(f"95%-ая верхняя граница для дисперсии: {upper_bound_variance}")
print(f"95%-ая верхняя граница для стандартного отклонения: {upper_bound_std_dev}")
