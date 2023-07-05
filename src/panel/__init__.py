import bpy
from .ot_cursor_snap import *
from .pt_eric import *
from .ot_apply_snap import *
from .ot_add_single_vertex import *
from .ot_mouse_position import *

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
    OT_ApplySnap,
    OT_Add_Single_Vertex,
    OT_Mouse_Position
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
