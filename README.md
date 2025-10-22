# Carbon_footprint
AI-Powered Carbon Footprint Estimation from 3D CAD Models
<br>
Author- Mohd Aamir Suhail

This project introduces an AI-driven solution that transforms 3D CAD models into actionable sustainability insights. By automatically extracting material and manufacturing details from CAD files and linking them with trusted emission factor databases, the system provides instant estimates of a part’s carbon footprint.

Instead of waiting for long and complex Life Cycle Assessments, engineers and manufacturers can now get real time feedback during the design phase helping them choose greener materials, reduce machining waste, and cut energy consumption.

## Methodology Logic
🔹 Methodology Logic

**Input from CAD**

Material type

Mass of part

Volume / Surface area (optional)

Material Footprint

Each material has an Emission Factor (EF) in kgCO₂e/kg (from ICE, ÖKOBAUDAT, or USLCI datasets).

Formula:
**CF_material = Mass × EF_material**

Machining Footprint

Case A (with machining time):
**Energy = Average Machine Power × Machining Time
CF_machining = Energy × EF_electricity**

Case B (with chip volume):

**Chip Volume = Stock Volume – Final Part Volume
Energy = Specific Cutting Energy × Chip Volume
CF_machining = Energy × EF_electricity**

Total Footprint

**CF_total = CF_material + CF_machining**

## 📊 Process Diagram

![Block Diagram](/demo/Process_diagram.svg)