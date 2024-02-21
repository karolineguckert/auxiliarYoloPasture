import os


class LabelRemover:
    def __init__(self):
        self.ROOT_PATH = './images'

    def remove_empty_file_label(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)
                file = open(label_path, "r")
                content = file.read()

                is_file_empty = len(content) == 0
                file.close()

                if is_file_empty:
                    os.remove(label_path)


    def remove_invalid_bounding_box(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)
                file = open(label_path, "w+")
                content = file.read()
                file.close()


