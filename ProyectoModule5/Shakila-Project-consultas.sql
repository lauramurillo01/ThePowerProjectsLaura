-- 1. Crea el esquema de la BBDD.


-- 2. Muestra los nombres de todas las películas con una clasificación por edades de ‘R’.

select title, rating
from film
where rating = 'R';

-- 3. Encuentra los nombres de los actores que tengan un “actor_id” entre 30 y 40.

select first_name, last_name  
from actor
where actor_id between 30 and 40;

-- 4. Obtén las películas cuyo idioma coincide con el idioma original.

select title 
from film
where language_id = original_language_id;
-- como no me ha aparecido ningun resultado, al comprobar los valores de cada columna he visto que original_language_id siempre es NULL
select title, language_id, original_language_id 
from film;

-- 5. Ordena las películas por duración de forma ascendente.

select title, length
from film 
order by length asc; 

-- 6. Encuentra el nombre y apellido de los actores que tengan ‘Allen’ en su apellido.

select first_name, last_name
from actor 
WHERE last_name like '%ALLEN%';

-- 7. Encuentra la cantidad total de películas en cada clasificación de la tabla “film” y muestra la clasificación junto con el recuento.

select rating, COUNT(*) AS total_peliculas
from  film 
group by rating 
order by rating; --Ordenamos alfabéticamente 

-- 8. Encuentra el título de todas las películas que son ‘PG-13’ o tienen una duración mayor a 3 horas en la tabla film.

select title, rating, length
from film 
where rating = 'PG-13' or length > 180; --since length seems to be in min 3 hours = 180 min


-- 9. Encuentra la variabilidad de lo que costaría reemplazar las películas.

select variance(replacement_cost) as var_costo_remplazo
from film;

-- 10. Encuentra la mayor y menor duración de una película de nuestra BBDD.

select max(length) as max_duration, 
	   min(length) as min_duration
from film;

-- 11. Encuentra lo que costó el antepenúltimo alquiler ordenado por día.

select r.rental_id, r.rental_date, p.amount 
from rental r
join payment p on r.rental_id = p.rental_id
order by r.rental_date desc
offset 2 limit 1;

-- 12. Encuentra el título de las películas en la tabla “film” que no sean ni ‘NC17’ ni ‘G’ en cuanto a su clasificación.

select title, rating
from film f
where rating not in ('NC-17', 'G');

-- 13. Encuentra el promedio de duración de las películas para cada clasificación de la tabla film 
--     y muestra la clasificación junto con el promedio de duración.

select rating, avg(length) as promedio_duration
from film 
group by rating
order by rating;

-- 14. Encuentra el título de todas las películas que tengan una duración mayor a 180 minutos.

select title 
from film f
where length > 180;

-- 15. ¿Cuánto dinero ha generado en total la empresa?

select sum(amount) as total_generado
from payment;

-- 16. Muestra los 10 clientes con mayor valor de id.

select customer_id, first_name, last_name
from customer c 
order by c.customer_id desc
limit 10;

-- 17. Encuentra el nombre y apellido de los actores que aparecen en la película con título ‘Egg Igby’.

select first_name, last_name
from actor a 
where a.actor_id in(
	select fa.actor_id
	from film_actor fa 
	join film f on fa.film_id = f.film_id 
	where f.title = 'Egg Igby'
);

-- 18. Selecciona todos los nombres de las películas únicos.

select distinct title
from film;

-- 19. Encuentra el título de las películas que son comedias y tienen una duración mayor a 180 minutos en la tabla “film”.

select title 
from film f
join film_category fc on f.film_id = fc.film_id -- join con la tabla film_category donde coincide el id de la película
join category c on fc.category_id = c.category_id -- join con tabla category donde coincide el id de categoria
where c.name = 'Comedy' and f.length > 180; -- category comedy and length mayor a 180 min

-- 20. Encuentra las categorías de películas que tienen un promedio de duración superior a 110 minutos y muestra el nombre de la categoría junto con el promedio de duración.

select c.name, avg(f.length) as promedio_duration
from category c 
join film_category fc on c.category_id = fc.category_id
join film f on fc.film_id = f.film_id
group by c.name -- agrupamos por categoría
having AVG(f.length) > 110; -- filtrando solo las categorías cuyo promedio supere 110 minutos

-- 21. ¿Cuál es la media de duración del alquiler de las películas?

select avg(rental_duration) as media_duracion_rental
from film;

-- 22. Crea una columna con el nombre y apellidos de todos los actores y actrices.

select concat(first_name, ' ', last_name) as nombre_completo
from actor;

-- 23. Números de alquiler por día, ordenados por cantidad de alquiler de forma descendente.

select date(rental_date) as day, count(*) as total_rentals
from rental
group by day
order by total_rentals desc;

-- 24. Encuentra las películas con una duración superior al promedio.

select title, length
from film 
where length > (
	select avg(length)
	from film
);

-- 25. Averigua el número de alquileres registrados por mes.

select extract(year from rental_date) as anio, --Extraemos el año
    extract(month from rental_date) as mes, --Extraemos el mes
    count(*) as total_alquileres --Contamos los alquileres
from rental
group by extract(year from rental_date), extract(month from rental_date)
order by anio, mes;

-- 26. Encuentra el promedio, la desviación estándar y varianza del total pagado.

select avg(amount) as promedio_pagado, -- media de los importes pagados
    stddev(amount) as desviacion_estandar, -- desviación estándar del importe
    variance(amount) as varianza -- varianza del importe
from payment;

-- 27. ¿Qué películas se alquilan por encima del precio medio?

select title, rental_rate
from film 
where rental_rate  > (
	select avg(rental_rate)
	from film
);

-- 28. Muestra el id de los actores que hayan participado en más de 40 películas.

select actor_id, count(film_id) as total_peliculas
from film_actor 
group by actor_id 
having count(film_id) > 40;

-- 29. Obtener todas las películas y, si están disponibles en el inventario, mostrar la cantidad disponible.

select f.title, count(i.inventory_id) as cantidad_disponible 
from film f 
left join inventory i -- unimos con inventory, pero con LEFT JOIN
    on f.film_id = i.film_id -- para no perder películas sin copias en inventario
group by f.title -- agrupamos por título
order by f.title;

-- 30. Obtener los actores y el número de películas en las que ha actuado.

select a.first_name, a.last_name, count(fa.film_id) as total_peliculas 
from actor a 
left join film_actor fa -- unimos con film_actor con LEFT JOIN
    on a.actor_id = fa.actor_id -- para no perder actores sin películas asociadas
group by a.actor_id, a.first_name, a.last_name
order by total_peliculas desc;


-- 31. Obtener todas las películas y mostrar los actores que han actuado en ellas, incluso si algunas películas no tienen actores asociados.

select f.title, a.first_name, a.last_name 
from  film f 
left join film_actor fa on f.film_id = fa.film_id -- unimos con film_actor con LEFT JOIN
left join actor a on fa.actor_id = a.actor_id -- unimos con actor con LEFT JOIN
order by f.title;

-- 32. Obtener todos los actores y mostrar las películas en las que han actuado, incluso si algunos actores no han actuado en ninguna película.

select a.first_name, a.last_name, f.title 
from actor a 
left join film_actor fa on a.actor_id = fa.actor_id -- unimos con film_actor con LEFT JOIN
left join film f on fa.film_id = f.film_id -- unimos con film con LEFT JOIN
order by a.last_name asc;

-- 33. Obtener todas las películas que tenemos y todos los registros de alquiler.

select f.title, r.rental_id, r.rental_date
from film f 
left join inventory i on f.film_id = i.film_id -- unimos con inventory (relaciona película con copias físicas)
full join rental r on i.inventory_id = r.inventory_id -- hacemos FULL JOIN con rental para no perder ni películas sin alquileres ni alquileres sin película asociada
order by f.title asc;

-- 34. Encuentra los 5 clientes que más dinero se hayan gastado con nosotros.

select c.customer_id, c.first_name, c.last_name, sum(p.amount) as total_gastado 
from customer c 
join payment p  on c.customer_id = p.customer_id -- unida con payment
group by c.customer_id, c.first_name, c.last_name -- agrupamos por cliente
order by total_gastado desc -- ordenamos de mayor a menor gasto
limit 5; -- nos quedamos solo con los 5 primeros

-- 35. Selecciona todos los actores cuyo primer nombre es 'Johnny'.

select first_name, last_name
from actor
where first_name  = 'JOHNNY';

-- 36. Renombra la columna “first_name” como Nombre y “last_name” como Apellido.

select first_name as "Nombre", last_name as "Apellido"
from actor;

-- 37. Encuentra el ID del actor más bajo y más alto en la tabla actor.

select max(actor_id) as id_max, 
	   min(actor_id) as id_min
from actor;

-- 38. Cuenta cuántos actores hay en la tabla “actor”.

select count(*) as total_actores
from actor;

-- 39. Selecciona todos los actores y ordénalos por apellido en orden ascendente.

select first_name, last_name
from actor
order by last_name asc;

-- 40. Selecciona las primeras 5 películas de la tabla “film”.

select *
from film 
limit 5;

-- 41. Agrupa los actores por su nombre y cuenta cuántos actores tienen el mismo nombre. ¿Cuál es el nombre más repetido?

select first_name, count(*) as total_actores
from actor 
group by first_name
order by total_actores desc;
-- EL NOMBRE MÁS REPETIDO ES KENNETH (podriamos usar LIMIT 1;)

-- 42. Encuentra todos los alquileres y los nombres de los clientes que los realizaron.

select r.rental_id, r.rental_date, c.first_name, c.last_name 
from rental r 
join customer c on r.customer_id = c.customer_id--Unida con customer
order by r.rental_date;

-- 43. Muestra todos los clientes y sus alquileres si existen, incluyendo aquellos que no tienen alquileres.

select c.first_name, c.last_name, r.rental_id, r.rental_date 
from  customer c 
left join rental r on c.customer_id = r.customer_id --Unimos con rental usando LEFT JOIN para no perder clientes sin alquileres
order by c.last_name;

-- 44. Realiza un CROSS JOIN entre las tablas film y category. ¿Aporta valor esta consulta? ¿Por qué? Deja después de la consulta la contestación.

select f.title, c.name 
from film f 
cross join category c;
-- RESPUESTA: No, esta consulta NO aporta valor real. Un CROSS JOIN genera el
-- producto cartesiano entre las dos tablas (todas las películas combinadas con todas las
-- categorías), sin tener en cuenta si esa película realmente pertenece a esa categoría.
-- El resultado no representa relaciones reales, solo todas las combinaciones matemáticas posibles,
-- y con tablas grandes puede generar un número enorme de filas sin ningún significado útil.

-- 45. Encuentra los actores que han participado en películas de la categoría 'Action'.

select distinct a.first_name, a.last_name 
from actor a 
join film_actor fa ON a.actor_id = fa.actor_id -- unida con film_actor
join film_category fc on fa.film_id = fc.film_id -- unida con film_category
join category c on fc.category_id = c.category_id -- unida con category
where c.name = 'Action'; -- donde la categoría sea Action

-- 46. Encuentra todos los actores que no han participado en películas.

select a.first_name, a.last_name 
from actor a 
where not exists ( 
    select 1 -- ninguna coincidencia
    from film_actor fa -- de la tabla film_actor
    where fa.actor_id = a.actor_id -- donde coincida el id del actor
);

-- 47. Selecciona el nombre de los actores y la cantidad de películas en las que han participado.

select a.first_name, a.last_name, count(fa.film_id) as total_peliculas 
from actor a 
join film_actor fa on a.actor_id = fa.actor_id -- unida con film_actor
group by a.actor_id, a.first_name, a.last_name -- agrupamos por actor
order by total_peliculas desc;

-- 48. Crea una vista llamada “actor_num_peliculas” que muestre los nombres de los actores y el número de películas en las que han participado.

create view actor_num_peliculas as -- creamos la vista
select a.first_name, a.last_name, count(fa.film_id) as num_peliculas 
from actor a 
join film_actor fa on a.actor_id = fa.actor_id -- unida con film_actor
group by a.actor_id, a.first_name, a.last_name;

-- para consultar la vista que hemos creado:
select * 
from actor_num_peliculas
order by num_peliculas desc;

-- 49. Calcula el número total de alquileres realizados por cada cliente.

select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_alquileres 
from customer c 
join rental r on c.customer_id = r.customer_id -- unida con rental
group by c.customer_id, c.first_name, c.last_name -- agrupamos por cliente
order by total_alquileres desc;

-- 50. Calcula la duración total de las películas en la categoría 'Action'.

select sum(f.length) as duracion_total -- sumamos la duración de todas las películas de Action
from film f 
join film_category fc on f.film_id = fc.film_id -- unida con film_category
join category c on fc.category_id = c.category_id-- unida con category
where c.name = 'Action'; -- donde la categoría sea Action

-- 51. Crea una tabla temporal llamada “cliente_rentas_temporal” para almacenar el total de alquileres por cliente.

create temporary table cliente_rentas_temporal as 
select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_alquileres 
from customer c 
join rental r on c.customer_id = r.customer_id-- unida con rental
group by c.customer_id, c.first_name, c.last_name; -- agrupamos por cliente

-- para consultar la tabla temporal que hemos creado:
SELECT * 
FROM cliente_rentas_temporal
ORDER BY total_alquileres DESC;

-- 52. Crea una tabla temporal llamada “peliculas_alquiladas” que almacene las películas que han sido alquiladas al menos 10 veces.

create temporary table peliculas_alquiladas as 
select f.film_id, f.title, count(r.rental_id) as veces_alquilada 
from film f 
join inventory i -- unida con inventory (copias físicas de cada película)
    on f.film_id = i.film_id
join rental r -- unida con rental
    on i.inventory_id = r.inventory_id
group by f.film_id, f.title -- agrupamos por película
having count(r.rental_id) >= 10; -- solo las alquiladas 10 veces o más

-- Consultamos la tabla temporal recién creada:
select * 
from peliculas_alquiladas
order by veces_alquilada desc;

-- 53. Encuentra el título de las películas que han sido alquiladas por el cliente con el nombre ‘Tammy Sanders’ y que aún no se han devuelto. Ordena los resultados alfabéticamente por título de película.

select f.title --Seleccionamos el título de la película
from film f --De la tabla film
join inventory i on f.film_id = i.film_id -- unida con inventory
join rental r on i.inventory_id = r.inventory_id -- unida con rental
join customer c on r.customer_id = c.customer_id -- unida con customer
where c.first_name = 'Tammy' 
  and c.last_name = 'Sanders' 
  and r.return_date is null -- y que todavía no se haya devuelto (fecha de devolución vacía)
order by f.title asc; -- ordenamos alfabéticamente por título

-- 54. Encuentra los nombres de los actores que han actuado en al menos una película que pertenece a la categoría ‘Sci-Fi’. Ordena los resultados alfabéticamente por apellido.

select distinct a.first_name, a.last_name -- sin duplicados
from actor a 
join film_actor fa on a.actor_id = fa.actor_id
join film_category fc on  fa.film_id = fc.film_id
join category c on fc.category_id = c.category_id
where c.name = 'Sci-Fi' -- donde la categoría sea Sci-Fi
order by a.last_name; -- ordenamos alfabéticamente por apellido

-- 55. Encuentra el nombre y apellido de los actores que han actuado en películas que se alquilaron después de que la película ‘Spartacus Cheaper’ se alquilara por primera vez. Ordena los resultados alfabéticamente por apellido.

select distinct a.first_name, a.last_name
from actor a 
join film_actor fa on a.actor_id = fa.actor_id
JOIN inventory i ON fa.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
where r.rental_date > ( -- donde la fecha de alquiler sea posterior a...
    select min(r2.rental_date) -- la primera fecha en que se alquiló
    from rental r2 
    join inventory i2 on r2.inventory_id = i2.inventory_id
    join film f2 on i2.film_id = f2.film_id
    where f2.title = 'Spartacus Cheaper' -- la película 'Spartacus Cheaper'
)
order by a.last_name; -- ordenamos alfabéticamente por apellido

-- como comprobación: 
select * 
from film 
where title  = 'Spartacus Cheaper';
-- no aparece ninguna película con ese titulo

-- 56. Encuentra el nombre y apellido de los actores que no han actuado en ninguna película de la categoría ‘Music’.

select a.first_name, a.last_name
from actor a 
where not exists ( -- donde no exista
    select 1 -- ninguna coincidencia
    from film_actor fa 
    join film_category fc on fa.film_id = fc.film_id
    join category c on fc.category_id = c.category_id
    where fa.actor_id = a.actor_id -- donde coincida el id del actor
      and c.name = 'Music' -- y la categoría sea Music
);

-- 57. Encuentra el título de todas las películas que fueron alquiladas por más de 8 días.

select distinct f.title -- titulo sin duplicados
from film f
join inventory i on f.film_id = i.film_id --unida con inventory
join rental r on i.inventory_id = r.inventory_id -- unida con rental
where r.return_date is not null and (r.return_date - r.rental_date) > interval '8 days'; -- solo alquileres ya devueltos y alquiladas más de 8 dias

-- 58. Encuentra el título de todas las películas que son de la misma categoría que ‘Animation’.

select distinct f.title -- titulo sin duplicados
from film f
join film_category fc on f.film_id = fc.film_id --unida con film_category
join category c on fc.category_id = c.category_id -- unida con category
where c.name = 'Animation'; -- que tengan categoria animation

-- 59. Encuentra los nombres de las películas que tienen la misma duración que la película con el título ‘Dancing Fever’. Ordena los resultados alfabéticamente por título de película.

select title, length -- título y duración de la película
from film -- de la tabla film
where length = ( -- donde la duración sea igual a
    select length -- la duración de
    from film
    where title = 'Dancing Fever' -- la película 'Dancing Fever'
)
and title <> 'Dancing Fever' -- excluimos la propia película de la comparación
order by title; --Ordenamos alfabéticamente por título


-- 60. Encuentra los nombres de los clientes que han alquilado al menos 7 películas distintas. Ordena los resultados alfabéticamente por apellido.

select c.first_name, c.last_name, count(distinct i.film_id) as peliculas_distintas -- cliente y conteo de películas distintas
from customer c 
join rental r on c.customer_id = r.customer_id -- unida con rental
join inventory i on r.inventory_id = i.inventory_id -- unida con inventory (para llegar al film_id)
group by c.customer_id, c.first_name, c.last_name -- agrupamos por cliente
having count(distinct i.film_id) >= 7 -- solo clientes con 7 o más películas distintas alquiladas
order by c.last_name asc; -- ordenamos alfabéticamente por apellido

-- 61. Encuentra la cantidad total de películas alquiladas por categoría y muestra el nombre de la categoría junto con el recuento de alquileres.

select c.name, count(r.rental_id) as total_alquileres -- nombre de categoría y conteo de alquileres
from category c 
join film_category fc on c.category_id = fc.category_id-- unida con film_category
join inventory i on fc.film_id = i.film_id -- unida con inventory
join rental r on i.inventory_id = r.inventory_id -- unida con rental
group by c.name --Agrupamos por categoría
order by total_alquileres desc;

-- 62. Encuentra el número de películas por categoría estrenadas en 2006.

select c.name, count(f.film_id) as total_peliculas_2006 -- nombre de categoría y conteo de alquileres
from category c
join film_category fc on c.category_id = fc.category_id-- unida con film_category
join film f on fc.film_id = f.film_id -- unida con inventory
where f.release_year = 2006
group by c.name --Agrupamos por categoría
order by total_peliculas_2006 desc;

-- 63. Obtén todas las combinaciones posibles de trabajadores con las tiendas que tenemos.

select s.first_name, s.last_name, st.store_id -- nombre del trabajador y id de la tienda
from staff s -- de la tabla staff
cross join store st; -- combinamos cada trabajador con cada tienda (todas las combinaciones posibles)

-- 64. Encuentra la cantidad total de películas alquiladas por cada cliente y muestra el ID del cliente, su nombre y apellido junto con la cantidad de películas alquiladas.

select c.customer_id, c.first_name, c.last_name, count(r.rental_id) as total_peliculas_alquiladas 
from customer c 
join rental r on c.customer_id = r.customer_id -- unida con rental
group by c.customer_id, c.first_name, c.last_name -- agrupamos por cliente
order by total_peliculas_alquiladas desc;


