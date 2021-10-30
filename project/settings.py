from dataclasses import dataclass
from pathlib import Path
from os import environ


e = environ.get


@dataclass
class Settings:

    BASE_DIR = Path("./")
    ASSETS: Path = BASE_DIR / "gui" / "assets"

    GUI_FILE_PATH: Path = e("GUI_FILE_PATH", ASSETS / "GUImain.ui")
    STYLE_FILE_PATH: Path = e("STYLE_FILE_PATH", ASSETS / "style.css")
    REFRESH_PERIOD: int = e("CAMERA_REFRESH_PERIOD", 2)

    DEBUG_DUMP = e("DEBUG_DUMP", False)
    DEBUG_DUMP_LOCATION = e("DEBUG_DUMP_LOCATION", BASE_DIR / "capturers" / "dump")

    STATIC_FILE_PATH = e("STATIC_FILE_PATH", BASE_DIR / "capturers" / "dump" / "man.png")
    STATIC_VIDEO_PATH = e("STATIC_VIDEO_PATH")


settings = Settings()
