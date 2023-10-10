import bpy
import os

"""#previous script without frame selection
def export_collection_to_fbx1(collection_name, folder_name):
    # Get the directory where the current .blend file is saved
    blend_file_directory = os.path.dirname(bpy.data.filepath)

    # Ensure the Blender file is saved
    if not blend_file_directory:
        raise Exception("Please save the Blender file before running the script.")

    # Set the path where the exported files will be saved
    export_path = os.path.join(blend_file_directory, folder_name)

    # Ensure the path exists
    os.makedirs(export_path, exist_ok=True)

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Reference the collection
    try:
        collection = bpy.data.collections[collection_name]
    except KeyError:
        print(f"No collection found with name {collection_name}")
        collection = None

    # Export each object in the collection
    if collection:
        for obj in collection.objects:
            # Ensure the object is a mesh
            if obj.type == 'MESH':
                # Select the object
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj

                # Set the export path and filename
                file_path = os.path.join(export_path, f"{obj.name}.fbx")

                # Export the object as FBX
                bpy.ops.export_scene.fbx(
                    filepath=file_path,
                    use_selection=True,
                    bake_anim=False
                )

                # Deselect the object after exporting
                obj.select_set(False)

# P1
# export_collection_to_fbx("P1", "fbxModels\P1")

# P2
# export_collection_to_fbx("P2", "fbxModels\P2")

# P3
# export_collection_to_fbx("P3", "fbxModels\P3")"""

# script with frame selection
def export_collection_to_fbx(collection_name, folder_name, frame):
    # Get the directory where the current .blend file is saved
    blend_file_directory = os.path.dirname(bpy.data.filepath)

    # Ensure the Blender file is saved
    if not blend_file_directory:
        raise Exception("Please save the Blender file before running the script.")

    # Set the path where the exported files will be saved
    export_path = os.path.join(blend_file_directory, folder_name)

    # Ensure the path exists
    os.makedirs(export_path, exist_ok=True)

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Set the frame to export
    bpy.context.scene.frame_set(frame)

    # Reference the collection
    try:
        collection = bpy.data.collections[collection_name]
    except KeyError:
        print(f"No collection found with name {collection_name}")
        collection = None

    # Export each object in the collection
    if collection:
        for obj in collection.objects:
            # Ensure the object is a mesh
            if obj.type == 'MESH':
                # Select the object
                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj

                # Set the export path and filename
                file_path = os.path.join(export_path, f"{obj.name}.fbx")

                # Export the object as FBX without baking animations
                bpy.ops.export_scene.fbx(
                    filepath=file_path,
                    use_selection=True,
                    bake_anim=False  # Disable baking animations
                )

                # Deselect the object after exporting
                obj.select_set(False)


# Apply function to export fbx for each collection and frame 12 which is the point where all facades are in place.

# P1
# export_collection_to_fbx("P1", "fbxModels\P1", 12)

# P2
# export_collection_to_fbx("P2", "fbxModels\P2", 12)

# P3
# export_collection_to_fbx("P3", "fbxModels\P3", 12)

