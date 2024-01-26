import wasdi
import rasterio
import matplotlib.pyplot as plt

import requests


def visualize_dem(sLocalImagePath, save_path):
    # Open the DEM file
    with rasterio.open(sLocalImagePath) as dem:
        # Read the elevation data
        elevations = dem.read(1)

        # Plot the elevation map
        plt.figure(figsize=(10, 8))
        plt.imshow(elevations, cmap='terrain', extent=dem.bounds)
        plt.colorbar(label='Elevation (meters)')
        plt.title('Digital Elevation Model')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')

        # Save the image
        plt.savefig(save_path, format='png')
        plt.close()

        return 0


def visualize_raster():
    from osgeo import gdal
    import pandas as pd

    # Specifica il percorso del tuo file TIFF DEM
    file_path = "C:\\Users\\drago\\Documents\\VR Projects\\data\\CopDEM30m_wbm_Pakistan_compressed (3).tif"

    # Apre il file TIFF DEM
    dataset = gdal.Open(file_path)

    # Legge i valori numerici delle altezze
    band = dataset.GetRasterBand(1)
    altezze = band.ReadAsArray()

    # Converte l'array in un DataFrame di Pandas
    df_altezze = pd.DataFrame(altezze)

    # Visualizza i primi 10x10 valori della tabella
    print(df_altezze.iloc[:10, :10])

    # Esporta il DataFrame in un file CSV
    output_csv_path = "altezze_table.csv"
    df_altezze.to_csv(output_csv_path, index=False)

    print(f"DataFrame exported to: {output_csv_path}")

    # Stampa la matrice delle altezze
    print(altezze)


def download_sld_from_geoserver(base_url, workspace, layer_name, output_path):
    # Construct the GeoServer URL for the SLD file
    sld_url = f"{base_url}/{workspace}/ows?service=WMS&version=1.1.1&request=GetStyles&layers={layer_name}"

    try:
        # Perform the download operation
        response = requests.get(sld_url, stream=True)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Write the content to the specified output file
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=128):
                    f.write(chunk)
            print(f"Download successful. SLD file saved at {output_path}")
        else:
            print(f"Error: Unable to download. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error during download: {e}")


def run():
    sProduct = wasdi.getParameter("PRODUCT", "CopDEM30m_wbm_Pakistan_compressed.tif")
    sLocalImagePath = wasdi.getPath(sProduct)
    wasdi.wasdiLog(sLocalImagePath)

    save_path = "elevation_map.png"
    # visualize_dem(sLocalImagePath, save_path)
    PATH = 'C:/Users/drago/AppData/Local/Temp/processing_QETCvj/139c499d069d40b6a82a6bfd8eb2c712/OUTPUT.tif'
    visualize_dem(PATH, save_path)
    # Example usage:
    base_geoserver_url = "https://creodias3.wasdi.net/geoserver"
    workspace_name = "wasdi"
    layer_name = "4827744e-6d22-4943-b83b-7209acc7504a"
    output_sld_path = "style-waterDepth.sld"

    # download_sld_from_geoserver(base_geoserver_url, workspace_name, layer_name, output_sld_path)
    # visualize_raster()


if __name__ == "__main__":
    wasdi.init('./config.json')
    run()
