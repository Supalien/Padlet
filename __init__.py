from .extract_cards import load, Padlet
from .get_csv import get
import os

def print_status():
    p = load(get(path = "C:/temp/Padlet.csv"))
    print(p.status())
    os.remove("C:/temp/Padlet.csv")
