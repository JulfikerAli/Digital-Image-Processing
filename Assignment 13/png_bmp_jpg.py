import sys
from PIL import Image

def main():
    png = Image.open(sys.argv[1])
    png.load()
    background = Image.new("RGB", png.size, (255, 255, 255))
    try:
        background.paste(png, mask=png.split()[3])
    except IndexError:
        background.paste(png, mask=png.convert('RGBA').split()[3])

    background.save(sys.argv[2], 'JPEG', quality=90)

if __name__ == "__main__":
    main()

