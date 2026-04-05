# -*- coding: utf-8 -*-

"""
This script is used to create a default configuration file.
"""

from configparser import ConfigParser
from Constants import LogLevel
from bin.ConfigManager import ConfigManager


if __name__ == "__main__":
    config = ConfigParser()

    config["UI"] = {
        "ThemeColor": "DeepPurple",
        "ThemeMode": "Light",
        "ThemeDensity": "Normal",
    }
    config["Log"] = {
        "path": "",
        "cLevel": LogLevel.DEBUG.name,
        "fLevel": LogLevel.DEBUG.name,
        "wLevel": LogLevel.INFO.name,
    }

    with open(ConfigManager.defaultConfigPath(), "w", encoding="UTF-8") as f:
        config.write(f)
