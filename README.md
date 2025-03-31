# Coursework_OOP_Andrianov_M_S
# Крсовой проект "введение в Object Oriented Programming"



## Запуск проекта
Запустите следующую команду в терминале, находясь в корневой дирректории проекта, чтобы увидеть результат работы всех функций:
```
python .\__main__.py
```

### Требование для запуска:
- python - v3.13
- poetry >=2.0.0
- requests >=2.32.3
Для обновления зависимостей необходимо запустить в терминале:
```
poetry update
```


## Модуль main
При запуске, из корневой папки проекта, будет запущена программа, в ней продемонстрированна работа всех методов



## Пакет src:
В пакете присутствуют следующие модули:
- get api hh
- saver
- vacancies
- filtering vacancies

#### Модуль get api hh:

Имеет класс HH, он может получать список вакансий из апи hh.ru (Или другого апи hh, ссылка передаётся в класс при создании)
Каласс HH имеент несколько матодов:
1. __init__ инициализирует переданные данные, создаёт атрибуты класса
    - self.__url приватный атрибут, который содержит ссылку на апи
    - self.__vacancies приватный арибут, список для добавления вакансий
    - self.__headers атрибут типа dict, необходим для создания get запроса
    - self.__params атрибут типа dict, содержит ключевое слово для поиска, необходим для создания get запроса

2. __str__
Метод срабатывает при:
print(object_hh)
Выводит строку с ссылкой на апи, заголовком и параметрами

3. load_vacancies
Метод возвращяет данные виде списка словарей вакансий из апи hh.ru
Использует атрибуты класса в качестве аргументов

#### Модуль vacancies:

Имеет класс VacanciOperator
На вход принимает список с вакансиями
Возвращает отсортированный список или строку

Класс сортировки вакансий включает в себя следующие методы:
1. __init__
Инициализирует входные данные, а так-же валидирует входные данные, при отсутствии атрибуты остаются пусты

2. __call__
Возвращает список вакансий при вызове объекта VacanciOperator

3. vacancy_job_title - метод возвращает название вакансии по её порядковому номеру
4. vacancy_link_to_vacancy - метод возвращает ссылку на вакансию по её порядковому номеру
5. vacancy_salary - метод возвращает зарплату по порядковому номеру вакансии
6. vacancy_job_requirements - метод возвращает требования к соискателю по порядковому номеру вакансии

7. sorting_vacancies_for_salary
Метод сортировки списка вакансий по зарплате
Принимает параметр типа bool - управляет направление сортировки
    - True по умолчанию, от большего к меньшему



## Тестирование 
Для запуска тестов потребуется:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Далее в терминале нужно запустить команду:
```
pytest
```


******************************************************************************************************************

# Coursework on "introduction to Object Oriented Programming"

## Launching the project
Run the following command in the terminal, being in the root directory of the project, to see the result of all functions:
```
python .\__main__.py
```

### Requirement for launching:
- python - v3.13
- poetry >=2.0.0
- requests >=2.32.3
To update dependencies, you need to run in the terminal:
```
poetry update
```

## Module main
When launched, from the root folder of the project, the program will be launched, it demonstrates the operation of all methods

## Package src:
The package contains the following modules:
- get api hh
- saver
- vacancies
- filtering vacancies

#### Module get api hh:

Has the HH class, it can get a list of vacancies from the hh.ru api (Or another hh api, the link is passed to the class when created)
The HH class has several methods:
1. __init__ initializes the transferred data, creates class attributes
- self.__url private attribute that contains a link to the api
- self.__vacancies private attribute, a list for adding vacancies
- self.__headers attribute of type dict, necessary for creating a get request
- self.__params attribute of type dict, contains a keyword for searching, necessary for creating a get request

2. __str__
The method is triggered when:
print(object_hh)
Outputs a string with a link to the api, header and parameters

3. load_vacancies
The method returns data as a list of vacancy dictionaries from the hh.ru api
Uses class attributes as arguments

#### Vacancies module:

Has a class VacanciOperator
It takes a list as input with vacancies
Returns a sorted list or string

The vacancy sorting class includes the following methods:

1. __init__
Initializes the input data, and also validates the input data, if absent, the attributes remain empty

2. __call__
Returns a list of vacancies when calling the VacanciOperator object

3. vacancy_job_title - the method returns the name of the vacancy by its serial number
4. vacancy_link_to_vacancy - the method returns a link to the vacancy by its serial number
5. vacancy_salary - the method returns the salary by the serial number of the vacancy
6. vacancy_job_requirements - the method returns the requirements for the applicant by the serial number of the vacancy

7. sorting_vacancies_for_salary
Method for sorting the list of vacancies by salary
Accepts bool parameter - controls the sorting direction
- True by default, from largest to smallest

## Testing
To run the tests you will need:
pytest = "^8.3.4"
pytest-cov = "^6.0.0"

Then in the terminal you need to run the command:
```
pytest
```