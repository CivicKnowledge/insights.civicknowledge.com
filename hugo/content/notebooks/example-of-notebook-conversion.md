

{
    "authors": [
        {
            "email": "eric@civicknowledge.com",
            "name": "Eric Busboom",
            "organization": "Civic Knowledge",
            "type": "wrangler"
        }
    ],
    "bref": "This is a converted notebook",
    "date": "2017-11-11T20:05:06.378196",
    "description": "An example of a metatab package, inlined into a Jupyter notebook.",
    "draft": false,
    "guthub": null,
    "section": "notebooks",
    "show_input": "hide",
    "slug": "example-of-notebook-conversion",
    "title": "Example Of Notebook Conversion",
    "toc": false,
    "weight": 2
}


Metatab has it's own Notebook conversion process, will will create a Metatab package with the notebook, it's Makrdown and HTML conversion, and the dataset it creates. FOr these conversions, input code cells are by default hidden and must be explicitly re-enabled by starting code cells with `%showinput`




The Notebook can include inline Metatab, in a line-oriented format. These cells are code cells and start with a `%%metatab` magic. 

```python
%%metatab 

Identifier: override_this
Identifier: this_one_too
Identifier: 7108517a-7163-41a5-943d-961f9a086a3f
Origin: example.com
Dataset: foobar.com 
Name: example.com-foobar.com
    
==== Contacts
Wrangler: Eric Busboom
Wrangler.Email: eric@civicknowledge.com
Wrangler.Organization: Civic Knowledge

    
==== References
Reference: http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv
Reference.Name: reference
Reference.Title: The First Example Data File
Reference.Startline: 5
Reference.HeaderLines: 3,4
    
==== Resources
Datafile: http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv
Datafile.Name: ext_resource
Datafile.Title: An Extern CSV Resource
Datafile.Startline: 5
Datafile.HeaderLines: 3,4
```






<h2>example.com-foobar.com</h2>
<p></p>

<p></p>

<h3>Contacts</h3>
<p><strong>Wrangler:</strong> <a href="mailto:eric@civicknowledge.com">Eric Busboom</a> </p>
<h3>Resources</h3>
<p><ol>
<li><p><strong>ext_resource</strong> - <a target="_blank" href="http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv">http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv</a> </p></li>
</ol></p>
<h3>References</h3>
<p><ol>
<li><p><strong>reference</strong> - <a target="_blank" href="http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv">http://public.source.civicknowledge.com/example.com/sources/renter_cost.csv</a> </p></li></p>
</ol>



By default, the metatab document is assigned to the variable named `mt_pkg`. This document can be displayed to show the package metadata. 

Below is a code input cell that will be shown, because it starts with a `%mt_showinput` magic. 






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
      <th>id</th>
      <th>gvid</th>
      <th>renter_cost_gt_30</th>
      <th>renter_cost_gt_30_cv</th>
      <th>owner_cost_gt_30_pct</th>
      <th>owner_cost_gt_30_pct_cv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0O0P01</td>
      <td>1447</td>
      <td>13.617607</td>
      <td>42.248175</td>
      <td>8.272141</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0O0P03</td>
      <td>5581</td>
      <td>6.235932</td>
      <td>49.280353</td>
      <td>4.933369</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0O0P05</td>
      <td>525</td>
      <td>17.648159</td>
      <td>45.219638</td>
      <td>13.288720</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0O0P07</td>
      <td>352</td>
      <td>28.061965</td>
      <td>47.439353</td>
      <td>17.383329</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0O0P09</td>
      <td>1189</td>
      <td>11.824215</td>
      <td>43.157895</td>
      <td>8.916487</td>
    </tr>
  </tbody>
</table>
</div>



Dataframes can be added to the metatadata as resources with the `%mt_add_dataframe df2` magic. The `references.dataframe()` method returns objects of class `MetatabDataframe`, which have `name` and `title` fields that are used in the metadata schemas, and the `MetatabSeries.description` is used for the column description 







When the dataframe is added, Metatab extracts its schema and adds it to the metadata. Fetching the resource and displaying it will show the schema in a prettty format





The HTML output will include any images, but unline the default HTML converted, the images are linked as seperate files into the HTML documentation.




![png](/img/example-of-notebook-conversion/output_16_0.png)


Here is an attachment.

![Screen%20Shot%202017-11-11%20at%202.13.00%20PM.png](/img/example-of-notebook-conversion/output_17_0.png)





