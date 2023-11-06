import bpy
from mathutils import Vector
from bpy.props import FloatVectorProperty, FloatProperty


class CADDON_OT_View(bpy.types.Operator):
    bl_idname = "view3d.modal_operator"
    bl_label = "Simple View Operator"

    offset: FloatVectorProperty(
        name="Offset",
        size=3,
    )

    distance: FloatProperty(name="Distance")

    def execute(self, context):
        v3d = context.space_data
        rv3d = v3d.region_3d

        rv3d.view_location = self._initial_location

    def modal(self, context, event):
        v3d = context.space_data
        rv3d = v3d.region_3d

        print(event.type)

        # if event.type == 'MOUSEMOVE':
        #     self.offset = (self._initial_mouse -
        #                    Vector((event.mouse_x, event.mouse_y, 0.0))) * 0.02
        #     self.execute(context)
        #     context.area.header_text_set(
        #         "Offset %.4f %.4f %.4f" % tuple(self.offset))

        # elif event.type == 'LEFTMOUSE':
        #     context.area.header_text_set(None)
        #     return {'FINISHED'}

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            rv3d.view_location = self._initial_location
            context.area.header_text_set(None)
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            v3d = context.space_data
            rv3d = v3d.region_3d

            if rv3d.view_perspective == 'CAMERA':
                rv3d.view_perspective = 'PERSP'

            self._initial_mouse = Vector((event.mouse_x, event.mouse_y, 0.0))
            self._initial_location = rv3d.view_location.copy()

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "Active space must be a View3d")
            return {'CANCELLED'}
