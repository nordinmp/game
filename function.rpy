init python:
    def set_not_datable(name):
        global characters
        for character in characters:
            if character['name'] == name:
                character['datable'] = False