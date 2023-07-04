import bpy
from .ot_cursor_snap import OT_CursorSnap


class PT_Eric(bpy.types.Panel):
    bl_idname = "TESTADDON_PT_TestPanel"
    bl_label = "Erics Addons"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Erics Addons"
    bl_context = "mesh_edit"

    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator(OT_CursorSnap.bl_idname)

        layout.operator('script.reload_my_scripts')

        # row = layout.row()
        # layout.label(text=str(count))
