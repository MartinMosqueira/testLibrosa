``` python
cancion, sr = librosa.load(ruta_cancion)
```
Línea de código que se utiliza en la biblioteca librosa de Python para cargar un archivo de audio desde tu sistema de archivos.
Devuelve dos valores en una tupla:
* 'y' **es una lista de valores**: es una lista (o un array NumPy) que contiene una serie de números. Cada número en esta lista representa la amplitud del sonido en un punto específico en el tiempo. En otras palabras, cada elemento de 'y' describe cuán fuerte o débil es el sonido en ese momento en particular. Esto es fundamental para entender cómo se escucha una canción o una grabación de audio, ya que la variación de la amplitud con el tiempo es lo que crea el sonido en sí.

* 'sr': es la tasa de muestreo, que indica cuántas muestras de amplitud de sonido se toman por segundo. Es importante para interpretar el tiempo en la señal de audio.

``` python
tempo, beats = librosa.beat.beat_track(y=cancion, sr=sr)
```
Línea de código que se utiliza en la biblioteca librosa de Python para calcular el tempo(BPM, latidos por minuto) de una canción y los momentos en los que ocurren los latidos en una señal de audio representada por 'y'.
Devuelve dos valores en una tupla:
* 'tempo': es una estimacion del tempo, representa la velocidad de la música, es decir, cuántos latidos hay por minuto en la canción.
* 'beats': es una lista de valores que contiene los momentos en los que ocurren los latidos en la señal de audio. Es decir indican en qué partes de la señal ocurren los latidos.

``` python
beat_times = librosa.frames_to_time(beats, sr=sr)
```
Es una lista de índices que toma los índices de frames de tiempo de los latidos(beats) en la señal de audio y los convierte en valores de tiempo en segundos. Es útil para obtener una representación de los latidos en términos de tiempo real.

``` python
duracion_segundos = librosa.get_duration(y=cancion, sr=sr)
```
Es una función que devuelve la duración de la señal de audio en segundos.
