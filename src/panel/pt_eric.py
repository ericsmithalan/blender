import bpy
from .ot_cursor_snap import OT_CursorSnap
from .ot_apply_snap import OT_ApplySnap
from .ot_add_single_vertex import OT_Add_Single_Vertex
from .ot_mouse_position import OT_Mouse_Position


class PT_Eric(bpy.types.Panel):
    bl_idname = "TESTADDON_PT_TestPanel"
    bl_label = "Erics Addons"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        # EDIT MODE
        if context.active_object.mode == 'EDIT':
            split = layout.split(factor=0.8)
            col = split.column()

            col.label(text=OT_CursorSnap.bl_label)

            col = split.column(align=False)

            col.operator(OT_CursorSnap.bl_idname,
                         text="", icon='PLAY')

            row = layout.row()

            row.operator(OT_Mouse_Position.bl_idname)

        # OBJECT MODE
        if context.active_object.mode == 'OBJECT':
            split = layout.split(factor=0.8)
            col = split.column()

            col.label(text=OT_ApplySnap.bl_label)

            col = split.column(align=True)

            col.operator(OT_ApplySnap.bl_idname,
                         text="", icon='PLAY')

        # row = layout.row()
        # layout.label(text=str(count))
