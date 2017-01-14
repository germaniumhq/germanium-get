import colorama
from styles import title, text, logo

#=====================================================
# Actual program starts here
#=====================================================
colorama.init()
print(logo("""
                                          _
   ____ ____  _________ ___  ____ _____  (_)_  ______ ___
  / __ `/ _ \/ ___/ __ `__ \/ __ `/ __ \/ / / / / __ `__ \\
 / /_/ /  __/ /  / / / / / / /_/ / / / / / /_/ / / / / / /
 \__, /\___/_/  /_/ /_/ /_/\__,_/_/ /_/_/\__,_/_/ /_/ /_/
/____/ 1.10.5

"""))

print(title("GET.germanium"))
print(text("""
This tool can be used to provision Windows Hosts with all
the necessary environment.
"""))

colorama.deinit()

