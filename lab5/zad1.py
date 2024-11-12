from PIL import Image
import numpy as np

def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    tab_bazowy = np.array(obraz_bazowy).astype(np.uint8)
    tab_wstawiany = np.array(obraz_wstawiany).astype(np.uint8)
    (h_bazowy, w_bazowy) = tab_bazowy.shape[:2]
    (h_wstawiany, w_wstawiany) = tab_wstawiany.shape
    n_wy = min(h_bazowy, n + h_wstawiany)
    m_wy = min(w_bazowy, m + w_wstawiany)
    n_we = max(0, n)
    m_we = max(0, m)

    for i in range(n_we, n_wy):
        for j in range(m_we, m_wy):
            if tab_wstawiany[i - n, j - m] == 0:  # Czarne piksele inicjałów
                tab_bazowy[i, j] = kolor

    return Image.fromarray(tab_bazowy)

obraz = Image.open('obraz.png')
inicjaly = Image.open('inicjaly.bmp')

obraz = wstaw_inicjaly(obraz, inicjaly, 0, obraz.height - inicjaly.height, [255, 0, 0])

obraz = wstaw_inicjaly(obraz, inicjaly, obraz.width - inicjaly.width, 0, [0, 255, 0])

obraz = wstaw_inicjaly(obraz, inicjaly, obraz.width - inicjaly.width // 2, obraz.height // 2 - inicjaly.height // 2, [0,0, 255])

obraz.save('obraz_inicjaly.png')