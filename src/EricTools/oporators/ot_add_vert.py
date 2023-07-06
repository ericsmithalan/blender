import bpy


class OT_AddVert(bpy.types.Operator):
    bl_idname = "object.add_vert"
    bl_label = "Add Vertex"
    bl_description = "Add Vertext to Cursor"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH' and obj.mode == 'EDIT')

    def execute(self, context):
        bpy.ops.mesh.primitive_vert_add()
        return {'FINISHED'}
