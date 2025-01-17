#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

screen_width = 2160
screen_height = 1440

map_width = 80
map_height = 45


def main():

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(map_width / 2),
                    int(map_height / 2), "@", (255, 255, 255))
    npc = Entity(int(map_width / 2 - 5),
                 int(map_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities, event_handler, game_map, player)

    with tcod.context.new(
        width=screen_width,
        height=screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(
            map_width, map_height, order="F")
        while True:
            engine.render(root_console, context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
