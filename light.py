import arcade
import player
import random
import time
from arcade.experimental.lights import Light, LightLayer

# Color of darkness
AMBIENT_COLOR = (10, 10, 10)


class GameLight:
    """Lights in the game"""

    def __init__(self, width, height) -> None:

        self.light_layer = LightLayer(width, height)
        self.player_light = None

    # def create_light_point(
    #     self, x_pos: int, y_pos: int, radius: int, color: arcade.csscolor, mode: str
    # ):
    #     """Create a static light point
    #     Example:
    #     Create a small white light
    #     x_pos = 100,
    #     y_pos = 200,
    #     radius = 100,
    #     mode = "soft",
    #     color = arcade.csscolor.WHITE"""
    #     # Create a small white light
    #     light = Light(x_pos, y_pos, radius, color, mode)
    #     # self.light_layer.add(light)
    #     return light

    def player_flashlight(self):
        """Creates the light point that follows the player around"""
        x = 0
        y = 0
        r = random.randint(250, 275)
        c = random.choice(
            [
                # arcade.csscolor.DARK_GOLDENROD,
                arcade.csscolor.PALE_GOLDENROD,
                # arcade.csscolor.LIGHT_SLATE_GREY,
                # arcade.csscolor.LIGHT_GOLDENROD_YELLOW,
                # arcade.csscolor.GREENYELLOW,
                # arcade.csscolor.MEDIUM_PURPLE,
                # arcade.csscolor.GHOST_WHITE,
                # arcade.csscolor.PALE_VIOLET_RED,
                # arcade.csscolor.ORANGE_RED,
            ]
        )
        player_light = Light(x, y, r, c, "soft")
        return player_light

    def light_on(self):

        if self.player_light not in self.light_layer:
            self.light_layer.add(self.player_light)

    def update(self, player: player.Player):
        """updates the light that follows player, centered to player"""
        if self.player_light not in self.light_layer:
            self.player_light = self.player_flashlight()
            self.player_light.position = player.position.x, player.position.y
            self.light_layer.add(self.player_light)
        else:
            self.player_light.position = player.position.x, player.position.y
            self.light_layer.remove(self.player_light)

    def receive_key_down(self, key: int):
        if key == arcade.key.TAB:
            # We can add/remove lights from the light layer. If they aren't
            # in the light layer, the light is off.
            # this doesnt appy when flicker is applied
            if self.player_light in self.light_layer:
                self.light_layer.remove(self.player_light)
            else:
                self.light_layer.add(self.player_light)
