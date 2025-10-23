from typing import Optional

class CarbonFootprintCalculator:
    """
    Class to calculate CO2e emissions for a manufactured part, including
    material, machining energy, and waste.
    """

    def __init__(
        self,
        mass_kg: float,
        power_kw: float,
        machining_time_s: float,
        ef_material: float,
        ef_electricity: float,
        stock_mass_kg: Optional[float] = None,
        recycling_credit: float = 0.0,
    ):
        """
        Initialize the calculator with part and process data.

        Args:
            material (str): Material name.
            mass_kg (float): Final part mass in kg.
            power_kw (float): Machine power in kW.
            machining_time_h (float): Machining time in hours.
            ef_material (float): Material emission factor in kg CO2e/kg.
            ef_electricity (float): Electricity grid emission factor in kg CO2e/kWh.
            stock_mass_kg (Optional[float]): Initial stock mass in kg for waste calculation.
            recycling_credit (float): Fraction of waste recycled (0.0 to 1.0). Default 0.0.
        """
        self.mass_kg = mass_kg
        self.power_kw = power_kw
        self.machining_time_s = machining_time_s
        self.ef_material = ef_material
        self.ef_electricity = ef_electricity
        self.stock_mass_kg = stock_mass_kg
        self.recycling_credit = recycling_credit

    def material_impact(self) -> float:
        """
        Calculate CO2e emissions from raw material.
        """
        if self.ef_material is None:
            raise ValueError(f"Emission factor for material '{self.material}' not provided.")
        return self.mass_kg * self.ef_material

    def machining_energy_impact(self) -> float:
        """
        Calculate CO2e emissions from machining energy.
        """
        energy_kwh = self.power_kw * self.machining_time_s/3600
        return energy_kwh * self.ef_electricity

    def material_waste_impact(self) -> float:
        """
        Calculate CO2e emissions from material waste.
        """
        if self.stock_mass_kg is None:
            return 0.0
        waste_mass = self.stock_mass_kg - self.mass_kg
        waste_impact = waste_mass * self.ef_material
        return waste_impact * (1 - self.recycling_credit)

    def total_co2e(self) -> float:
        """
        Calculate total CO2e emissions for the part.
        """
        return self.material_impact() + self.machining_energy_impact() + self.material_waste_impact()
