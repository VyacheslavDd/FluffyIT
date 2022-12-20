label third_task:
    show lab
    call show_customer("gui/nvl.png", "Котик-учёный", "#c9d2d5") from _call_show_customer_2
    hide lab
    show screen third_customer_talk
    show cat_science onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    play sound t2
    science_cat "{cps=35}Привет! Я начинающий ученый, и мы с моими коллегами решили вести сайт, на котором будем публиковать интересные научные статьи и наши открытия.{/cps}"
    play sound t3
    science_cat "{cps=18}Но наш сайт просто-напросто не открывается! Помогите нам. Ссылку уже отправил.{/cps}"
    play sound t1
    masya "{cps=20}Отлично! Сейчас разберемся.{/cps}"
    show screen show_image("loading_site")
    hide cat_science onlayer screens
    hide happy_cat onlayer screens
    hide screen third_customer_talk
    masya "Хм, надо его как-нибудь ускорить. Как думаешь, что поможет?"
    $correct_variants = 3
    $variants = [["Разместить на сайте Flash-баннеры", "punish 0"],
                ["Применить кэширование", "award 10"],
                ["Повысить разрешение изображений на сайте", "punish 2"],
                ["Добавить в код комментарии для ясности", "punish 3"],
                ["Сократить время ответа сервера", "award 40"],
                ["Применить поэтапную загрузку контента", "award 50"]
                ]
    show screen remained_answers()
    jump start_guessing
    return

label start_guessing:
    window hide
    $result = renpy.display_menu(variants)
    window show
    if "punish" in result:
        jump punish_character
    else:
        call award_character(result[-2:]) from _call_award_character
    return

label punish_character:
    call change_skill(-1, False) from _call_change_skill_6
    play sound bad_sound
    show sad_cat with vpunch
    masya "Боюсь, это только ухудшит работу сайта"
    hide sad_cat
    jump start_guessing
    return

label award_character(ind):
    if (ind[-1]) != "0":
        masya "Мы уже добавили это."
        jump start_guessing
    else:
        masya "Стало намного лучше!"
        $correct_variants -= 1
        if correct_variants == 0:
            hide screen remained_answers
            jump continue_third_task
        else:
            python:
                variants[int(ind[0])][1] =  variants[int(ind[0])][1][:-1] + "1"
            jump start_guessing
    return

label continue_third_task:
    hide neutral_cat
    masya "Так-то лучше..."
    hide screen show_image
    show screen show_image("articles")
    masya "Вот, как работает сайт сейчас!"
    hide screen show_image
    show screen third_customer_talk
    show cat_science onlayer screens at left_transform
    show happy onlayer screens at right_transform
    play sound t3
    science_cat "{cps=20}Спасибо! Видимо мы перестарались над оформлением сайта. Вы очень нас выручили.{/cps}"
    play sound t1
    main_character "{cps=18}Всегда рады Вам помочь!{/cps}"
    hide cat_science onlayer screens with slowdissolve
    hide happy onlayer screens with slowdissolve
    hide screen third_customer_talk with slowdissolve
    show cat_secretary at very_left_transform with slowdissolve
    nvl show dissolve
    masya_nvl "{color=#12e2e6}Мурка{/color}: {color=#e6d712}Если сайт не загрузится быстрее, чем за две секунды, то большая часть пользователей его покинет.{/color}"
    masya_nvl "{color=#e6d712}Веб-дизайнер должен тестировать скорость загрузки страниц сайта.{/color}"
    nvl clear
    masya_nvl "{color=#e6d712}Инструменты, которые можно использовать:{/color}"
    masya_nvl "{b}Инструмент от Google;\n\nPingdom;\n\nGT Metrix.{/b}"
    masya_nvl "{color=#e6d712}Каждый из них показывает, что замедляет работу сайта, и подсказывает, как это можно исправить.{/color}"
    nvl clear
    masya_nvl "{color=#e6d712}Способы ускорить быстродействие сайта:{/color}"
    masya_nvl "{b}Применение кэширования;\n\nПрименение поэтапной загрузки контента;\n\nСжатие изображений;\n\nОтказ от ненужных изображений.{/b}"
    masya_nvl "{color=#e6d712}И многое другое...{/color}"
    nvl hide dissolve
    hide cat_secretary
    show happy at front_transform
    main_character "[variations[16]], что мне пригодятся эти знания!"
    show happy at left_transform with move
    show cat_happy at right_transform with moveinright
    masya "Мы столько всего сделали!  Думаю, следующий заказ будет последним на сегодня."
    hide happy with moveoutleft
    hide cat_happy with moveoutright
    jump start_last_task
    return
