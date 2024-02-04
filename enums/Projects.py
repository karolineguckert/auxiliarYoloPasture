from enum import Enum


class ProjectsFields(Enum):
    project_number: int
    initial_image_id: int
    final_image_id: int
    name_main_folder: str


class Project(ProjectsFields, Enum):
    CAMPO_2_CIMA = 12, 338, 394, "CAMPO_2_CIMA"
    CAMPO_2_SUBIDA = 11, 293, 337, "CAMPO_2_SUBIDA"
    IMAGENS_SUBIDA_CAMPO_1_V = 10, 251, 290, "IMAGENS_SUBIDA_CAMPO_1_V"
    CAMPO_1_SUBIDA = 9, 172, 249, "CAMPO_1_SUBIDA"
    IMAGENS_CIMA_CAMPO_1_V = 8, 142, 171, "IMAGENS_CIMA_CAMPO_1_V"
    CAMPO_1_CIMA = 7, 97, 141, "CAMPO_1_CIMA"
    IMAGENS_V = 5, 87, 96, "IMAGENS_V"
    CAMPO_4_SUBIDA = 4, 20, 86, "CAMPO_4_SUBIDA"
    CAMPO_4_CIMA = 3, 1, 19, "CAMPO_4_CIMA"
