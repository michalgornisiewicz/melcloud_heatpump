
# MELCloud Heat Pump Home Assistant Integration

## Installation

1. Copy the `melcloud_heatpump` folder into your Home Assistant `custom_components` directory:
  - `/config/custom_components/melcloud_heatpump`
2. Restart Home Assistant.

## Configuration (Config Flow)

Do not add the integration to `configuration.yaml`! This integration uses the modern config flow:

1. Go to Settings → Integrations → Add Integration.
2. Search for "MELCloud Heat Pump" and add the integration via the user interface.
3. Enter your MELCloud login credentials and DeviceID.

## Usage

After adding the integration and restarting Home Assistant, your heat pump sensors will be available in the system. You can view them in Developer Tools → States.

## Notes
- For full functionality, you need to implement data fetching from the MELCloud API in `coordinator.py`.
- Currently, the integration returns example data (for testing).
- The integration is compatible with HACS – you can add the repository as a custom repository in HACS.

## Troubleshooting
- Make sure the `melcloud_heatpump` folder is in `custom_components`.
- Check Home Assistant logs after restart (Settings → System → Logs).
- Clear your browser cache after updating files.
- If the integration does not appear in the list, check the correctness of `manifest.json` and the presence of `config_flow.py`.

