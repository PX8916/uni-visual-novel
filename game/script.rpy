# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[playername]")
define joy = Character("Joy")
define kath = Character("Kathryn")
define daisy = Character("Daisy")
define missy = Character("Missy")
define jared = Character("Jared")

transform leftish:
    xalign 0.25
    yalign 1.0

transform rightish:
    xalign 0.75
    yalign 1.0

transform slide_left:
#    xalign 1.0
    linear 1.0 xalign 0.0

transform slide_right:
#    xalign 0.0
    linear 1.0 xalign 1.0

# The game starts here.

label start:

    # Ask for the player's name.
    python:
        playerfullname = renpy.input("Before we begin the story, what is your full name?", length=48)
        playerfullname = playerfullname.strip()

        if not playerfullname:
            playerfullname = "Juan Dela Cruz"

        playername = renpy.input("What is your nickname?", length=12)
        playername = playername.strip()

        if not playername:
            playername = "Juan"

    "What are your pronouns?"
    menu:
        "He/Him":
            $pronounthey = "he"
            $pronounthem = "him"
            $pronountheir = "his"
            $pronounare = "is"
            $pronountheyre = "he's"

        "She/Her":
            $pronounthey = "she"
            $pronounthem = "her"
            $pronountheir = "her"
            $pronounare = "is"
            $pronountheyre = "she's"

        "They/Them":
            $pronounthey = "they"
            $pronounthem = "them"
            $pronountheir = "their"
            $pronounare = "are"
            $pronountheyre = "they're"

    python:
        if not pronounthey:
            pronounthey = "they"
        if not pronounthem:
            pronounthem = "them"
        if not pronountheir:
            pronountheir = "their"
        if not pronounare:
            pronounare = "are"
        if not pronountheyre:
            pronountheyre = "they're"

    pause 1.0
    "Day 1"

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
    show missy confused at center

    "You turn around to see your friend Missy standing in front of the door."

    "She is in her usual accessories. Shades she never wears for her eyes, maybe using them as an illusion for extra inches to her height..."
    "...a weird silk fabric thing on her neck with intricate designs of green flowers, and a bag slung around her shoulders..."
    "...which I'm sure is only big enough to hold a phone and a wallet."

    player "Hey, Missy. Where you off to?"

    show missy calm at center
    missy "The restroom. I'm just gonna comb my hair. How about you, what are you doing here? The poetry club is in the other building, 2nd floor. Did you take a wrong turn, or...?"

    player "Nope, No wrong turn here. I actually... quit the poetry club."

    show missy confused at center

    missy "You quit it? Mid-year? I didn't know that was allowed..."

    player "Well, it is. I talked to Sir. Brent about it and found a new club."

    "At this point, Missy had a good guess as to where this was going. There was no other club on this floor but the baking club."

    show missy irritated at center
    missy "Oh? Is that new club perhaps-"

    show joy happy at rightish
    show missy at leftish

    "???" "There you are, [playername]! Just in time, the gang's all here!"

    "She chirps, standing aside for both you and Missy to enter the room."
    "Missy sighs, following you back into the classroom."
    "Before you could follow Missy as she joins the other two girls in the club, that cheerful girl from a while ago gently places her hand over your shoulder."

    scene bg front_left
    show joy happy at center
    with Dissolve(1.0)

    "???" "Alright, girls! This is the new member! The one I was talking about in the group chat! Say hello, [playername]."

    "She urges. Her eyes are bright, gloating with the kind of life most people lose once they finish elementary."
    "There was a child-like wonder to her aura. The pink ribbons in her hair and the seamless blush make up only added more personality to her charming aura."

    scene black
    with Dissolve(0.75)
    pause(0.75)
    "Joy. The baking club's bright Joy. The baking club's bright and energetic president."
    "Everyone on campus knows her. Twin sister to the most popular guy on campus, Jared. Both the twins are admired for their exceptional skills in sports, music, academics, and most importantly, culinary arts."
    "According to school rumors, the only reason Joy established the baking club is because her twin brother founded the cooking club, and she didn't want to be outshone by him. Their friendly sibling rivalry is a well known thing around campus."

    scene bg front_left
    show kath calm at leftish
    with Dissolve(0.75)

    "???" "Oh wow, our first boy."

    "The tallest girl giggles. Her friend nudges her side."

    show daisy irritated at center behind kath
    "???" "Kathryn..."

    "The meek girl next to her scolds."
    "Kathryn looks at her friend with fond eyes, attempting to reassure her that the jab to my gender was not a big deal- which really, it was not."

    player "Don't worry, I don't mind. Although, it does seem like we lack a few members..."

    hide daisy
    hide kath
    with Dissolve(0.75)

    "\(I didn't tell anyone but, this was one of the reasons I joined this club. Other than being interested because of the desserts I often stole from Missy during recess.\)"
    "\(The cherry on top was that there were so few members. I never enjoyed being in a room with a lot of people.\)"
    "\(If I had to socialize, I'd prefer to do so in a small bubble.\)"
    "\(But I feigned confusion anyway, pretending I was never aware of their lack of members.\)"

    show missy happy
    with Dissolve(0.75)
    missy "That's because everyone's at the cooking club."

    show joy irritated at right
    joy "{i}groans{/i}"

    show kath irritated at left
    kath "Oh, don't listen to Missy. Half his members can't cook to save their lives, right?"
    show kath happy at left
    kath "It's about quality, not quantity!"

    "The girls next to Kathryn nod in unison, comforting Joy. Joy then claps her hands together to command attention."

    show joy happy at right
    joy "Alright, back to business! Since [pronounthey]'s new here, why don't we all introduce each other?"

    hide missy
    hide kath
    show joy happy at center
    joy "I'll go first. Hai hai! My name is Joy Jacinto, you've already met me because of, well, the whole club switching ordeal. I'm the club president!"

    hide joy
    show kath smile at center
    "Kathryn then steps forward."

    kath "Hello, I'm Kathryn Cruz. 11th grade STEM, classmates with Daisy here. I joined since I'm great with sugar arts, and I love sweet smells. I'm the club's treasurer."

    "Kathryn then looks at Daisy, and so the meeker girl steps forward."

    hide kath
    show daisy happy at center
    daisy "Hi... I'm Daisy Li. I'm the club's secretary and... I only joined the club because Kathryn did so..."

    "Daisy said with a shy smile. Probably feeling her reason for joining wasn't a good one."

    hide daisy
    with Dissolve(0.75)
    "I chuckled, feeling comfort knowing I'm not the only member with an unrelated reason to join a baking club."

    "Heck, I couldn't even bake a pancake if I tried. Or was that cooking? Are pancakes just cakes that can be cooked?"

    show missy irritated at center
    missy "*coughs*"
    show missy happy
    missy "And you already know who I am. Missy Mendoza, joined because i {b}can bake{/b}, and I'm friends with Joy. I'm the vice president."

    "Missy said, already knowing first-hand how bad my baking skills are. One time at her place, I didn't know the difference between a teaspoon and a tablespoon."
    "I made the saltiest cupcakes ever."

    show joy happy at right
    joy "Meaning, she's only useful when I'm absent. Which is never happening on my perfect attendance."

    "Joy said proudly."

    "Now that everyone else spoke, I guess it was my turn."

    menu:
        "(Name, Grade, why I joined)":
            $choice_no1 = 1
            jump choice_no1_1
        "(Name, Hobbies, irritate Missy)":
            $choice_no1 = 2
            jump choice_no1_2
        "(Name, interests, gossip about poetry club)":
            $choice_no1 = 3
            jump choice_no1_3

label choice_no1_1:
    player "Hi. I'm [playerfullname]. 11th grade HUMSS, and I joined because things were getting a bit too dramatic back at poetry club..."
    player "I thought Missy had a really cool club and so I just copied her. No escaping me, Missy."

    "I joked, watching my poor friend groan. I'd almost feel bad if it weren't so funny."

    show missy irritated
    missy "Why am I still friends with you."

    "I wink in response."
    jump choice_no1_done

label choice_no1_2:
    player "Hi. I'm [playerfullname]. My hobbies are journaling, reading manga, and taking free snacks from Missy."

    "I said with a playful smile while side eyeing my friend."

    show missy smile
    missy "Well, since you're already here, you have no reason to be stealing my snacks. I make them here, anyway."

    player "Haha, no promises."
    jump choice_no1_done

label choice_no1_3:
    player "Hi. I'm [playerfullname]. And well... I'm interested in writing and reading manga."
    player "It's kind of why I was in the poetry club."

    show kath smile at left
    kath "Ow, that's cool. But why did you quit?"

    player "A lot of drama... don't let this spread, but ever since i joined, the members there have been going crazy."
    player "Their vice president would just skip meetings to hang out, who knows where..."
    player "...this tall girl would read the weirdest books that were both explicit and gory..."
    player "...this other girl kept popping her joins while reading, and their president? Total control freak."

    show kath confused
    kath "Oh my..."
    jump choice_no1_done

label choice_no1_done:
    hide joy
    hide missy
    hide kath
    with Dissolve(0.75)

    "After the whole introduction, Joy gestures to me to take a seat. She then went straight into leader mode."

    show joy happy at center
    joy "Okay everyone! As you all know, next week is Halara! So we need to brainstorm ideas for what our club will present for the Halara fair."

    "Ah yes. Halara. Now an annual thing in our school that just started a year ago from the old senior high student council."
    "At the 2nd and 3rd weeks of December, a sort of club fair takes place. Each and every club gets 1-2 days to show off the best of what they can do."
    "They are judged by every department head in school. On the last day, the awards are given, and the best performing clubs are announced."
    "The winner not only gets a perfect mark for the club grades, but also a 800 peso gift card for the canteen. And a trophy too I guess."

    show joy at rightish
    show kath happy at leftish

    kath "Oh, why don't we just hold a mini cafe with cute miniature sweets and pastries!"

    show daisy confused at left
    daisy "Didn't the baking club do that last year?"

    show joy confused
    joy "Right, and that only got us 5th place. I like the idea, but maybe we should have something bolder?"

    show missy calm at right
    missy "Parlor games?"

    player "And what does that have to do with baking?"

    show missy irritated
    missy "I don't know, the food court could be a prize, maybe."

    player "Hard pass."

    "I was already feeling a bit too comfortable in this club."

    show daisy calm
    daisy "You know, I kinda liked that idea of a cafe..."

    show joy irritated
    joy "Yeah, but the cooking club is going to set up a cross dressing alfresco mini restaurant thing. I don't want our presentation to look like the basic or boring version of that."

    show kath confused
    kath "Cross dressing? That's some advertising."

    show missy happy
    missy "I know I'm going."

    "The two girls smirked shamelessly. I'd be lying if I said I wasn't interested myself."

    show joy irritated
    joy "Girls. Focus."

    "...after gathering enough courage, Daisy spoke up again."

    show daisy calm
    daisy "Then... maybe ours could be themed too. Like, woodland fae themed."

    show kath happy
    kath "OMG, yes! That sounds so adorable!"

    show joy sad
    joy "I don't know..."

    player "Maybe we could attract more attention if we have fancy sweets and pastries too?"

    show kath happy
    kath "Yes yes yes! We could have like eclairs, madeleines, cream puffs..."

    "As Kathryn kept listing french pastries, Missy leaned in and whispered to me."

    show missy smile
    missy "I can't bake puff pastries to save my life."

    "I chuckled before leaning in."

    player "I thought you knew how to bake."

    show missy irritated
    missy "I do know how to bake. I just have struggles with airy stuff. At least she didn't say macarons."

    "Kathryn then turned to Missy, her eyes wide and attentive like a hawk. Her smile was anything but comforting!"

    show kath happy
    kath "That's a perfect idea! Macarons! Our main will be maracons!"

    show missy sad
    missy "Wait! But that's not what-"

    show daisy happy
    daisy "Macarons really do taste good..."

    show joy happy
    joy "I love the idea!"

    player "What a nice suggestion, Missy!"

    "I added to the jab while she was visibly wincing..."

    show joy happy
    joy "Well then. Since we are all on board, it's decided! We will hold a mini fae themed cafe with our main desserts being macarons accompanied with other french pastries!"

    "As most of us cheered, excluding my friend next to me, Joy then asked a very important question."

    show joy smile
    joy "So, Kathryn. You'll teach us how to make macarons tomorrow, yes?"

    show kath confused
    kath "Oh, um..."

    "She turns away slightly with a nervous smile."

    show kath happy
    kath "I don't know how to make macarons… but the others, I can bake! Maybe one of you girls knows how?"

    show daisy confused
    daisy "Uhm..."

    show missy smile
    missy "Nope."

    player "Oh, uh..."

    show joy smile
    joy "I see… Well then, we still have a week. Looks like we'll just have to practice making macarons!"
    joy "I believe we can do this!"

    show joy happy
    show missy happy
    show kath happy
    show daisy happy
    "Everyone" "Yeah!"
    jump day2start