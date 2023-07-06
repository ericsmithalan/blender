import bpy
from ..oporators.ot_cursor_snap import OT_CursorSnap
from ..oporators.ot_apply_snap import OT_ApplySnap
from ..oporators.ot_add_vert import OT_AddVert


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
        split = layout.split(factor=0.8)
        col = split.column()

        col.label(text=OT_CursorSnap.bl_label)

        col = split.column(align=False)

        col.operator(OT_CursorSnap.bl_idname,
                     text="", icon='PLAY')

        # OT_ApplySnap
        split = layout.split(factor=0.8)
        col = split.column()

        col.label(text=OT_ApplySnap.bl_label)

        col = split.column(align=True)

        col.operator(OT_ApplySnap.bl_idname,
                     text="", icon='PLAY')

        # OT_AddVert
        split = layout.split(factor=0.8)
        col = split.column()

        col.label(text=OT_AddVert.bl_label)

        col = split.column(align=True)

        col.operator(OT_AddVert.bl_idname,
                     text="", icon='PLAY')
