x = float(input())
y = float(input())
h = float(input())

green_paint_per_kvm = 3.4
red_paint_per_kvm = 4.3

front_wall = (x * x) - (1.2 * 2)
back_wall = x * x
side_wall_1 = (x * y) - (1.5 * 1.5)
side_wall_2 = side_wall_1
roof_surface = (x * y) * 2 + 2 * (x * h/2)

total_surface_house = front_wall + back_wall + (side_wall_1 * 2)

green_paint_needed = total_surface_house / 3.4
red_paint_needed = roof_surface / 4.3

print(f'{green_paint_needed:.2f}')
print(f'{red_paint_needed:.2f}')