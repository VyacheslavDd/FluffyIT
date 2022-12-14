label start_last_task:
    show sunny_street
    call show_customer("gui/nvl.png", "Котик-Аноним", "#18aae4")
    hide sunny_street
    show screen last_customer_talk
    show cat_anon onlayer screens at touching_left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    anonymous_cat "Просто сделайте мне хороший сайт. На этом все."
    masya "К вечеру будет готово! Положитесь на нас."
    anonymous_cat "...."
    hide happy_cat onlayer screens
    show what_cat onlayer screens at right_transform
    hide cat_anon onlayer screens with slowdissolve
    hide screen last_customer_talk with slowdissolve
    hide what_cat onlayer screens
    show what_cat at right_transform
    show emwhat at left_transform with moveinleft
    masya "Какой то он странный и немногословный."
    hide what_cat
    show happy_cat at right_transform
    masya "Ну что ж, это не наше дело. Давай приступим к работе."
    show screen show_image(1280, 720, 0, 0, "loading_site")
    call show_viruses(False)
    hide happy_cat
    hide emwhat with vpunch
    main_character "О нет, это же вирусы!!"
    masya "С таким мы еще не сталкивались... Но ничего страшного, нам любая работа под силу! Попробуем справиться с ними, как настоящие уважающие себя программисты."
    jump what_to_do
    return

label show_viruses(is_interaction):
    show screen virus1(is_interaction)
    show screen virus2(is_interaction)
    show screen virus3(is_interaction)
    show screen virus4(is_interaction)
    show screen virus5(is_interaction)
    return

label hide_viruses:
    hide screen virus1
    hide screen virus2
    hide screen virus3
    hide screen virus4
    hide screen virus5
    return

label what_to_do:
    menu:
        "{size=30}Как поступить?{/size}"
        "Перезагрузить компьютер":
            call wrong_answer(True, "Это как-то слишком просто.", "what_to_do")
        "Попросить помощи у специалиста по кибербезопасности":
            call wrong_answer(False, "Я хочу, чтобы мы сами с этим справились!", "what_to_do")
        "Написать антивирусную программу":
            call wrong_answer(True, "Боюсь, что это не наша специализация...", "what_to_do")
        "Кликнуть несколько раз по вирусу":
            jump start_clicking
        "Поплакать":
            call wrong_answer(True, "Нельзя опускать руки! Подумай еще.", "what_to_do")

label wrong_answer(is_minus, phrase, label_name):
    if is_minus:
        call change_skill(-1, False)
    masya "[phrase]"
    $renpy.jump(label_name)
    return

label start_clicking:
    $renpy.set_return_stack([])
    masya "Хорошая идея!"
    window hide
    call hide_viruses
    $killed = 0
    call show_viruses(True)
    
    python:
        ui.interact()

    return

label continue_after_cleaning:
    window show
    masya "Другое дело!"
    call hide_viruses
    hide screen show_image
    show neutral at left_transform
    show cat_neutral at right_transform
    masya "Осталось сделать хороший сайт..."
    hide cat_neutral
    show cat_sad at right_transform
    masya "...но, к сожалению, от прошлого сайта ничего не осталось."
    hide neutral
    show emwhat at left_transform
    main_character "И что же нам делать?"
    hide emwhat
    hide cat_sad
    show happy at left_transform
    show cat_happy at right_transform
    hide happy
    hide cat_happy
    show neutral at left_transform
    show cat_neutral at right_transform
    masya "Можем создать макет для хорошего сайта! Думаю, теперь у нас достаточно навыков для этого."
    masya 'Давай определимся, сколько изображений будет на нашем "идеальном сайте"?'
    jump first_question
    return

label first_question:
    $renpy.set_return_stack([])
    menu:
        "Изображениям не место на идеальном сайте":
            call wrong_answer(True, "Без них сайт станет менее интересным, дизайн сайта ухудшится.", "first_question")
        "Сайт должен на 90%% процентов состоять из картинок":
            call wrong_answer(True, "Большое количество изображений уменьшают читабельность сайта и увеличивают скорость его работы.", "first_question")
        "Изображения должны быть добавлены, только если у них есть цель нахождения":
            call change_skill(1, True)
            masya "Правильно! Необходимо решить, какими должны быть изображения на сайте."
            jump second_question
    return

label second_question:
    $renpy.set_return_stack([])
    menu:
        "Большими и самого хорошего качества!":
            call wrong_answer(True, "Не-а! Картинки не должны быть слишком большими — иначе сайт становится медленнее, что негативно сказывается на общем юзабилити.", "second_question")
        "Маленькими и нечеткими":
            call wrong_answer(True, "Мася: Нет! Плохие картинки делают сайт менее читабельным.", "second_question")
        "Хорошего качества, но не сильно большого размера":
            call change_skill(1, True)
            masya "Верно! Решим вопрос с навигацией. За сколько кликов должна находиться нужная на сайте страница?"
            jump third_question
    return

label third_question:
    $renpy.set_return_stack([])
    menu:
        "Максимум 2 клика":
            call wrong_answer(True, "Было бы здорово, но не думаю, что это будет возможно осуществить для каждой страницы.", "third_question")
        "Не менее 5 кликов":
            call wrong_answer(True, "Слишком много! Посетителям будет легче найти с сайт с более просто навигацией.", "third_question")
        "± 3 клика":
            call change_skill(1, True)
            masya "Отлично! Думаю, для шаблона этого хватит. Давай отправим заказчику."
            jump finish_game
    return

