from qgis.core import QgsProject
from qgis._core import QgsRasterLayer, QgsProject
from qgis.core import QgsApplication, QgsVectorLayer
from qgis.gui import QgsMapCanvas
from PyQt5.QtCore import QFileInfo

from Qgis2threejs import q3dcontroller
import importlib
qgis2threejs = importlib.import_module('Qgis2threejs')



PATH = 'C:\\Users\\drago\\Downloads\\clipped_DEM.tif'


# Initialize QGIS application
qgs = QgsApplication([], False)
qgs.initQgis()

# Load DEM file as raster layer
fileInfo = QFileInfo(PATH)
base_name = fileInfo.baseName()
layer = QgsRasterLayer(PATH, base_name)

if not layer.isValid():
    print(f"Error: Unable to load DEM file at {PATH}")

project = QgsProject.instance().addMapLayer(layer)
# project.addRasterLayer(PATH, 'dem')


q3d = q3dcontroller.Q3DController()

#q3d.setMapSettings(
 #   baseSize=100,  # the base size of the 3D model in meters
  #  verticalExaggeration=1.5,  # the vertical exaggeration factor
   # extent=project.mapCanvas().extent()  # the map canvas extent
#)

q3d.addLayer(
    layerId=0,  # the layer ID, starting from 0
    layerType=qgis2threejs.LAYER_TYPE_DEM,  # the layer type, in this case DEM
    properties={
        'name': 'dem',  # the layer name
        'queryable': True,  # whether the layer is queryable or not
        'visible': True,  # whether the layer is visible or not
        'styleWidget': {
            'color': '#ffffff',  # the color of the layer
            'transparency': 0  # the transparency of the layer
        }
    }
)

q3d.exportToWebPage(
    filename='3dmodel.html',  # the output file name
    outputDirectory='path/to/your/output/directory'  # the output directory
)

# or

q3d.exportToGltf(
    filename='3dmodel.gltf',  # the output file name
    outputDirectory='path/to/your/output/directory'  # the output directory
)
