import os
import sys
import Image
from shutil import copytree, rmtree
from glob import glob
from scale import scale

def scale_image(path, out, scale):
    im = Image.open(path)
    w, h = im.size
    output_size = (int(w * scale), int(h*scale))
    print path, output_size
    im.thumbnail(output_size, Image.ANTIALIAS)
    im.save(out, "PNG")

if __name__ == "__main__":	
    if len(sys.argv) != 4:
        print "Usage: scale-all.py [input-folder] [output-folder] [float scale]"
        sys.exit(0)
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    scale = float(sys.argv[3])

    if os.path.exists(output_folder):
        rmtree(output_folder)
    copytree(input_folder, output_folder)

    pattern = output_folder+"/*.png"
    print pattern
    for path in glob(pattern):
        scale_image(path, path, scale)


