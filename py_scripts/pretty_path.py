import clipboard
import os

clipboard.copy(clipboard.paste().replace('\\','/').replace('//','/'))