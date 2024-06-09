screen light():

    zorder 100

    if light == "forestday":
        add "light/light_day_forest.png"

    if light == "forestnight":
        add "light/light_night_forest.png"

    if light == "rainday":
        add "light/light_day_rain.png"

    if light == "rainnight":
        add "light/light_night_rain.png"

init python:
    config.overlay_screens.append("light")
