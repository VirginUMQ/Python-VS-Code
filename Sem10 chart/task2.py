# """
# Написать EDA(разведочный анализ данных) для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap (тепловая диаграмма)
# ● Использовать 2-3 гистограммы
# """



from seaborn import load_dataset, scatterplot, PairGrid, heatmap # seaborn - модуль для построения графиков; 
# load_dataset - прочитать файл
# scatterplot - точечный график
#PairGrid - спец класс конструкторов, принимающий как количественные так и категориальные переменные
#heatmap - тепловая диаграмма


from matplotlib.pyplot import show # - модуль для визуализации графиков
# show() - визуализировать



from matplotlib import pyplot



peng = load_dataset('penguins') # здесь без расширения



# ● Использовать 2-3 точечных графика

def first():
    scatterplot(data= peng, x="flipper_length_mm", y="body_mass_g")
    show()
#first()



# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, style

def second():
    scatterplot(data= peng, x="flipper_length_mm", y="body_mass_g", hue= 'sex', size= 'island', style= 'island')
    show()
#second()



# ● Использовать PairGrid с типом графика на ваш выбор

def third():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"] # - количественные переменные
    y_vars = ['sex']
    PG = PairGrid(data=peng, x_vars=x_vars, y_vars=y_vars, hue='species')
    PG.map(scatterplot)
    show()
#third()



# ● Изобразить Heatmap

def fourth():
    peng2 = peng.pivot_table(index= 'species', columns= 'island', values= 'body_mass_g') # хз че такое
    heatmap(peng2)
    pyplot.xlabel('Остров', size= 14)
    pyplot.ylabel('Вид пингвинов', size= 14)
    show()
#fourth()



# ● Использовать 2-3 гистограммы
def def5():
    peng['bill_depth_mm'].hist(bins=8) # .hist() - метод гистограммы, bins - полосы
    show()
def5()