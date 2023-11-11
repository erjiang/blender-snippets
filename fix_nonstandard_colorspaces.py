import bpy

# When using an OCIO color profile, images may not have the blender default
# colorspaces and default to some incorrect colorspace. This script goes
# through the images and tries to set them to either "srgb_texture" or "raw"
# depending on whether it should be a image or data texture.

for img_name in bpy.data.images.keys():
    img = bpy.data.images[img_name]
    if img.colorspace_settings.name in ["srgb_texture", "raw"]:
        continue
    if img_name.endswith("_BaseColor.png"):
        print("Setting %s to srgb_texture" % (img_name,))
        # change "srgb_texture" if you're using a different name for image textures
        img.colorspace_settings.name = "srgb_texture"
    # modify these conditions if your textures follow a different format
    elif img_name.endswith("_Normal.png") or img_name.endswith("_Roughness.png") or img_name.endswith("_Displacement.png") or img_name.endswith("_Metallic.png"):
        print("Setting %s to raw" % (img_name,))
        # change "raw" if you're using a different name for data textures
        img.colorspace_settings.name = "raw"
    else:
        print("Don't know what to do with " + img_name)
    
