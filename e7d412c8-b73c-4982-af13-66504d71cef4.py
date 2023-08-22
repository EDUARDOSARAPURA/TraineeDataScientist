#!/usr/bin/env python
# coding: utf-8

# # Hola Eduardo!
# 
# Mi nombre es David Bautista, soy code reviewer de Practicum y voy a revisar el proyecto que acabas de desarrollar.
# 
# Cuando vea un error la primera vez, lo señalaré. Deberás encontrarlo y arreglarlo. La intención es que te prepares para un espacio real de trabajo. En un trabajo, el líder de tu equipo hará lo mismo. Si no puedes solucionar el error, te daré más información en la próxima ocasión.
# 
# Encontrarás mis comentarios más abajo - **por favor, no los muevas, no los modifiques ni los borres.**
# 
# ¿Cómo lo voy a hacer? Voy a leer detenidamente cada una de las implementaciones que has llevado a cabo para cumplir con lo solicitado. Verás los comentarios de esta forma:
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si todo está perfecto.
# </div>
# 
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
# 
# 
# <div class="alert alert-block alert-danger">
#     
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
#     
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
# 
# 
# Puedes responderme de esta forma: 
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class="tocSkip"></a>
# </div
# 
# ¡Empecemos!

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypotheses)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
#     * [3.2 Hipótesis 2: preferencias musicales los lunes y los viernes](#week)
#     * [3.3 Hipótesis 3: preferencias de género en Springfield y Shelbyville](#genre)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en datos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar las hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba tres hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad.
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville escuchan géneros distintos. Lo mismo ocurre con los viernes por la noche.
# 3. Los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap.
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar las hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos
#  2. Preprocesamiento de datos
#  3. Prueba de hipótesis
# 
# 
# ### Reto
# 
# En este proyecto, preparamos un pequeño reto para ti. Incluimos un nuevo tipo de estructura de datos: las marcas temporales. Las marcas temporales son muy comunes y merecen una atención adicional. Más adelante en el programa, aprenderás mucho sobre ellas. Sin embargo, por ahora las trataremos como simples strings. Necesitamos marcas temporales en este proyecto para poner a prueba una de nuestras hipótesis. No te preocupes, te ayudaremos con esto. Tu nivel de conocimientos actual será suficiente para abordarlo.
# 
# Por ejemplo, digamos que tenemos dos marcas temporales: `dt1 = "12:00:00"` y `dt2 = "06:00:00"`. Queremos comparar estas dos marcas temporales y ver cuál es posterior.
# 
# Podemos compararlas mediante los operadores de comparación estándar (`<`, `>`, `<=`, `>=`, `==`, `!=`). Ejecuta la siguiente celda de código para comparar dos marcas temporales:
# 

# In[ ]:


# Comparar los objetos datetime

dt1 = "12:00:00"
dt2 = "06:00:00"

if dt1 < dt2:
    print("La marca temporal 2 es posterior")
else:
    print("La marca temporal 1 es posterior")


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Muy bien, recuerda que para todo los proyectos que realices es importante genera un contexto donde se comente que trata el caso y cuáles con los objetivos a cumplir, además es indispensable que se genere una tabla de contenido con el fin de mantener el orden en la entrega.
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[2]:


# importar pandas
import pandas as pd


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>

# Si estás trabajando en la plataforma, lee el archivo `music_project_en.csv` de la carpeta /datasets/ y guárdalo en la variable `df`. Si estás trabajando localmente, no es necesario especificar carpeta alguna siempre y cuando el archivo `music_project_en.csv` esté en la misma carpeta que este Notebook:

# In[3]:


# leer el archivo y almacenarlo en df
df = pd.read_csv('/datasets/music_project_en.csv')


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>

# Muestra las 10 primeras filas de la tabla:

# In[4]:


# obtener las 10 primeras filas de la tabla df
display(df.head(10))


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Te recomiendo usar ``display()`` en vez de ``print()`` para mostrar las salidas de las tablas.~~
# </div>
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>

# Obtén la información general sobre la tabla con un comando:

# In[5]:


# obtener información general sobre los datos en df
print (df.info())


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Todas almacenan el mismo tipo de datos: `object` (objeto).
# 
# Según la documentación:
# - `'userID'` — identificador del usuario o la usuaria;
# - `'Track'` — título de la canción;
# - `'artist'` — nombre del artista;
# - `'genre'` — género musical;
# - `'City'` — ciudad del usuario o la usuaria;
# - `'time'` — hora exacta en la que se reprodujo la pista;
# - `'Day'` — día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros, en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. Algunos nombres de columnas no estan bajo el estandar snake_case, otros no son precisos sobre la informacion que guardan.
# 
# Se debe proceder a editar los nonmbres de las columnas para estandarizarlas y así tener una idea facil y clara de la información  que guardan.
# 
# 
# 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>

# ### Tus observaciones <a id='data_review_conclusions'></a>
# 
# `Escriba sus observaciones aquí:`
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# Todos los datos que se encuentran en el DataFrame son del tipo Object/String, se puede entender que cada fila corresponde a la reproduccion de una cancion en una determinada hora ('time') en un determinado dia ('Day'), así pudiendo encontrar un usuario  ('userID') repetido varias veces en la tabla con igual o diferente valor en las columnas de 'time' y/o 'Day', debido a que no hay  detalles sobre la fecha exacta de la reproducción (la informacion pudiera ser de mas de 1 semana), se procederá a tratar la informacion como si fuera solo de 1 semana, así elimimando valores repetidos de ser el caso, el procedimiento correcto es consultar a nuestra fuente sobre el alcance de la misma para evitar supuestos. 
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestras tres hipótesis, o necesitamos más información?`
# No es necesario más informacion, con la que nos proporcionan se puede concluir las hipotesis, siempre y cuando esta muestra  tenga la representatividad requerida para el estudio.
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`
# Hay muchos valores ausentes, especialmente en la columna "Artist", pero no habrá inconvenientes pues nuestro analisis no implica dicha variable, se tendra que completar dicha data con algun valor referencial, lo mismo ocurre con la columna "Track", caso diferente ocurre con la columna "Genre" que si implica analizarla, pero al no tener informacion al respecto, se tendrá que evaluar el impacto en los resultados ya en las pruebas de hipotesis que correspondan.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo con la sección, ten en cuenta los comentarios que te deje.
# </div>

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla:

# In[6]:


# la lista de encabezados para la tabla df
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * todos los caracteres deben ser minúsculas;
# * elimina los espacios;
# * si el nombre tiene varias palabras, utiliza snake_case.

# Pon todos los caracteres en minúsculas e imprime el encabezado de la tabla de nuevo:

# In[7]:


# bucle en los encabezados poniendo todo en minúsculas
new_columns =[]
for c in df.columns:
    n_c = c.lower()
    new_columns.append(n_c)
df.columns = new_columns
print(df.columns)


# Ahora elimina los espacios al principio y al final de los encabezados y muéstralos:

# In[8]:


# bucle en los encabezados eliminando los espacios
new_columns2 =[]
for c in df.columns:
    n_c2 = c.strip()
    new_columns2.append(n_c2)
df.columns = new_columns2
print(df.columns)


# Aplica snake_case al encabezado userID e imprime el encabezado de la tabla:

# In[9]:


# cambiar el nombre del encabezado "user_id"
df.rename(columns={"userid":"user_id"},inplace=True)
print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[10]:


# comprobar el resultado: la lista de encabezados
print(df.columns)


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Excelente trabajo, ¡sigue así! Además, ten en cuenta que en el futuro podrás llevar a cabo este tipo de procesos de manera más concisa.
# </div>
# 

# ### Valores ausentes <a id='missing_values'></a>
# Primero, encuentra el número de valores ausentes en la tabla. Para ello, utiliza dos métodos `pandas`:

# In[11]:


# calcular el número de valores ausentes
print (df.isna().sum())


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Para hacer esto, crea la lista `columns_to_replace`, recorre sobre ella con un bucle `for`, y para cada columna reemplaza los valores ausentes en ella:

# In[12]:


# bucle en los encabezados reemplazando los valores ausentes con 'unknown'
columns_to_replace = ['track','artist','genre']
for col in columns_to_replace:
    df[col].fillna("unknown",inplace=True)


# Asegúrate de que la tabla no contiene más valores ausentes. Cuenta de nuevo los valores ausentes.

# In[13]:


# contando valores ausentes
print (df.isna().sum())


# [Volver a Contenidos](#back)

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo lidiando con los valores nulos.
# </div>

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla usando un comando:

# In[14]:


# contar duplicados explícitos
print(df.duplicated().sum())


# Llama al método `pandas` para deshacerte de los duplicados explícitos:

# In[17]:


# eliminar duplicados explícitos
df.drop_duplicates().reset_index(drop=True,inplace=True)


# Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[18]:


# comprobación de duplicados
print(df.duplicated().sum())


# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Has realizado un buen trabajo. No obstante, es importante que consideres que al eliminar los duplicados se puede generar un problema con la indexación de la tabla. Para resolverlo, puedes seguir este ejemplo:~~
#     
# ```python
# df = df.drop_duplicates().reset_index(drop=True)    
# ```
#     
#     
# </div>
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo!
#     
#     
# </div>
# 

# Para hacerlo, primero imprimamos una lista de nombres de género únicos, ordenados en orden alfabético. Para hacerlo:
# * recupera la columna deseada del dataFrame;
# * llama al método que te devolverá todos los valores de columna únicos;
# * aplica un método de ordenamiento a tu resultado.
# 

# In[20]:


# inspeccionar los nombres de género únicos
unique_genre = df["genre"].unique()
print(unique_genre) #hiphop hip hip-hop hop 


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, declara la función `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=` — la lista de duplicados;
# * `correct_genre=` — el string con el valor correcto.
# 
# La función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplaza cada valor de la lista `wrong_genres` con el valor en `correct_genre`. Utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos y reemplazarlos con el género correcto en la lista principal.

# In[21]:


# función para reemplazar duplicados implícitos

wrong=["hip","hop","hip-hop"]

def replace_wrong_genres (wrong_genres,correct_genre):
    return df["genre"].replace(wrong_genres,correct_genre,inplace=True)


# Llama a `replace_wrong_genres()` y pásale argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[22]:


# eliminar duplicados implícitos
for w in wrong:
    replace_wrong_genres (w,"hiphop")


# Asegúrate de que los nombres duplicados se hayan eliminado. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[24]:


# comprobación de duplicados implícitos
unique_genre2 = df["genre"].unique()
print(unique_genre2)


# [Volver a Contenidos](#back)

# ### Tus observaciones <a id='data_preprocessing_conclusions'></a>
# 
# `Describa brevemente lo que ha observado al analizar los duplicados, cómo abordó sus eliminaciones y qué resultados logró.`
# Como bien se detallo en la primera etapa, se tubo q reeemplazar los valores ausentes con un valor para no borrar lineas de informacion importantes para algunas pruebas de hipotesis, y para los valores ausentes tenerlas en consideracion y evaluar el impacto en la comprobacion de la hipotesis, los valores duplicados no representaron mayor inconveniente, pero seria bueno evaluar si existe algun valor inconsistente por ejemplo un mismo user_id el mismo dia a la misma hora reprodujo alguna cancion diferente o tambien mismo user_id el mismo dia a la misma hora reprodujo la misma cancion en diferente ciudad, se obtubieron los resultados deseados.

# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Has hecho un buen trabajo, pero recuerda que lo ideal es mostrar los valores únicos de manera ordenada alfabéticamente.
#         
# </div>
# 

# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypotheses'></a>

# ### Hipótesis 1: comparar el comportamiento del usuario en las dos ciudades <a id='activity'></a>

# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de pistas que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Agrupa los datos por ciudad y encuentra el número de canciones reproducidas en cada grupo.
# 
# 

# In[93]:


# contando las pistas reproducidas en cada ciudad
print(df.groupby('city')["track"].count())


# `Comenta tus observaciones aquí`:
# La cantidad de canciones reproducidas en ambas ciudades son diferentes, se usa mas este reproductor en Srpingfield que en Shelbyville, la proporcion es como de 2.3 a 1.

# Ahora agrupa los datos por día de la semana y encuentra el número de pistas reproducidas el lunes, el miércoles y el viernes.
# 

# In[94]:


# Cálculo de las pistas reproducidas cada día de la semana
Sprinfield_tracks = df[df['city'] == 'Springfield']
Shelbyville_tracks = df[df['city'] == 'Shelbyville']

print(Sprinfield_tracks.groupby("day")["track"].count())
print(Shelbyville_tracks.groupby("day")["track"].count())


# `Comenta tus observaciones aquí`:
# Para la ciudad de Sprinfield los usuarios tienen actividad muy similar los dias Viernes y Lunes, mientras que los miercoles tienen un poco menos de actividad respecto a esos dias. Por otro lado en Shelbyville los dias Viernes y Lunes mantienen su actividad similar pero los dias Miercoles tienen mas reproducciones con respecto a los otros dias.

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'`.
# - `city`: ciudad: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>
# 

# In[25]:


# <crear la función number_tracks()>
# declararemos la función con dos parámetros: day=, city=.
# deja que la variable track_list almacene las filas df en las que
# el valor del nombre de la columna ‘day’ sea igual al parámetro day= y, al mismo tiempo,
# el valor del nombre de la columna ‘city’ sea igual al parámetro city= (aplica el filtrado consecutivo
# con indexación lógica)
# deja que la variable track_list_count almacene el número de valores de la columna 'user_id' en track_list
# (igual al número de filas en track_list después de filtrar dos veces).
# permite que la función devuelva un número: el valor de track_list_count.

# la función cuenta las pistas reproducidas en un cierto día y ciudad.
# primero recupera las filas del día deseado de la tabla,
# después filtra las filas de la ciudad deseada del resultado,
# luego encuentra el número de pistas en la tabla filtrada,
# y devuelve ese número.
# para ver lo que devuelve, envuelve la llamada de la función en print().


# empieza a escribir tu código aquí

def number_tracks(day,city):
    track_list = df[(df['day'] == day) & (df['city']==city)]
    track_list_count = track_list["user_id"].count()
    return track_list_count


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros, para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[26]:


# el número de canciones reproducidas en Springfield el lunes
print (number_tracks("Monday","Springfield"))


# In[27]:


# el número de canciones reproducidas en Shelbyville el lunes
print (number_tracks("Monday","Shelbyville"))


# In[28]:


# el número de canciones reproducidas en Springfield el miércoles
print (number_tracks("Wednesday","Springfield"))


# In[29]:


# el número de canciones reproducidas en Shelbyville el miércoles
print (number_tracks("Wednesday","Shelbyville"))


# In[30]:


# el número de canciones reproducidas en Springfield el viernes
print (number_tracks("Friday","Springfield"))


# In[31]:


# el número de canciones reproducidas en Shelbyville el viernes
print (number_tracks("Friday","Shelbyville"))


# Utiliza `pd.DataFrame` para crear una tabla, donde
# * los encabezados de la tabla son: `['city', 'monday', 'wednesday', 'friday']`
# * Los datos son los resultados que conseguiste de `number_tracks()`

# In[32]:


# tabla con los resultados
col = ['city', 'monday', 'wednesday', 'friday']
cyties = df["city"].unique()
dat = []
for c in cyties:
    dat.append([c,number_tracks("Monday",c),number_tracks("Wednesday",c),number_tracks("Friday",c)])
table_data = pd.DataFrame(data=dat, columns=col)
print (table_data)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Has hecho un buen trabajo, pero podrías mejorar la forma en que estás creando las condiciones dentro de la función. Permíteme mostrarte un ejemplo.~~
#     
# ```python
# def number_tracks(day,city):
#     track_list=df[(df['day']==day) & (df['city']==city)]
#     track_list_count = track_list['user_id'].count()
#     return track_list_count #Retorno del número de canciones que cumplen con el parametro
#  
# ```
# </div>
# 
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>
# 
# 

# **Conclusiones**
# 
# `Comente si la primera hipótesis es correcta o debe rechazarse. Explicar tu razonamiento`:
# La primera hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música, pues en base a los resumenes realizados podemos aceptar esta hipotesis, ya que los usuarios de las 2 ciudades consumen musica de manera diferente, mientras que en Springfield consumen más musica por este medio en Shelbyville lo hacen en mucho menos proporcion, ademas en Shelbyville hay mas actividad los Miercoles y en Springfield es todo lo contrario pues hay menos actividad.

# [Volver a Contenidos](#back)

# ### Hipótesis 2: música al principio y al final de la semana <a id='week'></a>

# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros que difieren de los que disfrutan los usuarios de Shelbyville.

# Cree dos tablas con los nombres proporcionados en los dos bloques de código a continuación:
# * Para Springfield — `spr_general`
# * Para Shelbyville — `shel_general`

# In[33]:


# crear la tabla spr_general a partir de las filas df
# donde los valores en la columna 'city' es 'Springfield'
spr_general = df[df["city"]=="Springfield"]
display (spr_general) 


# In[34]:


# crear la tabla shel_general a partir de las filas df
# donde los valores en la columna 'city' es 'Shelbyville'
shel_general = df[df["city"]=="Shelbyville"]
display (shel_general)


# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~Te recomiendo usar ``display()`` en vez de ``print()`` para mostrar las salidas de las tablas.~~
# </div>

# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>
# 

# Escribe la función `genre_weekday()` con cuatro parámetros:
# * Una tabla para los datos (`df`)
# * El día de la semana (`day`)
# * La marca de fecha y hora en formato 'hh:mm:ss' (`time1`)
# * La marca de fecha y hora en formato 'hh:mm:ss' (`time2`)
# 
# La función debe devolver los 15 géneros más populares en un día específico dentro del período definido por las dos marcas de tiempo, junto con sus respectivos recuentos de reproducción.
# Aplica la misma lógica de filtrado consecutiva, pero usa cuatro filtros esta vez y luego crea una nueva columna con los recuentos de reproducción respectivos.
# Ordena el resultado de un recuento más grande a uno más pequeño y devuélvelo.

# In[37]:


# 1) Deja que la variable genre_df almacene las filas que cumplen varias condiciones:
#    - el valor de la columna 'day' es igual al valor del argumento day=
#    - el valor de la columna 'time' es mayor que el valor del argumento time1=
#    - el valor en la columna 'time' es menor que el valor del argumento time2=
#    Utiliza un filtrado consecutivo con indexación lógica.

# 2) Agrupa genre_df por la columna 'genre', toma una de sus columnas,
#    y utiliza el método size() para encontrar el número de entradas por cada uno de
#    los géneros representados; almacena los Series resultantes en
#    la variable genre_df_count

# 3) Ordena genre_df_count en orden descendente de frecuencia y guarda el resultado
#    en la variable genre_df_sorted

# 4) Devuelve un objeto Series con los primeros 15 valores de genre_df_sorted - los 15
#    géneros más populares (en un determinado día, en un determinado periodo de tiempo)

# escribe tu función aquí

def genre_weekday(df,day,time1,time2):
    genre_df = df[(df["day"]==day)&(df["time"]>time1)&(df["time"]<time2)]
    genre_df_count = genre_df.groupby("genre")["track"].count()
    genre_df_sorted = genre_df_count.sort_values(ascending=False)
    return genre_df_sorted[:15]

   # filtrado consecutivo
    # Crea la variable genre_df que almacenará solo aquellas filas df donde el día es igual a day=
    #genre_df = # escribe tu código aquí

    # Filtra genre_df nuevamente para almacenar solo las filas donde el tiempo es menor que time2=
    #genre_df = # escribe tu código aquí

    # Filtra genre_df una vez más para almacenar solo las filas donde el tiempo es mayor que time1=
    #genre_df = # escribe tu código aquí

    # Agrupa el DataFrame filtrado por la columna con los nombres de los géneros, selecciona la columna 'genre',
    # y encuentra el número de filas para cada género con el método count()
    #genre_df_count = # escribe tu código aquí

    # Ordenaremos el resultado en orden descendente (por lo que los géneros más populares aparecerán primero en el objeto Series)
    #genre_df_sorted = # escribe tu código aquí

    # Devuelve un objeto de Series con los primeros 15 valores de genre_df_sorted: los 15 géneros más populares (en un día determinado, dentro de un período de timeframe)
    #return genre_df_sorted[:15]


# Compara los resultados de la función `genre_weekday()` para Springfield y Shelbyville el lunes por la mañana (de 7 a 11) y el viernes por la tarde (de 17:00 a 23:00). Utiliza el mismo formato de hora de 24 horas que el conjunto de datos (por ejemplo, 05:00 = 17:00:00):

# In[38]:


# llamando a la función para el lunes por la mañana en Springfield (utilizando spr_general en vez de la tabla df)
Spr_mm = genre_weekday (spr_general,"Monday","07:00:00","11:00:00")
print (Spr_mm)


# In[39]:


# llamando a la función para el lunes por la mañana en Shelbyville (utilizando shel_general en vez de la tabla df)
She_mm = genre_weekday (shel_general,"Monday","07:00:00","11:00:00")
print (She_mm)


# In[40]:


# llamando a la función para el viernes por la tarde en Springfield
Spr_fn = genre_weekday (spr_general,"Friday","17:00:00","23:00:00")
print (Spr_fn)


# In[41]:


# llamando a la función para el viernes por la tarde en Shelbyville
She_fn = genre_weekday (shel_general,"Friday","17:00:00","23:00:00")
print (She_fn)


# **Conclusiones**
# 
# `Comente si la segunda hipótesis es correcta o debe rechazarse. Explica tu razonamiento.`:
# Según la segunda hipótesis, el lunes por la mañana y el viernes por la noche, los ciudadanos de Springfield escuchan géneros que difieren de los que disfrutan los usuarios de Shelbyville. Según la informacion mostrada rechazariamos esta segunda hipotesis  pues se evidencia que en ambas ciudades, los dias Lunes por la mañana y Viernes por la noche tienen una preferencia musical muy similar en ambas ciudades, siendo casi identico el top 5, a pesar de que las cantidades si muestran diferencias significativas, pero esto se explica por la cantidad de afluencia que tiene cada ciudad.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# ~~En general realizas buenas conclusiones y buen código; sin embargo, hay cosas en que la función ```genre_weekday``` que pueden mejorar, primero que todo los filtros que estás realizando para indexar no son consecutivos, estos podrían ser consecutivos, la idea sería algo como la siguiente:~~
#     
# ```python
# df = df[(condicion_1) & (condicion_2) & (condicion_3)]
# ```
# .</div>

# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor #2</b> <a class="tocSkip"></a>
#     
# Buen trabajo.
# </div>
# 

# [Volver a Contenidos](#back)

# ### Hipótesis 3: preferencias de género en Springfield y Shelbyville <a id='genre'></a>
# 
# Hipótesis: Shelbyville ama la música rap. A los residentes de Springfield les gusta más el pop.

# Agrupa la tabla `spr_general` por género y encuentra el número de canciones reproducidas de cada género con el método `count()`. Luego ordena el resultado en orden descendente y guárdalo en la variable `spr_genres`.

# In[67]:


# escribe una línea de código que:
# 1. agrupe la tabla spr_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en spr_genres.
spr_genres = spr_general.groupby("genre")["track"].count().sort_values(ascending=False)


# Imprime las 10 primeras filas de `spr_genres`:

# In[68]:


# muestra los primeros 10 valores de spr_genres
print (spr_genres[:10])


# Ahora haz lo mismo con los datos de Shelbyville.
# 
# Agrupa la tabla `shel_general` por género y encuentra el número de canciones reproducidas de cada género. Después, ordena el resultado en orden descendente y guárdalo en la tabla `shel_genres`:
# 

# In[71]:


# escribi una línea de código que:
# 1. agrupe la tabla shel_general por la columna 'genre';
# 2. cuente los valores 'genre' con count() en la agrupación;
# 3. ordene el Series resultante en orden descendente y lo guarde en shel_genres.
shel_genres = shel_general.groupby("genre")["track"].count().sort_values(ascending=False)


# Imprime las 10 primeras filas de `shel_genres`:

# In[72]:


# imprimir las 10 primeras filas de shel_genres
print (shel_genres[:10])


# **Conclusión**
# 
# `Comente si la tercera hipótesis es correcta o debe rechazarse. Explica tu razonamiento.`:
# Nuestra ultima hipótesis indica que los oyentes de Springfield y Shelbyville tienen preferencias distintas. En Springfield prefieren el pop, mientras que en Shelbyville hay más personas a las que les gusta el rap, en base a la informacion mostrada rechazariamos parcialmente esta hipotesis:
# 1. Las preferencias musicales en ambas ciudades son muy similares, el top 5 de generos mas escuchados en ambas ciudades es casi identico, razon por la cual rechazamos el primer enunciado de la hipotesis.
# 2. En Sprinflied realmente prefieren escuchar pop a otro genero, se encuentra en el Top 1, razon por la cual se acepta este fragmento de la hipotesis.
# 3. En Shelbyville al tener preferencias musicales muy similares que en Sprinflied tambien prefieren el pop a otro genero, el rap no aparece en el top 10, razon por la cual rechazamos este fragmento de la hipotesis.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# Genial, buen trabajo.</div>

# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resuma sus conclusiones sobre cada hipótesis aquí`:
# Al probar las tres hipótesis se concluye:
# 
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la cuidad, ya que los usuarios de las 2 ciudades consumen musica de manera diferente, mientras que en Springfield consumen más musica por este medio en Shelbyville lo hacen en mucho menos proporcion, ademas en Shelbyville tienen mas actividad los Miercoles y en Springfield es todo lo contrario pues hay menos actividad.
# 
# 2. Los lunes por la mañana, los habitantes de Springfield y Shelbyville no escuchan géneros distintos, lo mismo ocurre con los viernes por la noche, pues se evidencia que en ambas ciudades, tienen una preferencia musical muy similar, siendo casi identico el top 5, a pesar de que las cantidades si muestran diferencias significativas.
# 
# 3. Los oyentes de Springfield y Shelbyville no tienen preferencias distintas. Tanto en Springfield como en Shelbyville prefieren el pop, por sobre otros generos, tienen el top 5 de generos mas escuchados casi identicos, ademas en Shelbyville no hay mucha cantidad de personas a las que les gusta el rap.

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General
#     
# ~~Hola Eduardo, te felicito por el desarrollo del proyecto hasta el momento, ahora bien, debes tener en cuenta los comentarios que he generado para la próxima entrega.~~
# </div>

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#     
# # Comentario General #2
#     
# Buen trabajo, Eduardo, has culminado el proyecto. </div>

# [Volver a Contenidos](#back)
