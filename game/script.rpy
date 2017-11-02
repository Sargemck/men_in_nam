# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Frank")
define h = Character("Harry")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Harry

    # These display lines of dialogue.

    f "What, you not gonna join the knuckleheads?"
    
    "Harry was referring to the heated row about a called foul from the guys in the court."
    "They sure knew how to get upset over basketball without any proper hoops."
    
    show Frank

    h "Ah, let 'em have their fun. They're good guys."
    h "Anyway, what you got there?"

    # This ends the game.

    return
