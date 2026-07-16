contener

- readme
- esquema BBDD que me proporcionan
- archivo sql con las consultas resueltas


## 📊 Proyecto SQL: Análisis de la Base de Datos Sakila (PostgreSQL)

# 📖 Descripción

Este proyecto aplica los conocimientos adquiridos en el módulo 5 de SQL, siguiendo las especificaciones de la lección "Lógica: Consultas de SQL". El objetivo es demostrar el manejo de PostgreSQL y DBeaver a través de la resolución de 64 consultas sobre la base de datos proporcionada (Sakila), un esquema relacional que simula el negocio de una tienda de alquiler de películas (clientes, empleados, tiendas, alquileres, pagos, películas, actores, categorías, etc.).

A lo largo del proyecto se ha trabajado con:

Consultas sobre una única tabla (filtros, agregaciones, ordenaciones).
Relaciones entre tablas mediante distintos tipos de JOIN (INNER, LEFT, FULL, CROSS).
Subconsultas (en WHERE, FROM, SELECT, con EXISTS / NOT EXISTS).
Vistas (CREATE VIEW).
Estructuras de datos temporales (CREATE TEMPORARY TABLE).
Buenas prácticas de legibilidad y comentarios en el código SQL.


# 🗂️ Estructura del Proyecto

ProyectoModule5/
├── BBDD_Proyecto_shakila_sinuser.sql      # Script del esquema de la BBDD (tablas, tipos, secuencias y datos)
├── EnunciadoDataProject_SQL_Lógica.pdf     # Enunciado original con los 64 ejercicios propuestos
├── Shakila-Project-consultas.sql           # Archivo con las 64 consultas resueltas y comentadas
└── README.md                               # Descripción del proyecto (archivo README)

# 🛠️ Instalación y Requisitos

Para ejecutar este proyecto necesitas:


PostgreSQL instalado (o acceso a un servidor PostgreSQL).
DBeaver como cliente para conectarte a la base de datos y ejecutar las consultas.


Pasos para configurar el entorno:


Crea una base de datos nueva en PostgreSQL (por ejemplo, sakila).
Ejecuta el script BBDD_Proyecto_shakila_sinuser.sql en DBeaver sobre esa base de datos para crear el esquema (tablas, tipos, secuencias, claves primarias/foráneas) y cargar los datos de ejemplo.
Verifica que las tablas se han creado correctamente

Abre el archivo Shakila-Project-consultas.sql en DBeaver y ejecuta cada consulta de forma individual.


⚠️ Nota: las consultas de los ejercicios 51 y 52 crean tablas temporales, que solo existen durante la sesión activa de conexión en DBeaver. Si cierras la conexión, deberás volver a ejecutarlas antes de consultarlas de nuevo. La vista del ejercicio 48, en cambio, queda guardada de forma permanente en la base de datos.



# 📊 Resultados y Conclusiones


- El esquema Sakila permite practicar relaciones típicas de negocio a través de tablas puente como film_actor, film_category e inventory.
- El uso de JOIN frente a LEFT JOIN cambia radicalmente el resultado cuando se busca incluir registros sin correspondencia (por ejemplo, actores sin películas asociadas o clientes sin alquileres), lo cual quedó reflejado en varios ejercicios (29, 31, 32, 43, 46).
- Las subconsultas con EXISTS / NOT EXISTS resultaron más legibles que los JOIN equivalentes en los casos donde solo se necesita comprobar la existencia de una relación, sin necesitar datos de la tabla relacionada.
- El CROSS JOIN solo aporta valor cuando se necesitan todas las combinaciones posibles entre dos conjuntos (como en el ejercicio 63, trabajador-tienda), pero no tiene sentido de negocio cuando se cruzan entidades sin relación directa (ejercicio 44, película-categoría).
- Las vistas y tablas temporales facilitan reutilizar resultados intermedios (como el total de alquileres por cliente) sin tener que repetir la misma lógica de agregación en cada consulta.


# 🔄 Próximos Pasos


- Seguir practicando y profundizando en SQL, especialmente en consultas más avanzadas (funciones de ventana, optimización de rendimiento).
- Continuar aprendiendo nuevas herramientas y técnicas para mejorar.


# 🤝 Contribuciones

Este es un proyecto individual de carácter académico, por lo que no se aceptan contribuciones externas por el momento. Cualquier sugerencia de mejora es bienvenida a través de un issue en el repositorio.

# ✒️ Autores


Laura Murillo Guijarro
[@lauramurillo01] (https://github.com/lauramurillo01)