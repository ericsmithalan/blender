import bpy
import bgl
import blf
from bpy.props import IntProperty, FloatProperty, FloatVectorProperty
from bpy_extras import view3d_utils
import bpy
import blf
import gpu
from gpu_extras.batch import batch_for_shader
from .ot_cursor_snap import OT_CursorSnap
from mathutils import Vector
from mathutils.interpolate import poly_3d_calc


def add_vert(context):
    bpy.ops.mesh.select_mode(type="VERT")

    obj = context.active_object
    obj.update_from_editmode()

    old_cursor_loc = context.scene.cursor.location.copy()
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.mesh.primitive_vert_add()

    context.scene.cursor.location = old_cursor_loc


def add_empty(location):
    # Create new empty object
    if location:
        bpy.ops.object.empty_add(type="PLAIN_AXES", location=location)
    # Link empty to the current object's collection.
    # empty = bpy.context.scene.objects.active
    # context.object.users_collection[0].objects.link(empty)


def bu_to_inches(scene, d):
    scale = scene.unit_settings.scale_length
    # 1bu = 1 / 0.3048 ft
    return 12 * scale * d / 0.3048


def inches_to_bu(scene, d):
    return d / bu_to_inches(scene, 1)


class ModalMousePosition(bpy.types.Operator):
    bl_idname = "view3d.modal_mouse_position"
    bl_label = "Mouse Position"
    bl_description = "Mouse Position"
    bl_options = {'REGISTER', 'UNDO'}

    mouse_position: FloatVectorProperty(
        subtype="TRANSLATION"
    )
    loc: FloatVectorProperty(
        subtype="TRANSLATION"
    )

    z_position: FloatProperty()

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == 'MESH' and obj.mode == 'EDIT')

    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type == 'MOUSEMOVE':
            self.mouse_position = (event.mouse_region_x,
                                   event.mouse_region_y, self.z_position)
            print(self.mouse_position)

        elif event.type == 'LEFTMOUSE':
            self.mouse_position = (event.mouse_region_x,
                                   event.mouse_region_y, self.z_position)

            region = bpy.context.region
            region3D = bpy.context.space_data.region_3d
            self.selected_object = bpy.context.object

            depsgraph = context.evaluated_depsgraph_get()
            depsgraph.update()

            view_vector = view3d_utils.region_2d_to_vector_3d(
                region, region3D, self.mouse_position)
            # The 3D location in this direction
            self.loc = view3d_utils.region_2d_to_location_3d(
                region, region3D, self.mouse_position, view_vector)
            # The 3D location converted in object local coordinates
            # self.loc = self.selected_object.matrix_local @ self.loc

            # bpy.ops.object.mode_set(mode='OBJECT')

            obj = context.active_object

            ray_direction = Vector(self.loc)

            ray_local = obj.matrix_local @ self.mouse_position

            cast_result = obj.ray_cast(ray_local, ray_direction)

            # mesh = obj.data
            # poly = mesh.polygons[poly_index]

            # corners = [mesh.vertices[vid].co for vid in poly.vertices]
            # bcoords = poly_3d_calc(corners, location)

            # check_location = sum(
            #     [b * c for b, c in zip(bcoords, corners)], Vector(location))

            # o = bpy.data.objects.new("EMPTY", None)
            # o.empty_display_type = "PLAIN_AXES"
            # o.location = check_location
            # bpy.context.collection.objects.link(o)

            # bpy.ops.object.mode_set(mode="EDIT")
            print("")
            print(ray_local)
            print("")
            print(cast_result)
            print("")
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback

            bpy.ops.mesh.select_mode(type="VERT")

            obj = context.active_object
            self.z_position = obj.location.z
            # obj.update_from_editmode()

            self.mouse_position = (0, 0, 0)

            context.window_manager.modal_handler_add(self)

            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}


# bpy.ops.object.modal_mouse_position('INVOKE_DEFAULT')
