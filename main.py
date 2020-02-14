# Developers: K.Kravtsov  --  %
#             A.Mikhailov --  %

#import turtle
print('''1. Кривая Коха
2. Снежинка Коха.
3. Ледяной фрактал (пример 1)
4. Ледяной фрактал (пример 2)
5. Снежинка к ледяному фракталу (пример 1) c построением внешнего и внутреннего фракталов.
6. Снежинка к ледяному фракталу (пример 2) c построением внешнего и внутреннего фракталов.
7. Кривая Минковского
8. Кривая Леви
9. Построение двоичного дерева
10. Дракон Хартера-Хейтуэя''')
fractal = int(input('Введите номер для построения фрактала:'))
if fractal == 1:
    koch_line(lenght, num_iteration)

elif fractal == 2:
    k_snowflake(lenght, num_iteration)

elif fractal == 3:
    ice_fractal_1(lenght, num_iteration)

elif fractal == 4:
    ice_fractal_2(lenght, num_iteration)

elif fractal == 5:
    i_f_1_snowflake(lenght, num_iteration)

elif fractal == 6:
    i_f_2_snowflake(lenght, num_iteration)

elif fractal == 7:
    minkowski_curve(lenght, num_iteration)

elif fractal == 8:
    levy_curve(lenght, num_iteration)

elif fractal == 9:
    tree(lenght, num_iteration)

elif fractal == 10:
    dragon(lenght, num_iteration, turn)