import clipboard
import os

clipboard.copy(clipboard.paste().replace('\\','/').replace('//','/').replace("L'", "'").replace('L"', '"'))