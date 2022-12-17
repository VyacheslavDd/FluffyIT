label start_asking:
    hide neutral
    show emwhat at left_transform
    $narrator("\"{size=30}Стоит ли мне о чём-нибудь поинтересоваться...{/size}\"")
    $questions = [["Спросить про направления в университете", "ask_directions 0"],
                ["Спросить про баллы для поступления", "ask_scores 1"],
                ["Спросить, чем привлекла профессия", "ask_attraction 2"],
                ["Приступить к работе", "get_to_work 3"]]
    jump asking
    return

label asking:
    $result = renpy.display_menu(questions)
    if "work" in result:
        jump get_to_work
    else:
        $renpy.call(result[:-2], result[-1])
    return

label return_to_asking(ind):
    $questions = change_variants(questions, ind)
    jump asking
    return

label ask_directions(ind):
    call change_mood(1, True) from _call_change_mood
    main_character "А где учат на этого веб-дизайнера? Ни в одном университете не [variations[12]] я такого направления."
    masya "Навыки в области Web-дизайна с фокусом на IT можно получить в вузах в рамках направлений:"
    masya '"Программная инженерия"\n"Дизайн графических и пользовательских интерфейсов информационных систем"'
    masya '"Прикладная информатика в компьютерном дизайне"\n"Информационные технологии в дизайне"\n"Разработка и дизайн веб-приложений" и другие.'
    call return_to_asking(ind) from _call_return_to_asking
    return

label ask_scores(ind):
    call change_mood(1, True) from _call_change_mood_1
    main_character "Сколько баллов понадобиться, чтобы поступить на подходящее для этой профессии направление?"
    masya "Проходной балл зависит от вуза и профиля подготовки, от количества претендентов на одно место, престижности учебного заведения и даже от его географического положения."
    call return_to_asking(ind) from _call_return_to_asking_1
    return

label ask_attraction(ind):
    call change_mood(1, True) from _call_change_mood_2
    main_character "Почему ты выбрал именно эту профессию? Чем она тебя зацепила?"
    masya "Потому что она не только очень востребованная, но и очень творческая! Я могу выражать себя и помогать тем самым другим."
    call return_to_asking(ind) from _call_return_to_asking_2
    return
