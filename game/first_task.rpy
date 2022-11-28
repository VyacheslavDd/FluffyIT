label get_to_work:
    masya "Что-то мне подсказывает, что нам пора приступить к работе!"
    $renpy.set_return_stack([])
    hide neutral_cat with slowdissolve
    hide emwhat with slowdissolve
    show sunny_street
    show screen first_customer
    window hide
    $renpy.pause(4., hard=True)
    window show
    hide sunny_street
    show screen first_customer_talk
    show neutral_cat onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    kindegarten_cat "{size=20}Здравствуйте! У меня свой маленький магазинчик с цветами и декоративными  растениями. Мой внук сказал, что в магазины давно никто не ходит, а все покупают в Интернете.{/size}"
    show sad_cat onlayer screens at left_transform
    hide neutral_cat onlayer screens
    kindegarten_cat "Поэтому я решил, что мне нужен сайт! Внучок помог мне его сделать, но еще ни один из покупателей не заказал товар... Пожалуйста, подскажите, что же не так?"
    show serious_cat onlayer screens at right_transform
    hide happy_cat onlayer screens
    masya "Ну-ка, ну-ка... Давайте посмотрим на Ваш сайт."
    hide serious_cat onlayer screens
    hide sad_cat onlayer screens
    hide screen first_customer_talk
    show screen show_image(1280, 720, 0, 0, "bosscabinet")
    masya "Та-а-ак...."
    masya "Такая проблема... Создать сайт на свой вкус я могу без проблем, у меня есть и знания, и навыки! Но понять, что не так уже с готовым сайтом для меня сложно."
    hide screen show_image
    show neutral at front_transform
    main_character "Тут же все крайне очевидно..."
    menu:
        "{size=30}В чём же проблема?{/size}"
        "Список товаров расположен не в алфавитном порядке!":
            call neutral_choice(True)
        "Не хватает фотографий товаров!":
            jump right_choice
        "Тут очень маленький выбор!":
            call wrong_choice(True)
    return

label wrong_choice(offer_two):
    call change_skill(-1, False)
    hide neutral
    show serious_cat at front_transform with hpunch
    masya "Ты чего? У нашего заказчика очень много разных товаров! Я еще нигде не видел столько красивых растений!"
    hide serious_cat
    show sad at front_transform
    main_character "Ой..."
    call change_mood(-1, False)
    show neutral at front_transform
    hide sad
    if not offer_two:
        menu:
            "{size=30}В чём же проблема?{/size}"
            "Не хватает фотографий товаров!":
                jump right_choice
    else:
        menu:
            "{size=30}В чём же проблема?{/size}"
            "Не хватает фотографий товаров!":
                jump right_choice
            "Список товаров расположен не в алфавитном порядке!":
                call neutral_choice(False)
    
    return

label neutral_choice(offer_two):
    hide neutral
    show neutral_cat at front_transform with slowdissolve
    masya "Не думаю, что это сильно важно. Возможно, товары отсортированы по их популярности. Покупателю так даже удобней."
    hide neutral_cat
    show neutral at front_transform
    if not offer_two:
        menu:
            "{size=30}В чём же проблема?{/size}"
            "Не хватает фотографий товаров!":
                jump right_choice
    else:
        menu:
            "{size=30}В чём же проблема?{/size}"
            "Не хватает фотографий товаров!":
                jump right_choice
            "Тут очень маленький выбор!":
                call wrong_choice(False)

label right_choice:
    $renpy.set_return_stack([])
    call change_skill(1, True)
    hide neutral with slowdissolve
    show happy_cat at front_transform with slowdissolve
    masya "Точно! Я бы никогда не догадался без твоей помощи! Сейчас мы это исправим."
    hide happy_cat with moveoutright
    show happy at front_transform with slowdissolve
    "...да, сейчас мы кое-что добавим..."
    "...вам точно подходят такие варианты?"
    "..."
    show wow at front_transform
    hide happy
    masya "Мы все исправили! Ждем вашей оценки."
    hide wow
    show screen show_image(1280, 720, 0, 0, "schoolhall")
    call change_mood(1, True)
    kindegarten_cat "Просто прелестно! Как будто смотрю на свою прекрасную клумбу."
    main_character "Мы очень рады, что Вам понравилось! Желаем хороших продаж. Обращайтесь к нам еще."

    hide screen show_image
    show mur_cat at very_left_transform
    nvl show dissolve
    masya_nvl "{color=#12e2e6}Мурка{/color}: {color=#e6d712}Запомни, хорошие изображения добавляют ценность контенту в глазах посетителя сайта.{/color}"
    masya_nvl "{color=#e6d712}Это залог успеха веб-разработчика!{/color}"
    masya_nvl "{color=#e6d712} А вот правила, которые должен соблюдать веб-дизайнер при использовании изображений:{/color}"
    nvl clear
    masya_nvl "·Для большего доверия посетителей сайта, располагать изображения желательно слева;"
    masya_nvl "·Использовать изображения только высокого качества – это  делает сайт более читабельным;"
    masya_nvl "·Нахождение изображения на сайте должно иметь цель;"
    masya_nvl "·Размер изображений должен быть не слишком большим – иначе сайт становится медленнее, из-за этого меньше просматривается."
    nvl clear
    nvl hide dissolve
    hide mur_cat
    show happy at front_transform
    main_character "Это я обязательно запомню!"
    show happy at left_transform with move
    show happy_cat at right_transform with moveinright
    masya "Как же все-таки приятно помогать таким хорошим людям! Я очень люблю за это свое дело."
    hide happy
    show neutral at left_transform
    main_character "И вправду, на душе становится так тепло... Мне начинает нравиться это все."
    masya "Ну это же замечательно! Чем дальше - тем больше! Давай примем следующий заказ. Мне как раз кто-то пишет..."
    hide neutral with moveoutleft
    hide happy_cat with moveoutright
    jump second_task
    return