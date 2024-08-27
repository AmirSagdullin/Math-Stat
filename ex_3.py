import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

excel_file_path = "ZadanMS203.xls"
sheet_name = "Sheet2"
column_name = "Z1-4"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

sorted_data = np.sort(data)
empirical_cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

std = np.std(data) # стандартное отклонение
average = np.mean(data) # среднее значение

theoretical_cdf = norm.cdf(sorted_data, average, std)

max_deviation = np.max(np.abs(empirical_cdf - theoretical_cdf))
print(f'Максимальное расхождение между эмпирической и гипотетической функциями распределения: {max_deviation}')

plt.step(sorted_data, empirical_cdf, label='Эмпирическая ф.р.', where='post')
plt.plot(sorted_data, theoretical_cdf, label='Гипотетическая ф.р.')
plt.legend()
plt.xlabel('Прочность металла')
plt.ylabel('Вероятность')
plt.title('График эмпирической ф.р., совмещенный с графиком ф.р. гипотетического р.')
plt.show()