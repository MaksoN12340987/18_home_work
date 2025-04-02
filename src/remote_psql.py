import psycopg2
from src.abstract_sql import AbstractSQL


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
        self.password = (password,)
        self.host = (host,)
        self.database = database

    def database_query(self, query_content: str = ""):
        if not query_content:
            query_content = f"SELECT * FROM {self.__user};"
        connection = psycopg2.connect(
            host="localhost", port="5432", database="postgres", user="postgres", password="pi"
        )
        result = []

        try:
            with psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="pi") as connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"{query_content} RETURNING *")
                    result = cursor.fetchall()

            connection.commit()
        except:
            pass
        finally:
            cursor.close()
            connection.close()
        
        return result
