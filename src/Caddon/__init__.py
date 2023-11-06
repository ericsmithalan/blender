import bpy
from .classes import CLASSES
from .props import PROPS


bl_info = {
    "name": "Caddon",
    "description": "Cad Tools",
    "author": "Eric Smith",
    "location": "View3D",
    "blender": (3, 5, 0),
    "version": (1, 0, 0),
    "category": "3D View"
}


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
