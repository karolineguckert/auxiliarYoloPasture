import zipfile
from io import BytesIO
import requests
import os
import time


class DownloaderOfImages:

    def __init__(self, ip, port, token):
        self.URL = "http://{}:{}//api/projects".format(ip, port)
        self.TOKEN = token

    # Assistant method to export the images of labelStudio
    #
    #
    # project_number is the folder id in the labelImage
    # export_type is the type of file that the classification will be exported
    # initial_image_id is the id of the first image of the folder
    # final_image_id is the id of the last image of the folder
    def get_all_images(self, project_number, export_type, initial_image_id, final_image_id, name_main_folder):
        print("\nBeginning downloads {}...\n".format(name_main_folder))
        aux_id = initial_image_id

        for i in range(initial_image_id, final_image_id + 1):
            time.sleep(7)
            print("Executing the image...", i)
            self._get_image(project_number, export_type, aux_id, name_main_folder)
            aux_id += 1

    # Assistant method to get one image from the LabelStudio
    #
    #
    # project_number is the folder id in the labelImage
    # export_type is the type of file that the classification will be exported
    # image_id is the id of the image of the folder
    # name_main_folder is the name of principal folder
    def _get_image(self, project_number, export_type, image_id, name_main_folder):
        params = 'exportType={}&ids[]={}'.format(export_type, image_id)
        complete_url = '{}/{}/export?{}&download_all_tasks=true'.format(self.URL, project_number, params)
        complete_name_of_folder = './images/{}'.format(name_main_folder)

        self._download_zip(complete_url, complete_name_of_folder)

    # Assistant method to download the zip file from the LabelStudio
    #
    #
    # url is the complete route to request images
    # folder_name is the name of the folder where the zip will be downloaded
    def _download_zip(self, url, folder_name):
        # Create a folder to store the files
        os.makedirs(folder_name, exist_ok=True)

        response = requests.get(url, headers={"Authorization": "Token {}".format(self.TOKEN)})

        file_bytes = BytesIO(response.content)
        zip_file = zipfile.ZipFile(file_bytes)
        zip_file.extractall(folder_name)
