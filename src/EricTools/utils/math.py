from mathutils import Vector
import numpy


def vector_sum(vectors):
    return sum(vectors, Vector())


def coordinates_center(coordinates):
    return vector_sum((Vector(coord) for coord in coordinates)) / len(coordinates)


# NOT USED YET
def get_center_between_verts(vert1, vert2, center=0.5):
    return get_center_between_points(vert1.co, vert2.co, center=center)


def get_center_between_points(point1, point2, center=0.5):
    return point1 + (point2 - point1) * center


def coordinate_overlap2d(location1, location2, size=1):
    return (location1 - location2).length < size


def coordinates_dimension(coordinates):
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    z = [coord[2] for coord in coordinates]

    return Vector((max(x), max(y), max(z))) - Vector((min(x), min(y), min(z)))


def coordinate_bounds(coordinates):
    x = [c[0] for c in coordinates]
    y = [c[1] for c in coordinates]
    z = [c[2] for c in coordinates]

    def current_x(i): return min(x) if i < 4 else max(x)
    def current_y(i): return min(y) if i in {0, 1, 4, 5} else max(y)
    def current_z(i): return min(z) if i in {0, 3, 4, 7} else max(z)

    return [Vector((current_x(i), current_y(i), current_z(i))) for i in range(8)]


def max_distance(coordinates):
    return max([(v1 - v2).length for v1 in coordinates for v2 in coordinates])


def transform_coordinates(matrix, coords):
    return numpy.array(numpy.delete(numpy.append(coords, numpy.ones([len(coords), 1], dtype='f'), axis=1) @ numpy.array(matrix.transposed(), dtype='f'), [3], 1), dtype='f', copy=False, order='C')
