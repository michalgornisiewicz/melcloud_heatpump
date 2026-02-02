# MELCloud Heat Pump Home Assistant Integration

## Installation

1. Copy the `melcloud_heatpump` folder into your Home Assistant `custom_components` directory:
   - `/config/custom_components/melcloud_heatpump`
2. Restart Home Assistant.

## Example configuration.yaml

Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: melcloud_heatpump
    username: YOUR_MELCLOUD_EMAIL
    password: YOUR_MELCLOUD_PASSWORD
    device_id: 123677334
```

- Replace `YOUR_MELCLOUD_EMAIL` and `YOUR_MELCLOUD_PASSWORD` with your MELCloud credentials.
- Replace `device_id` with your actual DeviceID from MELCloud.

## Usage

After restarting, your heat pump sensors will be available in Home Assistant. Use Developer Tools → States to view sensor values.

## Notes
- For full functionality, you need to implement MELCloud API calls in `sensor.py` to fetch live data.
- This example assumes static configuration. For dynamic setup, implement a config flow.

## Troubleshooting
- Check Home Assistant logs for errors.
- Ensure your credentials and device_id are correct.
- For HACS installation, publish this folder to GitHub and add as a custom repository in HACS.
