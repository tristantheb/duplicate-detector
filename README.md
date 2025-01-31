# How to use

1. Install poetry
2. Set venv in project

    ```bash
    poetry config settings.virtualenvs.in-project true
    ```

3. Put sources in source folder
4. Use jupyter into vscode :
    <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>
5. Select the kernel in vscode
6. Crete an ipynb.
7. Run with directly in vscode

## to add pip dependency use

poetry add {dependency name}

## To convert a notebook to a python file

```bash
jupyter nbconvert --to script script.ipynb
```

## To convert a python file to an executable

```bash
pyinstaller --onefile script.py
```
