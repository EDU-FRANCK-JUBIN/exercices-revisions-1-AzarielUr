import turtle as tu

# Toutes les fonctions font revenir la tortue dans la même position que lors de l'appel

# On peut changer la taille des éléments et l'inclinaison sans rien casser

def draw_base(l):
    tu.down()
    tu.color('grey')
    tu.fd(l)
    tu.up()
    tu.back(l)


def draw_hexagon(d):
    tu.down()
    tu.rt(-60)
    for i in range(6):
        tu.fd(d / 2)
        tu.rt(60)

    tu.rt(60)
    tu.fd(d)

    for i in range(2):
        tu.up()
        tu.rt(-120)
        tu.fd(d / 2)
        tu.down()
        tu.rt(-120)
        tu.fd(d)

    # go back to initial pos
    tu.up()
    tu.rt(-120)
    tu.fd(d / 2)
    tu.rt(-120)


def draw_tree(h):
    # arbre
    tu.color('brown')
    tu.down()
    tu.fd(h)

    tu.color('green')
    draw_hexagon(80)

    tu.up()
    tu.back(40)
    tu.rt(-75)
    tu.color('brown')
    tu.down()
    tu.fd(30)
    tu.color('green')
    draw_hexagon(60)

    tu.up()
    tu.back(30)
    tu.rt(-105)
    tu.fd(60)
    tu.rt(105)
    tu.color('brown')
    tu.down()
    tu.fd(30)
    tu.color('green')
    draw_hexagon(60)

    tu.up()
    tu.back(30)
    tu.rt(75)
    tu.back(h - 100)


def draw_bike(l):
    selle_len = l / 2

    tu.color('gold')
    draw_hexagon(l)
    tu.fd(l / 2)
    tu.rt(30)

    tu.color('orange')
    tu.down()
    tu.fd(l)

    tu.rt(25)
    tu.color('red')
    tu.fd(selle_len)
    tu.up()
    tu.back(selle_len)
    tu.rt(-25)

    tu.color('orange')
    tu.down()
    tu.rt(60)
    tu.fd(l)

    tu.rt(60)
    tu.fd(l)

    for i in range(2):
        tu.rt(120)
        tu.fd(l)

    tu.up()
    tu.back(l)
    tu.down()

    tu.rt(-60)
    tu.fd(l)

    tu.up()
    tu.rt(120)
    tu.fd(l)

    tu.rt(-35)
    tu.color('red')
    tu.down()
    tu.fd(selle_len)
    tu.rt(-145)
    tu.fd(selle_len / 1.5)

    tu.up()
    tu.back(selle_len / 1.5)
    tu.rt(145)
    tu.back(selle_len)
    tu.rt(95)
    tu.fd(l)
    tu.rt(210)
    tu.back(l / 2)

    tu.color('gold')
    draw_hexagon(l)
    tu.up()
    tu.rt(-90)
    tu.fd(l * 2)
    tu.rt(90)


def draw_sky(d):
    tu.color('sky blue')
    tu.down()

    for i in range(2):
        draw_hexagon(d)
        tu.rt(90)
        tu.fd(d * 2)
        tu.rt(-90)
        tu.fd((d / 6))

    draw_hexagon(d)

    tu.rt(-90)
    tu.fd((d * 2) / 3)
    tu.rt(90)
    tu.back((d / 3) * 4)

    draw_hexagon(d)

    tu.rt(-90)
    tu.fd(d * 2)
    tu.rt(90)
    tu.back(d / 6)

    draw_hexagon(d)


# DEMO: commenter pour tester normalement
tu.rt(30)

tu.speed(10)
tu.up()
tu.goto(-200, -100)

draw_base(400)

tu.fd(80)
tu.rt(-90)

draw_bike(60)

tu.rt(90)
tu.fd(230)
tu.rt(-90)

draw_tree(175)

tu.rt(-90)
tu.fd(250)
tu.rt(90)
tu.fd(200)

draw_sky(30)

tu.done()
