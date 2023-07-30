import bpy
from .caddon_ot_snap import CADDON_OT_Snap
from .caddon_pt_main import CADDON_PT_Main
from .caddon_ot_snap_selected import CADDON_OT_SnapSelected
from .caddon_ot_snap_apply import CADDON_OT_SnapApply
from bpy.types import Scene

bl_info = {
    "name": "Caddon",
    "description": "Cad Tools",
    "author": "Eric Smith",
    "location": "View3D",
    "blender": (3, 5, 0),
    "version": (1, 0, 0),
    "category": "3D View"
}

classes = (
    CADDON_OT_Snap,
    CADDON_PT_Main,
    CADDON_OT_SnapSelected,
    CADDON_OT_SnapApply
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
