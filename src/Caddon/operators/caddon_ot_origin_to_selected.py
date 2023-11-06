import bpy


class CADDON_OT_OriginToSelected(bpy.types.Operator):
    bl_idname = "object.caddon_ot_origin_to_selected"
    bl_label = "Origin To Selected"
    bl_description = "Origin to selected object"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "OBJECT_ORIGIN"
    bl_button_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.mode == 'EDIT')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
