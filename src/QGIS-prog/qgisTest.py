# Import necessary QGIS modules
from qgis._core import QgsRasterLayer, QgsProject
from qgis.core import QgsApplication, QgsVectorLayer
from qgis.gui import QgsMapCanvas
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication
import processing

from Qgis2threejs import q3dcontroller

from Qgis2threejs import qgis2threejs


# Function to create a 3D model using Qgis2threejs plugin
def create_3d_model(dem_path, output_path):
    # Initialize QGIS application
    qgs = QgsApplication([], False)
    qgs.initQgis()

    # Load DEM file as raster layer
    fileInfo = QFileInfo(dem_path)
    base_name = fileInfo.baseName()
    layer = QgsRasterLayer(dem_path, base_name)

    if not layer.isValid():
        print(f"Error: Unable to load DEM file at {dem_path}")
        return

    # Add the raster layer to the map
    QgsProject.instance().addMapLayer(layer)

    # Set up QGIS map canvas

    canvas = QgsMapCanvas()
    canvas.setLayers([layer])

    # Run Qgis2threejs algorithm
    parameters = {
        'DEM': layer,
        'DEM_Clip': False,
        'Exaggeration': 1.0,
        'Image_Mode': 0,
        'Color_Mode': 0,
        'Texture': None,
        'DEM_Hillshade': True,
        'Hillshade_Elevation': 45,
        'Hillshade_Azimuth': 315,
        'Hillshade_Color': 0,
        'Contour': False,
        'Contour_Interval': 10,
        'Contour_Index': 0,
        'DEM_Mesh': True,
        'DEM_Mesh_Color': 0,
        'DEM_Mesh_Layer': None,
        'Culling': False,
        'Tileset_Output': output_path,
        'Tileset_Options': 'default',
    }

    # Create a Qgis2threejs object
    q3d = q3dcontroller.Q3DController()

    # Set the DEM layer as the base layer
    q3d.addLayer(layer)

    # Set the output filename
    output_file = "dem_model.glb"

    # Export the 3D model as a glTF file
    q3d.exportToGLTF(output_file)

    # processing.run("qgis2threejs:qgis2threejs", parameters)

    # Exit QGIS application
    qgs.exitQgis()

    


if __name__ == '__main__':
    # Replace 'path/to/your/dem/file.tif' with the actual path to your DEM file
    dem_file_path = 'C:\\Users\\drago\\Downloads\\clipped_DEM.tif'

    # Replace 'path/to/your/output/folder' with the desired output folder path
    output_folder_path = 'C:\\Users\\drago\\Downloads\\folder'

    create_3d_model(dem_file_path, output_folder_path)
