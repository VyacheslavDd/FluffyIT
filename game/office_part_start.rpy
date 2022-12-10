label office_part:
    window show
    main_character "Что? Где я? Куда я вообще [variations[7]]?"
    show cat_boss at very_right_transform with moveinright
    if mood_level < 5:
        call change_mood(-1, False) from _call_change_mood_10
        show emwhat at left_transform with move
        show oh_my_gosh at left_transform
        hide emwhat
        boss_cat "Ты кто еще [variations[8]]? Еще и выглядишь хмуро. [variations[9]] на вакансию сисадмина чтобы взломать нас?"
    else:
        call change_mood(1, True) from _call_change_mood_11
        show emwhat at left_transform with move
        show oh_my_gosh at left_transform
        hide emwhat
        boss_cat "Так-так, [variations[10]]! Выглядишь дружелюбно. Нам такие нужны. На какую вакансию претендуешь?"
    
    show sad at left_transform
    hide oh_my_gosh
    main_character "Если честно, я совсем не понимаю, про какую вакансию вы говорите. Кто Вы, и как я сюда [variations[7]]?"
    boss_cat 'Что за вопрос? Ты находишься в крупнейшей IT компании "Симпл Котинг", а я ее главный директор. Уж не знаю, как ты тут [variations[11]], но если ты уже здесь, то значит не зря!'

    if mood_level < 5:
        main_character "Очень даже зря! У меня даже нет знаний в этой сфере..."
    else:
        show neutral at left_transform
        hide sad
        main_character "Мне что-то нужно делать? Я ведь ничего не умею..."

    boss_cat "О, у нас как раз есть один такой стажёр. Тоже ничего не знает и ничего не умеет. Ему и будешь помогать."
    hide sad
    show emwhat at left_transform
    main_character "Так если ни он, ни я ничего не умеем, как мы справимся?"
    boss_cat "Вам поможет Мурка, моя ассистентка. Она занимается подбором персонала и отслеживает успехи стажёров. Вот и она, следуйте за ней! А я с Вами прощаюсь."
    hide cat_boss with moveoutright
    show cat_secretary at right_transform with moveinright
    murka "Приветик! Я отведу тебя к Масе, тому самому стажеру. Он не такой уж и глупый, как рассказывал тебе о нем директор, но помощь твоя ему точно не помешает."
    hide oh_my_gosh
    hide neutral
    show emwhat at very_left_transform with move
    show happy_cat at front_transform with moveinright
    show cat_secretary at very_right_transform with move
    show neutral at very_left_transform
    hide emwhat
    masya "Чего вы тут про меня шепчитесь? Это мой новый напарник? Ну наконец-то, теперь работа пойдет как по маслу!"
    murka "Отлично, тогда вот ваше первое совместное задание. Вы должны переделать сайт для нашего заказчика, для этого свяжитесь с ним и обговорите все ньюансы."
    hide cat_secretary with moveoutright
    hide happy_cat with slowdissolve
    hide neutral with slowdissolve
    show class_room with slowdissolve
    show happy_cat at right_transform with slowdissolve
    show neutral at left_transform with slowdissolve
    main_character "А что у тебя за профессия такая, сайты переделывать?"
    masya "Я пришел на должность веб-дизайнера, очень надеюсь что у меня получится!"
    hide happy_cat
    show neutral_cat at right_transform
    
    jump start_asking
    return