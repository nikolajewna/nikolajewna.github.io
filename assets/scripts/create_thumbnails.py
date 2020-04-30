#!/usr/bin/env python

import sys
from PIL import Image
from pathlib import Path
import glob

SIDE = 200.0

folder = Path(sys.argv[1])
path = folder.__str__() + r"\*.jpg"

for image in glob.glob(path):
    image_path = Path(image)
    thumbname = image_path.parent / (image_path.stem.__str__() + '_thumb' + image_path.suffix)
    img = Image.open(image_path)
    siz = img.size
    if siz[0] >= siz[1]:
        new_side = int(siz[0] * SIDE/siz[1])
        img = img.resize((new_side, int(SIDE)), Image.ANTIALIAS)
        box=(int((new_side-SIDE)/2),
             0,
             int(new_side/2 + SIDE/2),
             int(SIDE))
    else:
        new_side = int(siz[1] * SIDE/siz[0])
        img = img.resize((int(SIDE), new_side), Image.ANTIALIAS)
        box=(0,
             int((new_side-SIDE)/2),
             int(SIDE),
             int(new_side/2 + SIDE/2))

    img = img.crop(box=box)
    img.save(thumbname, format='JPEG', quality=90)
    print(img.size)

"""
Dir.glob(path) do |image|
    puts "Wroking on #{image}"
    thumbname = File.dirname(image) + "/" +
                File.basename(image, ".*") +
                "_thumb" + File.extname(image)

    image_data = MiniMagick::Image.open(image)
    crop_params = "#{MAX_SIDE.to_i}x#{MAX_SIDE.to_i}!"
    puts crop_params
    image_data.crop(crop_params)

    image_data.write(thumbname)

    puts "#{thumbname} written."
end
"""