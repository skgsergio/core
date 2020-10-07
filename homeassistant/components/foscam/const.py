"""Constants for Foscam component."""
import logging

LOGGER = logging.getLogger(__package__)

DOMAIN = "foscam"

CONF_STREAM = "stream"

STREAMS = ["Main", "Sub"]

DIR_UP = "up"
DIR_DOWN = "down"
DIR_LEFT = "left"
DIR_RIGHT = "right"

DIR_TOPLEFT = "top_left"
DIR_TOPRIGHT = "top_right"
DIR_BOTTOMLEFT = "bottom_left"
DIR_BOTTOMRIGHT = "bottom_right"

MOVEMENT_ATTRS = {
    DIR_UP: "ptz_move_up",
    DIR_DOWN: "ptz_move_down",
    DIR_LEFT: "ptz_move_left",
    DIR_RIGHT: "ptz_move_right",
    DIR_TOPLEFT: "ptz_move_top_left",
    DIR_TOPRIGHT: "ptz_move_top_right",
    DIR_BOTTOMLEFT: "ptz_move_bottom_left",
    DIR_BOTTOMRIGHT: "ptz_move_bottom_right",
}

DEFAULT_PORT = 88

DEFAULT_TRAVELTIME = 0.125

SERVICE_PTZ = "ptz"
ATTR_MOVEMENT = "movement"
ATTR_TRAVELTIME = "travel_time"
