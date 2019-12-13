import turtle as tu
tu.shape('turtle')

#maison

for i in range(4):
    tu.fd(80)
    tu.rt(-90)

#porte

tu.color('red')
tu.up()
tu.fd(20)
tu.down()
tu.rt(-90)
for i in range(3):
    tu.fd(40)
    tu.rt(90)

#toit

tu.color('green')
tu.up()
tu.goto(0, 80)
tu.down()
tu.seth(60)
tu.fd(80)
tu.rt(120)
tu.fd(80)

tu.done()
