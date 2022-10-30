# ha_lights

Simple python library to control lights and switches in Home Assistant.

Relies on dataclasses and namedtuples to provide auto-completion for interactive environments such as colab.

## Requirements

Install homeassistant-api

```shell
pip install 'homeassistant_api==4.0.0.post2'
```

## Sample use

```python
import homeassistant_api as ha
from collections import namedtuple

client = ha.Client(URL, TOKEN)
factory = Factory(client)
lights,switches = factory.AllLights(), factory.AllSwitches()


COLORS = {
    'chill_evening': [255,220,180],
    'pure_white': [255] * 3,
    'red': [255, 0, 0],
}
Colors = namedtuple('Colors', COLORS.keys())(*COLORS.values())


lights.living_room_tripod.turn_on(brightness=255, rgb_color=Colors.chill_evening)


```
