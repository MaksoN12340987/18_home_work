import logging
import re

from src.filtering_vacancies import FilteringVacancies
from src.get_api_hh import HH
from src.saver import VacanciSaver
from src.vacancies import VacanciOperator

logger_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main():
    logger_main.info("Get started main")
    triger = True

    # Входные данные
    api_src = "https://api.hh.ru/vacancies"
    # Куда сохранить список вакансий, полученных из апи
    save_to_file = "data/vacancies_hh.json"
    # Куда сохранить список отсортированных и отфильтрованных вакансий
    save_to_file_sort = "data/selected_vacancies_hh.json"

    pattern = re.compile(r"[.,?]")

    while triger:

        user_choice = re.sub(
            pattern,
            "",
            (
                input(
                    "Привет! Добро пожаловать в программу подбора вакансий\n"
                    + """Выберите необходимый пункт меню:
    1. Запросить список вакансий по ключевому слову
    2. Выйти

    Введите номер варианта: """
                )
            ),
        ).lower()

        if user_choice == "1":
            find_word = re.sub(pattern, "", input("Введите слово, по которому я подберу вакансии: ")).lower()
            item_hh = HH(api_src, find_word)
            vacancies_hh = item_hh.load_vacancies
            # vacancies_hh = [{"": ""}]

            if vacancies_hh != []:
                print(f"\nУспешно получили список вакансий, сохраню их:\n{save_to_file}\n")
                vacancies = VacanciSaver("data/vacancies_hh.json")
                # vacancies.save_vacancy(vacancies_hh)

                to_sort = re.sub(
                    pattern,
                    "",
                    (
                        input(
                            """Если желаете отсортировать по убываню или по возврастанию, то
                введите соответствующее слово или нажмите продолжть:\n"""
                        )
                    ),
                ).lower()
                logger_main.info(f"{to_sort}")

                to_filtring = re.sub(
                    pattern,
                    "",
                    (
                        input(
                            """             Если желаете отфильтровать по типу занятости, то
                введите параметр в точности:
                - Частичная занятость
                - Проектная работа
                - Полная занятость
                - Вахта
                - Гибрид
                - Удалённо
                - Разъездной
                - На месте работодателя
                или нажмите продолжть:\n"""
                        )
                    ),
                )
                logger_main.info(f"{to_filtring}")

                to_filtring_vacanci = FilteringVacancies(vacancies.load_vacancy())
                sorted_vacanci = []

                if to_filtring in ["Полная занятость", "Частичная занятость", "Проектная работа", "Вахта"]:
                    to_filtring_vacanci = FilteringVacancies(vacancies.load_vacancy())
                    sorted_vacanci = to_filtring_vacanci.sorting_vacancies_for_salary(
                        triger=False, parameter="employment", filters=to_filtring
                    )
                    logger_main.info(f"{to_filtring}")
                else:
                    to_filtring_vacanci = FilteringVacancies(vacancies.load_vacancy())
                    sorted_vacanci = to_filtring_vacanci.sorting_vacancies_for_salary(
                        triger=False, parameter="work_format", filters=to_filtring
                    )
                    logger_main.info(f"{to_filtring}")

                to_sorted_vacanci = VacanciOperator(sorted_vacanci)

                if to_sort == "убываню":
                    sorted_vacanci = to_sorted_vacanci.sorting_vacancies_for_salary(True)
                    print(to_sorted_vacanci)
                    logger_main.info("убываню")

                elif to_sort == "возврастанию":
                    sorted_vacanci = to_sorted_vacanci.sorting_vacancies_for_salary(False)
                    print(to_sorted_vacanci)
                    logger_main.info("возврастанию")

                else:
                    print(to_filtring_vacanci)

            result = VacanciSaver(save_to_file_sort)
            result.save_vacancy(sorted_vacanci)
            print("\nВозвращаюсь в главное меню\n")

        elif user_choice == "2":
            print("До следующей встречи)")
            triger = False
        else:
            print("Хм, кажется такого варианта у меня пока нет(")

    logger_main.info("End main")


if __name__ == "__main__":
    main()
