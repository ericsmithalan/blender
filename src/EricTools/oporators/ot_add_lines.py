import bpy


class OT_AddLines(bpy.types.Operator):
    bl_idname = "object.add_lines"
    bl_label = "Add Lines"
    bl_description = "Add Lines to something"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH' and obj.mode == 'OBJECT')

    def execute(self, context):
        print("cool")
        return {'FINISHED'}
