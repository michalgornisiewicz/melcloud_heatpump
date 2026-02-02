from homeassistant.helpers.entity import Entity
from .models import MelcloudHeatPump

# Example: You would fetch real data from MELCloud API here
EXAMPLE_DATA = {
    # ... (use your real device data here)
}

class MelcloudHeatPumpSensor(Entity):
    def __init__(self, device: MelcloudHeatPump, field: str, name: str, unit: str = None):
        self._device = device
        self._field = field
        self._name = name
        self._unit = unit

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return getattr(self._device, self._field, None)

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def extra_state_attributes(self):
        fields = [
            "defrost_mode",
            "heat_pump_frequency",
            "room_temperature_zone1",
            "outdoor_temperature",
            "flow_temperature",
            "flow_temperature_zone1",
            "flow_temperature_boiler",
            "return_temperature",
            "return_temperature_zone1",
            "return_temperature_boiler",
            "boiler_status",
            "booster_heater1_status",
            "booster_heater2_status",
            "booster_heater2plus_status",
            "immersion_heater_status",
            "water_pump1_status",
            "water_pump2_status",
            "water_pump3_status",
            "tank_water_temperature",
            "eco_hot_water",
            "power",
            "operation_mode",
            "operation_mode_zone1",
            "target_hc_temperature_zone1",
            "forced_hot_water_mode",
            "prohibit_hot_water",
            "current_energy_mode",
        ]
        attrs = {f: getattr(self._device, f, None) for f in fields}
        return attrs
