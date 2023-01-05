from os import file


def Create(DIR,EXE):
    shortcut = file(DIR, 'w')
    shortcut.write('[InternetShortcut]\n')
    shortcut.write('URL=%s' % EXE)
    shortcut.close()