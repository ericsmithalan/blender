import bpy


class OT_DrawSomething(bpy.types.Operator):
    bl_idname = "object.draw_something"
    bl_label = "Draw Something"
    bl_description = "Draw Something"
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
