from PIL import Image
import os
import numpy as np

base_path = 'pics/'

pics = []

with os.scandir(f'{base_path}wake-up-light') as entries:
    for entry in entries:
        pics.append(entry.name)


for pic in pics:
    try:   
        image = Image.open(f'{base_path}wake-up-light/{pic}')
  
        for i in np.arange(15,360, 15):
            image.rotate(i, expand=True).save(f'pics/wake-up-light/{pic[:-4]}_{i}.jpg')
    except:
        pass
