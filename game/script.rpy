﻿screen title_screen():
    frame:
        xalign 0.5
        yalign 0.3
        background None
        text "{b}Выберите пол главного героя{/b}:":
            slow_cps 20
            underline True
            bold True
            italic True
            size 30

screen choose_character():
    use title_screen()
    use character(0, "boy_neutral", "boy_happy", "boy")
    use character(0.95, "girl_neutral", "girl_happy", "girl")

screen character(row_align, image_idle, image_hover, move_to_label):
    frame:
        xalign row_align
        yalign 0.95
        background None

        imagebutton:
            idle image_idle
            hover image_hover
            action Jump(move_to_label)


screen mood():
    timer 3.0 action Hide("mood")
    frame:
        xalign 0
        yalign 0
        xsize 100
        background "#282828"
        bar:
            left_bar "gui/bar/[bar_part].png"
            right_bar "gui/bar/right.png"
            value VariableValue("mood_level", 10)

transform front_transform:
    xalign 0.5
    yalign 0.4


init python:
    def update_mood(mood_level, value):
        mood_level += value
        if mood_level > 10:
            mood_level = 10
        if mood_level < 0:
            mood_level = 0
        return ("red_left" if mood_level < 5 else ("yellow_left" if mood_level < 8 else "green_left"), mood_level)


define main_character_name = "Денис"
define img_prefix = "boy"
define slowdissolve = Dissolve(1.5)
define very_slow_dissolve = Dissolve(3.5)
define main_character = Character("[main_character_name]", color="#b406de")
define mum = Character("Мама", color="#0a30f0")
define mood_level = 5
define bar_part = "yellow_left"

image neutral = "[img_prefix]_neutral"
image angry = "[img_prefix]_angry"
image emwhat = "[img_prefix]_emwhat"
image happy = "[img_prefix]_happy"
image omg = "[img_prefix]_OMG"
image sad = "[img_prefix]_sad"
image wow = "[img_prefix]_wow"
image sunny_street = "street"
image pretty_kitchen = "kitchen"
image room = "[img_prefix]sroom"
image dream_office = "office"
image mom = "mom([img_prefix])"
image black = "#000000"

label start:
    show sunny_street with slowdissolve
    show screen choose_character with slowdissolve

    python:
        ui.interact()

    return

label boy:
    $renpy.notify("Вы играете за мальчика")
    $words.set_variation()
    jump start_story

label girl:
    $renpy.notify("Вы играете за девочку")
    $main_character_name = "Аня"
    $img_prefix = "girl"
    $words.set_variation(is_boy=False)
    jump start_story

label start_story:
    init python:
        class CharacterWords:
            def __init__(self):
                self.character_variation = None
                self.__boy_variation = ["определился", "сынок", "Такой", "большой стал", "стал", "нервным", "сделал", "попал"]
                self.__girl_variation = ["определилась", "дочка", "Такая", "большая стала", "стала", "нервной", "сделала", "попала"]

            def set_variation(self, is_boy=True):
                self.character_variation = self.__boy_variation if is_boy else self.__girl_variation

    define words = CharacterWords()
    hide screen title_screen
    hide screen choose_character

    show happy at front_transform
    $character_name = renpy.input("Введите имя главного героя:\n")
    $main_character_name = character_name or main_character_name
    hide happy
    "Вот и наступил июль! Как же быстро пролетело время... Выпускники радуются окончанию школы и наслаждаются летней порой. Но только не [main_character_name]."
    show screen mood

    show room with fade
    hide sunny_street
    show sad at front_transform with slowdissolve
    main_character "Скука... Ничего не хочется, ничего не нравится... Одноклассники уже документы подали в университеты, а я еще даже не [words.character_variation[0]] с направлением. Ну, пойду перекушу что-ли..."
    hide sad with slowdissolve

    show kitchen with pixellate
    show mom at front_transform with moveinbottom
    mum "О, [words.character_variation[1]]! [words.character_variation[2]] ты у меня [words.character_variation[3]]! Совсем скоро студенческая жизнь. Ты уже [words.character_variation[0]], кем хочешь стать?"

    menu:
        "Что бы сказать..."

        "Нагрубить":
            $bar_part, mood_level = update_mood(mood_level, -1)
            $renpy.notify("Уровень настроения понижен.")
            call mum_choice(True, "Это не твоё дело! И так голова кипит из-за поступления, а ты ещё и напоминаешь каждый раз об этом!", "Всё, надоело! Больше из своей комнаты не выйду.") from _call_mum_choice
        "Спокойно ответить":
            $bar_part, mood_level = update_mood(mood_level, 1)
            $renpy.notify("Уровень настроения повышен.")
            call mum_choice(False, "Нет, и я очень переживаю по этому поводу... Совсем опускаются руки.",  "Надо бы и вправду отдохнуть от навязчивых мыслей.") from _call_mum_choice_1
    
    return

label mum_choice(isrude, fphrase, final_phrase):
    show screen mood
    hide mom
    if isrude:
        show angry at front_transform with vpunch
        main_character "[fphrase]"
        hide angry
    else:
        show sad at front_transform with slowdissolve
        main_character "[fphrase]"
        hide sad

    show mom at front_transform with slowdissolve

    if isrude:
        mum "Ох, ты [words.character_variation[4]] очень [words.character_variation[5]]. Тебе стоит немедленно успокоиться!"
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
        "Чем бы теперь заняться..."

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
    show screen mood
    $bar_part, mood_level = update_mood(mood_level, -1)
    $renpy.notify("Уровень настроения понижен.")
    main_character "Опять я не [words.character_variation[6]] ничего полезного... Ужасно!"
    call room_choice(picture) from _call_room_choice_2
    return

label play_with_cat(picture):
    hide picture
    show wow at front_transform
    show screen mood
    $bar_part, mood_level = update_mood(mood_level, 1)
    $renpy.notify("Уровень настроения повышен.")
    main_character "Он моя радость! Хоть что-то делает жизнь веселее."
    hide wow
    show neutral at front_transform
    call room_choice("[img_prefix]_neutral") from _call_room_choice_3
    return

label play_phone(picture):
    main_character "Ну, попробую поиграть в телефон..."
    hide picture
    show happy at front_transform
    main_character 'Ведь наконец-то "Котляндия" вышла! Все так долго ждали эту игру, не терпится поиграть!'
    "*Играет*"
    hide happy
    main_character "Ой, что-то я засыпаю..."
    hide neutral
    hide sad
    scene black with very_slow_dissolve
    define teleport_office = ImageDissolve("images/scenes/office.png", 3.0, 0)
    show office with teleport_office
    show emwhat at front_transform
    main_character "Что? Где я? Куда я вообще [words.character_variation[7]]?"
    return


