import bpy
from ..oporators.ot_cursor_snap import OT_CursorSnap
from ..oporators.ot_apply_snap import OT_ApplySnap
from ..oporators.ot_add_vert import OT_AddVert
from ..oporators.ot_add_lines import OT_AddLines
from ..oporators.modal_mouse_position import ModalMousePosition


class PT_MainPanel(bpy.types.Panel):
    bl_idname = "ERIC_PT_MainPanel"
    bl_label = "Eric's Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        # OT_CursorSnap
        split1 = layout.split(factor=0.8)
        col1a = split1.column()
        col1a.label(text=OT_CursorSnap.bl_label)
        col1b = split1.column(align=False)
        col1b.operator(OT_CursorSnap.bl_idname,
                       text="", icon='PIVOT_CURSOR')

        # OT_ApplySnap
        split2 = layout.split(factor=0.8)
        col2a = split2.column()
        col2a.label(text=OT_ApplySnap.bl_label)
        col2b = split2.column(align=True)
        col2b.operator(OT_ApplySnap.bl_idname,
                       text="", icon='PIVOT_BOUNDBOX')

        # ModalMousePosition
        split3 = layout.split(factor=0.8)
        col3a = split3.column()
        col3a.label(text=ModalMousePosition.bl_label)
        col3b = split3.column(align=True)
        col3b.operator(ModalMousePosition.bl_idname,
                       text="", icon='IPO_LINEAR')

        # OT_AddVert
        split4 = layout.split(factor=0.8)
        col4a = split4.column()
        col4a.label(text=OT_AddVert.bl_label)
        col4b = split4.column(align=True)
        col4b.operator(OT_AddVert.bl_idname,
                       text="", icon='DECORATE')
