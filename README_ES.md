
# Limpieza de Datos tras Web Scraping – Categoría Machine Learning & Data Analytics

## 📢 Descargo de Responsabilidad
Este repositorio contiene datos que fueron obtenidos mediante web scraping desde un sitio web de acceso público. El propósito de este proyecto es puramente educativo y no comercial. Está destinado a explorar técnicas de análisis de datos, visualización y machine learning con fines académicos y de desarrollo personal.

No reclamamos la propiedad de ningún contenido extraído del sitio web, y ningún dato ha sido utilizado para su redistribución, reventa o con intención de infringir derechos de propiedad intelectual. Se han tomado todas las medidas posibles para asegurar un uso ético de la información públicamente disponible.

Si eres representante del sitio original y tienes alguna inquietud, no dudes en contactarme para revisar o retirar el contenido según corresponda.

---

### 📌 Este documento resume el proceso de limpieza aplicado a los datos extraídos de los resultados web de gigs de:</br> [*Machine Learning*](https://github.com/anverpy/scraping-and-data-analysis/blob/main/ML-gigs.csv) y [*Data Analytics*](https://github.com/anverpy/scraping-and-data-analysis/blob/main/DA-gigs.csv). <br> El enfoque está en resolver los problemas estructurales del CSV causados por comas embebidas en los títulos.</br>

### En el archivo [og_DA_csv.zip](https://github.com/anverpy/scraping-and-data-analysis/blob/main/og_DA_csv.zip), puedes encontrar los datos crudos de los gigs de Data Analytics. </br>

### No pude conservar el crudo de Machine Learning por un error técnico. </br> (Dejé de usar shift + del 😅).

---

### 🔍 Campos de Datos Esperados
Campos esperados para cada gig:
- `title`
- `seller`
- `rating`
- `reviews`
- `price`
- `seller_level`
- `video_consultation`

<br><br>
---
# 🧹 1. Limpieza de Datos

- ## 1.1 Algunos títulos de gigs contenían comas sin el uso adecuado de comillas, lo que resultaba en filas con más de 7 columnas. Ejemplo:

```csv
 I will create Machine Learning, Deep Learning, and NLP,Andrew Veasman,4.9,152,"1499,90","Level 2",True
```

## Si no se respetan las comillas, esto se interpreta como más de 7 columnas, rompiendo la estructura del CSV.


- ## 1.2 Hay espacios en blanco en los campos de puntuación, reseñas y nivel porque hay más datos de gigs que de vendedores, y porque algunos vendedores aún no tienen un nivel asignado.
## ¿Qué significa esto?
### Los gigs reciben calificaciones y reseñas por gig, no por vendedor.<br>Algunos vendedores tienen dos o más gigs publicados (esto se verá más adelante en la visualización), por lo tanto hay gigs sin calificaciones <br>ni reseñas. (Un ejemplo claro es Johannes M.)
<br><br>
---

# 🛠️ 2. Estrategia de Solución
## Se implementó un enfoque de parsing inverso:
### 1. Para cada fila, se toman los últimos 6 elementos (campos fijos conocidos).
### 2. Se considera todo lo anterior como el `title`.
### 3. Se rellenan los vacíos en rating/reviews/seller_level con valores como unranked/unreviewed/unleveled

<br>

# 🔧 3. Resumen de Scripts

### - **[`title_extractor.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/title_extractor.py)**: Extrae solo la columna de título desde filas malformadas.
### - **[`rid_bad_titles.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/rid_bad_titles.py)**: Conserva solo los últimos 6 campos, descartando títulos corruptos.
### - En este punto eliminé todas las "," en Excel usando `CTRL + B`, pero puedes mejorarlo añadiendo esta función a cualquiera de los scripts.
### - **[`merge_titles_untitleds.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/merge_titles_untitleds.py)**: Une los títulos limpios con los datos corregidos.
### - **[`merge_all.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/merge_all.py)**: Concatena dos CSV completos desde distintas sesiones de scraping. Asegúrate de que los CSV tengan los mismos nombres de cabecera.
### - **[`fill_gaps.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/fill_gaps.py)**: Llena huecos en rating/reviews/seller_level con unranked/unreviewed/unleveled.
## Una vez hecha la limpieza de datos, se continúa al siguiente paso.

<br>

# 📊 4. Visualización
## En el repositorio encontrarás el archivo [`visualization.png`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/visualization.png), que contiene las visualizaciones finales renderizadas.<br> Puedes descargar el archivo y analizarlo por tu cuenta o según lo necesites.

<br>

# ✅ Resultado
## Este proceso permitió recuperar datos limpios y estructurados desde CSVs corruptos — un reto común en entornos reales de web scraping y análisis de datos. <br> La lógica de ingeniería inversa estructural demostró ser precisa, robusta y reutilizable.
