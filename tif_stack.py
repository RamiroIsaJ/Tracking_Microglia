from PIL import Image, ImageSequence

path_o = r'C:\Users\RAFIJ\PycharmProjects\Images\\'
path_r = r'C:\Users\RAFIJ\PycharmProjects\Images\Micro\\'

im = Image.open(path_o + "Stack1.TIF")
for i, page in enumerate(ImageSequence.Iterator(im)):
    page.save(path_r + "Page%d.png" % i)
