from pycatia import catia
from src.get_properties import CatPartProperties  # replace with the actual module name

def main(file_path: str):

    # Open the CATPart document
    cat_part = CatPartProperties(file_path)
    cat_part._load_document()  # load the CATPart into spa_workbench

    try:
        mass = cat_part.calculate_mass()
        volume = cat_part.calculate_volume()
        surface_area = cat_part.calculate_surface_area()
        material = cat_part.get_material_name()
        
        print(f"Properties for {file_path}:")
        print(f"Mass: {mass} kg")
        print(f"Volume: {volume} mm³")  # units depend on your CATIA settings
        print(f"Surface Area: {surface_area} mm²")
        print(f"Material: {material}")

    finally:
        cat_part.close()  # always close the document

if __name__ == "__main__":

    file_path = r"D:\Catia V5\Catia Assembly\screw jack assembly\special washer.CATPart" #Enter your file path
    main(file_path)
