import zipfile
from io import BytesIO
import requests
import os
import time


class DownloaderOfImages:

    def __init__(self):
        self.IP = "http://18.230.207.46:8080"
        self.BASE_URL = "//api/projects"
        self.URL = self.IP + self.BASE_URL

    # Assistant method to export the images of labelImage
    #
    #
    # project_number is the folder id in the labelImage
    # export_type is the type of file that the classification will be exported
    # initial_image_id is the id of the first image of the folder
    # final_image_id is the id of the last image of the folder
    def get_all_images(self, project_number, export_type, initial_image_id, final_image_id, name_main_folder):
        aux_id = initial_image_id

        for i in range(initial_image_id, final_image_id + 1):
            time.sleep(7)
            print("Executando a imagem...", i)
            self.get_image(project_number, export_type, aux_id, name_main_folder)
            aux_id += 1

    def get_image(self, project_number, export_type, image_id, name_main_folder):
        params = 'exportType={}&ids[]={}'.format(export_type, image_id)
        complete_url = '{}/{}/export?{}'.format(self.URL, project_number, params)
        complete_name_of_folder = './images/{}'.format(name_main_folder)

        self.download_zip(complete_url, complete_name_of_folder)

    def download_zip(self, url, folder_name):
        # Create a folder to store the files
        os.makedirs(folder_name, exist_ok=True)

        response = requests.get(url, headers={"Authorization": "Token 945a349a475449190cd61314a08d2eacc588841b"})

        file_bytes = BytesIO(response.content)
        zip_file = zipfile.ZipFile(file_bytes)
        zip_file.extractall(folder_name)
