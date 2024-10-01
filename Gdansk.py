import os

actual_lay = QgsProject.instance().mapLayers().values()

for lay in actual_lay:
    QgsProject.instance().removeMapLayer(lay)

#files_list = os.listdir('GIS_COURSES/Dane_Gdansk')
#
#for file in files_list:
#    if file.endswith('shp'):
#        layer_name = file.split('.')[0]
#        layer = iface.addVectorLayer(f'GIS_COURSES/Dane_Gdansk/{file}', layer_name, 'ogr')
        
uri = QgsDataSourceUri()
uri.setConnection('localhost', '5432', 'Gdansk', 'postgres', 'postgres')

objects = ['budynki', 'drogi', 'lasy', 'mosty', 'rzeki', 'poligon', 'linie']

for object in objects:
    uri.setDataSource('public', object, 'geom')
    vlayer = QgsVectorLayer(uri.uri(), object, 'postgres')
    QgsProject.instance().addMapLayers([vlayer])
    
actual_layers = QgsProject.instance().mapLayers().values()

for lay in actual_layers:
    if lay.name() == 'drogi':
        request = QgsFeatureRequest().setFilterExpression('wd1 > 6 AND rst = 1')
        request.setSubsetOfAttributes([])
        request.setFlags(QgsFeatureRequest.NoGeometry)
        result = lay.getFeatures(request)
        
        for r in result:
            szerokosc_drogi = r.attributes()[14]