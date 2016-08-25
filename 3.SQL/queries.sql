/*
Есть таблица phones с полями: phone - varchar users - int[]

Есть вторая таблица items id - serial user_id - int status - smallint (3 - не продан, 7 - продан, 5 - резерв)
*/


CREATE TABLE users (
    id serial
);

CREATE TABLE phones (
    phone varchar(20),
    users integer[],
);

CREATE TABLE items (
    id serial,
    user_id integer,
    status smallint
);

--- 1. Надо написать запрос который на заданные телефоны возвращает количество проданных вещей.
--- Ответ вида: 7924445544 | 5 8985545444 | 0


--- 2. Который возвращает в одном запросе количество и проданных и непроданных.

