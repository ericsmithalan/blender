import bpy
from .eas_tools_pt_main import EASTools_PT_Main
from .eas_tools_ot_template import EASTools_OT_Template
from .eas_tools_ot_align import EASTools_OT_Align
from bpy.types import Scene
import eas_tools_props


bl_info = {
    "name": "EAS Tools",
    "description": "Common Tools",
    "author": "Eric Smith",
    "location": "View3D",
    "blender": (3, 5, 0),
    "version": (1, 0, 0),
    "category": "3D View"
}

classes = (
    eas_tools_props.EASToolsProps,
    EASTools_OT_Template,
    EASTools_OT_Align,
    EASTools_PT_Main,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    Scene.eas_tools = bpy.props.PointerProperty(
        type=eas_tools_props.EASToolsProps)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
