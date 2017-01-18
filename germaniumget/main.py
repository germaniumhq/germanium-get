import colorama
import textwrap
from styles import title, text, question, option, options, read_option, warning, block, logo, read_string
from detectors import is_edge_detected, is_chrome_detected, is_firefox_detected, is_java8_installed
from download import download, extract_zip
import tempfile
import errno

from test_download_urls import \
    IE_DRIVER_DOWNLOAD_URL, \
    GECKO_DRIVER_DOWNLOAD_URL, \
    CHROME_DRIVER_DOWNLOAD_URL, \
    EDGE_DRIVER_DOWNLOAD_URL, \
    SELENIUM_STANDALONE_JAR_URL

import os


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
print('')
print(question("Should IE support be enabled?"))
option = read_option("[Y]es", "[N]o", "[C]ancel")

if option == "cancel":
    exit(1)

if option == "yes":
    install_ie = 1

#=====================================================
# Edge
#=====================================================
print('')
if is_edge_detected():
    print(question("Should Edge support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_edge = 1
else:
    print(warning("No Edge Support"))
    print(block(
    """
    Edge was not detected on this system, so no binary
    drivers will be downloaded, nor any configuration
    will be generated for the Selenium Node.
    """
    ))

#=====================================================
# Chrome
#=====================================================
print('')
if is_chrome_detected():
    print(question("Should Chrome support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_chrome = 1
else:
    print(warning("No Chrome Support"))
    print(block(
    """
    Chrome was not detected on this system, so no binary
    drivers will be downloaded, nor any configuration
    will be generated for the Selenium Node.
    """
    ))

#=====================================================
# Firefox
#=====================================================
print('')
if is_firefox_detected():
    print(question("Should Firefox support be enabled?"))
    option = read_option("[Y]es", "[N]o", "[C]ancel")

    if option == "cancel":
        exit(1)

    if option == "yes":
        install_firefox = 1
else:
    print(warning("No Firefox Support"))
    print(block(
    """
    Firefox was not detected on this system, so no binary
    drivers will be downloaded, nor any configuration
    will be generated for the Selenium Node.
    """
    ))

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


#=====================================================
# Selenium Hub location.
#=====================================================
print(question("Selenium Hub URL?"))
print(text("""
To what hub should this node connect to.
"""))

selenium_hub_url = read_string("Url:")

#=====================================================
# Now that the configuration is done, let's ask the user
# one more time, and be done with it.
#=====================================================
print('')
print(title("Planned steps:"))

if install_ie:
    print("  Install IE support.")

if install_edge:
    print("  Install Edge support.")

if install_chrome:
    print("  Install Chrome support.")

if install_firefox:
    print("  Install Firefox support.")

if install_java:
    print("  Install Java.")

print(question("Start downloading and installation?"))
option = read_option("[Y]es", "[N]o")

if option == "no":
    exit(1)

#=====================================================
# Ok, now we need to start fetching files.
# We will create first an empty folder for the downloads,
# then we will fetch stuff.
#=====================================================

def create_temp_folder():
    temp_folder = tempfile.mkdtemp(prefix='germanium_', suffix='install')
    def temp(subpath=''):
        return os.path.join(temp_folder, subpath)

    return temp


def get_germanium_folder():
    user_home = os.environ['USERPROFILE']

    def ge_folder(subpath=''):
        return os.path.join(user_home, 'Desktop', 'germanium', subpath)

    return ge_folder


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


temp = create_temp_folder()
ge_folder = get_germanium_folder()

mkdir_p(ge_folder("lib"))

#=====================================================
# Download and unzip the drivers that are needed.
#=====================================================
if install_ie:
    download(IE_DRIVER_DOWNLOAD_URL,
             temp("IEDriverServer.zip"))
    extract_zip(temp("IEDriverServer.zip"), ge_folder("lib"))

if install_firefox:
    download(GECKO_DRIVER_DOWNLOAD_URL,
             temp("GeckoDriver.zip"));

    extract_zip(temp("GeckoDriver.zip"), ge_folder("lib"))

if install_chrome:
    download(CHROME_DRIVER_DOWNLOAD_URL,
             temp("ChromeDriver.zip"));

    extract_zip(temp("ChromeDriver.zip"), ge_folder("lib"))

if install_edge:
    download(EDGE_DRIVER_DOWNLOAD_URL,
             ge_folder("lib/MicrosoftWebDriver.exe"))

download(SELENIUM_STANDALONE_JAR_URL,
         ge_folder("lib/selenium-standalone.jar"))

read_string("Done. Press ENTER to continue.")

colorama.deinit()

