from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt


obraz = Image.open('zeby.png')


print("Tryb obrazu:", obraz.mode)


obraz = obraz.convert('L')
print("Nowy tryb obrazu:", obraz.mode)



def histogram_norm(obraz):
    hist = obraz.histogram()
    liczba_pikseli = sum(hist)
    hist_norm = [h / liczba_pikseli for h in hist]
    return hist_norm



def histogram_cumul(obraz):
    hist_norm = histogram_norm(obraz)
    hist_kumul = np.cumsum(hist_norm)
    return hist_kumul



def histogram_equalization(obraz):
    hist_kumul = histogram_cumul(obraz)
    piksele = np.array(obraz)


    piksele_equalized = np.array([int(255 * hist_kumul[p]) for p in piksele.flatten()])
    piksele_equalized = piksele_equalized.reshape(piksele.shape)  # Przywrócenie kształtu


    obraz_equalized = Image.fromarray(piksele_equalized.astype('uint8'))
    return obraz_equalized



def statystyki(obraz):
    piksele = np.array(obraz)
    print("Min:", np.min(piksele))
    print("Max:", np.max(piksele))
    print("Średnia:", np.mean(piksele))
    print("Mediana:", np.median(piksele))
    print("Odchylenie standardowe:", np.std(piksele))





def konwertuj1(obraz, w_r, w_g, w_b):
    if obraz.mode != 'RGB':
        raise ValueError("Obraz musi być w trybie RGB")

    R, G, B = obraz.split()
    R = np.array(R)
    G = np.array(G)
    B = np.array(B)


    L = np.round(R * w_r + G * w_g + B * w_b)
    L = L.astype(np.uint8)

    return Image.fromarray(L)


obraz_mgla = Image.open('mgla.jpg')


w_r, w_g, w_b = 0.299, 0.587, 0.114
mgla_L1 = konwertuj1(obraz_mgla, w_r, w_g, w_b)
mgla_L1.save('mgla_L1.png')


mgla_L = obraz_mgla.convert('L')
mgla_L.save('mgla_L.png')


print("\nStatystyki - mgla_L1 (konwertuj1)")
statystyki(mgla_L1)

print("\nStatystyki - mgla_L (Image.convert)")
statystyki(mgla_L)





def konwertuj2(obraz, w_r, w_g, w_b):
    if obraz.mode != 'RGB':
        raise ValueError("Obraz musi być w trybie RGB")

    R, G, B = obraz.split()
    R = np.array(R)
    G = np.array(G)
    B = np.array(B)


    L = (R * w_r + G * w_g + B * w_b).astype(int)
    L = L.astype(np.uint8)

    return Image.fromarray(L)



mgla_L2 = konwertuj2(obraz_mgla, w_r, w_g, w_b)
mgla_L2.save('mgla_L2.png')


print("\nStatystyki - mgla_L2 (konwertuj2)")
statystyki(mgla_L2)


plt.figure(figsize=(12, 6))


plt.subplot(1, 4, 1)
plt.title("Oryginalny RGB")
plt.imshow(obraz_mgla)
plt.axis('off')


plt.subplot(1, 4, 2)
plt.title("Konwertuj1 (round)")
plt.imshow(mgla_L1, cmap='gray')
plt.axis('off')


plt.subplot(1, 4, 3)
plt.title("Image.convert('L')")
plt.imshow(mgla_L, cmap='gray')
plt.axis('off')


plt.subplot(1, 4, 4)
plt.title("Konwertuj2 (int)")
plt.imshow(mgla_L2, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.savefig('mgla_comparison.png')
plt.show()


print("\nPorównanie statystyk:")
print("Różnice między mgla_L1 a mgla_L wynikają z dokładności zaokrągleń (round vs Image.convert).\n"
      "Dodatkowo Image.convert używa precyzyjnego algorytmu z wagami ITU-R 601-2.\n")
print("Różnice między mgla_L1 a mgla_L2 wynikają z użycia round() vs int(). Int() ścina wartości pikseli, co może\n"
      "prowadzić do większych błędów w porównaniu do round().")
