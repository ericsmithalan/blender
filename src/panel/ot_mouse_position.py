import bpy


class OT_Mouse_Position(bpy.types.Operator):
    bl_idname = "wm.mouse_position"
    bl_label = "Mouse location"
    isPlaying = False

    x: bpy.props.IntProperty()
    y: bpy.props.IntProperty()

    def execute(self, context):
        self.report({'INFO'}, "Mouse coords are %d %d" % (self.x, self.y))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.x = event.mouse_x
        self.y = event.mouse_y
        return self.execute(context)


# class MousePanel(bpy.types.Panel):
#     bl_label = "Mouse"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "TOOL_PROPS"

#     def draw(self, context):
#         self.layout.operator("wm.mouse_position")


# #
# #   Registration
# #   Not really necessary to register the class, because this happens
# #   automatically when the module is registered. OTOH, it does not hurt either.
# bpy.utils.register_class(SimpleMouseOperator)
# bpy.utils.register_module(__name__)

# # Automatically display mouse position on startup
# bpy.ops.wm.mouse_position('INVOKE_DEFAULT')

# Another test call, this time call execute() directly with pre-defined settings.
# bpy.ops.wm.mouse_position('EXEC_DEFAULT', x=20, y=66)
