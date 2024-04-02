from enum import Enum


class ProjectsFields(Enum):
    project_number: int
    initial_image_id: int
    final_image_id: int
    name_main_folder: str


class Project(ProjectsFields, Enum):
    CAMPO_2_CIMA = 3, 14, 20, "CAMPO_2_CIMA"
    # CAMPO_2_SUBIDA = 11, 293, 337, "CAMPO_2_SUBIDA"
    # IMAGENS_SUBIDA_CAMPO_1_V = 10, 251, 290, "IMAGENS_SUBIDA_CAMPO_1_V"
    # CAMPO_1_SUBIDA = 9, 172, 249, "CAMPO_1_SUBIDA"
    IMAGENS_CIMA_CAMPO_1_V = 5, 25, 37, "IMAGENS_CIMA_CAMPO_1_V"
    CAMPO_1_CIMA = 2, 1, 13, "CAMPO_1_CIMA"
    IMAGENS_V = 6, 38, 40, "IMAGENS_V"
    # CAMPO_4_SUBIDA = 4, 20, 86, "CAMPO_4_SUBIDA"
    CAMPO_4_CIMA = 4, 21, 24, "CAMPO_4_CIMA"

    @classmethod
    def get_project(self, name):
        project = []

        project_number = Project[name].value[0]
        initial_image_id = Project[name].value[1]
        final_image_id = Project[name].value[2]
        name_main_folder = Project[name].value[3]

        project.append(project_number)
        project.append(initial_image_id)
        project.append(final_image_id)
        project.append(name_main_folder)

        return project
