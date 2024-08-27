import pandas

SHEET_NAME = "Sheet2"
COLUMN_NAME = 'Z1-4'
FILE_NAME = r'ZadanMS203.xls'

INFORMATION_DICTIONARY = {
    "Объем наблюдений:" : 0,
    "Среднее значение:": 0,
    "Медиана:": 0,
    "Смещенная дисперсия:": 0,
    "Несмещенная дисперсия:": 0,
    "Стандартное отклонение:": 0,
    "Минимальное значение:": 0,
    "Максимальное значение:": 0,
    "Размах выборки:": 0,
    "Асимметрия:": 0,
    "Эксцесс:": 0
}

INFORMATION_KEYS = [
    "Объем наблюдений:",
    "Среднее значение:",
    "Медиана:",
    "Смещенная дисперсия:",
    "Несмещенная дисперсия:",
    "Стандартное отклонение:",
    "Минимальное значение:",
    "Максимальное значение:",
    "Размах выборки:",
    "Ассиметрия:",
    "Эксцесс:"
]

INFORMATION_VALUE = []


def ReadFile(file_name, sheet_name, column_name):
    df = pandas.read_excel(file_name, sheet_name=sheet_name)
    data = df[column_name]
    data = data.dropna()
    return data


def Engine(data):
    observations_count = data.count()
    INFORMATION_VALUE.append(observations_count)
    mean_value = data.mean()
    INFORMATION_VALUE.append(mean_value)
    median_value = data.median()
    INFORMATION_VALUE.append(median_value)
    variance_value = data.var()
    INFORMATION_VALUE.append(variance_value)
    no_variance_value = data.var() * (observations_count / (observations_count - 1))
    INFORMATION_VALUE.append(no_variance_value)
    std_deviation = data.std()
    INFORMATION_VALUE.append(std_deviation)
    min_value = data.min()
    INFORMATION_VALUE.append(min_value)
    max_value = data.max()
    INFORMATION_VALUE.append(max_value)
    range_value = data.max() - data.min()
    INFORMATION_VALUE.append(range_value)
    skewness = data.skew()
    INFORMATION_VALUE.append(skewness)
    kurtosis = data.kurtosis()
    INFORMATION_VALUE.append(kurtosis)


def FillInformationDictionary():
    for i in range(len(INFORMATION_KEYS)):
        INFORMATION_DICTIONARY[INFORMATION_KEYS[i]] = INFORMATION_VALUE[i]


def PrintResult():
    for key in INFORMATION_KEYS:
        print(key,INFORMATION_DICTIONARY[key])


def main():
    data = ReadFile(FILE_NAME, SHEET_NAME, COLUMN_NAME)
    Engine(data)
    FillInformationDictionary()
    PrintResult()


main()