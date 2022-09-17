from random import randrange

cat_links = [
    'https://i.pinimg.com/736x/b3/ff/3a/b3ff3accc46377d013a80eb9519c8c1c.jpg', 
    'https://media.istockphoto.com/photos/closeup-portrait-of-funny-ginger-cat-wearing-sunglasses-isolated-on-picture-id1188445864?k=20&m=1188445864&s=612x612&w=0&h=0vuJeOxJr8Lu3Q1VdT1z7t6HcM8Oj7EVJe3CexGnH_8=', 
    'https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg',
    'https://i.ytimg.com/vi/317jz-PU7Mg/maxresdefault.jpg',
    'https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg'
]

def get_cat_pic():
    i = randrange(len(cat_links))
    link = cat_links[i]
    return link
