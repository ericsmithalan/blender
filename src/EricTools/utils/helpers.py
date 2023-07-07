import bpy


def deselect_all(context):
    bpy.ops.object.mode_set(mode='OBJECT')
    for polygon in bpy.context.active_object.data.polygons:
        polygon.select = False
    for edge in bpy.context.active_object.data.edges:
        edge.select = False
    for vertex in bpy.context.active_object.data.vertices:
        vertex.select = False
    bpy.ops.object.mode_set(mode='EDIT')
