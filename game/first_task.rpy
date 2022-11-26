label get_to_work:
    $renpy.set_return_stack([])
    hide neutral_cat with slowdissolve
    hide emwhat with slowdissolve
    show sunny_street
    show screen first_customer
    window hide
    $renpy.pause(4., hard=True)
    window show
    hide sunny_street
    show class_room with slowdissolve
    show neutral_cat at front_transform with slowdissolve
    kindegarten_cat "{size=20}Здравствуйте! У меня свой маленький магазинчик с цветами и декоративными  растениями. Мой внук сказал, что в магазины давно никто не ходит, а все покупают в Интернете.{/size}"
    show sad_cat at front_transform
    hide neutral_cat
    kindegarten_cat "Поэтому я решил, что мне нужен сайт! Внучок помог мне его сделать, но еще ни один из покупателей не заказал товар... Пожалуйста, подскажите, что же не так?"
    show serious_cat at front_transform
    hide sad_cat
    masya "Ну-ка, ну-ка... Давайте посмотрим на Ваш сайт."
    hide serious_cat
    show screen unfinished_flower_website
    masya "Та-а-ак...."
    masya "Такая проблема... Создать сайт на свой вкус я могу без проблем, у меня есть и знания, и навыки! Но понять, что не так уже с готовым сайтом для меня сложно."
    hide screen unfinished_flower_website
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
    show screen finished_flower_website
    call change_mood(1, True)
    kindegarten_cat "Просто прелестно! Как будто смотрю на свою прекрасную клумбу."
    main_character "Мы очень рады, что Вам понравилось! Желаем хороших продаж. Обращайтесь к нам еще."
    return