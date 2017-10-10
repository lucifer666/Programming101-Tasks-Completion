import math

def fill_tetrahedron(num):
    edge_length = num
    tetrahedron_volume = (1.0/12.0 * math.sqrt(2) * math.pow(edge_length, 3) / 1000)
    return tetrahedron_volume


print("The tetrahedron can be filled with %.2f liters amount of water." % fill_tetrahedron(100))

