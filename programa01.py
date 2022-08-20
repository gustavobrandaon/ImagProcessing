from pickletools import optimize
from PIL import Image

# quality = 0 a 1

def img_converter(input_file, output_file, format):
    image = Image.open(input_file)
    image.save(output_file, format = format, optimize = True, quality = 1)

def to_thumbnail(input_file):
    image = Image.open(input_file)
    image.thumbnail((75,75))
    image.save("thumbnail.jpg")

def img_format(input_file):
    imagem = Image.open(input_file)
    print(f"Formato: >>{imagem.format_description}<<")

if __name__ == "__main__":
    img_converter("img.jpg", "pizza.teste", "PNG")
    #img_format("img.jpg")
    #img_format("pizza.png")
    #img_format("pizza.teste")
    to_thumbnail("img.jpg")