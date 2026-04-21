# Day 3 starts here.
# This is around the point there aren't proper character emotions.

label day3start:

    # Player substitution if necessary.
    python:
        if not playerfullname:
            playerfullname = "Juan Dela Cruz"

        if not playername:
            playername = "Juan"

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

    scene black
    pause 0.75
    "Day 3"

    scene bg stairs
    with Dissolve(0.75)

    "It was another usual day. At least, it would have been if not it being day 2 for another round of macaron making hell."
    "Hopefully, today will be a successful batch that everyone in the club can agree on."
    "Classes just ended and I was on the way to the TLE room."

    show kath smile
    kath "[playername], oh, hey there!"

    "Kathryn waved to me, coming from the TLE room. Odd, she should be helping us."

    player "Hi, Kath. Where are you going? Don't we all need to help with macaron making today?"

    kath "Oh, I was excused to go home so I can get to work on the other pastries. Macarons will be all on yo guys~"

    menu:
        "Well that's not fair.":
            $choice_no8 = 1
            jump choice_no8_1
        "Lucky. Wish I can bail out.":
            $choice_no8 = 2
            jump choice_no8_2
        "Wait, you're baking all the rest?":
            $choice_no8 = 3
            jump choice_no8_3

label choice_no8_1:
    player "Well that's not fair. Why do you get a pass at the pain of macaron baking?"

    "It seemed I gave the wrong reaction, because the look she gave me..."
    "...was almost that of a parent trying to teach their child manners."
    "She stood tall, composed, and elegant as always. Even her sigh carried a manner of grace."

    show kath irritated
    kath "While I'm not baking macarons, I'm still baking. Madeleines, Eclairs, and cream puffs are no walk in the park."
    jump choice_no8_done
label choice_no8_2:
    player "Lucky. Wish I could bail out like that. I hate making those cookies."

    "Kathryn chuckled softly. Her voice carried a demure aura even when complaining."

    show kath smile
    kath "Tell me about it. I hated baking those things yesterday."
    kath "I can't believe mine burnt... I'm usually really good with puff pastries..."

    jump choice_no8_done
label choice_no8_3:
    player "Wait, you're baking all the rest on your own?"

    "Kathryn nodded with a modest smile. Almost everything about her demeanor right now seems to carry a sort of curt decorum."

    show kath happy
    kath "Nothing I'm not accustomed to. I bake about every week anyways. Pastries like these are a staple in my home."
    jump choice_no8_done

label choice_no8_done:
    "Almost just on time, Joy pops out from the corner and sees us."

    show joy smile at right
    joy "Ah! There you are, [playername]. Kathy, why dont'cha join us? So we can have just an emergency mini meeting before departing."
    joy "Looks like we all have something to do for today."

    "Kathryn nodded and I followed after her as we ascended the stairs to the club room."

    scene bg hallway
    with Dissolve(0.75)

    "Instead of being brought into the TLE room, we stood outside of it. There, Missy and Daisy were waiting."

    "Joy then stood in the middle of our unconsciously formed half circle and announced."

    show joy smile at leftish
    show missy smile at left
    show kath smile at rightish
    show daisy calm at right

    joy "So, since we all will be doing something different for today, I just wanted to give a small assignment."
    joy "Make sure to at least attempt at least one batch of macarons of macarons."
    joy "Go ahead and take all the ingredients you need from the club room."

    "I titled my head a bit, confused."

    player "We won't be baking together?"

    joy "Not today since we all seem to be busy. Well, all of us but Missy."

    missy "I'll be staying at school to practice baking here."

    joy "I have a meeting with the student council and other club presidents."

    kath "I have to bake the other pastries at home."

    daisy "I have a book report due tomorrow that I need to write..."

    "They all seemed to have tasks that meant the club would have to go separate ways. All except Missy."

    joy "Do you have anything to do today, [playername]?"

    player "Nope. Classes are all done. Although... I guess I also have a book report I need to write..."
    player "but it's due in two days, so I have time."

    missy "If that's the case, you can stay here and help me bake macarons."

    "A perfectly reasonable offer, but then Joy spoke up."

    joy "Actually, if anyone needs help, it might be Kathy. She has to bake a lot of other pastries for the event other than macarons."

    kath "Oh, that would be a big help. But I can manage on my own."

    "Suddenly, I saw the book {i}I have no mouth, and I must scream{/i} poking out of Daisy's bag. Exactly the book my report is about..."

    player "Daisy, what's that book report about?"

    show daisy confused
    "She flinched and seemed unpleasant."

    daisy "Um... I have no mouth, and I must scream..."

    player "My book report is also in that book. We chose the same story."

    "I chuckled, but she didn't seem so amused."

    "I just realized. I had a choice. I could help any one of these girls with their tasks."
    "All I had to do was choose. And I think the girl that could need my help the most right now is..."
    menu:
        "Missy":
            $choice_no9 = 1
            jump choice_no9_1
        "Kathryn":
            $choice_no9 = 2
            jump choice_no9_2
        "Daisy":
            $choice_no9 = 3
            jump choice_no9_3
        "Joy":
            $choice_no9 = 4
            jump choice_no9_4
    
label choice_no9_1:
    "I turned to Joy."

    player "Is it alright if I stay to help Missy? I think she needs my skills."

    missy "Since when?"

    "Joy chuckled at our little banter and nodded."

    joy "Sure! That's more than fine. Kathy, you can manage on your own, right?"

    kath "Don't worry about me, Joy. I got this."

    "Daisy then went closer to her friend and locked arms with her."

    daisy "Kath... could I do my book report... at your place? Then when I'm done, I can help you with baking.."

    "Kath nodded eagerly before pulling her friend closer."

    kath "That's a lovely idea! Thank you, Daisy. Well then, me and Daisy will go ahead out. Chat if you need us."

    hide kath
    hide daisy
    with Dissolve(0.75)
    "Daisy then got some of the ingredients and then walked out of the room with Kathryn by her side."

    hide joy
    with Dissolve(0.75)
    "Joy followed after waving us bye."
    jump choice_no9_1plus

label choice_no9_1plus:
    scene bg cooking_room
    with Dissolve(0.75)

    "As I entered the TLE room now with Missy, the first thing we did was set the ingredients, utensils, and equipment."
    "Missy looked deep in thought while looking at the almond flour."

    missy "Tsk... last time I made these, the shells were soft..."

    player "So how do we make the macarons today?"

    "She picked up her phone and scrolled a bit. Smiled at one technique."

    show missy smiling
    missy "The choice is obvious. The Italian method. It creates the most stable batter, and lets the feet rise much quicker."

    "She handed me her phone so I could see the method for myself much clearer. Seems different... but..."

    player "...Do we even have a heavy bottom sauce pan? What even is a heavy bottom sauce pan?"

    "I asked while hopping on the counter top to take a seat."
    "Since it's just me and Missy, my sense of courtesy has vanished."
    "I propped one leg over the other as I continued to watch the video."

    player "What's the difference? The pan we have already should be enough- hey!"

    "I hissed. Missy suddenly tossed her shades to my face. Big mistake."
    "I then put the phone down and threatened to break the glasses."
    "Not that I'd actually break them, but it was always fun messing with her to an extent."

    show missy irritated
    missy "Give thsoe back!"

    "She launched herself at me, attempting to snatch it back. But I quickly evaded her grubby little hands and held her shades overhead."
    "It was easy getting things out of her arms reach."

    player "You threw it at me first!"

    "I chuckled while waving it in the air as she tried to grab it on her mary janes. But those heels could only do so much for her height."
    "It was always a game of Pabitin whenever I did this with her."

    missy "Idiot! Give it back!"

    "Is there a name for this skill? To try to keep a rather delicate object safe while simultaneously making it look like it could be in harm's way?"
    "She kept jumping, each time her fingers got near to close, I pulled away."

    player "Hahaha, okay, okay, fine. Here- WHOA-"

    "I lost balance. I didn't actually have any intentions to break these shades. Missy loves them, she wears them all the time."
    "The last thing I want is to actually ruin our friendship."
    "Because of some stupid shades. I held them up in the air as I tripped backwards..."
    "...but my attempt at balance only ended up tripping her too. On instinct, my body moved to protect her and the shades."

    "We fell on top of each other."
    "There we were."
    "Laying chest to chest on the polished floor."
    "Wide eyed and speechless."
    "Are there strawberries here? Why do I smell them? And what is that powdery scent I'm getting? It's almost addicting..."

    missy "I-"

    "We stared at each other for too long. We then quickly rolled off each other and sat up."

    missy "Sorry for falling on top of you-"

    player "No, no, I'm sorry, I made you trip-"

    missy "No! I'm sorry, I made you lose balance."

    player "Ha... don't be so modest, I started it. I should have just handed your shades back.."

    missy "Idiot. I threw them at you in the first place."

    "An awkward silence settled down on us."

    player "Well... good news, your shades are safe."

    "I handed over her shades with a nervous chuckle. She meekly took it back and placed it on her head."

    missy "Are you... okay?"

    player "Yeah, yeah. I'm good... you?"

    "She slowly got up. Dusting her skirt off as she regained her composure. She then extended a hand for me with a calm smile."

    missy "I'm fine thanks to you. You make a great cushion."

    "I took her hand and got up chuckling."

    player "I feel used."

    "I said with mock hurt. My palm places dramatically to my chest."
    "Now with normalcy back in the air, Missy eased up as well. She tossed me an apron and nodded."

    missy "Stop whining. Let's start making these stupid cookies."

    scene bg cooking_room

    "Now that all things have come back to normal, me and Missy entered a sort of flow state in making these macarons."
    "We were locked in making sure this batch, our second batch, was going to be perfect."

    "While Missy was sifting the dry ingredients, she turned to me."

    missy "Got any plans after school?"
    menu:
        "Nah, not really.":
            $choice_no10 = 1
            jump choice_no10_1
        "Why are you asking?":
            $choice_no10 = 2
            jump choice_no10_2
        "I do, yeah...":
            $choice_no10 = 3
            jump choice_no10_3

label choice_no10_1:
    player "Nah, not really."

    player "Is there something... you wanted to ask?"

    "I asked with a small smirk I didn't know I could make."
    "After spending time with her so much today, I've been having all sorts of weird feelings towards her."

    missy "Yeah, there was."

    "I've never seen Missy look this shy before."
    "She usually held herself with so much sarcasm and nonchalance, that tone in her voice threw me off guard."

    jump choice_no10_done

label choice_no10_2:
    player "Why are you asking?"

    missy "Well, I'm going out later to do some window shopping."

    "She told me with a coy smirk. I could even feel my cheeks heating up. This wasn't a date, so why was I so affected?"
    "Everything happening today has got me feeling off about how I feel about her."

    "She chuckled. My silence maybe amusing her."

    jump choice_no10_done

label choice_no10_3:
    player "I do, yeah..."

    "Missy frowned. It was meant to be a joke. To bait her to get irritated."
    "But seeing her eyes look so… disappointed, I felt a pang in my chest."

    player "It's just my book report. Don't worry about it. What's up?"

    "She bounced back slowly. The beautiful glow in her eyes returned."

    missy "Well, I'm going out later."

    jump choice_no10_done

label choice_no10_done:

    "Is she asking me out?"

    missy "I want you to come with me if that's fine with you."

    player "Come with you?... Where?"

    missy "Podium."

    "She said with a friendly smile."
    "After we finished baking, our 3rd batch for today was..."
    "A success."

    "Something was wrong though. While the shell was stable, this batch barely grew any feet."
    "It was thin, and the cookie was pretty hollow inside. But overall, it went well."

    scene bg gate
    with Dissolve(0.75)

    "I and Missy left the school side by side as we went out for her little shopping spree."

    jump day4start

label choice_no9_2:
    "I turned to Joy."

    player "I'm actually good with helping Kathryn. She has a lot to do anyways"

    "Kathryn turned to me with a warm smile"

    joy "That's very kind of you. Kathy, would that be alright?"

    "Kathryn nodded."

    kath "That would be a big help... Thank you so much, [playername]."

    daisy "{b}O͓̓h̖͑,̬͒ ̩bu̺͂t̗̆...{/b}"

    "Daisy suddenly spoke up. Looking at her best friend shyly, then at Joy. as if trying to communicate something."

    daisy "I was actually planning to join Kathryn... I could help her with the other baked goods."

    joy "Oh? Well that's awfully kind of you, Daisy, but what about your book report?"

    daisy "I can do it at her home. Then I can help her bake."

    joy "Well I can't stop you. What do you say, [playername]?"

    menu:
        "I can stay behind.":
            $choice_no11 = 1
            $choice_no9 = 1
            jump choice_no11_1
        "I offered to help Kathryn first.":
            $choice_no11 = 2
            jump choice_no11_2

label choice_no11_1:
    "Joy nods and turns to Daisy with a kind smile"

    joy "You two are basically inseparable sometimes"

    "She giggles. Kathryn links her arm with Daisy and pulls her friend to the door."

    kath "We'll see you all tomorrow! Me and Daisy will see ourselves out now."

    hide daisy
    hide kath
    hide joy
    with Dissolve(0.75)
    "The two girls then leave with Joy following not too far from them."
    
    jump choice_no9_1plus

label choice_no11_2:

    scene black
    with Dissolve(0.75)
    "Me and daisy then went to her house to help in baking the other treats, then the macarons. They turned out flat and the feet spread out."

    jump day4start

label choice_no9_3:
    "I turned to Joy."

    player "I want to help Daisy."

    show daisy irritated
    daisy "{b}n̄̉oͯͮ ͛̑t̊h͈̅ḁn̙k̳ ̾y͓ͩͦo͒u̒...{/b}"

    "Daisy suddenly spoke up. Looking at me with a sudden serious stare."

    daisy "Choose again."
    menu:
        "Help Missy.":
            $choice_no12 = 1
            $choice_no9 = 1
            jump choice_no12_1
        "Help Daisy.":
            $choice_no12 = 2
            jump choice_no12_2

label choice_no12_1:
    daisy "Good."
    jump choice_no9_1plus

label choice_no12_2:
    scene bg cooking_room
    show daisy irritated
    with Dissolve(0.75)

    "Daisy didn't look pleased with my decision."

    scene black
    with Dissolve(0.75)

    "Af͢t̸er̵ ̷t̶he̶ ͟b͞oo͝k̸ ̢r͟ep̡o̷rt͘ ͠w̶e ̀m̸ad͟e m͢a͠c̡a͢r̡ons͢ ̶a̸ǹd{b} ͟f͠ailed͞.{/b}"

    jump day4start

label choice_no9_4:
    "I turned to Joy."

    player "Joy..."

    "Joy turned to me. Confused. Then she chuckled lightly."

    show joy smile
    joy "Oh, you don't have to help me-"

    show daisy irritated

    daisy "{b}C̸ho̴os̡e ag̢ain̵.{/b}"

    "Daisy suddenly spoke up. Her cold eyes stare at me with insistence."
    menu:
        "Help Missy.":
            $choice_no13 = 1
            $choice_no9 = 1
            jump choice_no12_1
        "Help Daisy.":
            $choice_no13 = 2
            jump choice_no12_2

label choice_no13_1:
    daisy "Good."
    jump choice_no9_1plus

label choice_no13_2:
    scene bg cooking_room
    show daisy irritated
    with Dissolve(0.75)

    "Daisy didn't look pleased with my decision."

    scene black
    with Dissolve(0.75)

    "Af͗teͭr helṕing ͩJoy͋, ̽we ͊m̌ade macaro͂nͦsͧ a̒n̋d́ ȉtͣ ͬfail̄ed. ẁeͬ ac̋c͛idenͣta̅ll̋y̏ {b}burne̒dͪ iͤt toͫ aͤ ͧcͫri̐s̅p.{/b}"

    jump day4start