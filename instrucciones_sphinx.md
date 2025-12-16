- Para crear la documentacion debes ir a la carpeta donde quieres guardar la documentacion creada en el codgo y poner:
            (cd carpeta)
            uv run sphinx-quickstart
            darle a yes (y)
            nombre
            nombre
            nada
            en, es, etc
- La carpeta source es el codigo para crear el docstring y la carpeta build es la que se pasa a cliente
- Para rellenar la carpeta build hay que:
    -Ir a source y en conf.py poner:
        import os
        import sys

        sys.path.insert(0, os.path.abspath('../..'))
        ...
        ...
        ...
        extensions = [
            'sphinx.ext.autodoc',
            'sphinx.ext.doctest',
            ]
FALTAN COSAS (COPIAR LO QUE HAY O MIRAR DOCUMENTACION)