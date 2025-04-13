# N Reinas

El **problema de las *n* reinas** consiste en colocar *n* reinas en un tablero de ajedrez de tamaño *n×n* sin que se ataquen entre sí. Una reina puede moverse cualquier número de casillas en horizontal, vertical o diagonal, por lo que ninguna reina puede compartir la misma fila, columna o diagonal.  

El objetivo es encontrar todas las configuraciones posibles (o al menos una) que cumplan esta condición. Es un problema clásico en algoritmos de **backtracking** y se usa para ilustrar técnicas de búsqueda y optimización en ciencias de la computación.  

**Ejemplo clásico:**  
Para *n = 8* (tablero estándar), hay **92 soluciones** distintas, considerando simetrías.  

**Complejidad:**  
Es un problema NP-duro para *n* arbitrariamente grande, ya que el número de soluciones crece exponencialmente con *n*.  

## Crear entorno virtual

```bash
python -m venv .env
```

## Activar entorno virtual

```bash
source .env/Scripts/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecutar aplicación

```bash
python main.py 8
```

## Capturas

<p align="center">
    <img src="https://github.com/user-attachments/assets/a5f2d9eb-3162-416c-bd40-a87d5f7a8bb8" />
</p>
