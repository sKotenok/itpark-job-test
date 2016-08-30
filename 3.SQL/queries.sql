/*
Есть таблица phones с полями: phone - varchar users - int[]

Есть вторая таблица items id - serial user_id - int status - smallint (3 - не продан, 7 - продан, 5 - резерв)
*/

CREATE TABLE phones (
    id serial PRIMARY KEY,
    phone varchar(20),
    users integer[],
);

CREATE TABLE items (
    id serial PRIMARY KEY,
    user_id integer,
    status smallint
);

--- 1. Надо написать запрос который на заданные телефоны возвращает количество проданных вещей.
--- Ответ вида: 7924445544 | 5 8985545444 | 0
SELECT p.phone, count(i.status)
FROM phones p, unnest(p.users) pu_id
LEFT JOIN items i ON i.user_id = pu_id
WHERE i.status=7 AND p.phone IN $phones
GROUP BY p.phone


--- 2. Который возвращает в одном запросе количество и проданных и непроданных.
-- Если нужно именно со статусом "не продан"
SELECT status, count(*)
FROM items
WHERE status IN (3,7)
GROUP BY status

-- Если нужно отдельно сложить по всем статусам, которые означают, что товар не продан
SELECT
    sum(case when status=7 then 1 else 0 end) as selled
    sum(case when status<>7 then 1 else 0 end) as not_selled
FROM items
