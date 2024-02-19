from src.downloader.DownloaderOfImages import DownloaderOfImages
from src.enums.Projects import Project


class MenuDownload:
    def __init__(self):
        self.CANCELED = None
        self.YES = "Y"
        self.OPTIONS = [
            "CAMPO_2_CIMA",
            "CAMPO_2_SUBIDA",
            "IMAGENS_SUBIDA_CAMPO_1_V",
            "CAMPO_1_SUBIDA",
            "IMAGENS_CIMA_CAMPO_1_V",
            "CAMPO_1_CIMA",
            "IMAGENS_V",
            "CAMPO_4_SUBIDA",
            "CAMPO_4_CIMA"
        ]

    def __create_options(self):
        menu_options = "";
        for i in range(len(self.OPTIONS)):
            menu_options += "\n[{}] {}".format(i + 1, self.OPTIONS[i])

        return menu_options

    def __create_menu_download(self):
        menu = "---- CHOOSE WHICH PROJECT DO YOU WANT TO DOWNLOAD ----\n"
        menu += self.__create_options()
        print(menu)

        option_answer = input("->  ")
        confirmation_answer = input("Do you want to continue? [Y/n]")

        if confirmation_answer.upper() == self.YES:
            option_name = self.OPTIONS[int(option_answer) - 1]
            return Project.get_project(option_name)

        return self.CANCELED

    def download_one_folder_by_user(self):
        project = self.__create_menu_download()

        if project is not None:
            project_number = project[0]
            initial_image_id = project[1]
            final_image_id = project[2]
            name_main_folder = project[3]

            DownloaderOfImages().get_all_images(project_number, "YOLO", initial_image_id, final_image_id,
                                                name_main_folder)

    def __download_one_folder(self, project):
        if project is not None:
            project_number = project[0]
            initial_image_id = project[1]
            final_image_id = project[2]
            name_main_folder = project[3]

            DownloaderOfImages().get_all_images(project_number, "YOLO", initial_image_id, final_image_id,
                                                name_main_folder)

    def __get_project_by_option_answer(self, option_answer):
        option_name = self.OPTIONS[int(option_answer) - 1]
        return Project.get_project(option_name)

    def download_all_folders(self):
        for i in range(1, len(self.OPTIONS) + 1):
            project = self.__get_project_by_option_answer(i)
            self.__download_one_folder(project)
