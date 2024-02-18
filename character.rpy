
include "function.rpy"
# main character
include "characters/player.rpy"

# dateble characters
include "characters/kristian.rpy"
include "characters/christoffer.rpy"

default characters = [
    {'name': 'Kristian', 'datable': True},
    {'name': 'Christoffer', 'datable': True},
]

# other
define vært = Character("Vært")

define ukendt = Character("???")



