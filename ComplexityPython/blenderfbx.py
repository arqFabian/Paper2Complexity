import bpy
import os


def export_collection_to_fbx(collection_name, folder_name):
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

# export_collection_to_fbx("P1", "UnityModels\P1")

# export_collection_to_fbx("P2", "UnityModels\P2")

 export_collection_to_fbx("P3", "UnityModels\P3")
