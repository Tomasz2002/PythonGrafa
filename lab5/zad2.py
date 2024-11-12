from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import numpy as np


obraz = Image.open('obraz.png')
obraz.save('obraz1.jpg')


for i in range(1, 5):
   obraz = Image.open(f'obraz{i}.jpg')
   obraz.save(f'obraz{i+1}.jpg')


obraz_poczatkowy = Image.open('obraz.png')
obraz5 = Image.open('obraz5.jpg')


roznica = ImageChops.difference(obraz_poczatkowy, obraz5)


statystyki_roznicy = {
   'Max różnicy': np.max(np.array(roznica)),
   'Średnia różnicy': np.mean(np.array(roznica)),
   'Mediana różnicy': np.median(np.array(roznica)),
   'Odchylenie standardowe różnicy': np.std(np.array(roznica))
}


hist_poczatkowy = obraz_poczatkowy.histogram()
hist_obraz5 = obraz5.histogram()
hist_roznica = roznica.histogram()


fig, axs = plt.subplots(2, 3, figsize=(20, 10))
fig.suptitle("Porównanie obrazów")


axs[0, 0].imshow(obraz_poczatkowy)
axs[0, 0].set_title("Obraz początkowy")
axs[0, 1].imshow(obraz5)
axs[0, 1].set_title("Obraz5.jpg")
axs[0, 2].imshow(roznica)
axs[0, 2].set_title("Różnica (początkowy - obraz5)")


axs[1, 0].plot(hist_poczatkowy)
axs[1, 0].set_title("Histogram obrazu początkowego")
axs[1, 1].plot(hist_obraz5)
axs[1, 1].set_title("Histogram obraz5.jpg")
axs[1, 2].plot(hist_roznica)
axs[1, 2].set_title("Histogram różnicy")


plt.tight_layout()
plt.savefig("raport.jpg")
plt.show()




print("Statystyki różnicy między obrazem początkowym a obraz5.jpg:")
for k, v in statystyki_roznicy.items():
   print(f"{k}: {v}")


obraz4 = Image.open('obraz4.jpg')
roznica_4_5 = ImageChops.difference(obraz4, obraz5)

statystyki_roznicy_4_5 = {
   'Max różnicy': np.max(np.array(roznica_4_5)),
   'Średnia różnicy': np.mean(np.array(roznica_4_5)),
   'Mediana różnicy': np.median(np.array(roznica_4_5)),
   'Odchylenie standardowe różnicy': np.std(np.array(roznica_4_5))
}
print("\nStatystyki różnicy między obraz4.jpg a obraz5.jpg:")
for k, v in statystyki_roznicy_4_5.items():
   print(f"{k}: {v}")