from random import randrange

cat_links = [
    'https://media.istockphoto.com/photos/closeup-portrait-of-funny-ginger-cat-wearing-sunglasses-isolated-on-picture-id1188445864?k=20&m=1188445864&s=612x612&w=0&h=0vuJeOxJr8Lu3Q1VdT1z7t6HcM8Oj7EVJe3CexGnH_8=', 
    'https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg',
    'https://i.ytimg.com/vi/317jz-PU7Mg/maxresdefault.jpg',
    'https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg', 
    'https://i.pinimg.com/564x/16/ca/b1/16cab153397fc070d5369635ba891e8d.jpg',
    'https://i0.wp.com/catcaresolutions.com/wp-content/uploads/2020/12/cute-cat-with-yellow-headband-on.png?fit=1000%2C1500&ssl=1',
    'https://wl-brightside.cf.tsp.li/resize/728x/jpg/e54/e78/30a24451a8ba30d37a3dfa888c.jpg',
    'https://bookriot.com/wp-content/uploads/2020/04/image-of-cat-in-basket-beside-books-1280x720.jpg',
    'https://as1.ftcdn.net/v2/jpg/01/93/38/40/1000_F_193384026_F34lj9rX9W4ixlVZBrTJmijK010Tdv0j.jpg',
    'https://welovecatsandkittens.com/wp-content/uploads/2020/06/Funny-Cat-Names.jpg',
    'https://www.boredpanda.com/blog/wp-content/uploads/2014/02/funny-wet-cats-coverimage.jpg',
    'https://img.freepik.com/premium-photo/funny-cat-sunglasses-cat-with-glasses-light-blue-clean-sunny-background_90380-2753.jpg',
    'https://static9.depositphotos.com/1062590/1212/i/600/depositphotos_12126423-stock-photo-funny-european-cat-asking-for.jpg',
    'https://www.boredpanda.com/blog/wp-content/uploads/2020/11/unflattering-funny-cat-photo-challenge-13-5fa4f8edad8be__700.jpg',
    'https://www.rd.com/wp-content/uploads/2021/03/GettyImages-985984802-e1615488865623.jpg',
    'https://s36537.pcdn.co/wp-content/uploads/2017/12/A-cat-licking-with-his-tongue-out.jpg.optimal.jpg',
    'https://i.pinimg.com/736x/5f/80/85/5f80854fd1475958717a19e345695942.jpg',
    'https://wallpaper.dog/large/10737523.jpg', 
    'https://i2-prod.mirror.co.uk/incoming/article25609246.ece/ALTERNATES/s1200/0_PUSS-IN-BOOTS.jpg',
    'https://www.dogalize.com/wp-content/uploads/2017/05/funny-cat-img.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaBKDk1bsxtgeI0lnNYdXOrlPaby-wxY7rFQ&usqp=CAU',
    'https://media.istockphoto.com/photos/cat-surfing-on-internet-picture-id1172290687?k=20&m=1172290687&s=612x612&w=0&h=xINesZHX6C7C6PH5PfRx2cDn8d69o01osus3YjXq1QU=',
    'https://static.demilked.com/wp-content/uploads/2022/05/funny-pics-the-cat-trap-is-working-1.jpeg',
    'https://www.boredpanda.com/blog/wp-content/uploads/2022/08/funny-cat-pics-memes-630871ab120c3__700.jpg',
    'https://www.thehappycatsite.com/wp-content/uploads/2021/05/Funny-Cat-Names-HC-long.jpg',
    'https://ae01.alicdn.com/kf/HTB1ZkKqaMkLL1JjSZFpq6y7nFXaI/Funny-Cat-Costumes-Pirate-Suit-Cat-Clothes-Kitty-Kitten-Corsair-Halloween-Costume-Puppy-Suits-Dressing-Up.jpg_Q90.jpg_.webp',
]

def get_cat_pic():
    i = randrange(len(cat_links))
    link = cat_links[i]
    return link
