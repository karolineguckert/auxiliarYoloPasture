from DownloaderOfImages import DownloaderOfImages
from menu.Menu import Menu

if __name__ == '__main__':
    project = Menu().create_menu_download()

    if project is not None:
        project_number = project[0]
        initial_image_id = project[1]
        final_image_id = project[2]
        name_main_folder = project[3]

        DownloaderOfImages().get_all_images(project_number,"YOLO", initial_image_id, final_image_id, name_main_folder)