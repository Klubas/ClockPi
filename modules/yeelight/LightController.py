import logging
from yeelight import discover_bulbs, Bulb


class LightController:
    def __init__(self):
        self.bulbs = list()

        for bulb in discover_bulbs():

            found_bulb = Bulb(
                    ip=bulb['ip']
                    , port=bulb['port']
                    , model=bulb['capabilities']['model']
            )

            if bulb['capabilities']['name'] == '':
                name = bulb['ip']
                found_bulb.set_name(name)
            else:
                name = bulb['capabilities']['name']

            bulb_name = name

            self.bulbs.append({
                    'bulb': found_bulb
                    , 'name': bulb_name
                    , 'ip': bulb['ip']
                }
            )

    def turn_on(self, bulb_name=None):
        if bulb_name:
            for bulb in self.bulbs:
                if bulb['name'] == bulb_name:
                    bulb['bulb'].turn_on()
        else:
            for bulb in self.bulbs:
                bulb['bulb'].turn_on()

    def turn_off(self, bulb_name=None):
        if bulb_name:
            for bulb in self.bulbs:
                if bulb['name'] == bulb_name:
                    bulb['bulb'].turn_off()
        else:
            for bulb in self.bulbs:
                bulb['bulb'].turn_off()

    def set_bulb_color(self, color=(255, 255, 255), bulb_name=None):
        if bulb_name:
            for bulb in self.bulbs:
                if bulb['name'] == bulb_name:
                    bulb['bulb'].set_rgb(
                        red=int(color[0]), green=int(color[1]), blue=int(color[2])
                    )
        else:
            for bulb in self.bulbs:
                bulb['bulb'].set_rgb(
                    red=int(color[0]), green=int(color[1]), blue=int(color[2])
                )

    def get_all_bulbs_properties(self) -> list:
        properties = list()
        for bulb in self.bulbs:
            properties.append(bulb['bulb'].get_properties())
        return properties

    def get_bulb_names(self) -> list:
        names = list()
        for bulb in self.bulbs:
            names.append(bulb['name'])
        return names

    def set_bulb_name(self, new_name, bulb_name=None):
        if not bulb_name:
            return

        bulb_to_rename = None

        for bulb in self.bulbs:
            if bulb['name'] == bulb_name:
                bulb_to_rename = bulb['bulb']
                break

        if not bulb_to_rename:
            logging.info(
                '{modulo} Bulb {bulb_name} not found'.format(
                    modulo=__file__, bulb_name=bulb_name
                )
            )
            return

        bulb_to_rename.set_name(new_name)

    def run_action(self, ip=None, name=None, action=None, params=None):

        if ip is not None:
            name = ip

        if action == 'on':
            self.turn_on(bulb_name=name)

        elif action == 'off':
            self.turn_off(bulb_name=name)

        elif action == 'color':

            color = params['color'] if 'color' in params else None

            if not color:
                return
            else:
                color = color.split(' ')

            print(color)

            self.set_bulb_color(bulb_name=name, color=color)

        elif action == 'rename':

            new_name = params['new_name'] if 'new_name' in params else None

            if not new_name:
                return

            self.set_bulb_name(new_name=new_name, bulb_name=name)


