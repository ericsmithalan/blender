import bpy


class OT_MouseClickSingleVertext(bpy.types.Operator):
    bl_idname = "object.mouse_click_single_vertex"
    bl_label = "Mouse Click"
    bl_description = "Mouse Click"
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    def execute(self, context):
        print(self.value)
        if (self.is_active == True):
            bpy.ops.mesh.primitive_vert_add()
            print("added")
        # context.object.location.x = self.value / 100.0
        return {'FINISHED'}

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':  # Apply
            self.value = event.mouse_x
            self.execute(context)
        elif event.type == 'LEFTMOUSE':  # Confirm
            self.is_active = True
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:  # Cancel
            context.object.location.x = self.init_loc_x
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        self.init_loc_x = context.object.location.x
        self.value = event.mouse_x
        self.is_active = False
        self.execute(context)

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
