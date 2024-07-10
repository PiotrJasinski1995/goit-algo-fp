import turtle

def pythagorean_tree(point_1_x, point_1_y, point_2_x, point_2_y, order=0):
    if order > 0:
        x1,x2 = point_1_x, point_2_x
        y1,y2 = point_1_y, point_2_y
        dx,dy = x2 - x1, y1 - y2
        x3,y3 = x2 - dy, y2 - dx
        x4,y4 = x1 - dy, y1 - dx
        x5,y5 = x4 + (dx - dy) / 2, y4 - (dx + dy) / 2
        turtle.goto(x1, y1)
        turtle.pd()

        for x, y in ((x2, y2), (x3, y3), (x4, y4), (x1, y1)):
            turtle.goto(x, y)
        
        turtle.pu()
        pythagorean_tree(x4,y4, x5,y5, order - 1)
        pythagorean_tree(x5,y5, x3,y3, order - 1)


def draw_pythagorean_tree(order):
    window = turtle.Screen()
    window.bgcolor("white")

    turtle.speed(0)  
    turtle.pu()
    pythagorean_tree(0, 100, 100, 100, order)
    window.mainloop()


def main():
    while True:
        order_level = input('Type order level for pythagorean tree:\n')

        if not order_level.isnumeric():
            print('Order level should be a number greater than or equal 0!')
        else:
            draw_pythagorean_tree(int(order_level))
            break
    
    print('\nGoodbye!')
          

if __name__ == '__main__':
    main()
