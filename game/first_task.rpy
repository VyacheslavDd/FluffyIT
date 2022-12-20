label show_customer(picture, name, color):
    show screen customer_notification(picture, name, color)
    window hide
    $renpy.pause(4., hard=True)
    window show
    return

label get_to_work:
    masya "Что-то мне подсказывает, что нам пора приступить к работе!"
    $renpy.set_return_stack([])
    hide neutral_cat with slowdissolve
    hide emwhat with slowdissolve
    show kinden_f
    call show_customer("gui/nvl.png", "Котик-Садовод", "#2ea40d") from _call_show_customer
    hide kinden_f
    show screen first_customer_talk
    show cat_kindegarten onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    play sound t5
    kindegarten_cat "{size=20}{cps=50}Здравствуйте! У меня свой маленький магазинчик с цветами и декоративными  растениями. Мой внук сказал, что в магазины давно никто не ходит, а все покупают в Интернете.{/cps}{/size}"
    play sound t5
    kindegarten_cat "{cps=46}Поэтому я решил, что мне нужен сайт! Внучок помог мне его сделать, но еще ни один из покупателей не заказал товар... Пожалуйста, подскажите, что же не так?{/cps}"
    show serious_cat onlayer screens at right_transform
    hide happy_cat onlayer screens
    play sound t1
    masya "{cps=30}Ну-ка, ну-ка... Давайте посмотрим на Ваш сайт.{/cps}"
    hide serious_cat onlayer screens
    hide cat_kindegarten onlayer screens
    hide screen first_customer_talk
    show screen show_image("broken_flowers")
    masya "Та-а-ак...."
    masya "Такая проблема... Создать сайт на свой вкус я могу без проблем, у меня есть и знания, и навыки! Но понять, что не так уже с готовым сайтом для меня сложно."
    hide screen show_image
    show neutral at front_transform
    main_character "Тут же все крайне очевидно..."
    jump problem_menu
    return

label problem_menu:
    menu:
        "\"{size=30}В чём же проблема?{/size}\""
        "Список товаров расположен не в алфавитном порядке!":
            jump neutral_choice
        "Не хватает фотографий товаров!":
            jump right_choice
        "Тут очень маленький выбор!":
            jump wrong_choice
    return

label wrong_choice:
    call change_skill(-1, False) from _call_change_skill
    hide neutral
    play sound bad_sound
    show serious_cat at front_transform with hpunch
    masya "Ты чего? У нашего заказчика очень много разных товаров! Я еще нигде не видел столько красивых растений!"
    hide serious_cat
    show sad at front_transform
    main_character "Ой..."
    call change_mood(-1, False) from _call_change_mood_3
    show neutral at front_transform
    hide sad
    jump problem_menu
    return

label neutral_choice:
    hide neutral
    show neutral_cat at front_transform with slowdissolve
    masya "Не думаю, что это сильно важно. Возможно, товары отсортированы по их популярности. Покупателю так даже удобней."
    hide neutral_cat
    show neutral at front_transform
    jump problem_menu
    return

label right_choice:
    $renpy.set_return_stack([])
    call change_skill(1, True) from _call_change_skill_1
    hide neutral with slowdissolve
    show happy_cat at front_transform with slowdissolve
    masya "Точно! Я бы никогда не догадался без твоей помощи! Сейчас мы это исправим."
    hide happy_cat with moveoutright
    show screen show_image("broken_flowers") with slowdissolve
    "..."
    main_character "Жду не дождусь, когда они придут к какому-нибудь результату!"
    "..."
    hide screen show_image
    show screen show_image("flowers_cool")
    play sound t1
    masya "{cps=30}Мы все исправили! Ждем вашей оценки.{/cps}"
    hide screen show_image
    show screen first_customer_talk
    show cat_kindegarten onlayer screens at left_transform
    show happy onlayer screens at right_transform
    call change_mood(1, True) from _call_change_mood_4
    play sound t3
    kindegarten_cat "{cps=15}Просто прелестно! Как будто смотрю на свою прекрасную клумбу.{/cps}"
    play sound t3
    main_character "{cps=19}Мы очень рады, что Вам понравилось! Желаем хороших продаж. Обращайтесь к нам еще.{/cps}"
    hide cat_kindegarten onlayer screens with slowdissolve
    hide happy onlayer screens with slowdissolve
    hide screen first_customer_talk with slowdissolve
    show cat_secretary at very_left_transform
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
    hide cat_secretary
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