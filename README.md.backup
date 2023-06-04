# yt-feeds
Aplicación en Python creada para la obtención de las direcciones rss de canales de youtube.

Esta aplicación incorpora 2 modos:

1. **Simple**. El cual mediante la incorporación de links de canales de youtube arroja un dataframe que incluye la dirección del rss feed correspondiento.

2. **Interfaz**. Una interfaz gráfica que permite tanto la incrustación de las direcciones de canales, así como la lectura de archivos de texto con distintas direcciones, permitiendo distintas opciones de exportación del resultado.

## 1. Simple mode

En este modo, se deberá proporcionar las direcciones de los canales de youtube en forma de lista dentro del objeto "urls", y con el que finalmente se obtendrá un dataframe el cual se guardará en un archivo csv dentro del directorio home o en el directorio de tu preferencia.


## 2. GUI mode

Este modo despliega una interfaz sobre la cual es posible poner links de canales directos, así como importar archivos `.txt` que al interior contengan los canales de los cuales se pretende obtener la dirección del rss. Asimismo, permite distintas opciones de exportación.

### Notas de importación

- En caso de presentar problemas, es posible que esten relacionados con la importación de los links del archivo de texto. Para evitarlos, es necesario asegurarse en la pantalla de importación que los links tienen una estructura vertical, es decir, que cada link se encuentre separado en distintas filas y no haya espacios al inicio o al final de cada cadena, por ejemplo:    

```{python}
    link1
    link2
    link3
```

Y evitar estructuras tipo:

```{python}
[_]link1
link2[_]
[tab]link3
```

