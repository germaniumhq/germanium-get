import subprocess

def execute_program(*program):
    """
    Execute a single program. Returns both stderr and stdout combined.
    The program parameter is an array of the command and the parameters.
    """
    process = subprocess.Popen(program,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    return stdout + stderr

