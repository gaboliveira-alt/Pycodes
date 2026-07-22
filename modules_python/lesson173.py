import os
import shutil

HOME = os.path.expanduser("~")
DOCUMENTS = os.path.join(HOME, "OneDrive", "Documentos")
ORIGINAL_FOLDER = os.path.join(DOCUMENTS, "Artigos_China")
NEW_FOLDER = os.path.join(DOCUMENTS, "Artigos_Copia")

shutil.copytree(ORIGINAL_FOLDER, NEW_FOLDER)
shutil.rmtree(NEW_FOLDER, ignore_errors=True)
shutil.move(NEW_FOLDER, NEW_FOLDER + "RECEBA")
