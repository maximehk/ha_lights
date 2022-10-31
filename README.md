# ha_lights

Simple python library to control lights and switches in Home Assistant.

Relies on dataclasses and namedtuples to provide auto-completion for interactive environments such as colab.

## Requirements

Install the package with pip

```shell
pip install 'home-assistant-lights'
```

## Sample use

```python
import homeassistant_api as ha
import ha_lights
from collections import namedtuple

client = ha.Client(URL, TOKEN)
factory = ha_lights.Factory(client)
lights,switches = factory.AllLights(), factory.AllSwitches()


COLORS = {
    'chill_evening': [255,220,180],
    'pure_white': [255, 255, 255],
    'red': [255, 0, 0],
}
Colors = namedtuple('Colors', COLORS)(**COLORS)


# Turn on a specific light with optional brightness and color settings
lights.living_room_tripod.turn_on(brightness=255, rgb_color=Colors.chill_evening)

# Create an entity group and use it to control lights and switches with a single API
living_room = EntityGroup([lights.living_room_tripod, switches.lr_smart_plug])
living_room.toggle()
```

## Optionally (if you have an invalid cert)

```python
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = ha.Client(URL, TOKEN, global_request_kwargs={'verify': False})
```
