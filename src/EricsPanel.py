import bpy


bl_info = {
    "name": "Erics Addons",
    "description": "Addon for testing",
    "author": "Tester",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "category": "Eric",
}


class OT_CursorSnapOperator(bpy.types.Operator):
    """Snap Cursor Operator"""
    bl_idname = "object.cursor_snap_operator"
    bl_label = "Snap Cursor Operator"
    bl_options = {'REGISTER', 'UNDO'}

    # @classmethod
    # def poll(cls, context):
    #     obj = context.active_object
    #     return (obj is not None and obj.type == 'MESH')

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
        bpy.ops.object.editmode_toggle()
        return {'FINISHED'}


# def register():
#     bpy.utils.register_class(OT_CursorSnapOperator)


# def unregister():
#     bpy.utils.unregister_class(OT_CursorSnapOperator)


class ERICSADDONS_PT_Eric(bpy.types.Panel):
    bl_idname = "TESTADDON_PT_TestPanel"
    bl_label = "Erics Addons"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Erics Addons"
    bl_context = "mesh_edit"

    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.label(text="Snap Cursor to Selected")

        row = layout.row()
        row.operator(OT_CursorSnapOperator.bl_idname)


def register():
    bpy.utils.register_class(ERICSADDONS_PT_Eric)
    bpy.utils.register_class(OT_CursorSnapOperator)


def unregister():
    bpy.utils.unregister_class(ERICSADDONS_PT_Eric)
    bpy.utils.unregister_class(OT_CursorSnapOperator)


if __name__ == "__main__":
    register()
