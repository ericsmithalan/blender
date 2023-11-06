import bpy


class CADDON_OT_CursorToSelected(bpy.types.Operator):
    bl_idname = "object.caddon_ot_cursor_to_selected"
    bl_label = "Cursor to selected"
    bl_description = "Snap Cursor To Selected"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "PIVOT_CURSOR"
    bl_button_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.mode == 'EDIT')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {'FINISHED'}
