label show_dialog_second:
    show screen second_customer_talk
    show cat_restaurant onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    return

label hide_dialog_second:
    hide screen second_customer_talk
    hide cat_restaurant onlayer screens
    hide happy_cat onlayer screens
    return

label second_task:
    show restaurant_f
    call show_customer("gui/nvl.png", "Котик-Ресторатор", "#ec043d") from _call_show_customer_1
    hide restaurant_f
    call show_dialog_second from _call_show_dialog_second
    play sound t1
    restaurant_cat "{cps=60}Доброго времени суток! Я очень занята, нету времени все подробно описывать.{/cps}"
    play sound t1
    restaurant_cat "{cps=71}Скажем так, мы специально сделали сайт, чтобы клиенты могли пользоваться доставкой, но за два месяца ее заказали всего 3 раза.{/cps}"
    play sound t1
    restaurant_cat "{cps=45}Надеюсь вы сумеете исправить это. Жду вашей работы.{/cps}"
    play sound t3
    masya "{cps=19}Приветствую! Все будет сделано в лучшем виде. Ждем ссылку на ваш сайт.{/cps}"
    show screen show_image("broken_menu")
    call hide_dialog_second from _call_hide_dialog_second
    main_character "Хм... Я не вижу ни слова про доставку на этом сайте."
    masya "Я тоже ничего не могу найти... Займешься этим, пока я доделываю свои старые работы?"
    
    menu:
        "\"{size=30}И что же мне ответить?{/size}\""
        "Конечно, я с радостью помогу тебе!":
            jump do_help
        "Ой... Как-то мне лень...":
            jump refuse_help
        "Может, лучше поступим наоборот? Я постараюсь доделать твои сайты, а ты поможешь нашему клиенту.":
            jump think_twice

    return

label do_help:
    call change_skill(1, True) from _call_change_skill_2
    masya "Спасибо. Ты настоящий друг. Тогда за работу!"
    call change_mood(1, True) from _call_change_mood_12
    main_character "Уже начинаю!"
    jump start_work
    return

label refuse_help:
    call change_skill(-1, False) from _call_change_skill_3
    play sound bad_sound
    show serious_cat at front_transform with vpunch
    masya "Хэй, тут не место лентяям. Мы должны ответственно относиться к своей работе!"
    masya "Прости, но тебе все же придется сделать это."
    call change_mood(-1, False) from _call_change_mood_13
    hide serious_cat
    main_character "Видимо у меня изначально не было выбора..."
    jump start_work
    return

label think_twice:
    masya "Хм, подумай хорошо. Дорабатывать сайты, созданные с нуля, довольно непростая работа."

    menu:
        "\"{size=30}И всё же, чем я займусь...{/size}\""
        "Найти доставку на сайте заказчика.":
            jump start_work
        "Доделать работы Маси":
            jump finish_masya_task
    return

label finish_masya_task:
    hide screen show_image
    scene black with very_slow_dissolve
    "Проходит какое-то время..."
    show class_room with slowdissolve
    show happy at front_transform with slowdissolve
    call change_skill(1, True) from _call_change_skill_4
    main_character "Мася, я все [variations[13]]. Ты уже нашел источник проблемы?"
    hide happy
    show emwhat at front_transform
    masya "...Ой, я немного уснул. Боюсь, тебе придется самому поискать его, иначе мы совсем ничего не успеем."
    hide emwhat
    show sad at front_transform
    main_character "Видимо у меня изначально не было выбора..."
    hide sad
    jump start_work
    return

label start_work:
    show neutral at front_transform
    hide screen show_image
    main_character "Хм, с какого бы раздела сайта начать?"
    menu:
        "\"{size=30}Хм, с какого бы раздела сайта начать?{/size}\""
        "Наши адреса":
            call afraid_that_nothing from _call_afraid_that_nothing
        "Отзывы":
            call afraid_that_nothing from _call_afraid_that_nothing_1
        "Меню":
            jump rest_menu
        "Контакты":
            jump contacts
        "Акции":
            jump discounts
    return

label afraid_that_nothing(previous_label=None):
    main_character "Боюсь, что тут нет ничего, связанного с доставкой...."
    if previous_label is None:
        jump start_work
    else:
        menu:
            "\"{size=30}А теперь что?{/size}\""
            "Вернуться к главному меню":
                jump start_work
            "Вернуться к подразделам":
                $renpy.jump(previous_label)
    return

label contacts:
    $jump_to = "contacts"
    menu:
        "\"{size=30}Какой раздел?{/size}\""
        "Наш персонал":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_2
        "Наши соцсети":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_3
        "Телефоны":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_4
    return

label rest_menu:
    $jump_to = "rest_menu"
    menu:
        "\"{size=30}Какой раздел?{/size}\""
        "Горячее":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_5
        "Десерты":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_6
        "Супы":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_7
        "Закуски":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_8
        "Напитки":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_9
    return

label discounts:
    $jump_to = "discounts"
    menu:
        "\"{size=30}Какой раздел?{/size}\""
        "Для именинников":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_10
        "Комбо-наборы":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_11
        "Сезонные акции":
            call afraid_that_nothing(jump_to) from _call_afraid_that_nothing_12
        "Доставка при заказе от 299 рублей!!!":
            jump found_site
    return

label working_rest_menu:
    menu:
        "\"{size=30}Что попробую заказать?{/size}\""
        "Горячее":
            call what_chosen("Фаршированный овощами цыпленок\n590р") from _call_what_chosen
        "Десерты":
            call what_chosen("Наполеон\n400р") from _call_what_chosen_1
        "Супы":
            call what_chosen("Суп с лапшой и курицей\n350р") from _call_what_chosen_2
        "Закуски":
            call what_chosen('салат "Цезарь"\n300р') from _call_what_chosen_3
        "Напитки":
            call what_chosen("Самодельный лимонад 1 литр\n320р") from _call_what_chosen_4
    return

label what_chosen(food):
    main_character "Т-а-а-к... Выберу вот это..."
    main_character "'[food]'"
    jump after_choosing
    return

label found_site:
    call change_skill(True, 5) from _call_change_skill_5
    main_character "Ну наконец-то [variations[14]]!!! Это было сложно... Теперь-то я понимаю, почему никто не заказывал доставку."
    main_character "Теперь нужно попробовать ее заказать самому."
    jump working_rest_menu
    return

label after_choosing:
    hide neutral
    show emwhat at front_transform
    main_character "Ну, вроде бы товар [variations[15]], а где же корзина?..."
    main_character "Как мне оплатить товар? Видимо от доставки тут только ее упоминание..."
    main_character "Надо сказать об этом Масе."
    hide emwhat
    show neutral at front_transform
    main_character "Мася, мне кажется, тут в принципе нет доставки, с этим нужно что-то сделать."
    show neutral at left_transform with move
    show happy_cat at right_transform with moveinright
    masya "Будет готово! Ты [variations[19]] молодец, задание выполнено на отлично!"
    hide neutral with moveoutleft
    hide happy_cat with moveoutright
    show screen show_image("repaired_menu") with very_slow_dissolve
    masya "Красота..."
    hide screen show_image
    show screen second_customer_talk
    show cat_restaurant onlayer screens at left_transform
    show happy onlayer screens at right_transform
    play sound t1
    restaurant_cat "{cps=60}Благодарю вас! Заказов стало гораздо больше. Я порекомендую вас своим знакомым.{/cps}"
    play sound t3
    main_character "{cps=15}Всегда рады помочь! Тем более за такую хорошую рекламу.{/cps}"
    hide cat_restaurant onlayer screens with slowdissolve
    hide happy onlayer screens with slowdissolve
    hide screen second_customer_talk with slowdissolve
    show cat_secretary at very_left_transform with moveinleft
    nvl show dissolve
    masya_nvl "{color=#12e2e6}Мурка{/color}: {color=#e6d712}Запомните, то, насколько просто и понятно можно передвигаться по сайту — очень важно.{/color}"
    masya_nvl "{color=#e6d712}Простая навигация положительно сказывается на месте в поисковиках.{/color}"
    masya_nvl "{color=#e6d712}Какой должна быть хорошая навигация на сайте? Вот ее основные характеристики:{/color}"
    nvl clear
    masya_nvl "·{b}Ясность{/b}. Необходимо, чтобы все составляющие меню или пользовательского интерфейса хорошо просматривались и были понятны любому на интуитивном уровне.\nВ идеале на любую страницу или раздел на сайте пользователь должен сделать 3 клика;"
    masya_nvl "·{b}Доступность на любой странице веб-сайта{/b}. На каждой странице должны присутствовать тщательно проработанные элементы навигации.\nЭто дает посетителю возможность перейти из любого раздела туда, куда он хочет;"
    masya_nvl "·{b}Продуманное визуальное оформление{/b}. Элементы навигации должны контрастировать с фоном и основным текстом, но не выбиваться из общего цветового решения веб-ресурса."
    nvl clear
    nvl hide dissolve
    hide cat_secretary
    show happy at front_transform with slowdissolve
    main_character "Учтем это в следующих наших работах!"
    hide happy
    show neutral_cat at front_transform with slowdissolve
    masya "Это задание оказалось куда сложнее, чем я думал. Мы отлично справились!"
    masya "Надеюсь тебе нравится, то, что мы делаем?"
    hide neutral_cat
    show neutral at front_transform

    menu:
        "\"{size=30}Пора задуматься...{/size}\""
        "Думаю, что да. Меня действительно заинтересовала наша с тобой работа.":
            call answer_if_interesting(True, 1, "Это прелестно. Я рад, что смог привить тебе любовь к своей профессии.") from _call_answer_if_interesting
        "Честно говоря, я делаю это все только потому, что у меня нет другого выбора.":
            call answer_if_interesting(False, -1, "Жалко, что у тебя такой настрой. Возможно, это просто не твое. Однако мне моя работа очень даже по душе.") from _call_answer_if_interesting_1
    return

label answer_if_interesting(is_pos_mood, value, masya_answer):
    call change_mood(value, is_pos_mood) from _call_change_mood_14
    hide neutral
    show neutral_cat at front_transform
    masya "[masya_answer]"
    masya "Мне уже пишет новый клиент."
    masya "Давай посмотрим, что там!"
    hide neutral_cat
    jump third_task
    return

