from PIL import Image,ImageDraw

I_gray = f.convert('L')
I_gray.save('gray.png')