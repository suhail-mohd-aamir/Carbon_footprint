# Carbon_footprint
AI-Based Carbon Footprint Estimation from 3D CAD Models 
<br>
Author- Mohd Aamir Suhail

This project develops an AI model that estimates the carbon footprint of a part directly from its 3D CAD model.

🔹 Key Idea
Modern CAD software like CATIA provides part-level data such as:
Mass
Surface area
Vulume
Material type

By linking this information with emission factors of materials, the model calculates the material-related carbon footprint.

🔹 Machining Impact
The model also estimates the machining footprint for processes such as:
Milling
Turning
Drilling
Threading

Factors considered include:
Machine energy use
Tooling
Coolant
Recycling credits

🔹 Output
The system provides a clear breakdown of emissions per part:
🌱 Material impact
⚙️ Machining impact
📊 Total emissions
With further training on production data, the AI improves accuracy in predicting machining energy and process times.

🔹 Why It Matters
Traditionally, Life Cycle Assessment (LCA) is performed late in product development time-consuming, costly, and after key design decisions are made.
This project shifts sustainability analysis upstream into the design phase, enabling engineers to:
Get real-time sustainability feedback
Select greener materials and processes
Ensure compliance with EU Green Deal and Digital Product Passport (DPP)
