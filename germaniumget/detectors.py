import os
from os import path
import sys
import re
import subprocess
from styles import warning

def is_edge_detected():
    return is_program_in_classpath("edge")


def is_chrome_detected():
    return is_program_in_classpath("google-chrome")


def is_firefox_detected():
    return is_program_in_classpath("firefox")


def is_java8_installed():
    return not is_program_in_classpath("java") \
        or not program_execution_matches(
            ["java", "-version"],
            r'java version "1.8.\d+_\d+')


def is_program_in_classpath(program_name):
    """
    Check if the program is in the classpath. The full name of the binary
    should be specified (e.g. java.exe)
    """
    if sys.platform.startswith("win"):
        program_name += ".EXE"

    for path_entry in os.environ['PATH'].split(os.pathsep):
        full_path = os.path.join(path_entry, program_name)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            return True

    return None


def program_execution_matches(program, searched_pattern):
    """
    Checks if the executed program contains the serched pattern (expressed as a
    regex).
    """
    pattern = re.compile(searched_pattern, re.MULTILINE)
    stdout = execute_program(program)

    print(warning(stdout))

    return bool(pattern.search(stdout))


def execute_program(program):
    """
    Execute a single program.
    """
    process = subprocess.Popen(program, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout + stderr


