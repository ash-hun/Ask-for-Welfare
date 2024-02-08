import zipfile
import os

os.system("gdown https://drive.google.com/uc?id=1Oal-qhggsGtrdhW4R43Aks6UtJ4MYLre")
output_dir = './app/'
file_name = 'model.zip'
zip_file = zipfile.ZipFile(file_name)
zip_file.extractall(path=output_dir)