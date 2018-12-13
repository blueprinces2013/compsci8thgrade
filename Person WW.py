import pyautogui as pg 
import webbrowser as wb
import time as t 
points = 0
 

food = pg.prompt ("what is your favorite food?")
if food == "pepperoni pizza":
    wb.open ("https://www.youtube.com/watch?v=HCAPjIVOdJw")
    points += 10
    t.sleep (2)
    pg.alert ("I love pepperoni pizza!")
elif food == "ice cream":
    wb.open ("https://www.youtube.com/watch?v=bYO4fDJ3lGo")
    points += 16
    t.sleep(2)
    pg.alert ("my favorite flavor is chocolate")
elif food == "vegetables":
    wb.open ("https://www.youtube.com/watch?v=0bxZylSiJ78")
    points -= 50
    t.sleep(2)
    pg.alert ("I hate vegetables!")
elif food == "mashed potatoes":
    wb.open ("https://www.delish.com/cooking/recipe-ideas/recipes/a50630/perfect-mashed-potatoes-recipe/")
    points += 8
    t.sleep(2)
    pg.alert ("I love having mashed potatoes on Thanksgiving!")
elif food == "Apple pie":
    wb.open ("https://www.pillsbury.com/recipes/perfect-apple-pie/1fc2b60f-0a4f-441e-ad93-8bbd00fe5334")
    points += 9
    t.sleep(2) 
    pg.alert ("I also love having apple pie on Thanksgiving")
elif food == "sushi":
    wb.open ("https://www.allrecipes.com/video/303/how-to-make-sushi-rolls/")
    points += 8
    t.sleep(2)
    pg.alert ("I love salmon rolls.")
else:
    pg.alert ("Your favorite foods is" + food)
    
candy = pg.prompt ("what is your favorite candy?")
if candy == "Milky way":
    wb.open ("https://www.youtube.com/watch?v=4W8VA93rP9w")
    points += 12
    t.sleep(2)
    pg.alert ("I love caramel and chocolate!")
elif candy == "sour patch kids":
    wb.open ("https://www.tastemade.com/videos/diy-sour-patch-kids")
    points += 7
    t.sleep(2)
    pg.alert ("They are sour, but sweet!")
elif candy == "Three Musketeers":
    wb.open ("https://www.youtube.com/watch?v=sYanvjtt-ws")
    points += 8 
    t.sleep(2)
    pg.alert ("I love three musketeers!")
elif candy == "Snickers":
    wb.open ("https://www.youtube.com/watch?v=1IlOh1cXZdM")
    points += 9
    t.sleep(2)
    pg.alert ("Nuts and chocolate are the best!")
elif candy == "Kitkat":
    wb.open ("https://www.cnn.com/videos/cnnmoney/2018/06/22/chipotle-comeback-new-menu-quesadilla-milkshake-tostada-orig-cnnmoney.cnnmoney/video/playlists/cnnmoney/")
    points += 10
    t.sleep(2)
    pg.alert ("I love vanilla wafers covered in chocolate!")
elif candy == "M&M's":
    wb.open ("https://www.youtube.com/watch?v=NkZN3xr0sHs")
    points += 12
    t.sleep(2)
    pg.alert ("so many different colors!")
else:
    pg.alert ("Your favorite candys is" + candy)

movies = pg.prompt ("what is your favorite movies?")
if movies == "Jumanji":
    wb.open ("https://www.youtube.com/watch?v=2QKg5SZ_35I")
    points += 10
    t.sleep (2)
    pg.alert ("It's exciting and adventurous!")
elif movies == "Star Wars":
    wb.open ("https://www.youtube.com/watch?v=Q0CbN8sfihY")
    points += 1
    t.sleep (2)
    pg.alert ("I have never seen it!")
elif movies == "Annie":
    wb.open ("https://www.youtube.com/watch?v=Tg7JWB2SR7E")
    points += 6
    t.sleep (2)
    pg.alert ("I have seen it three times!")
elif movies == "Cinderella":
    wb.open ("https://www.youtube.com/watch?v=20DF6U1HcGQ")
    points += 4
    t.sleep (2)
    pg.alert (" It's the best disney princess movie!")
elif movies == "Mean Girls":
    wb.open ("https://www.youtube.com/watch?v=KAOmTMCtGkI")
    points += 9 
    t.sleep (2)
    pg.alert ("I have seen the play on Broadway!")
elif movies == "Ghost Busters":
    wb.open ("https://www.youtube.com/watch?v=vntAEVjPBzQ")
    points += 9 
    t.sleep (2)
    pg.alert ("I love watching it close to Halloween!")
else:
    pg.alert ("Your favorite moviess is" + movies)

sport = pg.prompt ("what is your favorite sport?")
if sport == "Soccer":
    wb.open ("https://www.youtube.com/watch?v=5__1PwHRpAM")
    points += 8 
    t.sleep (2)
    pg.alert ("I have been playing soccer since I was three!")
elif sport == "Ice Hockey":
    wb.open ("https://www.youtube.com/watch?v=2iGAIi3IUSg")
    points += 8 
    t.sleep (2)
    pg.alert ("I have been playing ice hockey since I was five!")
elif sport == "Lacrosse":
    wb.open ("https://www.youtube.com/watch?v=-sKVeYqXKuI")
    points += 8
    t.sleep (2)
    pg.alert ("I started playing lacrosse in first grade.")
elif sport == "Squash":
    wb.open ("https://www.youtube.com/watch?v=RTSLbcmesjA")
    points += 4 
    t.sleep (2)
    pg.alert ("I have been playing squash since I was seven.")
elif sport == "Tennis":
    wb.open ("https://www.youtube.com/watch?v=lMQ2dJ3E-nY")
    points += 4
    t.sleep (2)
    pg.alert ("I like to play tennis in the summer.")
elif sport == "Swimming":
    wb.open ("https://www.youtube.com/watch?v=sQsgUM3HvWI")
    points += 8
    t.sleep (2)
    pg.alert ("I used to be on a swim team.")
else:
    pg.alert ("Your favorite sport is" + sport)

clothes = pg.prompt ("what is your favorite clothes?")
if clothes == "dress":
    wb.open ("https://www.youtube.com/watch?v=UQJwdEEsLog")
    points += 6
    t.sleep (2)
    pg.alert ("I like to wear dresses in the summer and for special occasions!")
elif clothes == "rain boots":
    wb.open ("https://www.youtube.com/watch?v=lNKGCJVVNJE")
    points += 4 
    t.sleep (2)
    pg.alert ("I wear rain boots when it rains outside!")
elif clothes == "pants":
    wb.open ("https://www.youtube.com/watch?v=Orbd-CBUwVM")
    points += 3 
    t.sleep (2)
    pg.alert ("I only wear pants if it's cold or if I have too.")
elif clothes == "shorts":
    wb.open ("https://www.youtube.com/watch?v=Orbd-CBUwVM")
    points += 3 
    t.sleep (2)
    pg.alert ("I like wearing shorts when it's nice outside.")
elif clothes == "Sweater":
    wb.open ("https://www.youtube.com/watch?v=Wgck2mu3YBs")
    points += 2
    t.sleep (2)
    pg.alert ("I wear a sweater to school everyday.")
elif clothes == "skirt":
    wb.open ("https://www.youtube.com/watch?v=_SYsZ194zk8")
    points += 2
    t.sleep (2)
    pg.alert ("I also wear a skirt to school everyday.")
else:
    pg.alert ("Your favorite clothes is" + clothes)


pg.alert(points)
