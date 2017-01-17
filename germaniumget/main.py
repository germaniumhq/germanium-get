import colorama
from styles import title, text, logo, question, option, options, read_option, warning
from detectors import is_edge_detected, is_chrome_detected, is_firefox_detected, is_java8_installed

install_ie = False
install_edge = False
install_firefox = False
install_chrome = False
install_java = False

#=====================================================
# Actual program starts here
#=====================================================
colorama.init()
print(logo("""
                                       _
  __ _  ___ _ __ _ __ ___   __ _ _ __ (_)_   _ _ __ ___
 / _` |/ _ \ '__| '_ ` _ \ / _` | '_ \| | | | | '_ ` _ \\
| (_| |  __/ |  | | | | | | (_| | | | | | |_| | | | | | |
 \__, |\___|_|  |_| |_| |_|\__,_|_| |_|_|\__,_|_| |_| |_|
 |___/  1.10.5

"""))

print(title("GET.germanium"))
print(text("""
This tool can be used to provision Windows Hosts with all
the necessary environment.
"""))

print(title("Selenium Node"))

#=====================================================
# Internet Explorer
#=====================================================
print(question("Should IE support be enabled?"))
option = read_option("[Y]es", "[N]o", "[C]ancel")

if option == "cancel":
    exit(1)

if option == "yes":
    install_ie = 1

#=====================================================
# Edge
#=====================================================
if is_edge_detected():
    print(question("Should Edge support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_edge = 1


#=====================================================
# Chrome
#=====================================================
if is_chrome_detected():
    print(question("Should Chrome support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_chrome = 1

#=====================================================
# Firefox
#=====================================================
if is_firefox_detected():
    print(question("Should Firefox support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_firefox = 1

#=====================================================
# Java
#=====================================================
if not is_java8_installed():
    print(question("Install Java 8?"))
    print(warning("This is required for the Selenium Node to work."))

    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_java = 1


colorama.deinit()

