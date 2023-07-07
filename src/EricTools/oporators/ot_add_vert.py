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
        bpy.ops.mesh.select_mode(type="VERT")

        obj = context.active_object
        obj.update_from_editmode()

        old_cursor_loc = context.scene.cursor.location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.mesh.primitive_vert_add()

        context.scene.cursor.location = old_cursor_loc

        return {'FINISHED'}
