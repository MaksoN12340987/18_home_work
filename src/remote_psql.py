import psycopg2 # type: ignore
from src.abstract_sql import AbstractSQL
import logging

logger_remote_data_base = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_remote_data_base.addHandler(file_handler)
logger_remote_data_base.setLevel(logging.INFO)



# Conect to DB
class PostgreSQLremoteDataBase(AbstractSQL):
    port: str = ("5432",)
    user: str = "postgres"
    host: str = "localhost"
    password: str = "12345"
    database: str = "postgres"

    def __init__(self, port, user, password, host, database) -> None:
        super().__init__()
        self.__port = (port,)
        self.__user = (user,)
        self.__password = (password,)
        self.__host = (host,)
        self.__database = database

    def query_filling_tables_with_data(self, query_content: str = "", data: list[list] = [[]]) -> str:
        """Метод создания, отправки запроса на заполнение данными таблиц 
        Передайте только название таблици и ее столбцов, метод сомтавит запрос формата:
        "INSERT INTO {_ВАШ_ЗАПРОС_} VALUES ...."
        И передайте список списков на заполнение

        Args:
            query_content (str, optional): ваш запрс, только название таблици и ее столбцов. Defaults to "".
            data (list[list], optional): _description_. Defaults to [[]].

        Returns:
            _str_: 
        """
        if not query_content:
            query_content = f"SELECT * FROM {self.__user};"
        result = []

        try:
            with psycopg2.connect(
                self.__host, self.__port, self.__database, self.__user, self.__password
            ) as connection:
                with connection.cursor() as cursor:
                    for customer in data:
                        cursor.execute(f"INSERT INTO {query_content} VALUES ({", ".join(["%s"] * len(customer))} RETURNING *", customer)
                    result = str(cursor.fetchall())

            connection.commit()
        
        except psycopg2.InternalError as error:
            print("""ERROR: Таблица не найдена или уже существует,
            Синтаксическая ошибка в SQL-запросе
            Неправильное количество заданных параметров""")
            logger_remote_data_base.warning(error)
        
        except psycopg2.ProgrammingError as error:
            print("""ERROR: Таблица не найдена или уже существует,
            синтаксическая ошибка в SQL-запросе,
            неправильное количество заданных параметров""")
            logger_remote_data_base.warning(error)
        
        except psycopg2.Error as error:
            print(f"ERROR: Хм, исключительная ошибка {error}")
            logger_remote_data_base.warning(error)
        
        finally:
            cursor.close()
            connection.close()

        return result

    def create_table_query(self, query_content: str = ""):
        pass
