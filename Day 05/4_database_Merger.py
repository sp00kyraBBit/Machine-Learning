defaults = {
    "theme" : "light",
    "audio" : "on"
    } 

user_pref = {
    "theme" : "dark"
}

for key,value in user_pref.items():
    defaults.update({key:value})     #updating to user preference

print("updating to user preference: ", defaults)