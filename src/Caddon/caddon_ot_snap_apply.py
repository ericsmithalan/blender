import bpy


class CADDON_OT_SnapApply(bpy.types.Operator):
    bl_idname = "object.caddon_ot_snap_apply"
    bl_label = "Snap & Apply"
    bl_description = "Snap Cursor"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "CURSOR"
    bl_button_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == "MESH" and obj.mode == 'OBJECT')

    def execute(self, context):
        bpy.ops.object.transform_apply(
            location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(
            type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
        return {'FINISHED'}
