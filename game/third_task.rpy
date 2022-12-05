label third_task:
    show sunny_street
    call show_customer("gui/nvl.png", "Котик-учёный", "#c9d2d5")
    hide sunny_street
    show screen third_customer_talk
    show neutral_cat onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    science_cat "Привет! Я начинающий ученый, и мы с моими коллегами решили вести сайт, на котором будем публиковать интересные научные статьи и наши открытия."
    hide neutral_cat onlayer screens
    show sad_cat onlayer screens at left_transform
    science_cat "Но наш сайт просто-напросто не открывается! Помогите нам. Ссылку уже отправил."
    masya "Отлично! Сейчас разберемся."
    show screen show_image(1280, 720, 0, 0, "kitchen")
    hide sad_cat onlayer screens
    hide happy_cat onlayer screens
    hide screen third_customer_talk
    masya "Хм, надо его как-нибудь ускорить. Как думаешь, что поможет?"
    $correct_variants = 3
    $variants = [["Разместить на сайте Flash-баннеры", "punish 0"],
                ["Применить кэширование", "award 1"],
                ["Повысить разрешение изображений на сайте", "punish 2"],
                ["Добавить в код комментарии для ясности", "punish 3"],
                ["Сократить время ответа сервера", "award 4"],
                ["Применить поэтапную загрузку контента", "award 5"]
                ]
    jump start_guessing
    return

label start_guessing:
    window hide
    $result = renpy.display_menu(variants)
    window show
    if "punish" in result:
        call punish_character(result[-1])
    else:
        call award_character(result[-1])
    return

label punish_character(ind):
    call change_skill(-1, False)
    show sad_cat with vpunch
    masya "Боюсь, это только ухудшит работу сайта"
    hide sad_cat
    call update_variants(ind)
    return

label award_character(ind):
    masya "Стало намного лучше!"
    $correct_variants -= 1
    if correct_variants == 0:
        jump continue_third_task
    else:
        call update_variants(ind)
    return

label update_variants(ind):
    $variants = change_variants(variants, ind)
    jump start_guessing
    return

label continue_third_task:
    hide neutral_cat
    masya "Так-то лучше! Давай посмотрим, как работает сайт сейчас."
    hide screen show_image
    show screen show_image(1280, 720, 0, 0, "girlsroom")
    science_cat "Спасибо! Видимо мы перестарались над оформлением сайта. Вы очень нас выручили."
    main_character "Всегда рады Вам помочь!"
    hide screen show_image
    show mur_cat at very_left_transform with slowdissolve
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
    hide mur_cat
    show happy at front_transform
    "ok"
    return
