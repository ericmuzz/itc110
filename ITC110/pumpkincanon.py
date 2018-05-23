import math

def main():
    angle = float(input("Enter the launch angle(in degrees): "))
    speed = float(input("Enter the initial velocity (in m/s): "))
    initial_height = float(input("Enter the initial height(in m): "))
    time = 0.1

#pumkin start position
    pumpkin_x = 0
    pumpkin_y = initial_height

#pumpkin firing velocity
    theta = math.radians(angle)
    x_velocity = speed * math.cos(theta)
    y_velocity = speed * math.sin(theta)

    while pumpkin_y >= 0:
        pumpkin_x = pumpkin_x + (x_velocity * time)

        new_y_velocity = y_velocity - time * 9.8 #m/s^2
        pumpkin_y = pumpkin_y + time * (y_velocity + new_y_velocity) / 2.0
        y_velocity = new_y_velocity

        print("The pumpkin is at {0}, {1}".format(pumpkin_x, pumpkin_y))
    print("The pumpkin traveled {0} meters".format(pumpkin_x))

main()
