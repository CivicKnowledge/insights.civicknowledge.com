

{
    "bref": "Maps and time ryhthms in the San Diego Police calls for service dataset",
    "description": "This is the description",
    "draft": false,
    "section": "notebooks",
    "show_input": "show",
    "slug": "san-diego-police-calls-for-service",
    "title": " San Diego Police Calls For Service",
    "toc": false,
    "weight": 3
}



Eric Busboom, 7 Nov 2017

In preparation for the [SCALE and Open San Diego Crime ANalysis Presentation](https://www.eventbrite.com/e/exploring-san-diego-crime-data-using-python-workshop-tickets-39192959196?utm_source=eb_email&utm_medium=email&utm_campaign=reminder_attendees_48hour_email&utm_term=eventname), I downloaded the [data package for the presentation](https://drive.google.com/open?id=0B-sBXvhIZi_gWHJENGd2UkhWbVk) and started on the analysis a bit early. 

The presentation will use the San Diego Police 2015 calls for service, but the [data repository has 2016 and 2017 as well](https://data.sandiego.gov/datasets/police-calls-for-service/). The seperate files for each of the three years are converted into a data package on our repository, and I also created Metapack packages for the boundary files for beats, neighborhoods and districts. Merging in these boundary files allows for analysing crime counts by geography. Here are the packages: 

* [SD Police Calls For Service](http://data.sandiegodata.org/dataset/sandiego-gov-police_calls-2015e)
* [SD Police Beat, District Regions](http://data.sandiegodata.org/dataset/sandiego-gov-police_regions)
 
This notebook requires the metapack package for downloading URLS, which you should be able to install, on Python 3.5 or later, with ``pip install metapack``


```python
%matplotlib inline
import metapack as mp
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd 
```

The Metapack system allows for packaging data, long with all of the metadata, and the ``open_package`` function can be used to load packages off the web. The the URL below is to a CSV package, which just referrs to CSV files on the web. You can get the link by to the CSV package file from the resource for ``sandiego.gov-police_regions-1`` in the [SRDRL data library repository page for the package](http://data.sandiegodata.org/dataset/sandiego-gov-police_regions)

```python
regions = mp.open_package('http://library.metatab.org/sandiego.gov-police_regions-1.csv')
regions
```




<h1>San Diego Police Regions</h1>
<p><p>sandiego.gov-police_regions-1</p>
<p>Boundary shapes for San Diego neighborhoods, beats and divisions.</p>
<p>metapack+http://library.metatab.org/sandiego.gov-police_regions-1.csv</p></p>
<h2>Contacts</h2>
<p><strong>Wrangler:</strong> <a href="mailto:eric@civicknowledge.com">Eric Busboom</a> <a href="http://civicknowledge.com">Civic Knowledge</a></p>
<h2>Resources</h2>
<p><ol>
<li><p><strong>pd_beats</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_beats.csv">http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_beats.csv</a> Police beats</p></li>
<li><p><strong>pd_divisions</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_divisions.csv">http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_divisions.csv</a> Police Divisions</p></li>
<li><p><strong>pd_neighborhoods</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_neighborhoods.csv">http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_neighborhoods.csv</a> Police Neighborhoods</p></li>
</ol></p>
</ol>



After opening packages, we can ask the package for what resources it has, download those resources, and turn them into Pandas dataframes.

```python
calls_p = mp.open_package('http://library.metatab.org/sandiego.gov-police_calls-2015e-1.csv')
calls_p
```




<h1>Police Calls for Service</h1>
<p><p>sandiego.gov-police_calls-2015e-1</p>
<p>Calls dispatched by the San Diego Police Department’s communications dispatch</p>
<p>metapack+http://library.metatab.org/sandiego.gov-police_calls-2015e-1.csv</p></p>
<h2>Contacts</h2>
<p><strong>Wrangler:</strong> <a href="mailto:eric@civicknowledge.com">Eric Busboom</a> <a href="http://civicknowledge.com">Civic Knowledge</a></p>
<h2>Resources</h2>
<p><ol>
<li><p><strong>call_type</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/call_type.csv">http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/call_type.csv</a> Type of call</p></li>
<li><p><strong>disposition</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/disposition.csv">http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/disposition.csv</a> Classification</p></li>
<li><p><strong>beat</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/beat.csv">http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/beat.csv</a> San Diego PD Beat</p></li>
<li><p><strong>pd_calls</strong> - <a target="_blank" href="http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/pd_calls.csv">http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/pd_calls.csv</a> Combined pd_calls for 2015, 2016 and YTD 2017</p></li>
</ol></p>
<h2>References</h2>
<p><ol>
<li><p><strong>pd_calls_2015</strong> - <a target="_blank" href="http://seshat.datasd.org/pd/pd_calls_for_service_2015_datasd.csv">http://seshat.datasd.org/pd/pd_calls_for_service_2015_datasd.csv</a> Service calls for 2015</p></li>
<li><p><strong>pd_calls_2016</strong> - <a target="_blank" href="http://seshat.datasd.org/pd/pd_calls_for_service_2016_datasd.csv">http://seshat.datasd.org/pd/pd_calls_for_service_2016_datasd.csv</a> Service calls for 2016</p></li>
<li><p><strong>pd_calls_2017_ytd</strong> - <a target="_blank" href="http://seshat.datasd.org/pd/pd_calls_for_service_2017_datasd.csv">http://seshat.datasd.org/pd/pd_calls_for_service_2017_datasd.csv</a> Service calls for 2017, Year To Date</p></li></p>
</ol>



```python
calls_r = calls_p.resource('pd_calls')
calls_r
```




<h3><a name="resource-pd_calls"></a>pd_calls</h3><p><a target="_blank" href="http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/pd_calls.csv">http://library.metatab.org/sandiego.gov-police_calls-2015e-1/data/pd_calls.csv</a></p><table>
<tr><th>Header</th><th>Type</th><th>Description</th></tr><tr><td>incident_num</td><td>text</td><td>Unique Incident Identifier</td></tr> 
<tr><td>date_time</td><td>datetime</td><td>Date / Time in 24 Hour Format</td></tr> 
<tr><td>day</td><td>integer</td><td>Day of the week</td></tr> 
<tr><td>stno</td><td>integer</td><td>Street Number of Incident, Abstracted to block level</td></tr> 
<tr><td>stdir1</td><td>text</td><td>Direction of street in address</td></tr> 
<tr><td>street</td><td>text</td><td>Name of Street</td></tr> 
<tr><td>streettype</td><td>text</td><td>Street Type</td></tr> 
<tr><td>stdir2</td><td>text</td><td>If intersecting street available, direction of that street</td></tr> 
<tr><td>stname2</td><td>text</td><td>If intersecting street available, street name</td></tr> 
<tr><td>sttype2</td><td>text</td><td>If intersecting street available, street type</td></tr> 
<tr><td>call_type</td><td>text</td><td>Type of call</td></tr> 
<tr><td>disposition</td><td>text</td><td>Classification</td></tr> 
<tr><td>beat</td><td>integer</td><td>San Diego PD Beat</td></tr> 
<tr><td>priority</td><td>text</td><td>Priority assigned by dispatcher</td></tr> </table>



```python
call_type_r = calls_p.resource('call_type')
call_types = call_type_r.dataframe().rename(columns={'description':'call_type_desc'})
call_types.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>call_type</th>
      <th>call_type_desc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>OUT OF SERV, SUBJTOCALL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10-97</td>
      <td>ARRIVE ON SCENE</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1016</td>
      <td>PRISONER IN CUSTODY</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1016PT</td>
      <td>PTU (PRISONER TRANSPORT)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1016QC</td>
      <td>SHOPLIFTER/QUICK CITE</td>
    </tr>
  </tbody>
</table>
</div>



```python
regions_r = regions.resource('pd_beats')
regions_r
```




<h3><a name="resource-pd_beats"></a>pd_beats</h3><p><a target="_blank" href="http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_beats.csv">http://library.metatab.org/sandiego.gov-police_regions-1/data/pd_beats.csv</a></p><table>
<tr><th>Header</th><th>Type</th><th>Description</th></tr><tr><td>id</td><td>integer</td><td></td></tr> 
<tr><td>objectid</td><td>integer</td><td></td></tr> 
<tr><td>beat</td><td>integer</td><td></td></tr> 
<tr><td>div</td><td>integer</td><td></td></tr> 
<tr><td>serv</td><td>integer</td><td></td></tr> 
<tr><td>name</td><td>text</td><td></td></tr> 
<tr><td>geometry</td><td>geometry</td><td></td></tr> </table>



```python
# The beats.cx[:-116.8,:] bit indexes the bounding box to exclude the empty portion of the 
# county. San Diego owns the footprint of a dam in east county, which displays as a tiny
# dot in the middle of empty space. 
# Note that this isn't actually defininf the bounding box; it's cutting out far-east regions, 
# and then GeoPandas creates the smaller bounding box that excludes them. So, the actually 
# value in the cx indexder can vary a bit. 

# Converting to float makes merging with the calls df ewasier, since the beat column
# in that df has nans. 

beats = regions_r.dataframe().geo
beats['beat'] = beats.beat.astype(float)
beats = beats.set_index('beat').cx[:-116.55,:]
beats.plot();
```


![png](/img/san-diego-police-calls-for-service/output_9_0.png)


There are a lot of interesting patterns in crime data when you create heat maps of two time dimensions, a visualization called a "Rhythm Map". We'll add the time dimensions now for use later. 

```python
pd_calls = calls_r.read_csv(low_memory=False)

def augment_time(df):
    df['date_time'] = pd.to_datetime(df.date_time)
    
    df['hour'] = df.date_time.dt.hour
    df['month'] = df.date_time.dt.month
    df['year'] = df.date_time.dt.year
    df['dayofweek'] = df.date_time.dt.dayofweek
    df['weekofyear'] = df.date_time.dt.weekofyear

    df['weekofdata'] = (df.year-df.year.min())*52+df.date_time.dt.weekofyear
    df['monthofdata'] = (df.year-df.year.min())*12+df.date_time.dt.month

    return df

assert pd_calls.call_type.dtype == call_types.call_type.dtype

pd_calls = augment_time(pd_calls).merge(call_types, on='call_type')

pd_calls['beat'] = pd_calls.beat.astype(float)

pd_calls = pd_calls.merge(beats.reset_index()[['beat', 'name']], on='beat')\
    .rename(columns={'name':'beat_name'})

```

# Incident Count Maps

The following maps plot the counts of incidents, over the whole dataset, for different call types, per beat. As is familiar to anyone who has worked with San Diego area crime data, the host spots for most incident types are Pacific Beach and Downtown. 

```python

def plot_geo(df, color_col, title=None):
    # Need to get aspect right or it looks wacky
    bb = beats.total_bounds
    aspect = (bb[3] - bb[1])/ (bb[2]-bb[0])
    x_dim = 8

    fig = plt.figure(figsize = (x_dim,x_dim*aspect))
    ax = fig.add_subplot(111)

    df.plot(ax=ax,column=color_col, cmap='RdYlGn_r',
                     scheme='fisher_jenks', legend=True);
  
    if title:
        fig.suptitle(title, fontsize=18);

    leg = ax.get_legend()
   
    #leg.set_bbox_to_anchor((0., 1.02, 1., .102))
    leg.set_bbox_to_anchor((1,.5))

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        
_ = gpd.GeoDataFrame(pd_calls.groupby('beat').incident_num.count().to_frame()\
                               .join(beats))

plot_geo(_, 'incident_num', 'Incidents Per Beat, 2015 to Aug 2017')
```


![png](/img/san-diego-police-calls-for-service/output_13_0.png)


```python
pd_calls.call_type_desc.value_counts().iloc[10:30]
```




    FLAG DOWN/FIELD INITIATED         28280
    REQUEST FOR TOW TRUCK             27274
    NO DETAIL ACCIDENT                27070
    MENTAL CASE                       25779
    SPECIAL DETAIL                    25115
    SELECTIVE ENFORCEMENT             25098
    FOLLOW-UP BY FIELD UNIT           24348
    HAZARDOUS CONDITION               23954
    SLEEPER                           21584
    INFORMATION FOR DISPATCHERS       21490
    TRAFFIC STOP,FOR TMPOUT           19084
    ALL UNITS INFORMATION-PRI 2       19056
    LOUD PARTY                        17803
    CAR THEFT REPORT                  16952
    VEH VIOLATING 72HR PARKING RES    16155
    BATTERY                           15757
    RECKLESS DRIVING-ALL UNITS        15197
    CRIME CASE NUMBER REQUEST         15122
    FOOT PATROL/FIELD INITIATED       14955
    BURGLARY REPORT                   14652
    Name: call_type_desc, dtype: int64



```python
_ = gpd.GeoDataFrame(pd_calls[pd_calls.call_type_desc == 'LOUD PARTY']
                             .groupby('beat')
                             .incident_num.count().to_frame()\
                             .join(beats))

plot_geo(_, 'incident_num', "LOUD PARTY calls, 2015 to Aug 2017")             
```


![png](/img/san-diego-police-calls-for-service/output_15_0.png)


```python
_ = gpd.GeoDataFrame(pd_calls[pd_calls.call_type_desc == 'ILLEGAL PARKING']
                             .groupby('beat')
                             .incident_num.count().to_frame()\
                             .join(beats))

plot_geo(_, 'incident_num',  "ILLEGAL PARKING calls, 2015 to Aug 2017")  
```


![png](/img/san-diego-police-calls-for-service/output_16_0.png)


```python
_ = pd_calls[pd_calls.call_type_desc == 'BATTERY']\
                             .groupby('beat')\
                             .incident_num.count().to_frame()\
                             .join(beats)


plot_geo(gpd.GeoDataFrame(_), 'incident_num', "BATTERY calls, 2015 to Aug 2017")  
```


![png](/img/san-diego-police-calls-for-service/output_17_0.png)


Sometimes, very high density areas like PB and Downtown will obscure patterns in other areas. One of the ways to handle this is to just exclude those areas. First, let's locate which are the highest crime area. 

```python
_.sort_values('incident_num', ascending=False).head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>incident_num</th>
      <th>id</th>
      <th>objectid</th>
      <th>div</th>
      <th>serv</th>
      <th>name</th>
      <th>geometry</th>
    </tr>
    <tr>
      <th>beat</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>521.0</th>
      <td>1278</td>
      <td>98</td>
      <td>489</td>
      <td>5</td>
      <td>520</td>
      <td>EAST VILLAGE</td>
      <td>POLYGON ((-117.1508808796175 32.71942332829821...</td>
    </tr>
    <tr>
      <th>122.0</th>
      <td>738</td>
      <td>64</td>
      <td>231</td>
      <td>1</td>
      <td>120</td>
      <td>PACIFIC BEACH</td>
      <td>POLYGON ((-117.2221709033007 32.81525925531844...</td>
    </tr>
    <tr>
      <th>524.0</th>
      <td>695</td>
      <td>93</td>
      <td>463</td>
      <td>5</td>
      <td>520</td>
      <td>CORE-COLUMBIA</td>
      <td>POLYGON ((-117.171021304813 32.71987375185346,...</td>
    </tr>
    <tr>
      <th>523.0</th>
      <td>654</td>
      <td>30</td>
      <td>83</td>
      <td>5</td>
      <td>520</td>
      <td>GASLAMP</td>
      <td>POLYGON ((-117.1610808948147 32.71569562856276...</td>
    </tr>
    <tr>
      <th>627.0</th>
      <td>565</td>
      <td>83</td>
      <td>408</td>
      <td>6</td>
      <td>620</td>
      <td>HILLCREST</td>
      <td>POLYGON ((-117.1616090022237 32.75878799862505...</td>
    </tr>
    <tr>
      <th>813.0</th>
      <td>495</td>
      <td>74</td>
      <td>352</td>
      <td>8</td>
      <td>810</td>
      <td>NORTH PARK</td>
      <td>POLYGON ((-117.1304627884029 32.7691214134209,...</td>
    </tr>
    <tr>
      <th>512.0</th>
      <td>368</td>
      <td>58</td>
      <td>203</td>
      <td>5</td>
      <td>510</td>
      <td>LOGAN HEIGHTS</td>
      <td>POLYGON ((-117.1213484238577 32.70672846114386...</td>
    </tr>
    <tr>
      <th>614.0</th>
      <td>350</td>
      <td>24</td>
      <td>64</td>
      <td>6</td>
      <td>610</td>
      <td>OCEAN BEACH</td>
      <td>POLYGON ((-117.2340495278368 32.75789474471601...</td>
    </tr>
    <tr>
      <th>511.0</th>
      <td>348</td>
      <td>21</td>
      <td>52</td>
      <td>5</td>
      <td>510</td>
      <td>None</td>
      <td>(POLYGON ((-117.2252864171211 32.7026041543147...</td>
    </tr>
    <tr>
      <th>511.0</th>
      <td>348</td>
      <td>132</td>
      <td>626</td>
      <td>5</td>
      <td>510</td>
      <td>BARRIO LOGAN</td>
      <td>POLYGON ((-117.1527936937041 32.70523801385234...</td>
    </tr>
  </tbody>
</table>
</div>



Here is the map excluding the top 5 high crime areas. The excluded areas are omitted completely, shown in white. 

```python
# Could also get the beats by name. 
pb_beat = beats[beats.name=='PACIFIC BEACH'].index.values[0]
gas_beat = beats[beats.name=='GASLAMP'].index.values[0]

low_crime = _.sort_values('incident_num', ascending=False).iloc[5:]
_lc = _.loc[list(low_crime.index.values)]

plot_geo(gpd.GeoDataFrame(_lc), 'incident_num', 
         "BATTERY calls, 2015 to Aug 2017, Lower Crime Areas")  
```


![png](/img/san-diego-police-calls-for-service/output_21_0.png)


```python
_ = gpd.GeoDataFrame(pd_calls[pd_calls.call_type_desc == 'BATTERY']
                             .groupby('beat')
                             .incident_num.count().to_frame()\
                             .join(beats))

plot_geo(_, 'incident_num', "BATTERY calls, 2015 to Nov 2017")  
```


![png](/img/san-diego-police-calls-for-service/output_22_0.png)


```python
_ = gpd.GeoDataFrame(pd_calls[pd_calls.call_type_desc == 'MENTAL CASE']
                             .groupby('beat')
                             .incident_num.count().to_frame()\
                             .join(beats))

plot_geo(_, 'incident_num', "MENTAL CASE calls, 2015 to Aug 2017")  
```


![png](/img/san-diego-police-calls-for-service/output_23_0.png)


# Rhythm Maps

By plotting two time dimensions in a heat map we can often see interesting patterns. 

Here we'll look at the rhythm of parties in Pacific Beach, plotting the number of party calls as colors in a maps with an X axis of the day of the week, and a Y axis of the hour of the day. As you'd expect, the LOUD PARTY calls are primarily on Friday and Saturday nights. 


```python
pb_beat = beats[beats.name=='PACIFIC BEACH'].index.values[0]

_ = pd_calls[(pd_calls.call_type_desc=='LOUD PARTY') & (pd_calls.beat == pb_beat)]

ht = pd.pivot_table(data=_, 
                    values='incident_num', index=['hour'],columns=['dayofweek'],
                    aggfunc='count')

fig, ax = plt.subplots(figsize=(6,6))

sns.heatmap(ht, ax=ax);
```


![png](/img/san-diego-police-calls-for-service/output_25_0.png)


Looking at the hour of day versus month, there is a clear seasonal pattern, with fewer loud party calls during the winter. 

```python
pb_beat = beats[beats.name=='PACIFIC BEACH'].index.values[0]

_ = pd_calls[(pd_calls.call_type_desc=='LOUD PARTY') & (pd_calls.beat == pb_beat)]



fig, ax = plt.subplots(figsize=(8,8))

fig.suptitle("LOUD PARTY Calls In Pacific Beach\n2015 to Aug 2017\nBy Hour and Month", fontsize=18);

sns.heatmap(ht, ax=ax);
```


![png](/img/san-diego-police-calls-for-service/output_27_0.png)


```python
hm_beats = pd_calls[['beat_name', 'hour','month']].copy()
hm_beats['count'] = 1
hm_beats = hm_beats.groupby(['beat_name', 'hour','month']).count().reset_index()
```

# Small Multiple Rhythm Maps

Rhythm maps really shine when they are part of a small multiple grid, or in Seaborn terminology, a Facet Grid. These take a bit more work to setup, but they are really valuable for finding patterns. 

Note how clearly you can see when students go back to school, and the July rowdiness in PB and MB. 

But, the really interesting thing is that in many communities, most obviously in San Ysidro, Core-Columbia, Otay Mesa, and a few others, there are a high number of calls are 4:00 in the afternoon. Any ideas?

```python

# Top 16 beats
top_beats= pd_calls.beat_name.value_counts().index.values[:16]

from IPython.display import display

# select only the rows for the top 16 beats
_ = hm_beats[hm_beats.beat_name.isin(top_beats)]

g = sns.FacetGrid(_, col="beat_name", col_wrap=4)

def facet_heatmap(data,  color, **kwargs):

    ht = data.pivot(index="hour", columns='month', values='count')

    sns.heatmap(ht, cmap='Reds', **kwargs)  

#cbar_ax = g.fig.add_axes([.92, .3, .02, .4])  # Create a colorbar axes

    
with sns.plotting_context(font_scale=3.5):   
    g = g.map_dataframe(facet_heatmap) 
    
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
g.fig.suptitle("LOUD PARTY Calls By Month of Year, By Hour of Day, By Beat",
              fontsize=18);
```


![png](/img/san-diego-police-calls-for-service/output_30_0.png)

