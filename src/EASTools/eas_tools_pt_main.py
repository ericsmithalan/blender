import bpy
from bpy.types import Context
from .eas_utils import layout_2_columns_operator
from .eas_tools_ot_template import EASTools_OT_Template
from .eas_tools_ot_align import EASTools_OT_Align


class EASTools_PT_Main(bpy.types.Panel):
    bl_idname = "EASTools_PT_Main"
    bl_label = "EAS Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "EAS Tools"

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = False
        layout.use_property_decorate = False
        scene = context.scene
        sceneProps = scene.eas_tools

        layout_2_columns_operator(
            self=self, operator=EASTools_OT_Template)

        layout_2_columns_operator(
            self=self, operator=EASTools_OT_Align)

        box = layout.box()
        box.label(text="Show/Hide EASToolsProps")
        row = box.row(align=True)
        split = layout.split(factor=0.5)
        row = split.row(align=True)

        row.prop(sceneProps, 'x', text="X", toggle=1)
        row.prop(sceneProps, 'y', text="Y", toggle=1)
        row.prop(sceneProps, 'z', text="Z", toggle=1)
