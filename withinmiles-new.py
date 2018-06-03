import sqlite3
from qgis.core import QgsVectorLayer,QgsDataSourceUri,QgsProject
#from qgis.core import QgsMapLayerRegistry

layers = QgsProject.instance().mapLayersByName('ResultLayer')
for layer in layers:
    QgsProject.instance().removeMapLayer(layer)

with open("M:\\Spring18\\AdvDB\\Project\\2.0\\input.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

source=array[0].rstrip()
radius=float(array[1].rstrip())
radius=radius*0.00001
category=array[2]


with sqlite3.connect("M:\\Spring18\\AdvDB\\Project\\2.0\\FullMap.sqlite") as conn:
    conn.enable_load_extension(True)
    conn.load_extension("mod_spatialite")

c=conn.cursor()

if source == "Source":
    query = "select Name from 'UTA_Full_Map Polygon' where description='"+category+"'"
else:
    if category=="Category":
        query = "select b2.Name from 'UTA_Full_Map Polygon' b1,'UTA_Full_Map Polygon' b2 where intersects(b2.geom, buffer(b1.geom,"+str(radius)+")) and b1.Name='"+source+"' and b2.Name!='"+source+"'"
    else:
        query = "select b2.Name from 'UTA_Full_Map Polygon' b1,'UTA_Full_Map Polygon' b2 where intersects(b2.geom, buffer(b1.geom,"+str(radius)+")) and b1.Name='"+source+"' and b2.Name!='"+source+"' and b2.description='"+category+"'"

#print("select b2.Name from 'UTA_Full_Map Polygon' b1,'UTA_Full_Map Polygon' b2 where intersects(b2.geom, buffer(b1.geom,"+str(radius)+")) and b1.Name='"+source+"' and b2.Name!='"+source+"'")

opfile = open("M:\\Spring18\\AdvDB\\Project\\2.0\\output.txt","w")

for row in c.execute(query):
    for member in row:
        uri = QgsDataSourceUri()
        uri.setDatabase('M:\\Spring18\\AdvDB\\Project\\2.0\\FullMap.sqlite')
        uri.setDataSource('', 'uta_full_map polygon', 'geom',"Name = '"+member+"'",'')
        vlayer = QgsVectorLayer(uri.uri(), 'ResultLayer', 'spatialite')
        QgsProject.instance().addMapLayer(vlayer)
        vlayer.isValid()
        opfile.write(member+"\n")
        
opfile.close()
ins.close()
c.close()

