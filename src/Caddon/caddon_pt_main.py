import bpy
from .caddon_utils import panel_grid_with_operator
from .caddon_ot_snap import CADDON_OT_Snap
from .caddon_ot_snap_selected import CADDON_OT_SnapSelected
from .caddon_ot_snap_apply import CADDON_OT_SnapApply


class CADDON_PT_Main(bpy.types.Panel):
    bl_idname = "Caddon_PT_Main"
    bl_label = "Caddon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Caddon"

    def draw(self, context):
        panel_grid_with_operator(
            self=self, operator=CADDON_OT_Snap)

        panel_grid_with_operator(
            self=self, operator=CADDON_OT_SnapSelected)

        panel_grid_with_operator(
            self=self, operator=CADDON_OT_SnapApply)
