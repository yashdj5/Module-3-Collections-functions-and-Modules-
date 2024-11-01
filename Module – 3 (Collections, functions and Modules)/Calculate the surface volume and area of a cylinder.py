def cylinder_volume_area(radius, height):
    volume = math.pi * radius**2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area

print("Volume and surface area of cylinder:", cylinder_volume_area(3, 5))
