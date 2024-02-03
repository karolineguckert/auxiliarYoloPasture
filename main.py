import gzip
import zipfile
from io import BytesIO

import requests
import os

from gzip import GzipFile

class Request:

    def __init__(self):
        self.IP = "http://18.230.207.46:8080"
        self.BASE_URL = "//api/projects"
        self.URL = self.IP + self.BASE_URL

    # Assistant method to export the images of labelImage
    #
    #
    # project_number is the folder id in the labelImage
    # export_type is the type of file that the classification will be exported
    # initial_id is the id of the first image of the folder
    # final_id is the id of the last image of the folder
    def get_image(self, project_number, export_type, initial_id, final_id):
        params = 'exportType={}&ids[]={}'.format(export_type, initial_id)
        complete_url = '{}/{}/export?{}'.format(self.URL, project_number, params)
        self.download_zip(complete_url, "./teste")

    def download_zip(self, url, folder_name):
        # Criar um diretorio para armazenar o conteúdo
        os.makedirs(folder_name, exist_ok=True)

        response = requests.get(url, headers={"Authorization": "Token 945a349a475449190cd61314a08d2eacc588841b"})

        file_bytes = BytesIO(response.content)
        zip_file = zipfile.ZipFile(file_bytes)
        print(zip_file.filelist)
        # zip_file.extractall(folder_name)


if __name__ == '__main__':
    Request().get_image(3,"YOLO", 1, 2)