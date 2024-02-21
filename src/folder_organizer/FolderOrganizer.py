import os


class FolderOrganizer:
    def __init__(self):
        self.ROOT_PATH = './images'

    def move_images(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)
