from src.downloader.MenuDownload import MenuDownload
from src.label_changer.LabelChanger import LabelChanger
from src.label_remover.LabelRemover import LabelRemover
from src.folder_organizer.FolderOrganizer import FolderOrganizer


if __name__ == '__main__':
    # MenuDownload().download_all_folders()
    # MenuDownload().download_one_folder_by_user()
    # LabelRemover().remove_invalid_bounding_box()
    # LabelRemover().remove_empty_file_label()
    # FolderOrganizer().move_images_to_train()
    # FolderOrganizer().move_images_to_detect()
    LabelChanger().change_bounding_box()
