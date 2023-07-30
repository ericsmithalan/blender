import bpy
import bgl
import blf


def draw_callback_px(self, props):
    font_id = 0
    blf.position(font_id, 15, 100, 0)
    blf.size(font_id, 32, 72)
    blf.draw(font_id, "Mouse position: " +
             str(self.mouse_pos[0]) + "/" + str(self.mouse_pos[1]))
    blf.position(font_id, 15, 150, 0)
    blf.size(font_id, 32, 72)
    blf.draw(font_id, "3D position from " + self.object.name + ": " +
             str(self.loc[0]) + "/" + str(self.loc[1]) + "/" + str(self.loc[2]))
