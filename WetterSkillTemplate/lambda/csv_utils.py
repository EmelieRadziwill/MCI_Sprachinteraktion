inputset = [["1", "2", "3", "4", "5"], ["Deutsch", "Englisch"], ["langsam", "durchschnittlich"], ["keine", "kurz", "lang"]]
outputset = [["x-soft", "soft", "medium", "loud", "x-loud"], ["de-DE", "en-GB"], ["slow", "medium"], ["x-weak", "weak", "medium"]]
voices = ["Hans", "Brian", "Marlene", "Amy"]

def IdPresent(csv, id):
    flag = False
    for row in csv:
        if(row[0] == id):
            flag = True
    return flag

def getConfigs(csv, id):
    
    config=[]
    volume = ''
    voice = ''
    language= ''
    speed = ''
    breaks = ''
    expression = False
    
    for row in csv:
        if(row[0] == id):
            config = row
            break

    for i, value in enumerate(inputset[0]):
        if (config[4] == value):
            volume = outputset[0][i]
            break
        
    for i, value in enumerate(inputset[1]):
        if (config[5] == value):
            language = outputset[1][i]
            break
    
    for i, value in enumerate(inputset[2]):
        if (config[9] == value):
            speed = outputset[2][i]
            break

    for i, value in enumerate(inputset[3]):
        if (config[8] == value):
            breaks = outputset[3][i]
            break

    if config[1] == "maennlich":
        if config[5] == "Deutsch":
            voice = voices[0]
        else: voice = voices[1]
    else:
        if config[5] == "Deutsch":
            voice = voices[2]
        else: voice = voices[3]   
        
    if config[11] == "ja":
        expression = True
            
    return volume, voice, language, speed, breaks, expression
            

    
    