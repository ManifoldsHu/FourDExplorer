# -*- coding: utf-8 -*-

"""
*---------------------------- ConfigManager.py -------------------------------*
管理配置文件。当配置文件不存在时创建。

作者：          胡一鸣
创建日期：      2024年10月13日

Manage Configuration Files. Create one if not exists.

author:         Hu Yiming
date:           Oct 13, 2024
*---------------------------- ConfigManager.py -------------------------------*
"""

import os
import shutil
import sys
from configparser import ConfigParser

from PySide6.QtCore import QObject

from Constants import ROOT_PATH, LogLevel


class ConfigManager(QObject):
    def __init__(self, parent: QObject = None):
        super().__init__(parent)
        self._config = ConfigParser()
        self._config_path = self.userConfigPath()
        self._default_config_path = self.defaultConfigPath()
        self.initConfig()

    @staticmethod
    def defaultConfigPath() -> str:
        return os.path.join(ROOT_PATH, "config.ini")

    @staticmethod
    def userConfigDirPath() -> str:
        home_path = os.path.expanduser("~")
        if sys.platform.startswith("win"):
            base_path = os.environ.get("APPDATA")
            if not base_path:
                base_path = os.path.join(home_path, "AppData", "Roaming")
            return os.path.join(base_path, "FourDExplorer")
        if sys.platform == "darwin":
            return os.path.join(
                home_path,
                "Library",
                "Application Support",
                "FourDExplorer",
            )
        base_path = os.environ.get("XDG_CONFIG_HOME")
        if not base_path:
            base_path = os.path.join(home_path, ".config")
        return os.path.join(base_path, "FourDExplorer")

    @classmethod
    def userConfigPath(cls) -> str:
        return os.path.join(cls.userConfigDirPath(), "config.ini")

    def initConfig(self):
        os.makedirs(self.userConfigDirPath(), exist_ok=True)
        if not os.path.exists(self._config_path):
            self.restoreDefaults()
            return
        self.reload()
        self._repairConfig()
        self.save()

    def restoreDefaults(self):
        if os.path.exists(self._default_config_path):
            shutil.copyfile(self._default_config_path, self._config_path)
        else:
            self._config = ConfigParser()
            self._repairConfig()
            self.save()
            return
        self.reload()
        self._repairConfig()
        self.save()

    def reload(self):
        self._config = ConfigParser()
        self._config.read(self._config_path, encoding="UTF-8")

    def save(self):
        with open(self._config_path, "w", encoding="UTF-8") as f:
            self._config.write(f)

    def getSection(self, section_name: str, defaults: dict[str, str] = None):
        is_updated = False
        if not self._config.has_section(section_name):
            self._config.add_section(section_name)
            is_updated = True
        if defaults is not None:
            for key, value in defaults.items():
                if not self._config[section_name].get(key, "").strip() and value:
                    self._config[section_name][key] = value
                    is_updated = True
                elif key not in self._config[section_name]:
                    self._config[section_name][key] = value
                    is_updated = True
        if is_updated:
            self.save()
        return self._config[section_name]

    def _repairConfig(self):
        self.getSection(
            "UI",
            {
                "ThemeColor": "DeepPurple",
                "ThemeMode": "Light",
                "ThemeDensity": "Normal",
            },
        )
        log_section = self.getSection(
            "Log",
            {
                "path": "",
                "fLevel": LogLevel.DEBUG.name,
                "cLevel": LogLevel.DEBUG.name,
                "wLevel": LogLevel.INFO.name,
            },
        )
        for key, value in {
            "fLevel": LogLevel.DEBUG.name,
            "cLevel": LogLevel.DEBUG.name,
            "wLevel": LogLevel.INFO.name,
        }.items():
            if log_section.get(key, "") not in LogLevel.__members__:
                log_section[key] = value

    @property
    def config(self):
        return self._config

    @property
    def configPath(self) -> str:
        return self._config_path
