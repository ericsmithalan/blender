import bpy
from bpy.types import Panel, Operator
import bmesh


def layout_2_columns_operator(self: Panel, operator: Operator, factor: float = 0.8):
    layout = self.layout
    layout.row()

    split1 = layout.split(factor=factor)

    col1a = split1.column()
    col1a.label(text=operator.bl_label)

    col1b = split1.column(align=False)

    icon = "FILE"
    text = ""

    if operator.bl_text:
        icon = operator.bl_text

    if operator.bl_icon:
        icon = operator.bl_icon

    col1b.operator(operator.bl_idname,
                   text=text, icon=icon)
