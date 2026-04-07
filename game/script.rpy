# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playername]")
define joy = Character("Joy")
define kath = Character("Kathryn")
define daisy = Character("Daisy")
define missy = Character("Missy")

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    # Ask for the player's name.
    python:
        playerfullname = renpy.input("Before we begin the story, what is your full name?", length=48)
        playerfullname = playerfullname.strip()

        if not playerfullname:
            playerfullname = "John Dela Cruz"

        playername = renpy.input("What is your nickname?", length=12)
        playername = playername.strip()

        if not playername:
            playername = "John"

    "What are your pronouns?"
    menu:
        "He/Him":
            $pronoun1 = "he"
            $pronoun2 = "him"
            $pronoun3 = "his"
            $pronoun4 = "is"

        "She/Her":
            $pronoun1 = "she"
            $pronoun2 = "her"
            $pronoun3 = "her"
            $pronoun4 = "is"

        "They/Them":
            $pronoun1 = "they"
            $pronoun2 = "them"
            $pronoun3 = "their"
            $pronoun4 = "are"

    scene bg hallway
    with Dissolve(0.75)

    pause 0.75

    "As you walk at the hallway, you turn to look at the windows that pass by."

    "You notice the bright blue sky up ahead, without a single cloud blemishing its hue."

    "The simplicity amuses you."

    "You see a flock of maya birds descend around a tree from the roof, making you feel better."

    scene bg booths
    with Dissolve(0.75)

    pause 0.75

    "Looking down from the window, as your steps slow a bit to gaze down, you notice a few students in groups of three."

    "Those students seemingly claimed their own designated spot on the field, with tables marking their territory."

    "???" "[playername]?"

    scene bg hallway
    show missy concerned

    pause 0.75

    "You turn around to see your friend Missy standing in front of the door."

    "She is in her usual accessories-"

    player "Hey, Missy. Where you off to?"

    missy "Sa restroom. I'm just gonna comb my hair. Pero ikaw, what are you doing here? The poetry club is in the other building, 2nd floor. Did you take a wrong term, or...?"

    player "Nope, No wrong turn here. Ito kasi... I actually quit the poetry club."

    show missy shocked

    missy "You quit it? Mid-year? Pwede pala yun... kala ko bawal."

    player "Well, pwede siya. I talked to Sir. Brent about it and found a new club."

    "At this point, Missy had a good guess as to where this was going. There was no other club on this floor but the baking club."

    missy "Oh? Is that new club perhaps-"

    show joy at rightish
    show missy at leftish behind joy

    "???" "There you are, [playername]! Just in time, nandito lahat kami."

    "She chirps, standing aside for both you and Missy to enter the room."
    "Missy sighs, following you back into the classroom."
    "Before you could follow Missy as she joins the other two girls in the club, that cheerful girl from a while ago gently places her hand over your shoulder."

    "???" "Alright, girls! This is our new member! Yung kinukwento ko sa group chat! Say hello, [playername]."

    "She urgers. Her eyes are bright, gloating with the kind of life most people lose once they finish elementary."
    "There was a child-like wonder to her aura. The pink ribbons in her hair and the seamless blush make up only added more personality to her charming aura."

    # scene bg - which classroom bg though
    show joy normal
    "Joy. The baking club's bright Joy. The baking club’s bright and energetic president."
    "Everyone on campus knows her. Twin sister to the most popular guy on campus, Jared. Both the twins are admired for their exceptional skills in sports, music, academics, and most importantly, culinary arts."
    "According to school rumors, the only reason Joy established the baking club is because her twin brother founded the cooking club, and she didn’t want to be outshone by him. Their friendly sibling rivalry is a well known thing around campus."

    show kath
    "???" "Oh wow, our first boy."

    "The tallest girl giggles. Her friend nudges her side."

    show daisy
    "???" "Kathryn..."

    "The meek girl next to her scolds."
    "Kathryn looks at her friend with fond eyes, attempting to reassure her that the jab to my gender was not a big deal- which really, it was not."

    player "Don't worry, I don't mind. ALthough, parang kulang nga tayo sa members..."

    pause 0.5

    "\(I didn't tell anyone but, this was one of the reasons I joined this club. Other than being interested because of the desserts I often stole from Missy during recess.\)"
    "\(The cherry on top was that there were so few members. I never enjoyed being in a room with a lot of people.\)"
    "\(If I had to socialize, I'd prefer to do so in a small bubble.\)"
    "\(But I feigned confusion anyway, pretending I was never aware of their lack of members.\)"

    missy "That's because everyone's at the cooking club."

    joy "*groans*"

    kath "Oh, don't listen to Missy. Half his members can't cook to save their libes, diba? It's about quality, not quantity!"

    "The girls next to Kathryn nod in unison, comforting Joy. Joy then claps her hands together to command attention."

    joy "Alright, back to business! Since [pronoun1]'s bago siya dito, why don't we all introduce each other?"

    joy "Ako muna. Hai hai! My name is Joy Jacinto, kilala mo na ako because of, well, the whole club switching ordeal. I'm the club president!"

    "Kathryn then steps forward."

    show kath
    kath "Hello, I'm Kathryn Cruz. 11th grade STEM, classmates with Daisy here. I joined as magaling ako sa sugar arts, and I love sweet smells. I'm the club's treasurer."

    "Kathryn then looks at Daisy, and so the meeker girl steps forward."

    daisy "Hi... I'm Daisy Li. I'm the club's secretary and... Sumali lang ako dahil sumali si Kathryn..."

    "Daisy said with a shy smile. Probably feeling her reason for joining wasn't a good one."

    "I chuckled, feeling comfort knowing I’m not the only member with an unrelated reason to join a baking club."

    "Heck, I couldn't even bake a pancake if I tried. Or was that cooking? Are pancakes just cakes that can be cooked?"

    missy "*coughs*"

    missy "And you already know who I am. Missy Mendoza, joined because i *can bake*, and kaibigan ko si Joy. Ako ang vice president dito."

    "Missy said, already knwoing first-hand how bad my baking skills are. One time at her place, I didn't know the difference between a teaspoon and a tablespoon."
    "I made the saltiest cupcakes ever."

    joy "Meaning, may silbi lang siya pag nag absent ako. Which is never happening on my perfect attendance."

    "Joy said proudly."

    "Now that everyone else spoke, I guess it was my turn."

    player "Hi. Ako po si [playerfullname]. 11th grade HUMSS, and sumali ako kasi things were getting a bit too dramatic back sa poetry club..."
    player "I thought Missy had a really cool club and so gumaya lang ako sa kanya. No escaping me, Missy."

    "I joked, watching my poor friend groan. I'd almost feel bad if it weren't so funny."

    missy "Well, since nandito ka na, you have no reason to be stealing my snacks. Dito ko naman ginagawa."

    player "Haha, no promises."

    # The game ends here.

    return
