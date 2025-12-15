- uv init xxxx para iniciar un venv con uv
- Para cambiar de version de python me voy a .python-version y ponerle la version que quiera (necesito tenerla instalada con uv python install x.xx)
- Tras esto, nos metemos en la carpeta correspondiente: cd xxxxxx/
- Para instalar, estando en la carpeta del proyecto ejecutamos: uv add pandas numpy
    Esto hace un venv y te lo activa
- Para correr el fichero: uv run xxx.py