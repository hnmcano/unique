from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('PySide6')

a = Analysis(
    ['app.py'],
    datas=datas + [
        ('C:/Python/Lib/site-packages/PySide6/Qt/resources', 'resources'),
        ('C:/Python/Lib/site-packages/PySide6/Qt/translations', 'translations'),
    ],
    binaries=[
        ('C:/Python/Lib/site-packages/PySide6/Qt/libexec/QtWebEngineProcess.exe', '.')
    ],
    ...
)