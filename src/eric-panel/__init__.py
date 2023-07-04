import bpy
from .ot_cursor_snap import *
from .pt_eric import *

bl_info = {
    "name": "Erics Addons",
    "description": "Addon for testing",
    "author": "Tester",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "category": "Eric",
}

classes = (
    OT_CursorSnap,
    PT_Eric,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
