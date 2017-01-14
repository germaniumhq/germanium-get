from termcolor import colored

def title(text):
    """ Gets the text colored a something white and bold. """
    return colored(text, "white", attrs=["bold"])


def text(text):
    return colored(text, "white")


def logo(text):
    return colored(text, "grey", attrs=["bold"])

