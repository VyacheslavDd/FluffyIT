label finish_game:
    $renpy.set_return_stack([])
    hide cat_neutral with moveoutright
    show neutral at right_transform with move
    show screen last_customer_talk
    show neutral onlayer screens at right_transform
    hide neutral
    show cat_anon onlayer screens at touching_left_transform with slowdissolve
    show happy onlayer screens at right_transform
    hide neutral onlayer screens
    play sound t5
    main_character "{cps=30}Мы постарались сделать для Вас хороший шаблон, так как из-за вирусов ваш предыдущий сайт был полностью утерян.{/cps}"
    show cat_boss onlayer screens at touching_left_transform with slowdissolve
    hide cat_anon onlayer screens
    play sound t6
    boss_cat "{cps=20}Поздравляю Вас, ребята!{/cps}"
    hide happy onlayer screens
    show oh_my_gosh onlayer screens at right_transform
    show cat_what onlayer screens at very_right_transform behind oh_my_gosh
    play sound t6
    boss_cat "{cps=24}Вы отлично прошли мою проверку!{/cps}"
    hide screen last_customer_talk
    hide cat_boss onlayer screens
    show oh_my_gosh at right_transform
    hide oh_my_gosh onlayer screens
    show oh_my_gosh at left_transform with move
    show cat_oneeye at very_right_transform
    hide cat_what onlayer screens
    show cat_oneeye at right_transform with move
    masya "Так вот, кем был наш анонимный клиент!"
    hide oh_my_gosh
    hide cat_oneeye
    show cat_boss at front_transform with moveinleft
    boss_cat 'Мася, Вы отличный сотрудник, будем рады принять Вас в ряды "Симпл Котинг".'
    hide cat_boss
    show oh_my_gosh at left_transform
    show cat_happy at right_transform
    masya "Неужели... Я так рад! Один бы я не справился..."
    show cat_oneeye at right_transform
    hide cat_happy
    show happy at left_transform
    hide oh_my_gosh
    masya "[main_character_name], спасибо тебе, ты [variations[17]] мне стать ближе к мечте."
    masya "Я уверен, что в дальнейшем у тебя все сложится отлично."

    menu:
        "Пожалуйста.":
            call change_mood(-1, False) from _call_change_mood_15
            jump ending
        "Очень радостно было познакомиться с тобой! [variations[16]], что все полученные мною знания пригодятся мне в жизни.":
            call change_mood(1, True) from _call_change_mood_16
            jump ending

    return

label ending:
    window hide
    hide happy
    hide cat_happy
    play sound punch_door
    scene black with vpunch
    show room with very_slow_dissolve
    show emwhat at front_transform with very_slow_dissolve
    window show
    main_character "Неужели это все..."
    main_character "...мне приснилось?"
    hide emwhat
    show mom at front_transform with slowdissolve
    mum "Ох, прости, я не хотела тебя разбудить."
    mum "Может быть, тебе приснилась твоя будущая профессия?"
    $result_level = mood_level + skill_level
    hide mom

    if 5 < result_level <= 15:
        show neutral at front_transform
        $word = variations[16].lower()
        main_character "Еще не [word], но думаю, что я [variations[18]], в каком направлении мне стоит двигаться!"
        $description = "{0} {1} свой интерес в сфере IT.".format(main_character_name, variations[14])
        hide neutral
    elif result_level > 15:
        show happy at front_transform
        main_character "Да! Я буду веб-дизайнером!"
        $description = "{0} {1} профессиональным веб-дизайнером.".format(main_character_name, variations[4])
        hide happy
    else:
        show sad at front_transform
        main_character "Нет, никаких зацепок..."
        $description = "{0} в конце концов {1} себя...\nНо не в сфере IT.".format(main_character, variations[14])
        hide sad

    show mom at front_transform
    mum "Я верю, что, несмотря на то, какое направление в университете ты выберешь, в жизни у тебя все сложится прекрасно!"
    hide mom
    show happy at front_transform
    main_character "Верно! Поэтому, самое время подать документы!"
    window hide
    show screen the_ending(description) with slowdissolve
    $renpy.pause(4., hard=True)
    return