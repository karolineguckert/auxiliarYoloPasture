import os


class LabelChanger:
    def __init__(self, root_path):
        self.ROOT_PATH = root_path
        self.OLD_VALUES = [1, 2, 3, 6, 7, 8, 9, 10]  # BIG_BUSH, SMALL_BUSH, TREE, NARROW_LEAVES, WIDE_LEAVES, WEED,
        # PALM_TREE, PASTURE

    # Assistant method to change de type of the bounding box from images in the multiples folders
    #
    def change_bounding_boxes(self):
        folder_list = os.listdir(self.ROOT_PATH)

        for file_name in folder_list:
            file_path = "/{}".format(file_name)
            self.change_bounding_box(file_path)

    # Assistant method to change de type of the bounding box from images in the same folder
    #
    # folder_path is the value of a sub-folder and can be nullable
    def change_bounding_box(self, folder_path=""):
        labels_folder_path = '{}/labels'.format(self.ROOT_PATH + folder_path)
        labels_list = os.listdir(labels_folder_path)

        for label in labels_list:
            label_path = '{}/{}'.format(labels_folder_path, label)
            content = self.__get_label_lines(label_path)

            self.__write_to_file(label_path, content)

    # Assistant method to get all lines from file with classifications
    #
    # label_path is the path of the label
    def __get_label_lines(self, label_path):
        file = open(label_path, "r")
        content = file.readlines()

        file.close()

        return content

    # Assistant method to write values in the file with classifications
    #
    # label_path is the path of the label
    # content is the values written in the file classifications
    def __write_to_file(self, label_path, content):
        file = open(label_path, "w+")

        for line in content:
            lines_divided = line.split(" ")
            label_type = int(lines_divided[0])

            try:
                index = self.OLD_VALUES.index(label_type)
                lines_divided[0] = str(index)
                changed_line = " ".join(lines_divided)
                file.write(changed_line)
            except ValueError:
                file.write(line)
                continue
