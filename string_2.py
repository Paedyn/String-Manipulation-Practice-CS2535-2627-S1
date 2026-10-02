status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"
status = status.lower()
status= status.replace("::", " | ")
status= status.replace("_", " ")

print(status)