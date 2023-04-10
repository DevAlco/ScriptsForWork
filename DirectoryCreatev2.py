import os
from pathlib import Path

def GenerateFilesForPaths(paths):
    file = open("directory dict.txt", "w")

    isCreateFile = input("Добавить пути до файлов в созданые директории, по умолчанию будут созданы файлы с расширением .txt (Y/n)\n")

    while isCreateFile != "Y" and isCreateFile != "y" and isCreateFile != "N" and isCreateFile != "n":
        isCreateFile = input("Охидаемый ответ Y/n\n")

    if isCreateFile == "Y" or isCreateFile == "y":
        while True:
            try:
                howMutch = int(input("Сколько файлов создат в каждой директории?\n"))
            except:
                print("Вы ввели что-то не то, колличество директорй должно быть целым положительным числом\n")
                continue
            else:
                break

        for path in paths:
            i = 0
            while i < howMutch:
                file.write(path+ "/" + "GeneratedTestFile" + str(i) + ".txt" + "\n")
                i += 1


    else:
        for path in paths:
            file.write(path + '\n')    

# получение аргументов длинны и ширины теребуемого дерева порядок важен сначала ширина потом длина, разделитель пробел 
inputParams = input("введи ширину и глуюину предполагаемого дерева через пробел\n")

# получение пути до шары
sharePath = input("введи путь до шары, путь по умолчанию рабочая директория скрипта\n")
if sharePath == "":
    sharePath = "./"

# получение аргументов из введенной ранее строки с шириной и глубиной 
args = inputParams.split(" ")

# инициализации массива созданых путей 
levelPaths = []

# создание пути до корневой директории дерева с именем base
basePath = os.path.join(sharePath, "base")
levelPaths.append(basePath)

# инициализация счетчика итераций для ширины
i = 0
#счетчик шиины дерва
while i < int(args[0]):

    j=0

    #счетчик глубины дерва
    while j < int(args[1]):
        #определение корневого каталога для текущей итерации
        if j == 0:
            # создание пути до нового каталога с логикой каталог для текущей итерации, имя нового каталога с именем: level + номер итерации по ширине + . + номер итерации по глубине
            path = os.path.join(basePath, "level" + str(i + 1) + "." + str(j + 1))
            # добавление пути в массив и запись в файл
            levelPaths.append(path)
            # увеличение счетчика итераций
            j += 1
            # смещение каталагв для следующей итерации
            previousPath = path
        else:
            path = os.path.join(previousPath, "level" + str(i + 1) + "." + str(j + 1))
            levelPaths.append(path)
            j += 1
            previousPath = path
         
    i += 1

# создание каталогов в фс для каждого сгенерерованного пути последовательно
for path in levelPaths:
    Path(path).mkdir(exist_ok=True)

GenerateFilesForPaths(levelPaths)
