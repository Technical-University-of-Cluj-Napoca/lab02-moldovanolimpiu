import datetime

def smart_log(*args, **kwargs) -> None:
    mainstr = ""
    for x in args:
        mainstr = mainstr + " " +x

    #do arguments in an array
    argumenttypes = set()  
    argumentz = [""] * 5

    for key, val in kwargs.items():
        match key:
            case "level":
                argumenttypes.add("level")
                argumentz[0] = val
            case "color":
                argumenttypes.add("color")
                argumentz[1] = str(val)
            case "timestamp":
                argumenttypes.add("timestamp")
                argumentz[2] = str(val)
            case "date":
                argumenttypes.add("date")
                argumentz[3] = str(val)
            case "save_to":
                argumenttypes.add("save_to")
                argumentz[4] = val
            
    #print(argumenttypes)
    #print(argumentz)
    if "level" in argumenttypes:
        match argumentz[0]:
            case "info":
                levelstr = "[INFO]"
                mainstr = levelstr + mainstr
            case "debug":
                levelstr = "[DEBUG]"
                mainstr = levelstr + mainstr
            case "error":
                levelstr = "[ERROR]"
                mainstr = levelstr + mainstr
            case "warning":
                levelstr = "[WARNING]"
                mainstr = levelstr + mainstr
                
    if "date" in argumenttypes:
        if argumentz[3] == "True":
            x = datetime.datetime.now()
            mainstr = str(x.date())+ " " + mainstr
    
    if "timestamp" in argumenttypes:
        if argumentz[2] == "True":
            x = datetime.datetime.now().replace(microsecond=0)
            mainstr = str(x.time()) + " " + mainstr

    if "save_to" in argumenttypes:
        with open(argumentz[4], "a") as text_file:
            text_file.write('\n')
            text_file.write(mainstr)
    
    if "color" in argumenttypes:
        if argumentz[1] == "True":
            match argumentz[0]:
                case "info":
                    levelcolor = "\033[34m"
                    mainstr = levelcolor + mainstr + "\033[0m"
                case "debug":
                    levelcolor = "\033[37m"
                    mainstr = levelcolor + mainstr + "\033[0m"
                case "error":
                    levelcolor = "\033[31m"
                    mainstr = levelcolor + mainstr + "\033[0m"
                case "warning":
                    levelcolor = "\033[33m"
                    mainstr = levelcolor + mainstr + "\033[0m"
            
        
                
    print(mainstr)

def main():
    facility = "Site 19"
    smart_log("Lol", "Hello There",color = True ,level = "error", timestamp = True, date = True, save_to = "logs/errors.log")
    smart_log ("SCP-096", " has escaped", facility,date = False, color = True, level = "info")
    smart_log ("Containment procedures", " to begin immediately", color = False, level = "warning", timestamp = True)

main()