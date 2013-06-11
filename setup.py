from distutils.core import setup
import py2exe

setup(name="pyCodigoB",
      version="1.0",
      license="GPL",
    windows=[{"script":"captura.py", "icon_resources":[(1, "/src/img/barcode.gif")]}])

