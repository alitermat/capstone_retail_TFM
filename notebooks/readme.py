# RESUMEN

Inicialmente tenemos diferentes tablas:
- daily_calendar
- item_prices
- item_sales

Mas tarde veremos con un poco mas detalle las variables de cada tabla. Recomendable hacer un .merge() para quedarnos con una sola df donde trabajar (quitar la paja)

### **daily_calendar**
| Columna   |    Descripcion        |
|:-----     |   :---                |
|date       |date in y-m-d format   |
|weekday    |day of the week        |
|weekday_int|numeric day of the week(Saturday day 1, Friday day 7)|
|d          |day identifier         |
|event      |if the date includes an event, the name of this event(only a few are included)|



### **item_prices**
| Columna   |    Descripcion        |
|:-----     |   :---                |
|item       |product id             |
|category   |product category       |
|store_code |alphanumeric code of the store|
|yearweek   |date period for the price(year-week format)|
|sell_price |price for the product "item"for the period in "yearweek". Prices are proviced per week(average across 7 days). If not available, there were no sales for the product during that week|



### **item_sales**
| Columna   |    Descripcion        |
|:-----     |   :---                |
|id         |sales series id(combination of item + store_code)|
|item       |product id             |
|category   |product category       |
|department |department id (different identifier for different stores)|
|store      |store name             |
|store_code |store id               |
|region     |region                 |
|d_1,d_2,d_...|number of units sold per day|
### Tabla informativa sobre las variables tabla CALENDAR

Estas tablas se han obtenido por medio de tabla.nombre_columna.value_counts() por cada tabla. El codigo está mas abajo


| **Columna**   |    **Nº Valores distintos**        | **Significado**        |
|:-----     |   :---                         | :---               |
|date       |     1913                    |   Fecha de los dias en formato (year-month-day)  |
|weekday      |               7         |    Dia distinto de la semana en formato (day : Saturday)        |
|weekday_int   |               7           |   Dia de la semana en formato numerico(1,2,3,4,5,6,7). La semana empieza en Saturday (1) y termina en Friday(7)    |
|d |                   1913      |    Identificador numerico del dia desde el inicio de los datos                   |
|event      |             5          |     Evento especial del año. Existen los siguientes: SuperBowl, Ramadan starts , Thanksgiving, NewYear, Easter. Atencion que no hay ni Navidades ni el final del Ramadan, y esto pueden ser eventos a tener en cuenta tambien.                                          |
### Tabla informativa variables PRICES

| **Columna**   |    **Nº Valores distintos**        | **Significado**        |
|:-----     |   :---                         | :---               |
|item         | 3049                          |       Codigo que identifica el articulo vendido. Se compone de categoria + departamento +codigo articulo. Ej: SUPERMARKET_2_210   - |
|category      |               3         |    SUPERMARKET,  HOME_&_GARDEN  y ACCESORIES , las tres categorias distintas que existen        |
|store_code   |               10           |    Codigos a los que pertenecen las distintas tiendas por ciudades y por los que se agrupan NYC (1,2,3,4), BOS(1,2,3) y PHI(1,2,3).   |
|yearweek |                   279        |    Semana del año en formato (year-week)                   |
|sell_price |             na              |        Precio de venta de los articulos(POR SEMANA). **Posible correlacion con variable target 'unit_sold'**                                 |
### Tabla informativa de las distintas variables de la tabla SALES

| **Columna**   |    **Nº Valores distintos**        | **Significado**        |
|:-----     |   :---                         | :---               |
|id         | 30490                          |       Combinacion del item vendido + store_code. Tenemos 19130 observaciones por cada valor unico      - |
|item       |               3049                 |     Codigo que identifica el articulo vendido. Se compone de categoria + departamento +codigo articulo. Ej: SUPERMARKET_2_210      |
|category   |                  3         |    SUPERMARKET,  HOME_&_GARDEN  y ACCESORIES , las tres categorias distintas que existen        |
|department |                   3        |    por cada categoria anterior hay 3 departamentos (1,2 y 3. Ej: SUPERMARKET_2)                   |
|store      |                    10           |  Existen las siguientes tiendas: Greenwich_Village, Harlem, Tribeca, Brooklyn, South_End, Roxbury, Back_bay, Midtown_Village, Yorktown y Queen_Village.   Observaciones: 5832737. Entiendo que son distntos barrios de las distintas ciudades (NYC, BOS y PHI)   |
|store_code |                    10           |    Codigos a los que pertenecen las distintas tiendas por ciudades y por los que se agrupan NYC (1,2,3,4), BOS(1,2,3) y PHI(1,2,3). Ej: NYC_4    |
|region     |                    3           |     Pertenecen a las 3 distitnas ciudades, New York, Boston y Philadelphia        |
|day_number |                     1913         |         Nº de dias distintos reflejado en los datos, contienen datos de unos 5 años y unos 3 meses aprox            |
|unit_sold  |                 na              |    numero de ventas efectuada por observacion. **Variable Target en tarea de regresion?**                |

# Objetivos

### **INTRO**
Antes de nada debemos entender claramente cual es el problema a resolver que se nos presenta, entender los datos y sus variables y como se ven representadas en las distintas dataset.

Los datos que tenemos se centran solo las tiendas de 3 grandes ciudades (NY, Boston y Philadelphia).

Deberiamos tener un entendimiento basico del negocio, yo me hago las siguientes preguntas:
1. Cuales son las ciudades y tiendas que tienen mejor performance.
2. Cómo ha ido la facturacion en el historico (lineplot),
3. Cuales son los productos mas vendidos y el % que suponen del total
4. La varianza de precios entre productos
5. Entender los datos y qué lo componen, por ejemplo, cuantas regiones distintas tenemos en la variable region de la tabla sales.

### **1. Analisis exhaustivo**
Deberemos hacer un EDA pasando por los siguientes pasos:
- Informacion basica del Dataset: exploracion columnas, filas, tipos de datos...modificar tipos de datos si necesario
- Analisis estadistico basico de las variables
- Identificacion de Nulos y posterior tratamiento
- Identificacion de Duplicados
- Busqueda de Outliers y decision de tratamiento sobre estos (atipicos naturales o errores)
- Correlacion de las variables con la variable target( nº de ventas?)
- Visualizacion grafica de las distribuciones

### **2. Analisis BI**

### **3. Clustering**  (no posible hasta terminar temario, 6 Febrero)
### **4. Modelo de prediccion de las ventas**  ( no posible hasta terminar temario, 29 Enero)
### **5. Caso de uso de abastecimiento de las tiendas** (con MLOps) - Solo contarlo
### **6. Evaluacion del modelo - Piloto de casos A/B**
