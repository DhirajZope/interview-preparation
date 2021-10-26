from PIL import Image
import os

SIZE = (300, 300)
SIZE_700 = (700, 700)

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fx = os.path.splitext(f)

        i.thumbnail(SIZE_700)
        i.save(f'700/{fn}_700{fx}')
        
        i.thumbnail(SIZE)
        i.save(f'300/{fn}_300{fx}')

        print('Resizing Done..')

# with Image.open('photo-1586227740560-8cf2732c1531?ixid=MnwxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1261&q=80.jpg') as img:
#     # img.show()
#     img.save('sample.png')