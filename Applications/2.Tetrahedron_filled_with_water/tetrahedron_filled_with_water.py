import math

def tetrahedron_filled(tetrahedrons, water):
    max_tetrahedrons_filled = 0
    for tetrahedron_edge in tetrahedrons:
        tetrahedron_volume = (math.sqrt(2) * (tetrahedron_edge ** 3) / 12 / 1000)
        if (water >= tetrahedron_volume):
            water -= tetrahedron_volume
            max_tetrahedrons_filled += 1
    return max_tetrahedrons_filled


print("The number of all tetrahedrons is {}".format(len([100, 20, 30])))
print("The maximum number of tetrahedrons that can be filled with {} liters of water is {} \
	  ".format(10, tetrahedron_filled([100, 20, 30], 10)))