from bpy.types import Panel, Operator, Context


def panel_grid_with_operator(self: Panel, operator: Operator, factor: float = 0.8):
    layout = self.layout
    layout.row()
    text = ""
    icon = "FILE"

    if (operator.bl_button_text):
        text = operator.bl_button_text

    if (operator.bl_icon):
        icon = operator.bl_icon

    split1 = layout.split(factor=factor)

    col1a = split1.column()
    col1a.label(text=operator.bl_label)

    col1b = split1.column(align=False)

    col1b.operator(operator.bl_idname,
                   text=text, icon=icon)
