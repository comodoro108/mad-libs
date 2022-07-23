# Mad Libs - Jairo Garzon Santana 11/02/2022

# Loop back to this point once code finishes
ronda = 1

while (ronda < 10):

    # preguntas para el usuario!
    sustantivo = input("Selecciona un sustantivo: ")
    sustantivo_pl = input("Selecciona un sustantivo en plural: ")
    sustantivo2 = input("Selecciona un sustantivo: ")
    lugar = input("Nombra un lugar: ")
    adjetivo = input("Selecciona un adjetivo (Describe una palabra): ")
    sustantivo3 = input("Selecciona un sustantivo: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Se amable con tu",sustantivo,"- patea", sustantivo_pl)
    print ("piensa en ", sustantivo2,",")
    print ("Se amable con tu",sustantivo,"en el",lugar)
    print ("donde el clima es siempre",adjetivo,".")
    print ()
    print ("Puedes pensar que siempre sea",sustantivo3,",")
    print ("Bien eso es todo.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    ronda = ronda + 1