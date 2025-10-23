from src.calculation import CarbonFootprintCalculator
from pycatia import catia
from src.get_properties import CatPartProperties 
from src.machining_time import extract_cutting_time

def main(cad_file_path, cam_doc_path):

    # Open the CATPart document
    cat_part = CatPartProperties(cad_file_path)
    cat_part._load_document()  # load the CATPart into spa_workbench

    try:
        mass = cat_part.calculate_mass()
        volume = cat_part.calculate_volume()
        surface_area = cat_part.calculate_surface_area()
        material = cat_part.get_material_name()
        
        # print(f"Properties for {file_path}:")
        print(f"Mass: {mass} kg")
        # print(f"Volume: {volume} mm³")  # units depend on your CATIA settings!!! Pl check CATIA units and change accordingly
        # print(f"Surface Area: {surface_area} mm²")
        # print(f"Material: {material}")

    finally:
        cat_part.close()  # close the document

    machining_time_s = extract_cutting_time(cam_doc_path)
    print(f"Machining time in seconds is: {machining_time_s}")

    print("=== Carbon Footprint Calculator ===")
    
    stock_input = input("Enter stock mass (kg): ")
    stock_mass_kg = float(stock_input) 
    power_kw = float(input("Enter machine power (kW): "))
    ef_material = float(input("Enter material emission factor (kg CO2e/kg): "))
    ef_electricity = float(input("Enter electricity emission factor (kg CO2e/kWh): "))
    
    recycling_input = input("Enter recycling credit (0.0 to 1.0, leave blank for 0): ")
    recycling_credit = float(recycling_input) if recycling_input else 0.0

    calculator = CarbonFootprintCalculator(
        mass_kg=mass,
        stock_mass_kg=stock_mass_kg,
        power_kw=power_kw,
        machining_time_s=machining_time_s,
        ef_material=ef_material,
        ef_electricity=ef_electricity,
        recycling_credit=recycling_credit
    )

    total = calculator.total_co2e()
    print(f"\nTotal CO2e footprint: {total:.2f} kg CO2e")


if __name__ == "__main__":
    
    cad_file_path = r"C:\Users\yasin\Desktop\catis_proj\cube\cube.CATPart" #Enter CAD file path
    cam_doc_path = r"C:/Users/yasin/Desktop/catis_proj/cube/test_cam_doc/PartOperation1/Prog_1_1.html" #Enter CAM document path
    main(cad_file_path, cam_doc_path)
