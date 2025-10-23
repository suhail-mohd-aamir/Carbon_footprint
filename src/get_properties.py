from pathlib import Path
from pycatia import CATIADocHandler
from pycatia.mec_mod_interfaces.part_document import PartDocument
from pycatia.cat_mat_interfaces.material_manager import MaterialManager

class CatPartProperties:
    """
    Class to extract the properties of a part in CATIA. Properties currently include ,ass, volume, material, surface area.
    """
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.mass = None
        self.volume = None
        self.material_name = None
        self.surface_area = None

    def _load_document(self):
        """Loads the CATPart document."""
        self.caa = CATIADocHandler(self.file_path)
        self.caa.__enter__()
        self.document = self.caa.document

        if not self.document.is_part:
            raise TypeError("Document is not a CATPart file.")
        
        self.part_document = PartDocument(self.document.com_object)
        self.part = self.part_document.part
        self.spa_workbench = self.document.spa_workbench()

    def calculate_mass(self):
        """Calculates the mass"""
        inertias = self.spa_workbench.inertias
        inertia = inertias.add(self.part)
        self.mass = inertia.mass
        return self.mass

    def calculate_volume(self):
        """Calculates the volume."""
        body = self.part.bodies.item(1)
        reference = self.part.create_reference_from_object(body)
        measurable = self.spa_workbench.get_measurable(reference)
        self.volume = measurable.volume
        return self.volume

    def calculate_surface_area(self):
        """Calculates the surface area"""
        body = self.part.bodies.item(1)
        reference = self.part.create_reference_from_object(body)
        measurable = self.spa_workbench.get_measurable(reference)
        self.surface_area = measurable.area
        return self.surface_area

    def get_material_name(self):
        """Fetch the material"""
        material_item = self.part.get_item("CATMatManagerVBExt")
        material_manager = MaterialManager(material_item.com_object)
        material = material_manager.get_material_on_part(i_part=self.part)
        self.material_name = material.name
        return self.material_name

    def close(self):
        """Close the CATIA document handler."""
        self.caa.__exit__(None, None, None)

