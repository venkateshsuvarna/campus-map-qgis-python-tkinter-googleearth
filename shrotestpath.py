layer = iface.activeLayer()
layer.selectAll()
d = QgsDistanceArea()
d.setEllipsoid('WGS84')
#d.setEllipsoidalMode(True)


for feature in layer.getFeatures():
    #print(feature.geometry().length())
    #print(feature[0],feature[1])
    feature1 = feature[0]
    feature2 = feature[1]
    a = [0.0] * 4
    i = 0
    for x in feature1.split(','):
        a.insert(i,x)
        i = i + 1
    for x in feature2.split(','):
        a.insert(i,x)
        i = i + 1
        
    #print("distance in meters: ", d.measureLine(QgsPointXY(-97.1158402247, 32.7314863791),QgsPointXY(-97.1157399527, 32.7314863791)))
    #d.measureLine(QgsPointXY
    
#opfile = open("M:\\Spring18\\AdvDB\\Project\\2.0\\output.txt","w")
    
dis=d.measureLine(QgsPointXY(float(a[0]),float(a[1])),QgsPointXY(float(a[2]),float(a[3])))
print("distance in meters: ", dis)
print("time: ", ((dis/1000*1.6)/3)*60)

'''opfile.write("distance in meters: ")
opfile.write(str(dis))
opfile.write("\ntime: ")

opfile.write(str(((dis/1000*1.6)/3)*60))
    
opfile.close()'''

