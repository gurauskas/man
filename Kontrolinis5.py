# Penkta užduotis - Pillow
# Sukurti programa, kuri uždėtų nuotraukai kontrastą ir išsaugotų atnaujintą nuotrauką

from PIL import Image, ImageEnhance

from PIL import Image

# im = Image.open("OIP.jpg")
# im.show()




panda = Image.open('OIP.jpg')
enh = ImageEnhance.Contrast(panda)
enh.enhance(1.3).show()

#ishsugoti
enh.enhance(1.6).save('test.png')