import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# Logger SECTION
config_file["Logger"] = {
        "LogFilePath": "<Path to log file>",
        "LogFileName": "application.log",
        "LogLevel": "INFO",
        "when": "m",
        "interval": 2,
        "backupCount": 60
        }


# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file created")
