import bpy


class OT_ApplySnap(bpy.types.Operator):
    bl_idname = "object.apply_snap"
    bl_label = "Apply All Center"
    bl_description = "Apply Transforms and Set Cursor to Center"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH' and obj.mode == 'OBJECT')

    def execute(self, context):
        bpy.ops.object.transform_apply(
            location=True, rotation=True, scale=True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

        return {'FINISHED'}
