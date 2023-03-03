from PIL import Image
import numpy as np
import random
import json
import os

COUNT = 50
 
def write_json():
    with open('nft/data.json', 'w') as json_dosya:
        json.dump(nft, json_dosya, indent = 4)

def hue_shift(img, amount):
    hsv_img = img.convert('HSV')
    hsv = np.array(hsv_img)
    hsv[..., 0] = (hsv[..., 0]+amount) % 360
    new_img = Image.fromarray(hsv, 'HSV')
    return new_img.convert('RGB')

def imageGet(path):
    list = []

    dosyalar = os.listdir(path)

    for dosya in dosyalar:
        if dosya.endswith(".png"):
            list.append(path+"//"+dosya)
    
    return list

 
arkaplan = imageGet('resimler//arkaplan')
goz = imageGet('resimler//goz')
kas = imageGet('resimler//kas')
agiz = imageGet('resimler//agiz')

nft = {}

for i in range(COUNT):

    ap = random.choice(arkaplan)
    apr = random.randint(1,50)*10
    img1 = Image.open(ap)
    img11 = hue_shift(img1, apr)

    g = random.choice(goz)
    gr = random.randint(1,50)*10
    img2 = Image.open(g)
    img22 = hue_shift(img2, gr)

    k = random.choice(kas)
    kr = random.randint(1,50)*10
    img3 = Image.open(k)
    img33 = hue_shift(img3, kr)

    a = random.choice(agiz)
    ar = random.randint(1,50)*10
    img4 = Image.open(a)
    img44 = hue_shift(img4, ar)

    x = {
        "name": "NFT_" + str(i+1),
        "arkaplan": ap.split('//')[2],
        "arkaplan hue": apr,
        "goz": g.split('//')[2],
        "goz hue": gr,
        "kas": k.split('//')[2],
        "kas hue": kr,
        "agiz": a.split('//')[2],
        "agiz hue": ar
    }

    nft["NFT_" + str(i+1)] = x

    img11.paste(img22, (0, 0), mask=img2)
    img11.paste(img33, (0, 0), mask=img3)
    img11.paste(img44, (0, 0), mask=img4)

    name = "nft/NFT_"+str(i+1)+".png"

    img11.save(name, "png")

write_json()