# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# one hot - табличный вид из "0" и "1"

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data.loc[data['whoAmI'] == 'robot', 'Robot'] = '1'
data.loc[data['whoAmI'] == 'robot', 'Human'] = '0'

data.loc[data['whoAmI'] == 'human', 'Human'] = '1'
data.loc[data['whoAmI'] == 'human', 'Robot'] = '0'

print(data)
