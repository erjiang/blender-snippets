import bpy

# Change all objects (excluding those with the word "volume" in their name) to
# be a matteObject and holdout

for obj_name in bpy.data.objects.keys():
    if 'volume' in obj_name:
        continue
    bpy.data.objects[obj_name].renderman.rman_matteObject = '1'
    bpy.data.objects[obj_name].renderman.rman_holdout = '1'

# and the same thing, but setting matteObject and holdout to "inherit" (the
# default value)

for obj_name in bpy.data.objects.keys():
    if 'volume' in obj_name:
        continue
    bpy.data.objects[obj_name].renderman.rman_matteObject = '1'
    bpy.data.objects[obj_name].renderman.rman_holdout = '1'
