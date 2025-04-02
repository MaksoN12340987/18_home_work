# Подключение
<!-- Подключение к Postgres через cmd -->
```
psql -h <хост-localhost> -p <порт-5432> -d <имя_базы_данных> -U <имя_пользователя>
```

# Command
| Команда           | Описание                                                            |
|-------------------|---------------------------------------------------------------------|
| \l                | Показать список всех баз данных                                     |
| \c name_DB        | Сменить текущую базу данных                                         |
| \dt               | Показать список всех таблиц в текущей базе данных                   |
| \d name_table     | Показать структуру таблицы                                          |
| \q                | Выйти из PostgreSQL                                                 |

<!-- Создание таблиц -->
```
CREATE TABLE post
(
    post_id int PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text
);
```

### При ошибках в кодировке win+R => regedit
HKEY_LOCAL_MACHINE => SOFTWARE => Microsoft => Command Processor => create str parametr => Autorun => "chcp 1251"

# Создание
<!-- Создание второй таблицы -->
```
CREATE TABLE user_account
(
    user_id int PRIMARY KEY,
    fullname varchar(100) NOT NULL
);
```

# Заполнение
<!-- Заполнение таблицы данными последовательно по колонкам -->
```
INSERT INTO post VALUES (1, 'Happy New Year', '');
```
```
INSERT INTO post VALUES
(2, 'My plans for 2023', ''),
(3, 'Lesson learned from 2022', ''),
(4, 'NewPost!', '');
```

# Отношения
<!--  -->
```
CREATE TABLE post
(
	post_id int PRIMARY KEY,
	title varchar(100) NOT NULL,
	content text,
	author int REFERENCES table_name(<название_колонки>) NOT NULL
);
```

# Выборка
<!-- Выборка данных из таблицы -->
```
SELECT * FROM table_name
```
```
SELECT <название_колонки>, <перемножит> * <колонки> as <колонка_результата>
FROM table_name
```
### DISTINCT — оператор, который используется для выбора уникальных значений из столбца таблицы
```
SELECT DISTINCT country FROM employees;
```

## Выборка с условием
#### WHERE — оператор, который используется для фильтрации строк по определенным условиям.
```
SELECT * FROM table_name WHERE colum_name = 'France';
```

#### BETWEEN — оператор, который используется для выбора строк, где значение столбца находится между двумя заданными значениями.
```
SELECT * FROM products
WHERE unit_price BETWEEN 30 AND 50;
```

#### IN и NOT IN — операторы, которые используются для выбора строк, где значение столбца равно одному из нескольких заданных значений.
```
SELECT * FROM orders
WHERE ship_country IN ('France', 'Germany');
```

https://github.com/pthom/northwind_psql/blob/master/northwind.sql
