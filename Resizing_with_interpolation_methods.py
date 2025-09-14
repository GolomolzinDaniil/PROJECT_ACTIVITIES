import cv2
from skimage import data
import matplotlib.pyplot as plt


def resize_image_with_methods(image, methods=None, koef_resize=4, return_method=cv2.INTER_CUBIC):

    ''' Изменения размера изображений с разными методами '''

    # проверка на валидность переданного изображения
    if image is None:
        return ValueError('Не подходящее изображение')
    
    # если вы хотите изменить разрешение изображения в koef_resize раз
    # if koef_resize = 4 => (512, 512, 1) -> (128, 128, 1)
    koef_resize = 1 / koef_resize
    
    # если методы не указаны, то используем по умолчанию
    if methods is None:
        methods = {
            'INTER_AREA'   : cv2.INTER_AREA,
            'INTER_LINEAR' : cv2.INTER_LINEAR,
            'INTER_NEAREST': cv2.INTER_NEAREST,
        }
    
    # автоматически определяем размеры изображения
    orig_height, orig_width = image.shape[:2]
    new_width  = int(orig_width * koef_resize)
    new_height = int(orig_height * koef_resize)
    
    # если получившиеся размеры не валидны
    if new_width <= 0 or new_height <= 0:
        raise ValueError('Не подходящий размер для масштабирования изображений')
    
    pictures = {}
    for name, method in methods.items():
        # изменяем в одну сторону
        try:
            curr_image = cv2.resize(image, (new_width, new_height), interpolation=method)
            # возвращем изображение в другую
            try:
                pictures[name] = cv2.resize(curr_image, (orig_width, orig_height), interpolation=return_method)
            except Exception as e:
                print(f'Ошибка с методом {return_method}: {e}')
                continue
        except Exception as e:
            print(f'Ошибка с методом {name}: {e}')
            continue
    
    # возвращаем словарь массив измененных изображений
    return pictures



if __name__ == '__main__':

    # взятие camera-man (512,512,1)
    image = data.camera()
    
    try:
        # получем измененное изображение
        pictures = resize_image_with_methods(image)
        
        # отображение результатов
        ind = 0
        for name, img in pictures.items():
            plt.subplot(1, 3, ind + 1) # сетка изображений
            plt.title(name) # название
            plt.imshow(img, cmap='gray')
            plt.axis('off') # без осей
            ind += 1
        
        # настройка отступов для красоты
        plt.tight_layout()
        # вывод всех изображений
        plt.show()
        
    except Exception as e:
        print(f'Error: {e}')