# Developers: K.Kravtsov  --  %
#             A.Mikhailov --  %

import turtle as t
import random as r
colors = ["green", "yellow", "blue", "brown", "red", "orange", "pink", "black"]
t.speed(0)

def tree(length):
    """

    :param length:
    :return:
    """

    t.down()
    if length > 5:
        t.forward(length)
        t.right(30)
        tree(0.6 * length)
        t.left(60)
        tree(0.6 * length)
        t.right(30)
        t.backward(length)


def koch_line(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration == 0:
        t.forward(length)
    else:
        koch_line(length / 3, num_iteration - 1)
        t.left(60)
        koch_line(length / 3, num_iteration - 1)
        t.right(120)
        koch_line(length / 3, num_iteration - 1)
        t.left(60)
        koch_line(length / 3, num_iteration - 1)


def k_snowflake(length, num_corners, num_iteration):
    """

    :param length:
    :param num_corners:
    :param num_iteration:
    :return:
    """

    t.down()
    for i in range(num_corners):
        koch_line(length, num_iteration)
        t.right(180 - ((180 * (num_corners - 2)) / num_corners))


def ice_fractal_1(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration == 0:
        t.forward(length)
    else:
        ice_fractal_1(length / 2, num_iteration - 1)
        t.left(90)
        ice_fractal_1(length / 3, num_iteration - 1)
        t.left(180)
        ice_fractal_1(length / 3, num_iteration - 1)
        t.left(90)
        ice_fractal_1(length / 2, num_iteration - 1)


def i_f_1_snowflake(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    for i in range(4):
        ice_fractal_1(length, num_iteration)
        t.left(90)
        ice_fractal_1(length, num_iteration)
        t.left(180)


def ice_fractal_2(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration == 0:
        t.forward(length)
    else:
        ice_fractal_2(length/2, num_iteration - 1)
        for i in range(2):
            t.left(120)
            ice_fractal_2(length / 4, num_iteration - 1)
            t.left(180)
            ice_fractal_2(length / 4, num_iteration - 1)
        t.left(120)
        ice_fractal_2(length / 2, num_iteration - 1)


def i_f_2_snowflake(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    for i in range(4):
        ice_fractal_2(length, num_iteration)
        t.left(90)
        ice_fractal_2(length, num_iteration)
        t.left(180)


def branch(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration > 0:
        t.forward(length)
        t.left(45)
        branch(0.3 * length, num_iteration - 1)
        t.right(45)
        branch(0.6 * length, num_iteration - 1)
        t.right(45)
        branch(0.3 * length, num_iteration - 1)
        t.left(45)
        t.backward(length)
    else:
        t.forward(length)
        t.backward(length)


def levy_curve(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration == 0:
        t.forward(length)
    else:
        t.left(45)
        levy_curve(length / 2, num_iteration - 1)
        t.right(90)
        levy_curve(length / 2, num_iteration - 1)
        t.left(45)


def minkowski_curve(length, num_iteration):
    """

    :param length:
    :param num_iteration:
    :return:
    """

    t.down()
    if num_iteration != 0:
        minkowski_curve(length / 4, num_iteration - 1)
        t.left(90)
        minkowski_curve(length / 4, num_iteration - 1)
        t.right(90)
        minkowski_curve(length / 4, num_iteration - 1)
        t.right(90)
        minkowski_curve(length / 2, num_iteration - 1)
        t.left(90)
        minkowski_curve(length / 4, num_iteration - 1)
        t.left(90)
        minkowski_curve(length / 4, num_iteration - 1)
        t.right(90)
        minkowski_curve(length / 4, num_iteration - 1)
    else:
        t.forward(length)


def dragon(length, num_iteration, turn):
    """

    :param length:
    :param num_iteration:
    :param turn:
    :return:
    """

    t.down()
    if num_iteration > 0:
        t.left(90 * turn)
        dragon(length / 2, num_iteration - 1, 1)
        t.right(90 * turn)
        dragon(length / 2, num_iteration - 1, -1)
        t.left(90 * turn)
    else:
        t.forward(length)


print('''1. Кривая Коха
2. Снежинка Коха.
3. Ледяной фрактал (пример 1)
4. Ледяной фрактал (пример 2)
5. Снежинка к ледяному фракталу (пример 1)
6. Снежинка к ледяному фракталу (пример 2)
7. Кривая Минковского
8. Кривая Леви
9. Построение двоичного дерева
10. Дракон Хартера-Хейтуэя
11. Ветвь''')
fractal = int(input('Введите номер для построения фрактала:'))
if fractal == 1:
    koch_line(lenght, num_iteration)
    t.mainloop()

elif fractal == 2:
    k_snowflake(lenght, num_iteration)
    t.mainloop()

elif fractal == 3:
    ice_fractal_1(lenght, num_iteration)
    t.mainloop()

elif fractal == 4:
    ice_fractal_2(lenght, num_iteration)
    t.mainloop()

elif fractal == 5:
    i_f_1_snowflake(lenght, num_iteration)
    t.mainloop()

elif fractal == 6:
    i_f_2_snowflake(lenght, num_iteration)
    t.mainloop()

elif fractal == 7:
    minkowski_curve(lenght, num_iteration)
    t.mainloop()

elif fractal == 8:
    levy_curve(lenght, num_iteration)
    t.mainloop()

elif fractal == 9:
    tree(lenght, num_iteration)
    t.mainloop()

elif fractal == 10:
    dragon(lenght, num_iteration, turn)
    t.mainloop()

elif fractal == 11:
    branch(lenght, num_iteration, turn)
    t.mainloop()