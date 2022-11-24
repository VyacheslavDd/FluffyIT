init python:
        class CharacterWords:
            def __init__(self):
                self.character_variation = None
                self.__boy_variation = ["определился", "сынок", "Такой", "большой стал", "стал", "нервным", "сделал", "попал", "такой", "пришёл", "новенький", "оказался"]
                self.__girl_variation = ["определилась", "дочка", "Такая", "большая стала", "стала", "нервной", "сделала", "попала", "такая", "пришла", "новенькая", "оказалась"]

            def set_variation(self, is_boy=True):
                return self.__boy_variation if is_boy else self.__girl_variation

screen title_screen():
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

transform left_transform:
    xalign 0.2
    yalign 0.4

transform right_transform:
    xalign 0.8
    yalign 0.4

transform very_left_transform:
    xalign 0.05
    yalign 0.4

transform very_right_transform:
    xalign 0.95
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
define boss_cat = Character("Василий Мяукович", color="#597e0e")
define murka = Character("Мурка", color="#c30f8a")
define masya = Character("Мася", color="#b2c601")
define mood_level = 5
define words = CharacterWords()
define bar_part = "yellow_left"
define variations = []

image neutral = "[img_prefix]_neutral"
image angry = "[img_prefix]_angry"
image emwhat = "[img_prefix]_emwhat"
image happy = "[img_prefix]_happy"
image sad = "[img_prefix]_sad"
image wow = "[img_prefix]_wow"
image oh_my_gosh = "[img_prefix]_omg"
image sunny_street = "street"
image pretty_kitchen = "kitchen"
image class_room = "class"
image room = "[img_prefix]sroom"
image dream_office = "office"
image neutral_cat = "cat_neutral"
image serious_cat = "cat_serious"
image happy_cat = "cat_happy"
image mur_cat = "cat_mur"
image oneeye_cat = "cat_oneeye"
image sad_cat = "cat_sad"
image what_cat = "cat_what"
image mom = "mom([img_prefix])"

image black = "#000000"

label start:
    show sunny_street with slowdissolve
    show screen choose_character with slowdissolve

    python:
        ui.interact()

    return

label boy:
    $persistent.is_boy = True
    $renpy.notify("Вы играете за мальчика")
    jump start_story

label girl:
    $persistent.is_boy = False
    $renpy.notify("Вы играете за девочку")
    $main_character_name = "Аня"
    $img_prefix = "girl"
    jump start_story

label start_story:
    $variations = words.set_variation(is_boy=persistent.is_boy)[:]
    
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
    main_character "Скука... Ничего не хочется, ничего не нравится... Одноклассники уже документы подали в университеты, а я еще даже не [variations[0]] с направлением. Ну, пойду перекушу что-ли..."
    hide sad with slowdissolve

    show kitchen with pixellate
    show mom at front_transform with moveinbottom
    mum "О, [variations[1]]! [variations[2]] ты у меня [variations[3]]! Совсем скоро студенческая жизнь. Ты уже [variations[0]], кем хочешь стать?"

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
    main_character "Опять я не [variations[6]] ничего полезного... Ужасно!"
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
    jump office_part
    return

label office_part:
    main_character "Что? Где я? Куда я вообще [variations[7]]?"
    show screen mood

    if mood_level < 5:
        $bar_part, mood_level = update_mood(mood_level, -1)
        $renpy.notify("Уровень настроения понижен.")
        show emwhat at left_transform with move
        show serious_cat at right_transform with moveinright
        show oh_my_gosh at left_transform
        hide emwhat
        boss_cat "Ты кто еще [variations[8]]? Еще и выглядишь хмуро. [variations[9]] на вакансию сисадмина чтобы взломать нас?"
    else:
        $bar_part, mood_level = update_mood(mood_level, 1)
        $renpy.notify("Уровень настроения повышен.")
        show emwhat at left_transform with move
        show neutral_cat at right_transform with moveinright
        show oh_my_gosh at left_transform
        hide emwhat
        boss_cat "Так-так, [variations[10]]! Выглядишь дружелюбно. Нам такие нужны. На какую вакансию претендуешь?"
    
    show sad at left_transform
    hide oh_my_gosh
    main_character "Если честно, я совсем не понимаю, про какую вакансию вы говорите. Кто Вы, и как я сюда [variations[7]]?"
    show what_cat at right_transform
    hide serious_cat
    hide neutral_cat
    boss_cat 'Что за вопрос? Ты находишься в крупнейшей IT компании "Симпл Котинг", а я ее главный директор. Уж не знаю, как ты тут [variations[11]], но если ты уже здесь, то значит не зря!'

    if mood_level < 5:
        main_character "Очень даже зря! У меня даже нет знаний в этой сфере..."
    else:
        show neutral at left_transform
        hide sad
        main_character "Мне что-то нужно делать? Я ведь ничего не умею..."

    hide what_cat
    show happy_cat at right_transform
    boss_cat "О, у нас как раз есть один такой стажёр. Тоже ничего не знает и ничего не умеет. Ему и будешь помогать."
    hide sad
    show emwhat at left_transform
    main_character "Так если ни он, ни я ничего не умеем, как мы справимся?"
    hide happy_cat
    show neutral_cat at right_transform
    boss_cat "Вам поможет Мурка, моя ассистентка. Она занимается подбором персонала и отслеживает успехи стажёров. Вот и она, следуйте за ней! А я с Вами прощаюсь."
    hide neutral_cat with moveoutright
    show mur_cat at right_transform with moveinright
    murka "Приветик! Я отведу тебя к Масе, тому самому стажеру. Он не такой уж и глупый, как рассказывал тебе о нем директор, но помощь твоя ему точно не помешает."
    hide oh_my_gosh
    hide neutral
    show emwhat at very_left_transform with move
    show happy_cat at front_transform with moveinright
    show mur_cat at very_right_transform with move
    show neutral at very_left_transform
    hide emwhat
    masya "Чего вы тут про меня шепчитесь? Это мой новый напарник? Ну наконец-то, теперь работа пойдет как по маслу!"
    murka "Отлично, тогда вот ваше первое совместное задание. Вы должны переделать сайт для нашего заказчика, для этого свяжитесь с ним и обговорите все ньюансы."
    hide mur_cat with moveoutright
    hide happy_cat with slowdissolve
    hide neutral with slowdissolve
    show class_room with slowdissolve
    show happy_cat at right_transform with slowdissolve
    show neutral at left_transform with slowdissolve
    main_character "А что у тебя за профессия такая, сайты переделывать?"
    masya "Я пришел на должность веб-дизайнера, очень надеюсь что у меня получится!"
    hide happy_cat
    show neutral_cat at right_transform
    return


