import bpy
from .oporators.ot_cursor_snap import *
from .panels.pt_main_panel import *
from .oporators.ot_apply_snap import *
from .oporators.ot_add_vert import *

bl_info = {
    "name": "Erics Addons",
    "description": "Addon for testing",
    "author": "Eric Smith",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "category": "Eric",
}

classes = (
    OT_CursorSnap,
    PT_MainPanel,
    OT_ApplySnap,
    OT_AddVert
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
