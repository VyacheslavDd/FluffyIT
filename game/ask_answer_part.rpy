label start_asking:
    hide neutral
    show emwhat at left_transform
    menu:
        "{size=30}Стоит ли мне о чём-нибудь поинтересоваться...{/size}"
        "Спросить про направления в университете":
            call ask_directions(False) from _call_ask_directions
        "Спросить про баллы для поступления":
            call ask_scores(False) from _call_ask_scores
        "Спросить, чем привлекла профессия":
            call ask_attraction(False) from _call_ask_attraction
        "Приступить к работе":
            jump get_to_work


label ask_directions(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True) from _call_change_mood
    main_character "А где учат на этого веб-дизайнера? Ни в одном университете не [variations[12]] я такого направления."
    masya "Навыки в области Web-дизайна с фокусом на IT можно получить в вузах в рамках направлений:"
    masya '"Программная инженерия"\n"Дизайн графических и пользовательских интерфейсов информационных систем"'
    masya '"Прикладная информатика в компьютерном дизайне"\n"Информационные технологии в дизайне"\n"Разработка и дизайн веб-приложений" и другие.'
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "{size=30}Чем бы еще поинтересоваться...{/size}"
            "Спросить про баллы для поступления":
                call ask_scores(False, True, 'ask_attraction') from _call_ask_scores_1
            "Спросить, чем привлекла профессия":
                call ask_attraction(False, True, 'ask_scores') from _call_ask_attraction_1

label ask_scores(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True) from _call_change_mood_1
    main_character "Сколько баллов понадобиться, чтобы поступить на подходящее для этой профессии направление?"
    masya "// ждем доклада ксюши //"
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "{size=30}Чем бы еще поинтересоваться...{/size}"
            "Спросить про направления в университете":
                call ask_directions(False, True, 'ask_attraction') from _call_ask_directions_1
            "Спросить, чем привлекла профессия":
                call ask_attraction(False, True, 'ask_directions') from _call_ask_attraction_2

label ask_attraction(is_end, automatic_end=False, next_label_name=""):
    call change_mood(1, True) from _call_change_mood_2
    main_character "Почему ты выбрал именно эту профессию? Чем она тебя зацепила?"
    masya "Потому что она не только очень востребованная, но и очень творческая! Я могу выражать себя и помогать тем самым другим."
    if automatic_end:
        $renpy.call(next_label_name, True)
    if is_end:
        jump get_to_work
    else:
        menu:
            "{size=30}Чем бы еще поинтересоваться...{/size}"
            "Спросить про направления в университете":
                call ask_directions(False, True, 'ask_scores') from _call_ask_directions_2
            "Спросить про баллы для поступления":
                call ask_scores(False, True, 'ask_directions') from _call_ask_scores_2