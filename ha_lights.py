from dataclasses import dataclass
from collections import namedtuple
import homeassistant_api as ha


@dataclass
class BaseEntity:
    domain: ha.Domain
    entity: ha.Entity
    
    SERVICE_LIST = ['toggle', 'turn_on', 'turn_off']
    
    @property
    def entity_id(self):
        return self.entity.entity_id
    
    @property
    def services(self):
        ServiceList = namedtuple('SeviceList', BaseEntity.SERVICE_LIST)
        return ServiceList(*[self.domain.get_service(x) for x in BaseEntity.SERVICE_LIST])

    def toggle(self):
        self.services.toggle.trigger(entity_id=self.entity.entity_id)
        
    def turn_on(self, **kargs):
        self.services.turn_on.trigger(entity_id=self.entity.entity_id, **kargs)
        
    def turn_off(self):
        self.services.turn_off.trigger(entity_id=self.entity.entity_id)
        
    def state(self):
        return self.entity.update_state()
        
        
class Light(BaseEntity):
    def turn_on(self, brightness=None, rgb_color=None):
        kwargs = {}
        if brightness:
            kwargs['brightness'] = brightness
        if rgb_color:
            kwargs['rgb_color'] = rgb_color
        BaseEntity.turn_on(self, **kwargs)

class Switch(BaseEntity):
    pass



# TODO: use async
@dataclass
class EntityGroup:
    entities: list[BaseEntity]
        
    def toggle(self):
        for entity in self.entities:
            entity.toggle()
            
    def turn_on(self):
        for entity in self.entities:
            entity.turn_on()
            
    def turn_off(self):
        for entity in self.entities:
            entity.turn_off()
            
            
@dataclass
class Factory:
    client: ha.Client
        
    @property
    def light_domain(self):
        return self.client.get_domain('light')
        
    @property
    def switch_domain(self):
        return self.client.get_domain('switch')
        
    def MakeSwitch(self, entity_slug):
        return Switch(self.switch_domain, self.client.get_entity(entity_id=f'switch.{entity_slug}'))
    
    def MakeLight(self, entity_slug):
        return Light(self.light_domain, self.client.get_entity(entity_id=f'light.{entity_slug}'))
    
    def AllLights(self):
        light_ids = client.get_entities()['light'].entities.keys()
        return namedtuple('Lights', light_ids)(*[factory.MakeLight(x) for x in light_ids])

    def AllSwitches(self):
        switch_ids = client.get_entities()['switch'].entities.keys()
        return namedtuple('Switches', switch_ids)(*[factory.MakeSwitch(x) for x in switch_ids])
    
