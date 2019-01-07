var wms_layers = [];

        var lyr_StamenTerrain_0 = new ol.layer.Tile({
            'title': 'StamenTerrain_0',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: '<a href=""></a>',
                url: 'http://a.tile.stamen.com/terrain/{z}/{x}/{y}.png'
            })
        });var format_re_homeless_1 = new ol.format.GeoJSON();
var features_re_homeless_1 = format_re_homeless_1.readFeatures(json_re_homeless_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_re_homeless_1 = new ol.source.Vector({
    attributions: '<a href=""></a>',
});
jsonSource_re_homeless_1.addFeatures(features_re_homeless_1);var lyr_re_homeless_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_re_homeless_1, 
                style: style_re_homeless_1,
    title: 're_homeless<br />\
    <img src="styles/legend/re_homeless_1_0.png" /> aian<br />\
    <img src="styles/legend/re_homeless_1_1.png" /> asian<br />\
    <img src="styles/legend/re_homeless_1_2.png" /> black<br />\
    <img src="styles/legend/re_homeless_1_3.png" /> hisp<br />\
    <img src="styles/legend/re_homeless_1_4.png" /> nhwhite<br />\
    <img src="styles/legend/re_homeless_1_5.png" /> other<br />'
        });

lyr_StamenTerrain_0.setVisible(true);lyr_re_homeless_1.setVisible(true);
var layersList = [lyr_StamenTerrain_0,lyr_re_homeless_1];
lyr_re_homeless_1.set('fieldAliases', {'geoid': 'geoid', 'aian': 'aian', 'asian': 'asian', 'black': 'black', 'hisp': 'hisp', 'nhopi': 'nhopi', 'nhwhite': 'nhwhite', 'other': 'other', 'max_re': 'max_re', });
lyr_re_homeless_1.set('fieldImages', {'geoid': 'TextEdit', 'aian': 'TextEdit', 'asian': 'TextEdit', 'black': 'TextEdit', 'hisp': 'TextEdit', 'nhopi': 'TextEdit', 'nhwhite': 'TextEdit', 'other': 'TextEdit', 'max_re': 'TextEdit', });
lyr_re_homeless_1.set('fieldLabels', {'geoid': 'no label', 'aian': 'no label', 'asian': 'no label', 'black': 'no label', 'hisp': 'no label', 'nhopi': 'no label', 'nhwhite': 'no label', 'other': 'no label', 'max_re': 'no label', });
lyr_re_homeless_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});