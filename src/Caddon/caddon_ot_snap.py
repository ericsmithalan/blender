import bpy


class CADDON_OT_Snap(bpy.types.Operator):
    bl_idname = "object.caddon_ot_snap"
    bl_label = "Snap"
    bl_description = "Snap Cursor and Origin to Active"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "SNAP_FACE_CENTER"
    bl_button_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == "MESH" and obj.mode == 'EDIT')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
