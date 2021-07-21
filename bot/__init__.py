#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("2461325"))

API_HASH = os.environ.get("5b7eeed67b0ced06213aefa9d58236c4")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("BQBUY3Dxa01YVK9fWXIy28Ofu0SeMEBssyO-ZpQh8YoyBXJrUGrt-f_h4zmfTZj6GViunOjFrdNy2BNHPCSaxLXN2qLoYCa8vlzYqFKWGR-iBbKjKzAl1L17pEJoMUmQI8NBk05haDAkXefpc_V0cB2Jvp2h56qtWNn4D44f7g7mOunVbvlXA2PCjrV-Bk1ZtebGQV3Ab0P4KKJ-q3iyjKwuDOw0AWIvlx99-RMRIIxI5Z9DCNxMdzUNCJmof5O0QCnvOaYxceLGYN6IViB3BsjnsqhjyjHvOwCd3UPwecuFlAmjSGPEESYfc2lthtgHFmeNkH8BnjOhfXpy-4yHfNzdFbZrCgA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
