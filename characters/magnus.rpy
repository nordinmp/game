define magnus = Character("Magnus")

label magnus_round1_intro:
    show magnus:
        zoom 1.2
        yalign 2.2
        xalign 0.7

    "Du skynder dig at gå over til nogen, men inden du når derhen har de fundet en anden"
    "Du går over til en anden, men igen er du forsent"
    "3 gang er lykkens gang, for du ser at en sexy man kigger på dig, og nu mødes jeres øjne"
    "Hans muskler er gigantiske, hans hår basic, og hans solbriller for ham til at se duchy ud. Men der er stadig et eller andet som vækker sommerfuglene nede i din mave."
    "i smiller sødt til hinanden, og du går over til ham, og han går mod dig"

    menu:

        "hvordan vil du introducere dig selv"

        "Kig saftigt på ham":
            
            "Du kigger saftigt på ham, har er måske nok den smukkeste mand du har lagt dine øjne på"
            "Du gør det sikkert at han lægger mærke til dine følelser"
            "Han rødmer"

            ukendt "J- je- jeg hed- hedder Mag- Magnus"
            
            player "Heyyy Snuske, jeg mener Mangnus, jeg er Nordin"

        "introducere dig selv":
            player "Jeg er Nordin, men du kan bare kalde mig Nordin"

            ukendt "Jeg er Magnus men du kan bare kalde mig Mangus"

            $ magnus = Character("Mangus")

        "Diss ham":
            player "Du lugter og ligner en basic ass white boy"
            player "Prøv at få nogen bitches"
            
            "Ingen synes det var særlig sjovt, men efter lidt tid for han taget sig sammen og siger:"

            ukendt "Det derfor jeg er her..."
            ukendt "Men jeg hedder Magnus, ikke særlig rart at møde dig"


        "Sig noget sejt":
            player "Hva så der, Nordin her"

            ukendt "Howdy partner, jeg er Magnus"
            ukendt "Men du kan bare kalde mig Cowboy Magnus"

            $ magnus = Character("Cowboy Magnus")

    "Efter I introduceret jer til hinanden snakker i lidt"

    hide magnus

label magnus_round1_fitness:
    show magnus:
        zoom 1.2
        yalign 2.2
        xalign 0.7
    
    "Du kigger på hans sexy krop"
    
    menu:
        "Den er megen veltrænet"

        "Dream body":
            player "Hvad er din dream body"

            magnus "Nogen der er stærk, men de skal ikke se alt for buff ud, ykyk"

            player "Aaah, jaer"
            player "Jeg kan nu godt lide når man kan se deres muskler, det er sku lidt sexy"
        
        "Rør ved hans muskler":
            "Uden at spørge begynder du at røre ham"
            "Du starten fra røven af, og begynder at arbejde op mod hans bryst"

            "Hans ansigt bliver rødt, men han siger aldrig at du skal stoppe"
            "Sådan står i bare i et stykke tid, hvor du piller lidt ved hans muskler"

            "..."
            "Efter lidt tid"
            "..."

            magnus "Damn..."
            magnus "Det var nok det mest gay..."
            magnus "Og det bedste jeg nogensinde har prøvet"
            mangus "tak"

            "Du smiler bare lumsk og siger:"
            player "det var så lidt, og skulle det være en anden gang"

        "Snak om jeres yndlings øvelser"
            mangus "Jeg kan sku lide at træne lidt af det hele"
            mangus "Men hvis der er dumbbells med så ved du bare det bliver godt 💪"   

            player "Jeg kan nu best lide ben"
            player "Det bare dem man kan mærke mest, du ved"
        
