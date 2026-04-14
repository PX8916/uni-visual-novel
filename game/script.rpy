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
        #playerfullname = renpy.input("Before we begin the story, what is your full name?", length=48)
        #playerfullname = playerfullname.strip()

        #if not playerfullname:
            playerfullname = "Juan Dela Cruz"

        #playername = renpy.input("What is your nickname?", length=12)
        #playername = playername.strip()

        #if not playername:
            playername = "Juan"

    #"What are your pronouns?"
    #menu:
    #    "He/Him":
    #        $pronounthey = "he"
    #        $pronounthem = "him"
    #        $pronountheir = "his"
    #        $pronounare = "is"
    #        $pronountheyre = "he's"
#
    #    "She/Her":
    #        $pronounthey = "she"
    #        $pronounthem = "her"
    #        $pronountheir = "her"
    #        $pronounare = "is"
    #        $pronountheyre = "she's"
#
    #    "They/Them":
    #        $pronounthey = "they"
    #        $pronounthem = "them"
    #        $pronountheir = "their"
    #        $pronounare = "are"
    #        $pronountheyre = "they're"

    python:
        #if not pronounthey:
            pronounthey = "they"
        #if not pronounthem:
            pronounthem = "them"
        #if not pronountheir:
            pronountheir = "their"
        #if not pronounare:
            pronounare = "are"
        #if not pronountheyre:
            pronountheir = "they're"

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
    show missy concerned

    "You turn around to see your friend Missy standing in front of the door."

    "She is in her usual accessories. Shades she never wears for her eyes, maybe using them as an illusion for extra inches to her height..."
    "...a weird silk fabric thing on her neck with intricate designs of green flowers, and a bag slung around her shoulders..."
    "...which I'm sure is only big enough to hold a phone and a wallet."

    player "Hey, Missy. Where you off to?"

    missy "The restroom. I'm just gonna comb my hair. How about you, what are you doing here? The poetry club is in the other building, 2nd floor. Did you take a wrong turn, or...?"

    player "Nope, No wrong turn here. I actually... quit the poetry club."

    show missy shocked

    missy "You quit it? Mid-year? I didn't know that was allowed..."

    player "Well, it is. I talked to Sir. Brent about it and found a new club."

    "At this point, Missy had a good guess as to where this was going. There was no other club on this floor but the baking club."

    missy "Oh? Is that new club perhaps-"

    show joy at rightish
    show missy at leftish behind joy

    "???" "There you are, [playername]! Just in time, the gang's all here!"

    "She chirps, standing aside for both you and Missy to enter the room."
    "Missy sighs, following you back into the classroom."
    "Before you could follow Missy as she joins the other two girls in the club, that cheerful girl from a while ago gently places her hand over your shoulder."

    scene bg front_left
    with Dissolve(1.0)

    show joy
    with Dissolve(0.5)
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
    with Dissolve(0.75)

    show kath at leftish
    "???" "Oh wow, our first boy."

    "The tallest girl giggles. Her friend nudges her side."

    show daisy at rightish behind kath
    "???" "Kathryn..."

    "The meek girl next to her scolds."
    "Kathryn looks at her friend with fond eyes, attempting to reassure her that the jab to my gender was not a big deal- which really, it was not."

    player "Don't worry, I don't mind. Although, it does seem like we lack a few members..."

    hide daisy and kath
    with Dissolve(0.75)

    "\(I didn't tell anyone but, this was one of the reasons I joined this club. Other than being interested because of the desserts I often stole from Missy during recess.\)"
    "\(The cherry on top was that there were so few members. I never enjoyed being in a room with a lot of people.\)"
    "\(If I had to socialize, I'd prefer to do so in a small bubble.\)"
    "\(But I feigned confusion anyway, pretending I was never aware of their lack of members.\)"

    show missy
    with Dissolve(0.75)
    missy "That's because everyone's at the cooking club."

    show joy angry at right
    joy "*groans*"

    show kath at left behind missy
    kath "Oh, don't listen to Missy. Half his members can't cook to save their lives, right? It's about quality, not quantity!"

    "The girls next to Kathryn nod in unison, comforting Joy. Joy then claps her hands together to command attention."

    show joy
    joy "Alright, back to business! Since [pronounthey]'s new here, why don't we all introduce each other?"

    hide missy
    hide kath
    show joy at center
    joy "I'll go first. Hai hai! My name is Joy Jacinto, you've already met me because of, well, the whole club switching ordeal. I'm the club president!"

    hide joy
    "Kathryn then steps forward."

    show kath at center
    kath "Hello, I'm Kathryn Cruz. 11th grade STEM, classmates with Daisy here. I joined since I'm great with sugar arts, and I love sweet smells. I'm the club's treasurer."

    "Kathryn then looks at Daisy, and so the meeker girl steps forward."

    hide kath
    show daisy
    daisy "Hi... I'm Daisy Li. I'm the club's secretary and... I only joined the club because Kathryn did so..."

    "Daisy said with a shy smile. Probably feeling her reason for joining wasn't a good one."
    
    hide daisy
    with Dissolve(0.75)
    "I chuckled, feeling comfort knowing I'm not the only member with an unrelated reason to join a baking club."

    "Heck, I couldn't even bake a pancake if I tried. Or was that cooking? Are pancakes just cakes that can be cooked?"

    show missy annoyed at center
    missy "*coughs*"
    show missy
    missy "And you already know who I am. Missy Mendoza, joined because i *can bake*, and I'm friends with Joy. I'm the vice president."

    "Missy said, already knwoing first-hand how bad my baking skills are. One time at her place, I didn't know the difference between a teaspoon and a tablespoon."
    "I made the saltiest cupcakes ever."

    show joy at right
    joy "Meaning, she's only useful when I'm absent. Which is never happening on my perfect attendance."

    "Joy said proudly."

    "Now that everyone else spoke, I guess it was my turn."

    player "Hi. I'm [playerfullname]. 11th grade HUMSS, and I joined because things were getting a bit too dramatic back at poetry club..."
    player "I thought Missy had a really cool club and so I just copied her. No escaping me, Missy."

    "I joked, watching my poor friend groan. I'd almost feel bad if it weren't so funny."

    missy "Well, since nandito ka na, you have no reason to be stealing my snacks. Dito ko naman ginagawa."

    player "Haha, no promises."

    hide joy
    with Dissolve(0.75)

    "After the whole introduction, Joy gestures to me to take a seat. She then went straight into leader mode."

    show joy at center
    joy "Okay everyone! As you all know, next week is Halara! So we need to brainstorm ideas for what our club will present for the Halara fair."

    "Ah yes. Halara. Now an annual thing in our school that just started a year ago from the old senior high student council."
    "At the 2nd and 3rd weeks of December, a sort of club fair takes place. Each and every club gets 1-2 days to show off the best of what they can do."
    "They are judged by every department head in school. On the last day, the awards are given, and the best performing clubs are announced."
    "The winner not only gets a perfect mark for the club grades, but also a 800 peso gift card for the canteen. And a trophy too I guess."

    show joy at rightish
    show kath at leftish

    kath "Oh, why don't we just hold a mini cafe with cute miniature sweets and pastries!"

    show daisy at left

    daisy "Didn't the baking club do that last year?"

    joy "Right, and that only got us 5th place. I like the idea, but maybe we should have something bolder?"

    show missy at right

    missy "Parlor games?"

    player "And what does that have to do with baking?"

    missy "I don't know, the food court could be a prize, maybe."

    player "Hard pass."

    "I was already feeling a bit too comfortable in this club."

    daisy "You know, I kinda liked that idea of a cafe..."

    joy "Yeah, but the cooking club is going to set up a cross dressing alfresco mini restaurant thing. I don't want our presentation to look like the basic or boring version of that."

    daisy "Cross dressing? That's some advertising."

    missy "I know I'm going."

    "The two girls smirked shamelessly. I'd be lying if I said I wasn't interested myself."

    joy "Girls. Focus."

    "...after gathering enough courage, Daisy spoke up again."

    daisy "Then... maybe ours could be themed too. Like, woodland fae themed."

    kath "OMG, yes! That sounds so adorable!"

    joy "I don't know..."

    player "Maybe we could attract more attention if we have fancy sweets and pastries too?"

    kath "Yes yes yes! We could have like eclairs, madeleines, cream puffs..."

    "As Kathryn kept listing french pastries, Missy leaned in and whispered to me."

    missy "I can't bake puff pastries to save my life."

    "I chuckled before leaning in."

    player "I thought you knew how to bake."

    missy "I do know how to bake. I just have struggles with airy stuff. At least she didn't say macarons."

    "Kathryn then turned to Missy, her eyes wide and attentive like a hawk. Her smile was anything but comforting!"

    kath "That's a perfect idea! Macarons! Our main will be maracons!"

    missy "Wait! But that's not what-"

    daisy "Macarons really do taste good..."

    joy "I love the idea!"

    player "What a nice suggestion, Missy!"

    "I added to the jab while she was visibly wincing..."

    joy "Well then. Since we are all on board, it's decided! We will hold a mini fae themed cafe with our main desserts being macarons accompanied with other french pastries!"

    "As most of us cheered, excluding my friend next to me, Joy then asked a very important question."

    joy "So, Kathryn. You'll teach us how to make macarons tomorrow, yes?"

    kath "Oh, um..."

    "She turns away slightly with a nervous smile."
    
    kath "I don't know how to make macarons… but the others, I can bake! Maybe one of you girls knows how?"

    daisy "Uhm..."

    Missy "Nope."

    player "Oh, uh..."

    joy "I see… Well then, we still have a week. Looks like we'll just have to practice making macarons!"
    joy "I believe we can do this!"

    "Everyone" "Yeah!"

    scene black
    with Dissolve(0.75)

    pause 0.75
    "Day 2"

    scene bg gate
    with Dissolve(0.75)

    "It was a fresh morning. The sun was up high, the light bathing the school in its soft hue."
    "Which means I'm late. 8 AM."

    missy "Tsk tsk tsk. Late again?"

    "My friend scolds me. Waiting in the guard house. After tappign my ID, I walk up to her."

    player "What about you? Why are you here?" 

    show missy shrug
    missy "I came here to get my P.E. shirt. Left it at home and had it lalamoved. Then I saw you so I thought I'd wait a little."

    "I noticed she was holding a plastic bag. Must be where her P.E. uniform is, no doubt."

    player "Let's go in together."
    
    scene black
    with Dissolve(0.75)

    "She nodded and we waited side by side to the school."

    scene field_for_booth
    with Dissolve(0.75)

    "While walking to our building, Missy speaks up."

    missy "In just a week, our booth will be somewhere here."

    player "Crazy how it's already the end of the first semester… So, what time will Kathryn be teaching us how to bake macarons?"

    missy "Oh, Kathryn won't be teaching us."

    player "Huh?"

    missy "She said she'll be busy or something with Joy. Not sure. Oh right, I'll have to add you to the baking club group chat."

    scene black
    with Dissolve(0.75)

    "Once we pass by her building, she waves me bye and we go our separate ways. I look down at my phone and see I was just added to the groupchat."

    scene bg hallway
    with Dissolve(0.75)

    "After my last classes, I go straight to the club room."

    show daisy surprised at rightish
    
    daisy "Ack!"

    "I accidentally bump into Daisy as she exits her classroom. Kathryn just behind her giggling softly."

    show kath at leftish

    kath "Ow, Daisy, are you okay?"

    daisy "Y-yeah, I'm okay… "

    show daisy flustered

    daisy "Daisy: oh- Oh, OH! (player) I'm so sorry! Are you hurt? I didn't mean to! I wasn't looking and i was mid chat with Daisy and I just…"
    menu:
        "It's alright, Daisy.":
            $choice_no1 = 1
            jump choice_no1_1
        "Why were you in a rush?":
            $choice_no1 = 2
            jump choice_no1_2
        "Uhhhhh":
            $choice_no1 = 3
            jump choice_no1_3

    label choice_no1_1:
        player "Haha, It's alright Daisy. It's not like I got hurt. How about you? Are you okay?"
        daisy "Oh, yes... I'm alright. I'm sorry again for bumping into you."
        "Daisy shyly tucks a loose strand of hair behind her ear. Looking off to the side, perhaps hoping her friend could interfere with the sudden awkward cadence in the air."
        jump choice_no1_done
    label choice_no1_2:
        player "Why were you in a rush? What if I was holding something."
        daisy "Right! I'm sorry- I'm so… I'm- I didn't mean to..."
        kath "It's alright, Daisy."
        "Kathryn said, glaring at me before her hands found Daisy's shoulders in hopes to steady her shaking friend. But it was her fault in the first place to not be looking where you're going."
        "Honestly, she should be more careful. Daisy then coughed to redirect the attention back to her."
        jump choice_no1_done
    label choice_no1_3:
        player "Uhhhhh UHHHHHHHHHHHH no no its okay i just... uhhhhhhhhh..."
        "Both Daisy and Kathryn chuckles at my flustered response. My lack of better social skills is becoming painfully obvious."

    label choice_no1_done:
        show daisy
        kath "Anyways... I'm guessing you're also on your way to LV 304?"

        player "Yeah. Wanna walk with?"

        "The two girls looked at each other for a few seconds before nodding. It's not like they had much of a choice anyways since I was already here and we were all going the same way. What are they going to do? Say no? That would go against social conventions."
    
    scene bg front_left
    with Dissolve(0.75)

    "As we entered the classroom, I saw Missy on her phone watching some tutorial on macarons with an unamused look in her eyes, and Joy in front of the white board contemplating the list written on it."

    "Joy turned around seeing us enter. She clapped her hands together with a ready look on her face."

    show joy at leftish
    "Joy: Great! You're all here! Okay everyone. Today is an important day. Day 1 of macaron making! But also day 1 for ingredient prepping for the other baked goods. Kath, you're with me."

    show kath at rightish
    "Kathyrn nods in response."

    joy "Then the rest of you will stay to practice on the macarons without us."

    "Joy then gestured to the blue plastic bags with a large SM logo. From where I'm standing, I could see flour, sugar, eggs, and small glass bottles. Maybe those being dye or flavorings."

    joy "The equipment is all at the TLE lab. I already got permission from Miss Ange to use the room."

    hide joy and kath
    with Dissolve(0.75)

    "Missy and Daisy seemed to share the same expressions, but both for different reasons."

    "Missy was looking off to the side annoyed. Still not fully on board with the macaron plan. While Daisy wa`s looking off to the side anxious, probably hoping the first attempt goes well."

    "Kathryn then realised something while looking at the list of ingredients on the wall. She turned to Joy."

    show kath at leftish
    kath "Joy?"

    show joy at rightish
    joy "Hmm?"

    kath "I think that's a lot on the list... won't it be a lot for just the two of us to get?"

    "Joy turned back to the list. It wasn't a lot of ingredients, the problem was everything else. The decorations, the packaging, and the weight of all those ingredients."
    "The once so cheery girl now seemed perplexed. She rubbed her chin and thought about it."

    joy "Maybe we do need another hand… oh, (player), do you think you could help us? I'm sure Missy and Daisy will be fine on their own making macarons. We will still make macarons today, just after we do some shopping."
    menu:
        "I don't know...":
            $choice_no2 = 1
            jump choice_no2_1
        "Sure! Why not?":
            $choice_no2 = 2
            jump choice_no2_2

    label choice_no2_1:
        "Joy sighs."
        
        kath "It is hot today..."
    label choice_no2_2:
        "WIP"
    # The game ends here.

    return
