import gradio as gr
from pycatia import catia
from src.get_properties import CatPartProperties

# Example processing function (kept separate / attached to the interface)
def process_file(file):
    # defensive handling of different Gradio upload shapes
    if file is None:
        return "No file provided."

    # determine a path to the uploaded file
    file_path = None
    if hasattr(file, "name") and file.name:
        file_path = file.name
    elif isinstance(file, dict) and "name" in file:
        file_path = file["name"]
    else:
        # fallback: try repr for debugging
        return "Unable to determine uploaded file path."

    print("Uploaded file path:", file_path)

    cat_part = CatPartProperties(file_path)
    try:
        cat_part._load_document()  # load the CATPart into spa_workbench

        mass = cat_part.calculate_mass()
        volume = cat_part.calculate_volume()
        surface_area = cat_part.calculate_surface_area()
        material = cat_part.get_material_name()

        # return a formatted summary string (important: return, so UI updates)
        return (
            f"Properties for {file_path}:\n"
            f"- Mass: {mass} kg\n"
            f"- Volume: {volume} mm³\n"
            f"- Surface Area: {surface_area} mm²\n"
            f"- Material: {material}\n"
        )

    except Exception as e:
        return f"Error processing CATPart: {e}"
    finally:
        try:
            cat_part.close()
        except Exception:
            pass

# Build a nicer UI using Blocks — no function attached to the Analyze button yet
with gr.Blocks(title="🌍 Carbon Footprint — File Analyzer") as demo:
    gr.Markdown("# 🌍 Carbon Footprint — File Analyzer")
    gr.Markdown(
        "Upload a file to get a quick summary and insights. "
        "This demo shows the interface only — the processing function is not attached yet. ✨📄\n\n"
        "- Planned: word/line/char counts, file metadata, and quick tips to reduce carbon footprint.\n"
        "- To enable processing: connect your function to the Analyze button (example below)."
    )

    with gr.Row():
        file_input = gr.File(label="Upload file", file_count="single")
        # larger, scrollable result area
        output = gr.Textbox(
            label="Result",
            placeholder="Results will appear here...",
            interactive=False,
            lines=15,      # visible height (~15 lines)
            max_lines=1000 # allow scrolling for large outputs
        )

    with gr.Row():
        analyze_btn = gr.Button("🔎 Analyze", variant="primary")
        analyze_btn.click(fn=process_file, inputs=file_input, outputs=output)
        gr.Markdown(
            "To attach processing, call:\n\n"
            "`analyze_btn.click(fn=process_file, inputs=file_input, outputs=output)`\n\n"
            "This line is intentionally omitted so the UI is shown without running any logic."
        )

if __name__ == "__main__":
    demo.launch()
