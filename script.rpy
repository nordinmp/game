# The game starts here.

include "function.rpy"
include "characters.rpy"


label start:
    queue  music "main_theme.mp3" loop

    $ renpy.music.set_volume(0.5)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dating_background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show player:
        zoom 0.8
        yalign 0.1
        xalign -0.1


    # These display lines of dialogue.

    nordin "Velkommen til Nordin's Harem, dette er et speed dating spil"


label introduktion:
    menu:
        nordin "Nogen spørgsmål?"

        "Hvem er jeg":
            nordin "Du er mig: Nordin, en dreng med KÆMPE rizz, og det skal du ud og bruge nu"

            jump introduktion

        "Hvor er jeg":
            nordin "Ah ja, glemte helt at sige det, du er i et speed dating program, lokaliseret i Hammel, Favrskovs hovedstad"

            jump introduktion

        "Hvor mange bitches er der.":

            $ datable_count = sum(1 for char in characters if char['datable'])

            nordin "Der [datable_count] bitches, alle klar til at lærere dig at kende"

            jump introduktion
        "Ok jeg har ikke flere spørgsmål":
            nordin "godt så lad os begynde"




    nordin "Målet er at få så mange bitches som muligt, men det får du ikke det svært ved 😉, held og lykke. Ik fordi du har brug for det!"

    menu:
        nordin "Er det første gang du spiller?"

        "Jeg er hjælpeløs, pls hjælp mig":

            jump tutorial
            

        "spurgt":

            nordin "WAAAAAAAUUUUUUW, jamen held og lykke så"

            jump first_round_intro


        
label first_round_intro:
    "Du kigger rundt i lokalet. Der er en intens stemning og du er ikke helt sikker på hvad du skal gøre"

    "Du beslutter at du bare skal tage dig sammen"

    menu:
        "Så du snupper"

        "noget vand":
            "Du tager et glas vand, nu er du klar"

        "en øl":
            "Du tager en øl, nu er du klar"

        "et glas vin":

            "Du tager et glas vin, nu er du klar"

        "et glas mjød":

            "Du tager et glas mjød, nu er du klar"

        "en cocktail":

            "Du får bartenderen til at lave den mest besværlige cocktail"
            
            "Bartenderen er ikke din største fan"

            "nu er du klar"

        "en mocktail":

            "Du får bartenderen til at lave en mocktail til dig, nu er du klar"

    vært "Skynd jeg at finde en ~lover~, inden tiden er gået"

    "du hører at folk er begyndt at finde deres nye \"mates\""

    ukendt "AAAAH, jeg har ikke fundet nogen endnu"

    "du kigger over mod stemmen"

    jump magnus_round1_intro
    # This ends the game.

    return
