# MS PowerBI with Python example 
# Prolog - Auto Generated 

import os, uuid, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import pandas

os.chdir(u'C:/Users/Zauza/PythonEditorWrapper_8b0761ca-ace8-4728-b910-931d58502acc')
dataset = pandas.read_csv('input_df_366a858e-b4a4-428a-b252-a0b650e30602.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667), dpi=72)
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))

# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# Следующий код для создания кадра данных и удаления повторяющихся строк выполняется всегда и служит начальным режимом для скрипта: 

dataset = pandas.DataFrame(Month of Year, Sessions)
dataset = dataset.drop_duplicates()

# Вставьте или введите здесь код скрипта:

# Epilog - Auto Generated #
os.chdir(u'C:/Users/Zauza/PythonEditorWrapper_8b0761ca-ace8-4728-b910-931d58502acc')
