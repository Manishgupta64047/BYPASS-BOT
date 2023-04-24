import os
import logging
class Config:
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
