from contextlib import contextmanager
import matplotlib.pyplot as plt 
import pandas as pd
import metapack as mp
import numpy as np


@contextmanager
def new_plot(title, source=None, figsize=(10,8), xlabel=None, ylabel=None, x_label_rot=0, y_label_rot=90,
            panes=1, layout=[0, 0.03, 1, 0.95]):
    
    
    
    if panes == 1:
        fig, ax = plt.subplots(figsize=figsize)
    elif panes == 2:
        fig, ax = plt.subplots(2, figsize=figsize)
    elif panes == 3:
        fig = plt.figure(figsize=figsize)
        ax = [
            plt.subplot2grid((2, 2), (0, 0)),
            plt.subplot2grid((2, 2), (0, 1)),
            plt.subplot2grid((2, 2), (1, 0), colspan=2)
        ]
    else:
        fig, ax = plt.subplots(panes, figsize=figsize)
        ax = np.ravel(ax)
        
    fig.suptitle(title, fontsize=20)
    
    yield fig, ax
    
    if panes==1:
        ax = [ax]
    
    if source: 

        fig.text(1,0, "Source: "+source, horizontalalignment='right',verticalalignment='top')
        #fig.text(1,-.18, "Source: "+source,
        #    horizontalalignment='right',verticalalignment='top', transform=ax.transAxes)
    

    if xlabel is not None:
    
        if isinstance(xlabel, str):
            xlabel = [xlabel]*len(ax)
            
        for a,x,y in zip(ax, xlabel, ylabel):
            if x:
                a.set_xlabel(x, rotation=x_label_rot)
            
    if ylabel is not None:
            
        if isinstance(ylabel, str):
            ylabel = [ylabel]*len(ax)

        for a,x,y in zip(ax, xlabel, ylabel):
            if y:
                a.set_ylabel(y, rotation=y_label_rot)

    fig.tight_layout(rect=layout)
            
    plt.show()
  