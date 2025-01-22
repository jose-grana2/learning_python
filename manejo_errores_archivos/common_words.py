"""PALABRAS COMUNES
Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count())."""

files = ['El Rio de los deseos.txt', 'La aventura de Luna y  encantado.txt']
print('---------------------------------------------------')
print('There are some books in the system')
for filename in files:
    print(filename)
print('---------------------------------------------------')
counter = 0
try:
    book = input('Write a available book from the list')
    with open(book, mode="r", encoding="utf-8") as file:
        word = input('Enter a word: ')
        lines = file.readlines()
        for line in lines:
            counter += line.count(word)
            
    print('The word or sentence', word, 'is in the book', counter, 'times')
except FileNotFoundError:
    print('The file not exist')
