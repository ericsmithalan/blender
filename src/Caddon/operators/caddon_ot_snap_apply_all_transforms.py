import bpy


class CADDON_OT_SnapApplyAllTransforms(bpy.types.Operator):
    bl_idname = "object.caddon_ot_snap_apply_all_transforms"
    bl_label = "Apply all transforms"
    bl_description = "Apply all and set origin to center"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "CURSOR"
    bl_button_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.mode == 'OBJECT')

    def execute(self, context):
        bpy.ops.object.transform_apply(
            location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

        return {'FINISHED'}
