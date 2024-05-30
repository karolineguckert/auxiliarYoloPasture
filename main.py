from src.downloader.MenuDownload import MenuDownload
from src.label_changer.LabelChanger import LabelChanger
from src.label_remover.LabelRemover import LabelRemover
from src.folder_organizer.FolderOrganizer import FolderOrganizer


if __name__ == '__main__':
    # MenuDownload("209.172.7.22","8080", "9b63bc5ffdf0358d2ac67918080a9756874abf50").download_all_folders()
    # MenuDownload("209.172.7.22","8080", "9b63bc5ffdf0358d2ac67918080a9756874abf50").download_one_folder_by_user()
    # LabelRemover().remove_invalid_bounding_box()
    # LabelRemover().remove_empty_file_label()
    # FolderOrganizer().move_images_to_train()
    # FolderOrganizer().move_images_to_detect()
    # LabelChanger("./images_to_train").change_bounding_box()
    LabelChanger("./images").change_bounding_box()
    # LabelRemover().remove_invalid_bounding_box_not_exposed_soil_and_terminate()
    # LabelRemover().remove_invalid_bounding_box_not_pasture()
    # LabelRemover().remove_invalid_bounding_box_of_small_and_big_brush()
