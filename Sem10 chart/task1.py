# 1. Изобразите отношение households к population с
# помощью точечного графика
# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age
# """

from pandas import read_csv # импортировать компонент read_csv из модуля pandas
# read_csv - прочитать файл

from seaborn import scatterplot, relplot, histplot # seaborn - модуль для построения графиков; 
# scatterplot - точечный график
# relplot - линейный график
# histplot - гистограмма

from matplotlib.pyplot import show # - модуль для визуализации графиков
# show() - визуализировать


data1 = read_csv('california_housing_test.csv')



# 1. Изобразите отношение households к population с
# помощью точечного графика

def first():
    scatterplot(data=data1, x= 'households', y= 'population') # - создание точечного графика
    show() # - визуализация графика
#first()



# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график

def second():
    relplot(data=data1, x= 'longitude', y='median_house_value', kind= 'line') # - создание линейного графика
    show() # - визуализация графика
#second()



# 3. Представить гистограмму по housing_median_age

def third():
    histplot(data=data1, x= 'housing_median_age') # - создать гистограмму
    show() # - визуализация графика
#third()



# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

def fourth():
    histplot(data=data1, x= 'median_house_value', hue= 'housing_median_age')
    show()
fourth()


