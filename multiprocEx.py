import time
from PIL import Image, ImageFilter
import concurrent.futures


image_names = [
    'photo-1586227740560-8cf2732c1531?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1261&q=80.jpg',
    'photo-1593642634524-b40b5baae6bb?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1332&q=80.jpg',
    'photo-1633899521562-7023998f19dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=802c1d46984c63.jpg',
    'photo-1634834425203-1be8a21ac9ef?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=661&q=80.jpg',
    'photo-1634837837337-7d41514247d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80.jpg',
    'photo-1634838037553-66f5ce322212?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80.jpg',
    'photo-1634839678877-d39a0343a681?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80.jpg',
    'photo-1634885912493-c96f19309b9a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1012&q=80.jpg'
]

start = time.perf_counter()

size = (1200, 1200)

def blurred(image_name):
    img = Image.open(image_name)
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{image_name}')

    print(f'{image_name} was processed...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(blurred, image_names)


# for image_name in image_names:
#     img = Image.open(image_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))

#     img.thumbnail(size)
#     img.save(f'processed/{image_name}')

#     print(f'{image_name} was processed...')

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)")