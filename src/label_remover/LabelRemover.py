import os


class LabelRemover:
    def __init__(self):
        self.ROOT_PATH = './images'
        self.WATER = 0
        self.BANANA_TREE = 4
        self.TERMITE = 5
        self.EXPOSED_SOIL = 11

    def remove_empty_file_label(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)
                content = self.__get_label_content(label_path)

                is_file_empty = len(content) == 0

                if is_file_empty:
                    os.remove(label_path)

    def remove_invalid_bounding_box(self):
        file_list = os.listdir(self.ROOT_PATH)

        for file in file_list:
            labels_folder_path = '{}/{}/labels'.format(self.ROOT_PATH, file)
            labels_list = os.listdir(labels_folder_path)

            for label in labels_list:
                label_path = '{}/{}'.format(labels_folder_path, label)
                content = self.__get_label_lines(label_path)

                self.__write_to_file(label_path, content)
                print(label_path)

    def __get_label_lines(self, label_path):
        file = open(label_path, "r")
        content = file.readlines()

        file.close()

        return content

    def __get_label_content(self, label_path):
        file = open(label_path, "r")
        content = file.read()
        file.close()

        return content

    def __write_to_file(self, label_path, content):
        file = open(label_path, "w+")

        for line in content:
            lines_divided = line.split(" ")
            label_type = int(lines_divided[0])

            if label_type != self.WATER and label_type != self.BANANA_TREE and label_type != self.TERMITE and label_type != self.EXPOSED_SOIL:
                file.write(line)
