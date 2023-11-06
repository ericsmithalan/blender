import bpy
from ..utils.panel_grid_with_operator import panel_grid_with_operator
from ..operators.caddon_ot_cursor_to_selected import CADDON_OT_CursorToSelected
from ..operators.caddon_ot_origin_to_selected import CADDON_OT_OriginToSelected
from ..operators.caddon_ot_snap_apply_all_transforms import CADDON_OT_SnapApplyAllTransforms
from bpy.types import Panel, Operator


class CADDON_PT_Main(bpy.types.Panel):
    bl_idname = "CADDON_PT_main"
    bl_label = "Caddon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Item"
    bl_order = 0

    def draw(self, context):

        panel_grid_with_operator(
            self=self, operator=CADDON_OT_OriginToSelected)

        panel_grid_with_operator(
            self=self, operator=CADDON_OT_CursorToSelected)

        panel_grid_with_operator(
            self=self, operator=CADDON_OT_SnapApplyAllTransforms)
