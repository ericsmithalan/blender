
import bpy


class OT_Add_Single_Vertex(bpy.types.Operator):
    bl_idname = "object.add_single_vertex"
    bl_label = "Add a vertex "
    bl_description = "Add a vertext to the nearest object after clicking mouse"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH')

    def execute(self, context):
        # bpy.ops.mesh.primitive_vert_add()
        return {'FINISHED'}
