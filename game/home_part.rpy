label start:
    show sunny_street with slowdissolve
    play sound info_type
    show screen choose_character with slowdissolve

    python:
        ui.interact()

    return

label boy:
    $renpy.notify("Вы играете за мальчика")
    jump start_story

label girl:
    $is_boy = False
    $renpy.notify("Вы играете за девочку")
    $main_character_name = "Аня"
    $img_prefix = "girl"
    jump start_story

label change_mood(value, positive):
    show screen mood
    $bar_part, mood_level = update_mood(mood_level, value)
    $renpy.notify("Уровень настроения повышен!" if positive else "Уровень настроения понижен.")
    return

label change_skill(value, positive):
    show screen skill
    $skill_level = update_skill(skill_level, value)
    $renpy.notify("Уверенность в навыке повышена!" if positive else "Вы усомнились в ваших навыках...")
    return

label start_story:
    $variations = bv[:] if is_boy else gv[:]
    hide screen title_screen 
    hide screen choose_character

    show happy at front_transform
    $character_name = renpy.input("Введите имя главного героя:\n")
    $main_character_name = character_name or main_character_name
    hide happy
    "Вот и наступил июль! Как же быстро пролетело время... Выпускники радуются окончанию школы и наслаждаются летней порой. Но только не [main_character_name]."
    show screen mood
    show screen skill
    show room with fade
    hide sunny_street
    show sad at front_transform with slowdissolve
    main_character "Скука... Ничего не хочется, ничего не нравится... Одноклассники уже документы подали в университеты, а я еще даже не [variations[0]] с направлением."
    main_character "Ну, пойду перекушу что-ли..."
    hide sad with slowdissolve

    show kitchen with pixellate
    show mom at front_transform with moveinbottom
    mum "О, [variations[1]]! [variations[2]] ты у меня [variations[3]]! Совсем скоро студенческая жизнь. Ты уже [variations[0]], кем хочешь стать?"

    menu:
        "\"{size=30}Что бы сказать...{/size}\""

        "Нагрубить":
            call change_mood(-1, False) from _call_change_mood_5
            call mum_choice(True, "Это не твоё дело! И так голова кипит из-за поступления, а ты ещё и напоминаешь каждый раз об этом!", "Всё, надоело! Больше из своей комнаты не выйду.") from _call_mum_choice
        "Спокойно ответить":
            call change_mood(1, True) from _call_change_mood_6
            call mum_choice(False, "Нет, и я очень переживаю по этому поводу... Совсем опускаются руки.",  "Надо бы и вправду отдохнуть от навязчивых мыслей.") from _call_mum_choice_1
    
    return

label mum_choice(isrude, fphrase, final_phrase):
    hide mom
    if isrude:
        play sound bad_sound
        show angry at front_transform with vpunch
        main_character "[fphrase]"
        hide angry
    else:
        show sad at front_transform with slowdissolve
        main_character "[fphrase]"
        hide sad

    show mom at front_transform with slowdissolve

    if isrude:
        mum "Ох, ты [variations[4]] очень [variations[5]]. Тебе стоит немедленно успокоиться!"
    else:
        mum "Понимаю тебя... Постарайся не думать об этом. Отвлекись, и я уверена, профессия сама найдёт тебя!"

    hide mom
    show room
    hide kitchen with pushright
    if isrude:
        show sad at front_transform with moveinleft
    else:
        show neutral at front_transform with moveinleft

    main_character "[final_phrase]"
    if isrude:
        call room_choice("[img_prefix]_sad") from _call_room_choice
    else:
        call room_choice("[img_prefix]_neutral") from _call_room_choice_1
    return

label room_choice(picture):
    menu:
        "\"{size=30}Чем бы теперь заняться...{/size}\""

        "Поспать":
            call sleep_or_watch(picture, very_slow_dissolve, "Спустя час...") from _call_sleep
        "Посмотреть смешные видео":
            call sleep_or_watch(picture, slowdissolve, "Спустя 30 минут...") from _call_sleep_or_watch
        "Погладить кота":
            call play_with_cat(picture) from _call_play_with_cat
        "Поиграть в телефон":
            call play_phone(picture) from _call_play_phone
    
    return

label sleep_or_watch(picture, effect, phrase):
    hide picture
    scene black with effect
    "[phrase]"
    show room with effect
    show sad at front_transform with slowdissolve
    call change_mood(-1, False) from _call_change_mood_7
    main_character "Опять я не [variations[6]] ничего полезного... Ужасно!"
    call room_choice(picture) from _call_room_choice_2
    return

label play_with_cat(picture):
    hide picture
    show wow at front_transform
    call change_mood(1, True) from _call_change_mood_8
    main_character "Хоть какая-то радость в жизни."
    hide wow
    show neutral at front_transform
    call room_choice("[img_prefix]_neutral") from _call_room_choice_3
    return

label play_phone(picture):
    main_character "Ну, попробую поиграть в телефон..."
    hide picture
    show happy at front_transform
    call change_mood(1, True) from _call_change_mood_9
    main_character 'Ведь наконец-то "Котляндия" вышла! Все так долго ждали эту игру, не терпится поиграть!'
    window hide
    hide happy
    hide neutral
    hide sad

    show screen phone_screen
    python:
        ui.interact()

    return

label playing_phone:
    hide screen phone_screen
    show screen show_image("phone_play")
    window show
    main_character "Выглядит шикарно, но, кажется, меня тянет в сон..."
    window hide
    hide screen show_image with slowdissolve
    scene black with very_slow_dissolve
    define teleport_office = ImageDissolve("images/scenes/office.png", 3.0, 0)
    show office with teleport_office
    show emwhat at front_transform
    jump office_part
    return
