from enums.Projects import Project


class Menu:
    CANCELED = None
    YES = "Y"
    OPTIONS = [
        "CAMPO_2_CIMA",
        "CAMPO_2_SUBIDA",
        "IMAGENS_SUBIDA_CAMPO_1_V",
        "CAMPO_1_SUBIDA",
        "IMAGENS_CIMA_CAMPO_1_V",
        "CAMPO_1_CIMA",
        "IMAGENS_V",
        "CAMPO_4_SUBIDA",
        "CAMPO_4_CIMA"
    ]

    def _create_options(self):
        menuOptions = "";
        for i in range(len(self.OPTIONS)):
            menuOptions += "\n[{}] {}".format(i + 1, self.OPTIONS[i])

        return menuOptions

    def create_menu_download(self):
        menu = "---- CHOOSE WHICH PROJECT DO YOU WANT TO DOWNLOAD ----\n"
        menu += self._create_options()
        print(menu)

        option_answer = input("->  ")
        confirmation_answer = input("Do you want to continue? [Y/n]")

        if confirmation_answer.upper() == self.YES:
            option_name = self.OPTIONS[int(option_answer) - 1]
            return Project.get_project(option_name)

        return self.CANCELED
