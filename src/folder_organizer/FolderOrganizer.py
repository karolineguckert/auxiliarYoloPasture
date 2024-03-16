import os
import shutil


class FolderOrganizer:
    def __init__(self):
        self.ROOT_PATH = './images'

    # Assistant method to move images with label to a new folder
    #
    def move_images_to_train(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            images_folder_path = '{}/{}/images'.format(self.ROOT_PATH, file)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)

                image_name = label.replace(".txt", ".jpg")
                image_path = '{}/{}'.format(images_folder_path, image_name)

                shutil.move(label_path, 'images_to_train/labels/{}'.format(label))
                shutil.move(image_path, 'images_to_train/images/{}'.format(image_name))

    # Assistant method to move images without label to a new folder
    #
    def move_images_to_detect(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            images_folder_path = '{}/{}/images'.format(self.ROOT_PATH, file)
            images_list = os.listdir(images_folder_path)

            for image in images_list:
                image_path = '{}/{}'.format(images_folder_path, image)
                shutil.move(image_path, 'image_to_detect/{}'.format(image))
