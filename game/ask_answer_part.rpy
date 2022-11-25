label start_asking:
    hide neutral
    show emwhat at left_transform
    menu:
        "Стоит ли мне о чём-нибудь поинтересоваться..."
        "Спросить про направления в университете":
            call ask_directions(False)
        "Спросить про баллы для поступления":
            call ask_scores(False)
        "Спросить, чем привлекла профессия":
            call ask_attraction(False)
        "Приступить к работе":
            jump get_to_work


label ask_directions(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True)
    main_character "А где учат на этого веб-дизайнера? Ни в одном университете не [variations[12]] я такого направления."
    masya "// ждем доклада ксюши //"
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "Чем бы еще поинтересоваться..."
            "Спросить про баллы для поступления":
                call ask_scores(False, True, 'ask_attraction')
            "Спросить, чем привлекла профессия":
                call ask_attraction(False, True, 'ask_scores')

label ask_scores(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True)
    main_character "Сколько баллов понадобиться, чтобы поступить на подходящее для этой профессии направление?"
    masya "// ждем доклада ксюши //"
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "Чем бы еще поинтересоваться..."
            "Спросить про направления в университете":
                call ask_directions(False, True, 'ask_attraction')
            "Спросить, чем привлекла профессия":
                call ask_attraction(False, True, 'ask_directions')

label ask_attraction(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True)
    main_character "Почему ты выбрал именно эту профессию? Чем она тебя зацепила?"
    masya "Потому что она не только очень востребованная, но и очень творческая! Я могу выражать себя и помогать тем самым другим."
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "Чем бы еще поинтересоваться..."
            "Спросить про направления в университете":
                call ask_directions(False, True, 'ask_scores')
            "Спросить про баллы для поступления":
                call ask_scores(False, True, 'ask_directions')

label get_to_work:
    $renpy.set_return_stack([])
    "Ну, за работу!"
    return