import bpy


def set_distance(self, value):
    return self.get("distance", value)


def get_distance(self):
    return self.get("distance")


PROPS = [
    ('distance', bpy.props.FloatProperty(name='Distance',
     default=0, get=get_distance, set=set_distance)),
]
