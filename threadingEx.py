import requests
import time
import concurrent.futures

image_urls = [
    'https://images.unsplash.com/photo-1586227740560-8cf2732c1531?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1261&q=80',
    'https://images.unsplash.com/photo-1633899521562-7023998f19dc?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=802c1d46984c63',
    'https://images.unsplash.com/photo-1634838037553-66f5ce322212?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1170&q=80',
    'https://images.unsplash.com/photo-1634837837337-7d41514247d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1634834425203-1be8a21ac9ef?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=661&q=80',
    'https://images.unsplash.com/photo-1593642634524-b40b5baae6bb?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1332&q=80',
    'https://images.unsplash.com/photo-1634839678877-d39a0343a681?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80',
    'https://images.unsplash.com/photo-1634885912493-c96f19309b9a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1012&q=80'
]

start = time.perf_counter()


def download_image(image_url):
    image_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[3]
    image_name = f"{image_name}.jpg"
    with open(image_name, "wb") as image_file:
        image_file.write(image_bytes)
        print(f"{image_name} is downloaded..")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, image_urls)


# for image_url in image_urls:
#     image_bytes = requests.get(image_url).content
#     image_name = image_url.split('/')[3]
#     image_name = f"{image_name}.jpg"
#     with open(image_name, "wb") as image_file:
#         image_file.write(image_bytes)
#         print(f"{image_name} is downloaded..")

finish = time.perf_counter()

# 10.55

print(f"Finished in {round(finish-start, 2)} second(s)")