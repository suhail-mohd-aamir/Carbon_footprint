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
**Material footprint (display):**
\[
CF_{\text{material}} = m \cdot EF_{\text{material}}
\]

Machining Footprint

Case A (with machining time):
**Machining (case A — with machining time):**
\[
E = P_{\text{avg}} \cdot t
\]
\[
CF_{\text{machining}} = E \cdot EF_{\text{electricity}}
\]

Case B (with chip volume):

**Machining (case B — with chip volume):**
\[
V_{\text{chip}} = V_{\text{stock}} - V_{\text{final}}
\]
\[
E = U_{\text{cut}} \cdot V_{\text{chip}}
\]
\[
CF_{\text{machining}} = E \cdot EF_{\text{electricity}}
\]

Total Footprint

**Total footprint (display):**
\[
CF_{\text{total}} = CF_{\text{material}} + CF_{\text{machining}}
\]

### Block Diagram
