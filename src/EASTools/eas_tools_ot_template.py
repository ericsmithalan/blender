import typing
import bpy
from bpy.types import Context


class EASTools_OT_Template(bpy.types.Operator):
    bl_idname = "object.eastools_ot_template"
    bl_label = "Template"
    bl_description = "Template"
    bl_options = {'REGISTER', 'UNDO'}
    bl_icon = "SELECT_SET"
    bl_text = ""

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj is not None and obj.type == "MESH" and obj.mode == "EDIT")

    def execute(self, context: Context):
        print("Hello World")
        return {'FINISHED'}
