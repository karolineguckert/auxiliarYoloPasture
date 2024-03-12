import os


class LabelChanger:
    def __init__(self):
        self.ROOT_PATH = './images_to_train'
        self.OLD_VALUES = [1, 2, 3, 6, 7, 8, 9, 10]  # BIG_BUSH, SMALL_BUSH, TREE, NARROW_LEAVES, WIDE_LEAVES, WEED,
        # PALM_TREE, PASTURE


    def change_bounding_box(self):
        labels_folder_path = '{}/labels'.format(self.ROOT_PATH)
        labels_list = os.listdir(labels_folder_path)

        for label in labels_list:
            label_path = '{}/{}'.format(labels_folder_path, label)
            content = self.__get_label_lines(label_path)

            self.__write_to_file(label_path, content)

    def __get_label_lines(self, label_path):
        file = open(label_path, "r")
        content = file.readlines()

        file.close()

        return content

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
