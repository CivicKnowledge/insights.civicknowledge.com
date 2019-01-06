# Plotting functions for working with
# http://s3.sandiegodata.org/repo/clarinova.com/crime-incidents-casnd-7ba4-r3/incidents-csv.zip

from math import ceil
import matplotlib.pyplot as plt
import numpy as np

def plot_heat_grid(df, title='', types = None):

    if not types:
        types = sorted([ l for l in df.type.unique() if l.strip() and l not in ('-', 'ARSON','HOMICIDE') ])

    c = len(types)
    ncols = 4.
    nrows = ceil(float(c)/ncols)

    cmap = plt.get_cmap('YlOrRd')

    fig, axes = plt.subplots(nrows=int(nrows), ncols=int(ncols),  squeeze=True, sharex=False, sharey=False)

    fig.set_size_inches(ncols*3,nrows*3)
    axes = axes.ravel() # Convert 2D array to 1D
    plt.tight_layout(h_pad=1)
    for i, crime_types in enumerate(types):

        sub = df[df.type == crime_types]
        heatg = sub.groupby(['dow','hour'])
        hgcounts = heatg.count()['id'].unstack('hour').fillna(0)
   
        # Converting to an array puts it into a form that
        # matplotlib expects. This probably only works b/c the
        # hours and days of week are 1-based indexes. 
        axes[i].pcolormesh(np.array(hgcounts.T),cmap=cmap)
        axes[i].set_title(crime_types.title())
        
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    fig.suptitle(title, fontsize=18)
    
    return fig

def plot_heat_grid_community(df,  title='', communities=None):

    if not communities:
        communities = sorted([ l for l in df.community.unique() if l.strip() and l not in ('-') ])

    c = len(communities)
    ncols = 4.
    nrows = ceil(float(c)/ncols)

    cmap = plt.get_cmap('YlOrRd')

    fig, axes = plt.subplots(nrows=int(nrows), ncols=int(ncols), squeeze=True, sharex=False, sharey=False)

    fig.set_size_inches(ncols*3,nrows*3)
    
    name_map = df[['community','name']].set_index('community').to_dict()['name']
    
    axes = axes.ravel() # Convert 2D array to 1D
    plt.tight_layout(h_pad=1)
    for i, community in enumerate(communities):

        sub = df[df.community == community]
        if not sub.empty:
            heatg = sub.groupby(['dow','hour'])

            hgcounts = heatg.count()['id'].unstack('hour').fillna(0)

            # Converting to an array puts it into a for that
            # matplotlib expects. This probably only works b/c the
            # hours and days of week are 1-based indexes. 
            axes[i].pcolormesh(np.array(hgcounts.T),cmap=cmap)
            axes[i].set_title(name_map.get(community))
                             
    fig.suptitle(title, fontsize=18)