import librosa

ruta_cancion = "music/Dylan Sitts - Cashmere.mp3"

cancion, sr = librosa.load(ruta_cancion)

duracion_segundos = librosa.get_duration(y=cancion, sr=sr)

print(f'Duración de la canción: {duracion_segundos:.2f} segundos')

tempo, beat_frames = librosa.beat.beat_track(y=cancion, sr=sr)

print(f'Tempo estimado: {tempo:.2f} latidos por minuto (BPM)')
