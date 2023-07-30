import bpy

from bpy.types import PropertyGroup, Object
from bmesh.types import BMVert
from bpy.props import StringProperty, BoolProperty,  PointerProperty, FloatProperty, IntProperty


class EASToolsProps(PropertyGroup):
    obj: PointerProperty(type=Object)
    pointA: PointerProperty(type=Object)
    pointB: PointerProperty(type=Object)

    x: BoolProperty()
    y: BoolProperty()
    z: BoolProperty()
