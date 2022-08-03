import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import locale

def show_value_counts(serie, value_counted=False, dask=False, column_desc=None, grain='Rows', 
                      size=None, total=None, title=None, height=10, width=5, index=None, save_to=False, ax=None):
    fig = plt.figure()
    fig.set_size_inches(width, height)

    if ax is None:
        print('criando outro eixo') 
        ax = plt.subplot(1,1,1)

    if not value_counted:
        serie = serie.value_counts()
    
    if dask:
        serie = serie.compute()
        
    serie = serie.sort_values(ascending=True)

    if not total:
        total = serie.sum()
    
    corte = ''
    
    if (index):
        serie = serie.rename(index)
    
    if serie.index.dtype != 'object':
        if serie.index.dtype == 'float64':
            serie.index = serie.index.map(int)
        serie.index = serie.index.map(str)
    serie.index = serie.index.map(str)
    
    if size and len(serie) > size:
        serie = serie.sort_values(ascending=False)
        serie = serie[:size]
        serie = serie.sort_values(ascending=True)
        corte = ' ({} mais frequentes)'.format(size)
    
    if not title:
        if column_desc:
            column = column_desc
        else:
            column = serie.name
        title = "{} by {}{}".format(grain, column, corte)
   
    ax.barh(serie.index, serie, align='center', color='c', ecolor='black')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    percentage = serie/total*100
    number_distance = serie.max()*0.005
    
    for i, v in enumerate(serie):
        pct = locale.format_string('%.2f', percentage[i], True)
        ax.text(v+number_distance , i-0.2, '{0:,} ({1}%)'.format(v, pct), color='k')
    ax.set(title=title,
           xlabel='',
           ylabel='')
    sns.despine(left=True, bottom=True)

    if save_to:
        plt.savefig(save_to)

def plot_grid(functions_and_parameters, n_cols=3, values_mapping=None, width_scale=5.5, height_scale=4):
    Tot = len(functions_and_parameters)
    # Compute Rows required
    n_rows = Tot // n_cols
    n_rows += Tot % n_cols
    fig = plt.figure(1)
    fig.set_figwidth(n_cols*width_scale)
    fig.set_figheight(n_rows*height_scale)
    for position, functions_and_parameter in enumerate(functions_and_parameters):
        ax = fig.add_subplot(n_rows, n_cols, position+1)
        kwargs = {'ax': ax}
        function = functions_and_parameter[0]
        parameters = functions_and_parameter[1]
        function(**parameters, **kwargs)
    plt.show()

