import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

DOMAIN = "melcloud_heatpump"

class MelcloudConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # TODO: Validate credentials with MELCloud API
            return self.async_create_entry(title="MELCloud Heat Pump", data=user_input)
        data_schema = vol.Schema({
            vol.Required("username"): str,
            vol.Required("password"): str,
            vol.Required("device_id"): str,
        })
        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
