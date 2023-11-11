import bpy
import datetime

# Given a list of list of objects, hide all of the listed objects, then render
# a series of renders that progressively unhide the listed objects. Useful for
# creating a series of "breakdown" images that show how each set of objects
# contributes to the scene.

OUTPUT_FILENAME = "//renders/breakdown/breakdown-render-%02d.exr"

# Modify these lists to have the names of the objects you want to hide, then
# unhide. Each list equals one render. Objects not listed here will not be
# touched.
OBJECTS = [
    ["object_01", "light_01"], # breakdown-render-00.exr will have these objects unhidden
    ["object_02", "object_03", "object_04"], # breakdown-render-01.exr will have these objects plus all of the ones above
    ["light_02", "light_03", "light_04"]
]

FLAT_OBJECTS = [item for sublist in OBJECTS for item in sublist]


for lt in FLAT_OBJECTS:
    obj = bpy.data.objects[lt]
    obj.hide_render = True

old_output_path = bpy.data.scenes["Scene"].render.filepath

for i, lt_group in enumerate(OBJECTS):
    for lt in lt_group:
        obj = bpy.data.objects[lt]
        obj.hide_render = False
    bpy.data.scenes["Scene"].render.filepath = OUTPUT_FILENAME % (i,)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z%z") + ": Starting render to " + bpy.data.scenes["Scene"].render.filepath)
    bpy.ops.render.render(write_still=True)
