import bpy
from ..oporators.ot_cursor_snap import OT_CursorSnap
from ..oporators.ot_apply_snap import OT_ApplySnap
from ..oporators.ot_add_vert import OT_AddVert
from ..oporators.ot_add_lines import OT_AddLines


class PT_MainPanel(bpy.types.Panel):
    bl_idname = "MainPanel"
    bl_label = "Eric's Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        # OT_CursorSnap
        split1 = layout.split(factor=0.8)
        col1 = split1.column()
        col1.label(text=OT_CursorSnap.bl_label)
        col1 = split1.column(align=False)
        col1.operator(OT_CursorSnap.bl_idname,
                      text="", icon='PIVOT_CURSOR')

        # OT_ApplySnap
        split2 = layout.split(factor=0.8)
        col2 = split2.column()
        col2.label(text=OT_ApplySnap.bl_label)
        col2 = split2.column(align=True)
        col2.operator(OT_ApplySnap.bl_idname,
                      text="", icon='PIVOT_BOUNDBOX')

        # OT_AddLines
        split3 = layout.split(factor=0.8)
        col3 = split3.column()
        col3.label(text=OT_AddLines.bl_label)
        col3 = split3.column(align=True)
        col3.operator(OT_AddLines.bl_idname,
                      text="", icon='DECORATE')

        # OT_AddVert
        split4 = layout.split(factor=0.8)
        col4 = split4.column()
        col4.label(text=OT_AddVert.bl_label)
        col4 = split4.column(align=True)
        col4.operator(OT_AddVert.bl_idname,
                      text="", icon='DECORATE')
