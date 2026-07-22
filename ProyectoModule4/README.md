# 🎧 Análisis de Spotify Tracks: Exploración y Dashboard por Género

## 📖 Descripción

Este proyecto realiza un análisis exploratorio de un dataset de más de 113.000 canciones de Spotify, con el objetivo de identificar patrones de popularidad, características de audio (energía, bailabilidad, tempo, valence) y contenido explícito a través de 114 géneros musicales distintos.

El análisis se centra en responder preguntas como: ¿qué géneros son más populares?, ¿qué caracteriza musicalmente a cada género?, ¿existe relación entre el contenido explícito y la popularidad?, y ¿qué "mood" (ánimo) predomina según el tempo de las canciones?

Para ello se aplicaron técnicas de limpieza y transformación de datos, análisis descriptivo y visualización mediante tablas dinámicas, gráficos y un dashboard interactivo, todo desarrollado en Microsoft Excel.


## 🗂 Estructura del Proyecto

```
├── original_spotify_tracks.xlsx        # Dataset original descargado de Kaggle, sin modificar
├── spotify_analysis_dashboard.xlsx     # Libro de Excel con la limpieza, el análisis y el dashboard
├── data_info.txt                       # Notas sobre las columnas y características del dataset original
├── informe_analisis.docx               # Informe explicativo del análisis (objetivo, metodología, hallazgos y conclusiones)
└── README.md                           # Descripción del proyecto
```

## 🛠 Instalación y Requisitos

Este proyecto se desarrolló íntegramente en **Microsoft Excel** (versión de escritorio, Windows). No requiere instalación de librerías ni entornos adicionales.

**Fuente de datos:**
- Dataset: [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) (Kaggle)
- Formato original: CSV, 114.000 filas × 21 columnas

**Para abrir el proyecto:**
1. Descarga el archivo `spotify_analysis.xlsx`
2. Ábrelo con Excel 
3. Habilita el contenido si Excel muestra alguna advertencia de seguridad

## 🧹 Limpieza y Transformación de Datos

- Eliminación de 1 fila con valores nulos (canción sin artista, álbum ni nombre).
- Conservación de canciones duplicadas por `track_id`, ya que cada duplicado corresponde a la misma canción etiquetada en un género distinto — necesario para poder comparar métricas por género.
- Conversión de `duration_ms` a minutos (`duration_min`).
- Creación de una versión legible de `explicit` (`explicit_texto`: Sí/No) y una versión numérica (`explicit_num`: 1/0) para poder calcular promedios y porcentajes.
- Revisión de la columna `track_genre` en busca de inconsistencias de escritura; se confirmó que categorías aparentemente similares (ej. "latin" y "latino") son géneros genuinamente distintos, ya que el dataset está balanceado con exactamente 1.000 canciones por cada uno de los 114 géneros.
- Verificación de ausencia de celdas vacías en el resto de columnas mediante formato condicional.
- Detección de valores atípicos (outliers): una canción de 0,14 minutos y otra de 87,29 minutos de duración, y múltiples canciones con `tempo = 0` (error técnico conocido del algoritmo de detección de tempo de Spotify, no un error de los datos en sí). Se documentan como limitación, sin eliminarse del dataset.

## 📊 Análisis Descriptivo

Se calcularon, mediante tablas dinámicas:
- Popularidad media, duración media y % de contenido explícito por género.
- Relación entre energía (`energy`) y bailabilidad (`danceability`) por género.
- Relación entre tempo (`tempo`) y valence (estado de ánimo) por género.
- Ranking de artistas por número de canciones.
- Estadísticos globales: total de canciones, canciones únicas, número de géneros, número de artistas únicos, popularidad media global, duración media global y % de contenido explícito global.
- Medidas de dispersión (mínimo, máximo) para identificar outliers en duración y tempo.

## 📈 Dashboard

El dashboard incluye:
- **5 indicadores clave (big numbers):** total de canciones, número de géneros, número de artistas, popularidad media y % de canciones explícitas (estos tres últimos dinámicos, conectados a los filtros).
- **Top 15 géneros por popularidad** (gráfico de barras).
- **Top 5 géneros más y menos populares**, con duración media y % explícito como contexto adicional.
- **Top 10 artistas con más canciones** (gráfico de barras).
- **Tempo vs Valence por género** (gráfico de dispersión), para explorar el "mood" musical de cada género.
- **2 segmentos de datos (slicers):** género musical y contenido explícito, cada uno conectado a los elementos del dashboard donde aporta una comparación con sentido.

La paleta de colores está inspirada en la identidad de marca de Spotify (verde como color principal y negro).

## 🔎 Resultados y Conclusiones

- Los géneros **pop-film** y **k-pop** lideran en popularidad media, muy por encima del resto.
- El género **comedy** destaca con el mayor porcentaje de contenido explícito (65,6%).
- La mayoría de géneros se concentran en un rango de tempo similar (110-130 BPM aprox.), mientras que la principal diferencia entre ellos está en el *valence* (ánimo), no en la velocidad.
- El dataset está balanceado por diseño: 114 géneros con exactamente 1.000 canciones cada uno, lo que garantiza que las diferencias observadas entre géneros no se deben a un desequilibrio en el tamaño de muestra.
- Se identificaron limitaciones relevantes: duplicados de canciones por género (necesarios para el análisis, pero a tener en cuenta al interpretar rankings de artistas), y outliers técnicos en duración y tempo.

## 🔄 Próximos Pasos

- Incorporar un análisis de correlación más amplio entre variables de audio (energy, loudness, acousticness).
- Enriquecer el dataset con datos adicionales, como el número de escuchas mensuales por canción, para poder analizar la popularidad no solo como un índice, sino en relación con el volumen real de reproducciones.
- Ampliar el dashboard con un análisis de canciones únicas (sin duplicados por género) para comparar rankings de artistas sin el sesgo de las repeticiones.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si detectas algún error o quieres proponer una mejora, abre un pull request o una issue.

## ✒️ Autora


Laura Murillo Guijarro

[@lauramurillo01] (https://github.com/lauramurillo01)



