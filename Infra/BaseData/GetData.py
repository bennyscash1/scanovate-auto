import json
import os
from enum import Enum
from pathlib import Path


env = os.getenv("ENV", "qa")

class VarData(Enum):
    ClientId = ("API", "ClientId")
    ClientSecret = ("API", "ClientSecret")
    BaseApiUrl = ("API", "BaseApiUrl")
    WebUrl = ("WebUi", "WebUrl")
    WebUserName = ("WebUi", "WebUserName")
    WebPassword = ("WebUi", "WebPassword")
    ContactName = ("Mobile", "ContactName")
    ContactNumber = ("Mobile", "ContactNumber")
    AppPackage = ("Mobile", "appPackage")
    AppActivity = ("Mobile", "appActivity")
    Environment = ("Common", "Enviorment")


file_path = Path(__file__).parent / f"jsonData.{env}.json"
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

loaded_data = {var: data[var.value[0]][var.value[1]] for var in VarData}