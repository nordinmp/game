include "../function.rpy"

define christoffer = Character("Cristoffer")

init python:
    christoffer_datable_score = 0

label christoffer_round1_intro:

    show christoffer:
        zoom 1.5 
        yalign 0.7
        xalign 0.75

        
    "Det er en asiatisk \"mand\". Han kigger på dig, I får øjenkontakt"

    "I stirrer intenst på hinanden - ikke romantsk bare intenst"

    "du hører en værten sige:"
    vært "HVIS DU IKKE HAR FUNDET EN NY PARTNER ER DET VED AT VÆRE SIDSTE CHANCE"

    "Du går over mod ham, og han imod dig, stadig med en meget dyb øjenkontakt, som kun døden kan skildre"

    "\"Hey\" siger asiateren til dig"

    menu:
        player "hvordan skal jeg svarer"

        "Hej selv du":
            player "Hey, selv du"

            "Han begynder at smile nu, det var tydeligt han synes det var meget erotisk sagt"

            ukendt "Min navn er Christoffer men du kan bare kalde mig Chrisser"

            $ christoffer = Character("Chrisser")
            $ christoffer_datable_score += 10

        "Lav sjov med hans udseende":
            "du tager hænderne op til øjnene og laver dem skæve"
            player "Ching Chong"

            "han griner, men du kan ikke gennemskue om han griner fordi det er sjovt, eller om han er i dyb smerte."

            "Du finder ud af at hans navn er Christoffer"
            
            $ christoffer_datable_score += 5

        "Svin ham til":
            "du siger noget om hvordan han ser ud. Asiateren synes ikke det er sjovt, og sviner dig tilbage"

            $ christoffer = Character("Asiater")

            $ christoffer_datable_score -= 5


        "introducere dig selv":
            "Du griner lidt - men ikke der skete noget sjovt"

            player "Jeg hedder Nordin, og du kan bare kalde mig Nordin"

            ukendt "Jeg hedder Christoffer"

            $ christoffer_datable_score += 2


        "Kram ham":
            "Du prøver at kramme ham, det virker, fordi han krammer dig tilbage lige med det samme, men du kan mærke noget omrkring din røv"

            "du kigger ned"

            "og ser han hans hænder hviler omkring dine balder"

            "Han hvisker forførende i dit ører"

            ukendt "Jeg hedder Christoffer, men du kan bare kalde mig Damrong"

            $ christoffer = Character("Damrong")

            $ christoffer_datable_score += 8

    hide christoffer

label christoffer_round1_interesser:

    show christoffer:
        zoom 1.5 
        yalign 0.7
        xalign 0.75

    menu:

        christoffer "Hvad er dine interesser?"

        "Snak om programmering":
            player "Jeg elsker at progge mine egene dating spil"

            christoffer "OMG, jeg progger også selv"
            christoffer "Lige nu er jeg ikke igang, baller bare du ved."

            menu:
                christoffer "Har du nogensinde været til en Game Jam?"

                "Ja":
                    player "Ja det har jeg, det var ret fedt"

                    $ christoffer_datable_score += 15

                "Nej (ikke interessant)":
                    player "Nææææ det kan jeg sku ikke sige jeg har"
                    player "Det er ikke lige noget jeg er interesseret i"

                    christoffer "Det er da en skam, ong ong"

                    $ christoffer_datable_score -= 2

                "Nej (ikke haft tid)":
                    player "Nej det har jeg ikke endnu"
                    player "Har ikke lige fundet tiden til det endnu"

                    christoffer "Nice du burde virkelig finde tid. Måske mødes vi endda 😏"

                    $ christoffer_datable_score += 10


                "Nej (vil ikke alene)":
                    player "Nej, jeg vil meget gerne, men"
                    player "Jeg vil ikke afsted alene"
                    player "Kunne du tænke dig at komme med en dag? 🥺👉👈"

                    christoffer "OMG, ja det vil jeg gerne"
                    "Du fik hans snap"

                    $ christoffer_datable_score += 25


        "Snak om hvor meget du elsker peanuts":
            player "Jeg er interesseret i at spise peanuts"
            christoffer "??"
            christoffer "Fortæl mig mere"
            "I snakker om din passion for peanuts"

            $ christoffer_datable_score += 10

            
        "Lav en skjult reference til hit serien Breaking Bad":
            "Den var ikke så skjult som du troede, for med det samme"
            "svarer han med:"
            christoffer "Let him cook👨‍🍳"
            "Han fangede hurtigt din reference og blev meget glad"

            $ christoffer_datable_score += 10


        "Snak om hvor meget du elsker små børn":
            christoffer "erm ja, det da meget cool?"
            "Han er lidt forvirret, men svarer"
            christoffer "Jeg har også en lillebror, men det der er måske lidt for meget"

            "Efter en kort pause tilføjer han:"
            christoffer "Vidste du at min lillebror faktisk er opkaldt efter Sebastian Klein"

            $ christoffer_datable_score += 5

    
    hide christoffer

label christoffer_round1_anime:

    show christoffer:
        zoom 1.5 
        yalign 0.7
        xalign 0.75

    "I kigger på hinanden hud"
    "Og i kor siger I"
    "OMG DU ER ASIATER SÅ DU MÅ SE ANIME"
    "(fordi man kan ikke være asiater uden at se anime)"

    menu:

        christoffer "hvad er den bedste anime?"

        "en hver slice of life":
            player "en hver slice of life, det er bare så wholesome"
            player "og der er et godt plot"

            christoffer "jeg er uenig"
            christoffer "Ikke at jeg siger nej til lidt fanservice."
            christoffer "Slice of life, fangede mig bare aldrig"

            "I bliver enig om at det er ok at være forskellige"

            $ christoffer_datable_score += 8

        "Isekai":
            player "Isekai - Jeg elsker at de alle er så unikke og at de har så godt et plot"

            christoffer "Jeg elsker TRUCK-KUN🚚"

            "Det bliver sagt lidt for højt, så alle kigger på ham, i en meget akavet stilhed"
            "Men stille og roligt vender folk tilbage til deres samtaler"
            
            christoffer "Men altså personligt synes jeg at der er lidt for mange furries, og hele det der harem noget det sku ik lige mig"
            christoffer "Men alle har være deres smag"

            $ christoffer_datable_score += 3


        "Death note":
            christoffer "ah yes, en klassiker 📓"
            "dog siger han øjne noget andet, de tænker \"Gud, en basic bitch\""

            menu:
                "Grunden til at du synes det er den bedste anime nogensinde er fordi"

                "Du er 14 år":
                    christoffer "WHAT"
                    # play a boom sound
                    christoffer "Du ser fanme gammel ud for din alder, og jeg har ikke drukket nok til at være pedo"
                    christoffer "Så du må have det godt"

                    $ christoffer_datable_score = 0

                    $ set_not_datable('Christoffer')

                    "Christoffer går fra dig, nu står du bare alene i et hjørne og tripper lidt, indtil at tiden går og du kan få en ny partner"

                "Temaet":
                    player "Jeg synes bare at det er sådan et godt sjov"
                    player "og temaet er mega godt, så solidt skrevet"

                    "Du er mega egdy og har en unik holdning"

                    christoffer "COOOOOOOOOOOOOOOOL...."
                    christoffer "Du er godt nok edgy og unik 👍"

                    $ christoffer_datable_score -= 5


                "Personerne":
                    player "Da jeg så det blev jeg bare fanget af personerne, de er så unikke "

                    menu:
                        "Hvem er din yndlings?"

                        "Light":
                            player "Light han er bare så klog, jeg vil sige han måske er den kloges..."

                            "Han putter sin finger op til din mund og siger:"

                            christoffer "SHHHHHHHH, ikke sig mere. Inden du gør dig mere til grin"

                            "I diskutere lidt frem og tilbage om hvorfor I er uenige"

                            $ christoffer_datable_score -= 5 


                        "L":
                            player "L han er bare så klog, jeg vil sige han måske er den klogeste i hele serien"

                            christoffer "Er helt enig, og I bonder lidt over at i begge er kloge og har ret"

                            $ christoffer_datable_score += 10

                        "Ryuk":
                            christoffer "🤨📸 hvem kan dog bedst lide ham, han er jo en dæmon"
                            christoffer "Du er bare så edgy, og unik"

                            $ christoffer_datable_score += 0

                        "Ingen":
                            player "Jeg kan ikke rigtigt lide nogen af dem"
                            "der kommer det størte spørgsmålstegn på han ansigt"
                            christoffer "Hvad memer du. Du giver ingen mening makker"

                            $ christoffer_datable_score += 1


                "Din far":
                    player "Det var det sidste min far så sammen med mig, inden han døde"
                    player "Derfor vil det altid har et specielt sted i mit hjerte"

                    "Han væd ikke helt hvad han skal sige til det, men siger at det er han ked af at hører"

                    $ christoffer_datable_score += 3


        "World's end harem":
            christoffer "erm ja, det da meget cool?"

            "Efter en kort pause tilføjer han:"
            christoffer "Jeg kan ikke forstå hvorfor folk vil se sådan noget, alt for meget harem."

            player "Ja, det nu ellers meget hyggeligt"

            $ christoffer_datable_score += 2

    
    hide christoffer

label christoffer_round1_outro:

    show christoffer:
        zoom 1.5 
        yalign 0.7
        xalign 0.75

    menu:
        vært "Tiden er næsten gået, så I skal begyndte at afslutte jeres samtaler"

        "Spørg om hans snap":
            if christoffer_datable_score > 25:
                "Du får hans snap, og du tjekker med det samme, for at tjekke at det er den rigtige han har givet dig"
            if christoffer_datable_score <= 25 and christoffer_datable_score >= 5:
                "Christoffer giver dig hans snap, men du får ikke dobbelt checked, og finder ud af at det var en secondary account, og at han ikke tjekker den så ofte"
            if christoffer_datable_score < 5:
                christoffer "NUH UH"

                "Han går, fordi han gider ikke mere af dit pis"

                $ christoffer_datable_score = 0

                $ set_not_datable('Christoffer')

        
        "Gå videre":
            "Der var ingen ild mellem jer to"
            player "Hyggeligt at møde dig"
            "Siger du inden du finder inden du går"
            if christoffer_datable_score > 20:
                christoffer "Vent ik g..."
                "Du er allerede for langt til at kunne hører hvad han siger"

                $ christoffer_datable_score = 0

                $ set_not_datable('Christoffer')

            else:
                "Han går lige så hurtigt væk som du gjorde"
        
        "Lav en joke":
            player "Jeg lader dig i stikken som politikere gør til de hjemløse"

            "Hans ansigt skriger bare \"Not funny didn't laugh\""
            
            $ christoffer_datable_score -= 10

        "Lav en reference":
            "Du laver en jojo reference"
            "Han ser glad ud"
            if christoffer_datable_score > 25:
                "Du får hans snap, og du tjekker med det samme, for at tjekke at det er den rigtige han har givet dig"
            if christoffer_datable_score <= 25 and christoffer_datable_score >= 5:
                "Christoffer giver dig hans snap, men du får ikke dobbelt checked, og finder ud af at det var en fake profil"
            if christoffer_datable_score < 5:
                christoffer "*kigger bare på dig, han troede lidt det ville ske noget mere*"
                "inden han beslutter sig for at finde en anden"

                $ christoffer_datable_score -= 5
    
    hide christoffer