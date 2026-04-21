# Day 3 starts here.

label day2start:

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
    "Day 2"

    scene bg gate
    with Dissolve(0.75)

    "It was a fresh morning. The sun was up high, the light bathing the school in its soft hue."
    "Which means I'm late. 8 AM."

    show missy smile at center
    missy "Tsk tsk tsk. Late again?"

    "My friend scolds me. Waiting in the guard house. After tappign my ID, I walk up to her."

    player "What about you? Why are you here?" 

    "Missy then shrugs."

    missy "I came here to get my P.E. shirt. Left it at home and had it lalamoved. Then I saw you so I thought I'd wait a little."

    "I noticed she was holding a plastic bag. Must be where her P.E. uniform is, no doubt."

    player "Let's go in together."

    scene black
    with Dissolve(0.75)

    "She nodded and we waited side by side to the school."

    scene bg field_for_booth
    show missy smile at center
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

    show daisy confused at rightish
    daisy "Ack!"

    "I accidentally bump into Daisy as she exits her classroom. Kathryn just behind her giggling softly."

    show kath confused at leftish
    kath "Ow, Daisy, are you okay?"

    show daisy smile
    daisy "Y-yeah, I'm okay… "

    show daisy confused
    daisy "Daisy: oh- Oh, OH! (player) I'm so sorry! Are you hurt? I didn't mean to! I wasn't looking and i was mid chat with Daisy and I just…"
    menu:
        "It's alright, Daisy.":
            $choice_no2 = 1
            jump choice_no2_1
        "Why were you in a rush?":
            $choice_no2 = 2
            jump choice_no2_2
        "Uhhhhh":
            $choice_no2 = 3
            jump choice_no2_3

label choice_no2_1:
    player "Haha, It's alright Daisy. It's not like I got hurt. How about you? Are you okay?"

    show daisy smile
    daisy "Oh, yes... I'm alright. I'm sorry again for bumping into you."

    "Daisy shyly tucks a loose strand of hair behind her ear. Looking off to the side, perhaps hoping her friend could interfere with the sudden awkward cadence in the air."

    jump choice_no2_done
label choice_no2_2:
    player "Why were you in a rush? What if I was holding something."

    show daisy sad
    daisy "Right! I'm sorry- I'm so… I'm- I didn't mean to..."

    show kath irritated
    kath "It's alright, Daisy."

    "Kathryn said, glaring at me before her hands found Daisy's shoulders in hopes to steady her shaking friend. But it was her fault in the first place to not be looking where you're going."
    "Honestly, she should be more careful. Daisy then coughed to redirect the attention back to her."
    jump choice_no2_done
label choice_no2_3:
    player "Uhhhhh UHHHHHHHHHHHH no no its okay i just... uhhhhhhhhh..."

    show daisy confused
    show kath confused
    "Both Daisy and Kathryn chuckles at my flustered response. My lack of better social skills is becoming painfully obvious."
    jump choice_no2_done

label choice_no2_done:
    show kath smile
    kath "Anyways... I'm guessing you're also on your way to LV 304?"

    player "Yeah. Wanna walk with?"

    "The two girls looked at each other for a few seconds before nodding. It's not like they had much of a choice anyways since I was already here and we were all going the same way."
    "What are they going to do? Say no? That would go against social conventions."

    scene bg front_left
    with Dissolve(0.75)

    "As we entered the classroom, I saw Missy on her phone watching some tutorial on macarons with an unamused look in her eyes, and Joy in front of the white board contemplating the list written on it."

    "Joy turned around seeing us enter. She clapped her hands together with a ready look on her face."

    show joy happy at leftish
    "Joy: Great! You're all here! Okay everyone. Today is an important day. Day 1 of macaron making! But also day 1 for ingredient prepping for the other baked goods. Kath, you're with me."

    show kath smile at rightish
    "Kathryn nods in response."

    show joy smile
    joy "Then the rest of you will stay to practice on the macarons without us."

    "Joy then gestured to the blue plastic bags with a large SM logo. From where I'm standing, I could see flour, sugar, eggs, and small glass bottles. Maybe those being dye or flavorings."

    joy "The equipment is all at the TLE lab. I already got permission from Miss Ange to use the room."

    hide joy
    hide kath
    with Dissolve(0.75)

    "Missy and Daisy seemed to share the same expressions, but both for different reasons."

    "Missy was looking off to the side annoyed, still not fully on board with the macaron plan, while Daisy was looking off to the side, anxious, probably hoping the first attempt goes well."

    "Kathryn then realised something while looking at the list of ingredients on the wall. She turned to Joy."

    show kath smile at leftish
    kath "Joy?"

    show joy smile at rightish
    joy "Hmm?"

    show kath confused
    kath "I think that's a lot on the list... won't it be a lot for just the two of us to get?"

    "Joy turned back to the list. It wasn't a lot of ingredients, the problem was everything else. The decorations, the packaging, and the weight of all those ingredients."
    "The once so cheery girl now seemed perplexed. She rubbed her chin and thought about it."

    show joy smile
    joy "Maybe we do need another hand… oh, (player), do you think you could help us? I'm sure Missy and Daisy will be fine on their own making macarons. We will still make macarons today, just after we do some shopping."
    menu:
        "I don't know...":
            $choice_no3 = 1
            jump choice_no3_1
        "Sure! Why not?":
            $choice_no3 = 2
            jump choice_no3_2

label choice_no3_1:
    player "I don't know... sorry girls it's a a no. It's so hot today, I'd rather suffer in the aircon than outside, haha."
    "Joy sighs."

    show kath irritated
    kath "It is hot today..."

    show joy happy
    joy "Hey! Don't worry, Kath, we got this!"

    "Joy said with her usual energetic charm, just lighting up the room. Kathryn smiled to her friend and looked more determined than ever."

    joy "Alright then y'all! I'll just give Miss Ange a call and we should be allowed to go to the TLE room right now."

    scene bg cooking_room
    with Dissolve(0.75)

    "Moments later, me and the rest of the club enter the TLE lab. The room's aricon was thankfully already on and all the equipment we needed was on the counter ready for Daisy and Missy to use."
    "Other things were present here too; table stoves, a microwave, whisks, spatulas, and even mittens."

    show missy happy at left
    missy "This room would make a way better room for the baking club than that random classroom."

    "Missy remarked while looking around. Her fingers gliding against the cool countertops. She brought her fingers up and smiled. She always loved clean surfaces."

    show daisy calm at leftish
    "Daisy nodded beside her."

    show kath irritated at rightish
    kath "Oh gosh..."
    
    "She looked at the window. Grimacing at the cloudless sky. The sun was basically glaring down."
    "Thank goodness I decided to stay behind."

    show daisy confused
    daisy "oh, Kath..."

    show joy irritated at right
    "Joy then broke that peaceful illusion with a clap of her hands. Immediately demanding attention back to her."

    show joy irritated at slide_right
    show kath irritated at slide_right
    "Like a horror monster dragging away its victim into the dark, Joy grabbed Kathryn's wrist and pulled the poor girl away into the heat of near midday."

    hide joy
    hide kath
    with Dissolve(0.75)

    "Missy then went up to the macaron ingredients on the counter and looked at Daisy, then me."
    "The real challenge was about to start."

    show missy smile
    missy "Alright, let's start. Do we know anything?"

    player "Nothing."

    show missy irritated
    "I said, maybe a bit too confidently. That earned me a whack to the back of my head from my supposedly best friend."

    player "Ow!"

    show daisy smile
    daisy "I watched a few videos about different types of macaron making... theres like... french, swiss, indian, and Italian... right?"
    "Daisy asked meekly. While I was still rubbing the nape of my neck, Missy nodded. She and Daisy both grabbed a bowl and I went off to get the stand mixers."

    show missy smile
    missy "What technique do you guys want to try? I think for the first attempt, we do the French method. But what do you suggest for the rest?"
    menu:
        "Let's do Swiss!":
            $choice_no4 = 1
            jump choice_no4_1
        "The Italian technique sounds cool.":
            $choice_no4 = 2
            jump choice_no4_2
        "How about the Indian way?":
            $choice_no4 = 3
            jump choice_no4_3
        "Does it really matter?":
            $choice_no4 = 4
            jump choice_no4_4

label choice_no4_1:
    player "Let's do Swiss!"

    show missy smile
    missy "Alright then."
    jump choice_no4_done

label choice_no4_2:
    player "The Italian technique sounds cool."

    show missy happy
    missy "Thats a pretty complicated technique... but alright!"
    jump choice_no4_done

label choice_no4_3:
    player "How about the Indian way?"

    show missy smile
    missy "Sure. Let me just pull up a YouTube tutorial on that."
    jump choice_no4_done

label choice_no4_4:
    player "Does it really matter?"

    show missy irritated
    "Missy narrows her eyes at me. I take a step away before I'm in hitting range."
    "Thankfully, Daisy saves me."

    show daisy smile
    daisy "I think the Italian method would be nice."

    show missy confused
    missy "It's a pretty hard method from what I researched..."

    player "I didn't research."
    show missy irritated
    missy "Shut up..."
    "She then turned back to Daisy with a gentle smile, the personality switch is insane."

    show missy smile
    missy "Alright! Let's try it! Swiss method it is!"
    jump choice_no4_done

label choice_no4_done:
    "Now with a technique in mind, we got to first trying the French method. Daisy explains to us."
    show daisy smile

    daisy "From what I saw, the french method is the easiest method. They way this is done is by three easy ways."
    daisy "Mixing the dry ingredients, making the margarine from egg whites, and then mixing those two together."
    daisy "The only problem with this technique is.."

    show missy confused
    missy "It's sensitive to over and under mixing."

    show daisy confused
    daisy "Right."

    player "What do you mean with that? Is it not stable or something?"
    missy "We have to treat this technique with care. Breathe wrong and the batter could go flat."

    "I rolled my eyes. That sounded ridiculous. But oh, I was a fool."
    "After simple mixing and perfect margarine beating, at the perfect point where the egg whites got stiff peaks, all we needed to do now was bake them. They came out..."
    "With {b}no feet{/b} and {b}flat tops{/b}. It {b}melted{/b}."
    "I felt genuinely disappointed in myself, looking at those sad, pancake-flat cookies."

    player "What...? How? We did everything correctly..."

    "Missy shakes her head."
    show missy sad
    missy "We obviously didn't, if they turned out like {i}this{/i}."
    "Missy turns to me with a pitiful glance. I was utterly disheartened. Missy reached out and patted my shoulder. With a soft smile, she told me..."

    show missy smile
    missy "Hey, it's okay... I told you these things are hard to make."

    player "I guess you're right... Gosh, macarons really do test your patience, huh?"

    show missy happy
    missy "Very much so."

    "Daisy was still disappointed, though, but she bounced back much faster than I did. She lifted her chin up high and grabbed another bowl."

    show daisy smile
    daisy "You guys go ahead and start the next batch. I'll do the dishes."

    "We all nod to each other before trying the next technique, this time with much success."
    "Thanks to the addition of heating the sugar first, then whipping it, it stabilized and, by the third batch, we {b}got feet{/b}. This time, the macarons came out with {b}feet{/b} and {b}clean tops{/b}. It {b}was a success{/b}."
    "I was needlessly too happy over a bunch of little cookies. But even as Daisy and I celebrated, Missy still looked at the cookies with an appraising gaze. She then pressed her finger on the top of one of the cookies and watched as it easily broke."
    "The tops were too fragile."

    show missy smile
    missy "...This is okay. For our third attempt? This is great. We have the right shape, and they have feet. This is good."
    "The door then suddenly opened, revealing Joy, Kathryn, and Jared coming in."

    show jared irritated at center
    show joy irritated at rightish
    show kath confused at right
    jared "I hate you..."

    "He said to his sister, before dropping the plastic bags of groceries on a countertop. Joy couldn't care less, that cheery smile on her face unwavering."

    show joy happy at right
    joy "You can go now, byeee~"

    jared "Wait, that's it!?-"

    "He wasn't even granted another word before Joy basically shoved him out."
    "Kathryn dazily walked over to Daisy, and the shorter girl welcomed her friend with open arms. Joy then walks up to us and our successful batch."

    joy "Oh my gosh! These look great! Good job, you three!"

    "I smiled proudly, and Missy couldn't accept the praise so quickly."

    show missy smile
    missy "Thanks, but it's not perfect. The tops are actually fragile, so the inside isn't exactly its iconic, chewy self."

    "Missy explained to joy. I shook my head with a soft smile. I then grabbed a cookie, and..."
    menu:
        "Fed it to Missy":
            $choice_no5 = 1
            jump choice_no5_1
        "Ate it myself":
            $choice_no5 = 2
            jump choice_no5_2

label choice_no5_1:
    "I brought it to Missy's mouth, saying \"Ahh~\""
    "Missy blushed and rolled her eyes. Her soft chuckle made me a little embarrassed with my bold stunt, but thankfully she played along and took a bite."

    player "So? How's the inside? Soft and chewy?"

    show missy irritated
    missy "Not in the way I like it."

    "She answered with a shake of her head, still amused by my sudden confidence."
    jump choice_no5_done
label choice_no5_2:
    "I popped it into my mouth with a cocky smile."

    player "Tastes perfectly fine to me."

    show missy confused
    missy "Of course it tastes fine, it's the texture that {i}I'm{/i} concerned about."

    "Missy sounded like she was scolding me... I shrugged and continued chewing. Seemed perfectly fine to me."
    jump choice_no5_done
label choice_no5_done:
    "Joy then giggled and turned to Kathryn, who was still being babied in Daisy's arms."

    show joy smile
    joy "Well, you three can go now. Kath and I will stay to try making macarons ourselves, okay? Oh, and bring those with you."
    "Joy gestured to the groceries they bought. I got the packaging, Missy got the ingredients, and Daisy got the decorations."

    show daisy smile
    daisy "Good luck, you two."

    show kath sad
    kath "Bye bye..."

    "Kath pouted while watching her friend leave the room, with Missy and I following just behind her."
    # todo: There's a line here in the original script. Not sure what that's supposed to mean.
    jump day3start
label choice_no3_2:
    show kath happy at leftish
    show joy happy at rightish
    kath "Great. Thanks for that!"

    joy "Alright. Now I'll just message Miss and confirm we are on the way to the TLE room so Missy and Daisy can start baking."

    scene bg cooking_room
    with Dissolve(0.75)

    "Moments later, me and the rest of the club enter the TLE lab. The room's aricon was thankfully already on and all the equipment we needed was on the counter ready for Daisy and Missy to use."
    "Other things were present here too; table stoves, a microwave, whisks, spatulas, and even mittens."

    show daisy confused at left
    show joy happy
    with Dissolve(0.75)

    "Daisy stood next to the window looking at the weather outside. Another cloudless sky."

    daisy "Seems to be awfully hot outside..."

    "She said to herself. But her voice had no room for any privacy with that statement. I walked next to her and nodded."

    player "You're right..."

    "Daisy looked at the time on her phone. 10:35 AM. She sighed."

    show daisy irritated
    daisy "It's so early and yet the sun is already shining so bright... I think even the air is hot..."

    "That sent an unpleasant shiver down my skin. I've always hated the heat. Not the best pet peeve when you're living in a tropical country like this."

    show joy sad at rightish
    joy "You may be right, Daisy..."

    show daisy confused
    daisy "Joy, are you sure asking [playername] to join you in buying groceries is a good idea? Don't they have a skin condition affected by too much heat?"

    "My eyebrows scrunched up. Th̷a͢t̴'s̸ no͟t ͟ true͢. At least, I don't think so. But before I could object, Joy nodded. Her face was ridden with guilt."

    show joy confused
    joy "Right. I remember the nurse mentioning that to me..."

    "I guess I do have a skin condition. Joy turned to me and asked me one more time."

    show joy sad
    joy "[playername], are you sure you want to help us with the groceries? We won't hold it against you if you say no."

    "Joy asked me again."
    menu:
        "Hmm... maybe I should stay...":
            $choice_no6 = 1
            jump choice_no6_1
        "A little sun never killed anyone!":
            $choice_no6 = 2
            jump choice_no6_2

label choice_no6_1:
    player "Hmm... now looking at the weather outside... maybe I should stay... Would that be alright, Joy?"

    show joy happy
    joy "It's perfectly fine! Don't worry, besides, I'm sure we can find someone else to-"

    "Before she could finish, a voice from the door suddenly called out."

    show jared smile at right
    "???" "Well well well... what are you doing in {i}my{/i} club room?"

    "The unexpected character said with a booming voice that commanded attention."
    "Not any voice. The voice that could only distinctly belong to the one and only, Jared Jacinto. President of the Cooking club."
    "While the baking club is usually assigned the room LV 304, the cooking club always held their meetings and such in the TLE room."
    "But him being here didn't make sense... It wasn't even a club day, and Joy already had this room reserved for us."

    show jared happy
    jared "I only stopped by because I left my water bottle here. Who knew I'd run into-"

    show joy irritated
    "The boy had no chance to finish his sentence. Just as he cut her off, Joy cut him off."
    show joy happy
    joy "Perfect timing. We found our replacement errand boy. Come on, Jay."

    show jared irritated
    jared "What!? I never agreed to anything-"

    "Joy grabbed him by the ear and dragged him out."

    show jared sad at slide_right # originally irritated
    show joy smile at slide_right
    jared "Ow ow OW! Let me go! Noooo!"

    "Everyone stood awkwardly still as we saw the most admirable guy in school be dragged away by his twin sister."

    show kath happy at leftish
    with Dissolve(0.75)

    "Kathryn chuckled softly before following after her friend."

    show kath happy at slide_right
    jump day3start # todo: "RESUME TO ROUTE A1"

label choice_no6_2:
    player "A little sun never killed anyone! Don't worry. Besides, we'll mostly be in a mall. I'll be fine!"

    show joy smile
    "Joy smiles, grateful for my decision."
    joy "Don't worry! The commute is the only thing hot. The rest of the the time, we'll mostly be at the mall, okay?"

    show kath happy
    kath "Come on then, let's get going."

    show joy smile at slide_right
    show kath happy at slide_right
    show daisy irritated

    "As I left the room, I waved by to Missy and Daisy, the latter seeming a bit irked with my decision."

    scene bg garden
    with Dissolve(0.75)

    "After a long shopping spree, I held bags of plastic SM bags to my sides. Two for each of my hands. Me and the girls came back tired, sweaty, but thankfully unscathed."

    show kath irritated at right
    kath "Ugh! That commute was brutal! I hate riding the Jeep. It's always so smelly on the way to the mall."

    player "Tell me about it. It was me and my jisu fan against the world."

    "I groaned. We walked through the school, still under that scorching sun, back to the TLE room. I was already feeling delirious with how excited I was to be bathed in the aircon. M͢ay̸be͝ ͟ I͠ śhou͘l̴d  ̵h͞a͞ve ̴ s͝ta̶y͝e̴d ̷ b̷e͟hi͠nd̶ ̸ w̸i̡th ͟ M͢i͜s͞s̡y͟ ͞ a͠n̸d ͟ D͠aisy͘."
    "Thankfully we got everything we needed for the other pastries; madeleines, eclairs, and d̢a̡n͠i̸sh̢e̶s͘. All to be baked by our sacrifices, Kathryn and Missy."

    scene bg cooking_room
    with Dissolve(0.75)
    show daisy happy at left
    show kath happy at leftish
    show missy smile at rightish
    show joy smile at right
    with Dissolve(0.75)

    "As we entered the TLE room, the smell of warm sugar accompanied with the refreshing coolness of the aircon filled the air. Kathryn lets out a sigh of relief and flings herself to Daisy's arms. Joy follows just behind me."
    joy "How has the testing been so far?"

    missy "It’s been alright. We did three batches. First two first, but this third one looks promising. The only thing wrong is the shells. It cracks way too easily."

    joy "Great! The macarons you two made already have feet!" # what? lol

    "Joy carefully took one of the successful products and took a bite. She squealed at its flavor and got another, but Missy still looked unsatisfied."

    show joy happy at right
    joy "[playername]! You have to try one, here!"
    menu:
        "Take the macaron from her hand":
            $choice_no7 = 1
            jump choice_no7_1
        "Open your mouth and let her feed you":
            $choice_no7 = 2
            jump choice_no7_2

label choice_no7_1:
    "I took the macaron from her hand and tried it myself."

    player "Missy was right... These shells are fragile. It's like it cracked the second it hit the roof of my mouth."

    show missy confused at rightish
    "I said with a playful smile, watching Missy roll her eyes."

    missy "I'd like to see you make a better one!"
    jump choice_no7_done
label choice_no7_2:
    "I opened my mouth meekly, letting her feed me. I blush for a moment."

    show joy happy at right
    joy "It tastes good, right?"

    player "Right..."

    "The way Joy was starting to get so comfortable around me was starting to make me flustered."
    jump choice_no7_done
label choice_no7_done:
    show daisy smile at left
    daisy "There there, it's okay..."

    "Daisy said soothingly to her friend while patting her back."

    show kath sad at leftish
    kath "{i}Sniff sniff, sob...{/i}"

    show missy smile at rightish
    missy "I think Daisy and I will go put away the stuff you guys bought now. The TLE room is all yours."

    "I waved goodbye and my friend and Daisy walked out of the room."

    show joy happy at right
    joy "Okay guys! Let's make 'em proud!"

    "Joy cheered, and we all got started at our attempt to make macarons."
    scene black with Dissolve(0.75)

    "It was brutal. And the first fail was mostly my fault for being too careless with the mixing. After 3 batches, we decided to stop. Still no progress for us today. Our macarons formed no feet, two of the three batches burned the cookies to a crisp, and the one other batch just came out flat."
    "Today’s attempt {b}F́ai̶l͞ed͟.{/b}"
    jump day3start