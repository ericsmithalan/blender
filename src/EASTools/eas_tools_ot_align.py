import typing
import bpy
from bpy.types import Context
from mathutils import Vector


class EASTools_OT_Align(bpy.types.Operator):
    bl_idname = "object.eastools_ot_align"
    bl_label = "Align"
    bl_description = "Template"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "DRIVER_DISTANCE"
    bl_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.object

        if obj is None:
            return False
        else:
            if obj.type in {"MESH", "EMPTY", "CAMERA", "LIGHT"}:
                return True
            else:
                return False

    def execute(self, context: Context):
        if context.area.type == "VIEW_3D" and bpy.context.mode == "EDIT_MESH":
            scene = context.scene
            sceneProps = scene.EASToolsProps

            obj = bpy.context.active_object
            obj.update_from_editmode()

            verts = []

            for vert in obj.data.vertices:
                if vert.select:
                    data = {}
                    data["index"] = vert.index
                    data["location"] = obj.matrix_world @ vert.co
                    verts.append(data)

            if len(verts):
                v1 = Vector(verts[0]["location"])
                v2 = Vector(verts[1]["location"])
                v = v2 - v1
                d0 = v.length
                x = d0
                final_v = Vector(
                    (v1[0] + (v[0] * x), v1[1] + (v[1] * x), v1[2] + (v[2] * x)))
               
                print(final_v)

                # data = {}
                # data["vertex"] = vert
                # data["location"] = obj.matrix_world @ vert.co
                # data["index"] = vert.index
                # verts.append(data)

                # i = 0
                # if len(verts):
                #     for v in verts:
                #         print(i, v)
                #         i += 1

                # sceneProps.pointA = selected[0]["obj"]
                # sceneProps.pointB = selected[1]["obj"]

                # print(sceneProps.pointA, sceneProps.pointB)

        return {'FINISHED'}
