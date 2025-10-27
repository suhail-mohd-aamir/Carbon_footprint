import gradio as gr
import pythoncom
from src.calculation import CarbonFootprintCalculator
from src.get_properties import CatPartProperties
from src.machining_time import extract_cutting_time


def calculate_carbon_footprint(
    cad_file, cam_file, stock_mass_kg, power_kw, ef_material, ef_electricity, recycling_credit
):
    import traceback
    import pythoncom

    try:
        if not cad_file or not cam_file:
            return "❌ Please upload both a CATPart and CAM HTML file."

        pythoncom.CoInitialize()  # Initialize COM

        cat_part = CatPartProperties(cad_file.name)
        cat_part._load_document()
        try:
            mass = cat_part.calculate_mass()
            volume = cat_part.calculate_volume()
            surface_area = cat_part.calculate_surface_area()
            material = cat_part.get_material_name()
        finally:
            cat_part.close()

        machining_time_s = extract_cutting_time(cam_file.name)

        calculator = CarbonFootprintCalculator(
            mass_kg=mass,
            stock_mass_kg=stock_mass_kg,
            power_kw=power_kw,
            machining_time_s=machining_time_s,
            ef_material=ef_material,
            ef_electricity=ef_electricity,
            recycling_credit=recycling_credit or 0.0
        )

        total = calculator.total_co2e()

        return (
            f"✅ **Carbon Footprint Report**\n\n"
            f"**Material:** {material}  \n"
            f"**Mass:** {mass:.3f} kg  \n"
            f"**Volume:** {volume:.3f} mm³  \n"
            f"**Surface Area:** {surface_area:.3f} mm²  \n"
            f"**Machining Time:** {machining_time_s:.1f} s  \n\n"
            f"**Total CO₂e:** {total:.2f} kg CO₂e"
        )


    except Exception as e:
        # Show full traceback in UI for debugging
        return f"❌ Error: {str(e)}\n\n{traceback.format_exc()}"



# --- Gradio Interface ---
demo = gr.Interface(
    fn=calculate_carbon_footprint,
    inputs=[
        gr.File(label="Upload CATIA Part File (.CATPart)"),
        gr.File(label="Upload CAM HTML File"),
        gr.Number(label="Stock Mass (kg)", value=1.0),
        gr.Number(label="Machine Power (kW)", value=2.0),
        gr.Number(label="Material Emission Factor (kg CO2e/kg)", value=8.5),
        gr.Number(label="Electricity Emission Factor (kg CO2e/kWh)", value=0.4),
        gr.Number(label="Recycling Credit (0.0 - 1.0)", value=0.0),
    ],
    outputs=gr.Markdown(label="Carbon Footprint Report"),
    title="🌍 CATIA Carbon Footprint Estimator",
    description="Upload your CATIA .CATPart and CAM HTML file to calculate the total CO₂e footprint."
)

if __name__ == "__main__":
    demo.launch()
