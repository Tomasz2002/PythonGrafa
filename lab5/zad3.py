from PIL import Image

def odkoduj(obraz1_path, obraz2_path, output_path):
    obraz1 = Image.open(obraz1_path).convert("RGB")
    obraz2 = Image.open(obraz2_path).convert("RGB")

    if obraz1.size != obraz2.size:
        raise ValueError("Obrazy mają różne wymiary!")

    wynik = Image.new("L", obraz1.size)

    pixels1 = obraz1.load()
    pixels2 = obraz2.load()
    wynik_pixels = wynik.load()

    for x in range(obraz1.width):
        for y in range(obraz1.height):
            if pixels1[x, y] != pixels2[x, y]:
                wynik_pixels[x, y] = 255
            else:
                wynik_pixels[x, y] = 0

    wynik.save(output_path)

odkoduj("jesien.jpg", "zakodowany2.bmp", "kod2.bmp")