import cv2
from skimage import data
import matplotlib.pyplot as plt


# 1. Уменьшите изображение в 4 раза с INTER_AREA, INTER_LINEAR, INTER_NEAREST.
# 2. Увеличьте обратно с INTER_CUBIC.
# 3. Отобразите все варианты.


# взятие camera-man (512,512,1) => (128,128,1)
image = data.camera()

# методы изменения изображения
methods = {
    'INTER_AREA': cv2.INTER_AREA,
    'INTER_LINEAR': cv2.INTER_LINEAR,
    'INTER_NEAREST': cv2.INTER_NEAREST,
}

pictures = {}
for name, method in methods.items():
    # изменим по методу, а потом вернем обратно по cv2.INTER_CUBIC
    pictures[name] = cv2.resize(cv2.resize(image, (128, 128), interpolation=method), (512,512), interpolation=cv2.INTER_CUBIC)

ind = 0
for name in pictures:

    plt.subplot(1,3,ind+1) # будет подграфом в сетке из 1 строки, 3 столбцов на ind+1 месте
    plt.title(name) # подписанный
    plt.imshow(pictures[name], cmap='gray') # изображение в градации серого
    plt.axis('off') # бес осей

    ind += 1


# настройка отступов для красоты
plt.tight_layout()
# выывод всех изображений
plt.show()


