import pandas as pd
import numpy as np
import scipy.stats as stats

# Путь к файлу
excel_file_path = "ZadanMS203.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z13"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

size = len(data)
num_kondicion = sum(data > 116.5)
dolya_kondicion = num_kondicion / size
std_error = np.sqrt(dolya_kondicion * (1 - dolya_kondicion) / size)

Q = 0.975
alpha = 1 - Q
degrees_of_freedom = size - 1
t_quantile = stats.norm.ppf(1 - alpha, size, dolya_kondicion)

def tocno_board_upper(Q, size, num_kondicion):
    p_upper_bound = stats.binom.ppf(Q, size, num_kondicion)
    return p_upper_bound / size

def pribliz_board_upper(dolya_kondicion, t_quantile, std_error):
    upper_bound = dolya_kondicion + t_quantile * std_error
    return upper_bound

print(f"Объем выборки: {size}")
print(f"Число кондиционных: {num_kondicion}")
print(f"Доля кондиционных: {dolya_kondicion}")
print(f"Станд. ошибка среднего: {std_error}")
print(f"97.5%-я верхняя граница\n(приближенная) <= {pribliz_board_upper(dolya_kondicion, t_quantile, std_error)}\n(точная) <= {tocno_board_upper(Q, size, dolya_kondicion)}")
