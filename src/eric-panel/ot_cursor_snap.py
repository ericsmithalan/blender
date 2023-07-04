import bpy


class OT_CursorSnap(bpy.types.Operator):
    bl_idname = "object.cursor_snap_operator"
    bl_label = "Snap Cursor Operator"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}
