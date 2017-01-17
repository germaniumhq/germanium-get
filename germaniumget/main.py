import colorama
import textwrap
from styles import title, text, question, option, options, read_option, warning, block, logo
from detectors import is_edge_detected, is_chrome_detected, is_firefox_detected, is_java8_installed
from download import download_url
import tempfile
import errno


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
    def temp(subpath):
        return os.path.join(temp_folder, subpath)

    return temp


def get_germanium_folder():
    user_home = os.environ['USERPROFILE']

    def ge_folder(subpath):
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

mkdir_p(ge_folder(''))

if install_ie:
    download_url("http://selenium-release.storage.googleapis.com/3.0/IEDriverServer_Win32_3.0.0.zip",
                 temp("IEDriverServer.zip"))

colorama.deinit()

