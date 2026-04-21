# Day 4 starts here.

label day4start:

    # Player substitution if necessary.
    python:
        if not playerfullname:
            playerfullname = "Juan Dela Cruz"
        if not playername:
            playername = "Juan"
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
    "Day 4"

    scene bg classroom_3_4_view
    with Dissolve(0.75)
    "Today was the day just before the festival, and everyone has been acting off lately... But, as always, I must move on."
    "I have to pick a friend to help with the preparations... Who should I pick?"
    menu:
        "{u}Missy{/u}":
            $choice_no14 = 1
            jump choice_no14_1
        "Kathryn":
            $choice_no14 = 2
            jump choice_no14_2and3
        "Joy":
            $choice_no14 = 3
            jump choice_no14_2and3
        "{b}Dͅa̟̓i̘s͍͊y{/b}":
            $choice_no14 = 4
            jump choice_no14_4

    label choice_no14_1:
        "I helped Missy today with the macarons and other pastries, spending a good time with her and sharing laughs. It was a very calm day where nothing went wrong."
        jump day4_end
    label choice_no14_2and3:
        "I offered to help them, but the whole day was hellish. Kathryn was too cynical and judged everything I did, and Joy was creepy, all over me, and kept staring at me... The moment the bell rang to end the day, I was relieved."
        jump day4_end
    label choice_no14_4:
        "Daisy didn't seem pleased with my decision. She glared at me and-{nw}"
        scene black
        "{b}F̀OR̴̃C͢E̿͠ ͑ S̴ͫT̴OP͟ ̢ D̢A̴Y̌͠{/b}{fast}"
        jump day5

    label day4_end:
        scene black
        with Dissolve(0.75)
        jump day5
# Starting day 5 here since day 4 was so short
label day5:
    # Don't need to show the black scene since both endings cut to it
    pause 0.75
    "Day 5"

    scene bg booths
    with Dissolve(0.75)

    "After a whole day of presenting, the results are out for which club won... I got nervous, and wanted to stand next to one of my friends..."
    menu:
        "{u}Missy{/u}":
            $choice_no15 = 1
            jump choice_no15_1
        "K̍̽aͮṱ̄h̺̑̀r̙͋yͧ̽nͤ":
            $choice_no15 = 2
            jump choice_no15_2
        "J̴̡̑̔o̶̺͠y̢̡̡͊y":
            $choice_no15 = 3
            jump choice_no15_3
        "{b}Ḋ̵͔ͭ͜a̜ͮ͘i̞s̱̈̀͠y͈͠{/b}":
            $choice_no15 = 4
            jump choice_no15_4

label choice_no15_1:
    "I stand next to my friend, Missy. With bated breath, the judge announced that the winning club is... {b}The Baking Club!{/b}"
    "Everyone jumps up with joy. I suddenly lift Missy up in the air and spin her around."
    player "We did it!"
    missy "Yes, we did..."
    # Cutscene, maybe change to a CG of the player picking up Missy.
    pause 0.75
    "I held my best friend high in the air, spinning her around."
    "When I finally set her down, there was a moment where we just looked into eachothers' eyes."
    "The sun bathed her skin, and it's as if the world around us became still, encased in this moment of honey gold. Were her eyes always that brown under the sun? It's almost like she's wearing contacts... So beautiful."
    "Shyly, she tucked a strand of loose hair behind her ears and asked..."
    missy "[playername]... After this, maybe we should-"
    "I wasn't going to let her say it. Before I could stop myself, words just started spouting out of my mouth."
    player "Missy, do you want to go see a movie later, after school? Just the two of us?"
    scene black
    with Dissolve(0.75)
    "{b}GAME OVER - ENDING 1 - MISSY{/b}"
    return
label choice_no15_2:
    "I stand next to my friend, Kathryn. With bated breath, the judge announced that the winning club is... {b}The History Club!{/b}"
    "Kathryn clenches her fist and swings at me."
    player "What the hell--?"
    kath "This is all {i}your{/i} fault!"
    "Thē̺ ͌ͅ wo̲͐rl̥̾ḏ̾ ̐ st̻̑a̘rted̘ ̌ t̳ͭoͅ ̉ d̓is̻o̭ͩrientͅ àn̹dͧ ĕve̮r͂ỷt͎̑h̰̄iͅnǧ̲ ̺ w̽as̄ gl̠i̱t͇̍c̗̈hin̯̈g͙ ouț.ͮ ͇ͩ I ͙ d͇o̰n̟'t k̟̍n̼̾oͣẘ̲ wh̻a̫͋t̮̋ wȅn̔tͫ wr͚ͩo͐n̠̓g͙,  ̝̂bͭu̥ͧt-"
    scene black
    "{b}F̀OR̴̃C͢E̿͠ ͑ S̴ͫT̴OP͟ ̢ D̢A̴Y̌͠{/b}"
    # Cutscene
    pause 0.75
    "I reeled back from the punch. What the hell was that all about? Kathryn was becoming unstable for no reason. I know we lost it, but it can't be {i}that{/i} much of a big deal."
    "Daisy then ran to her friend, crying, begging for Kathryn to \"snap out of it\"."
    daisy "This is all your fault!"
    "...Daisy yelled at me. I have no idea what I did, but whatever it was, I ruined it."
    "{b}GAME OVER - ENDING 2 - KATHRYN{/b}"
    return
label choice_no15_3:
    "I stand next to my friend, Joy. With bated breath, the judge announced that the winning club is... {b}The Cooking Club!{/b}"
    "Joy hunches over, chuckling softly to herself."
    player "Joy? Hey, it's okay-"
    joy "Ha ha, hahahaha AHAHAHAHA h͖̊ȁ̟h͟a̡̺ͮH̸Aͫh̞͌͠a͘H̖͠ A̬͞H́A͚̐H̭̔͜Ä͢h͚͒͠áhͮa̶̟͒H̴͇͗Ḁ͢ h̡̜ͤȧ{b}HͫA͘Hͧ͜A͒͟HͨA͌́h̶̅a̯͜h̵aH̀ A͍h̶̹͂a̳͠H̓͝AͧH̔͢ȀHÁ̩͘!!{/b}"
    "Thē̺ ͌ͅ wo̲͐rl̥̾ḏ̾ ̐ st̻̑a̘rted̘ ̌ t̳ͭoͅ ̉ d̓is̻o̭ͩrientͅ àn̹dͧ ĕve̮r͂ỷt͎̑h̰̄iͅnǧ̲ ̺ w̽as̄ gl̠i̱t͇̍c̗̈hin̯̈g͙ ouț.ͮ ͇ͩ I ͙ d͇o̰n̟'t k̟̍n̼̾oͣẘ̲ wh̻a̫͋t̮̋ wȅn̔tͫ wr͚ͩo͐n̠̓g͙,  ̝̂bͭu̥ͧt-"
    scene black
    "{b}F̀OR̴̃C͢E̿͠ ͑ S̴ͫT̴OP͟ ̢ D̢A̴Y̌͠{/b}"
    # Cutscene
    pause 0.75
    "Joy seemed to be going insane. Something is wrong. Very wrong. Did the fair mean this much to her? Even her brother started to look worried. I turned around for help, and while everyone was screaming for their lives, Daisy was standing in place, fiercely typing on air."
    "...Wait, what? What was she doing?"
    "I didn't even have that much time to think about that, as Joy spun me around to look at her. She gripped my shoulders with painful amounts of force, and an eerie smile on her face."
    "{b}GAME OVER - ENDING 3 - JOY{/b}"
    return
label choice_no15_4:
    "I stand next to my friend, Daisy. With bated breath, the judge announced that the winning club is... {b}The T̵̽e̖c̵̼̋h̢ Club!{/b}"
    "Daisy spins towards me, her face pale with worry."
    player "Daisy? What's wrong-"
    daisy "Y̥̋o̿͘u͛͘."
    "Thē̺ ͌ͅ wo̲͐rl̥̾ḏ̾ ̐ st̻̑a̘rted̘ ̌ t̳ͭoͅ ̉ d̓is̻o̭ͩrientͅ àn̹dͧ ĕve̮r͂ỷt͎̑h̰̄iͅnǧ̲ ̺ w̽as̄ gl̠i̱t͇̍c̗̈hin̯̈g͙ ouț.ͮ ͇ͩ I ͙ d͇o̰n̟'t k̟̍n̼̾oͣẘ̲ wh̻a̫͋t̮̋ wȅn̔tͫ wr͚ͩo͐n̠̓g͙,  ̝̂bͭu̥ͧt-"
    scene black
    "{b}F̀OR̴̃C͢E̿͠ ͑ S̴ͫT̴OP͟ ̢ D̢A̴Y̌͠{/b}"
    # Cutscene
    pause 0.75
    scene white
    with Dissolve(0.75)
    "When I opened my eyes, everything was white. Everything and everyone was gone. All except for Daisy. She seemed to be grumbling to herself, looking at strings of numbers and such in the air."
    "She turned to me, sensing my presence. Biting her lower lip, she lashed out."
    daisy "This is all your fault! You humans, you can't do anything right! First you code a half-baked game, then you bring in a player where one wrong choice would destroy my world! I hate you, {i}I hate you, {b}I hate you!{/b}{/i}"
    "She kept yelling as she threw jabs left and right at me."
    "{b}GAME OVER - ENDING 4 - DAISY{/b}"
    return
