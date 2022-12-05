label second_task:
    show sunny_street
    call show_customer("gui/nvl.png", "Котик-Ресторатор", "#ec043d")
    hide sunny_street
    show screen second_customer_talk
    show serious_cat onlayer screens at left_transform with slowdissolve
    show happy_cat onlayer screens at right_transform with slowdissolve
    restaurant_cat "Доброго времени суток! Я очень занята, нету времени все подробно описывать."
    restaurant_cat "Скажем так, мы специально сделали сайт, чтобы клиенты могли пользоваться доставкой, но за два месяца ее заказали всего 3 раза."
    restaurant_cat "Надеюсь вы сумеете исправить это. Жду вашей работы."
    masya "Приветствую! Все будет сделано в лучшем виде. Ждем ссылку на ваш сайт."
    show screen show_image(1280, 720, 0, 0, "kitchen")
    hide screen second_customer_talk
    hide serious_cat onlayer screens
    hide happy_cat onlayer screens
    main_character "Хм... Я не вижу ни слова про доставку на этом сайте."
    masya "Я тоже ничего не могу найти... Займешься этим, пока я доделываю свои старые работы?"
    
    menu:
        "{size=30}И что же мне ответить?{/size}"
        "Конечно, я с радостью помогу тебе!":
            jump do_help
        "Ой... Как-то мне лень...":
            jump refuse_help
        "Может, лучше поступим наоборот? Я постараюсь доделать твои сайты, а ты поможешь нашему клиенту.":
            jump think_twice

    return

label do_help:
    call change_skill(1, True)
    masya "Спасибо. Ты настоящий друг. Тогда за работу!"
    call change_mood(1, True)
    main_character "Уже начинаю!"
    jump start_work
    return

label refuse_help:
    call change_skill(-1, False)
    show serious_cat at front_transform with vpunch
    masya "Хэй, тут не место лентяям. Мы должны ответственно относиться к своей работе!"
    masya "Прости, но тебе все же придется сделать это."
    call change_mood(-1, False)
    hide serious_cat
    main_character "Видимо у меня изначально не было выбора..."
    jump start_work
    return

label think_twice:
    masya "Хм, подумай хорошо. Дорабатывать сайты, созданные с нуля, довольно непростая работа."

    menu:
        "И всё же, чем я займусь..."
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
    call change_skill(1, True)
    main_character "Мася, я все [variations[13]]. Ты уже нашел источник проблемы?"
    hide happy
    show emwhat at front_transform
    masya "...Ой, я немного уснул. Боюсь, тебе придется самому поискать его, иначе мы совсем ничего не успеем."
    hide emwhat
    show sad at front_transform
    main_character "Видимо у меня изначально не было выбора..."
    hide sad
    show screen show_image(1280, 720, 0, 0, "kitchen")
    jump start_work
    return

label start_work:
    main_character "Хм, с какого бы раздела сайта начать?"
    menu:
        "{size=30}Хм, с какого бы раздела сайта начать?{/size}"
        "Наши адреса":
            call afraid_that_nothing
        "Отзывы":
            call afraid_that_nothing
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
            "{size=30}А теперь что?{/size}"
            "Вернуться к главному меню":
                jump start_work
            "Вернуться к подразделам":
                $renpy.jump(previous_label)
    return

label contacts:
    $jump_to = "contacts"
    menu:
        "{size=30}Какой раздел?{/size}"
        "Наш персонал":
            call afraid_that_nothing(jump_to)
        "Наши соцсети":
            call afraid_that_nothing(jump_to)
        "Телефоны":
            call afraid_that_nothing(jump_to)
    return

label rest_menu:
    $jump_to = "rest_menu"
    menu:
        "{size=30}Какой раздел?{/size}"
        "Горячее":
            call afraid_that_nothing(jump_to)
        "Десерты":
            call afraid_that_nothing(jump_to)
        "Супы":
            call afraid_that_nothing(jump_to)
        "Закуски":
            call afraid_that_nothing(jump_to)
        "Напитки":
            call afraid_that_nothing(jump_to)
    return

label discounts:
    $jump_to = "discounts"
    menu:
        "{size=30}Какой раздел?{/size}"
        "Для именинников":
            call afraid_that_nothing(jump_to)
        "Комбо-наборы":
            call afraid_that_nothing(jump_to)
        "Сезонные акции":
            call afraid_that_nothing(jump_to)
        "Доставка при заказе от 299 рублей!!!":
            jump found_site
    return

label working_rest_menu:
    menu:
        "{size=30}Что попробую заказать?{/size}"
        "Горячее":
            call what_chosen("Фаршированный овощами цыпленок\n590р")
        "Десерты":
            call what_chosen("Наполеон\n400р")
        "Супы":
            call what_chosen("Суп с лапшой и курицей\n350р")
        "Закуски":
            call what_chosen('салат "Цезарь"\n300р')
        "Напитки":
            call what_chosen("Самодельный лимонад 1 литр\n320р")
    return

label what_chosen(food):
    main_character "Т-а-а-к... Выберу вот это..."
    main_character "'[food]'"
    jump after_choosing
    return

label found_site:
    call change_skill(True, 5)
    main_character "Ну наконец-то [variations[14]]!!! Это было сложно... Теперь-то я понимаю, почему никто не заказывал доставку."
    main_character "Теперь нужно попробовать ее заказать самому."
    jump working_rest_menu
    return

label after_choosing:
    main_character "Ну, вроде бы товар [variations[15]], а где же корзина?..."
    main_character "Как мне оплатить товар? Видимо от доставки тут только ее упоминание..."
    main_character "Надо сказать об этом Масе."
    hide screen show_image
    show neutral at front_transform
    main_character "Мася, мне кажется, тут в принципе нет доставки, с этим нужно что-то сделать."
    show neutral at left_transform with move
    show happy_cat at right_transform with moveinright
    masya "Будет готово! Ты огромный молодец, задание выполнено на отлично!"
    hide neutral with moveoutleft
    hide happy_cat with moveoutright
    show screen show_image(1280, 720, 0, 0, "kitchen") with very_slow_dissolve
    masya "Красота..."
    hide screen show_image with very_slow_dissolve

    show mur_cat at very_left_transform with moveinleft
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
    hide mur_cat
    show happy at front_transform with slowdissolve
    main_character "Учтем это в следующих наших работах!"
    hide happy
    show neutral_cat at front_transform with slowdissolve
    masya "Это задание оказалось куда сложнее, чем я думал. Мы отлично справились!"
    masya "Надеюсь тебе нравится, то, что мы делаем?"
    hide neutral_cat
    show neutral at front_transform

    menu:
        "{size=30}Пора задуматься...{/size}"
        "Думаю, что да. Меня действительно заинтересовала наша с тобой работа.":
            call answer_if_interesting(True, 1, "Это прелестно. Я рад, что смог привить тебе любовь к своей профессии.")
        "Честно говоря, я делаю это все только потому, что у меня нет другого выбора.":
            call answer_if_interesting(False, -1, "Жалко, что у тебя такой настрой. Возможно, это просто не твое. Однако мне моя работа очень даже по душе.")
        
    return

label answer_if_interesting(is_pos_mood, value, masya_answer):
    call change_mood(is_pos_mood, value)
    hide neutral
    show neutral_cat at front_transform
    masya "[masya_answer]"
    masya "Мне уже пишет новый клиент."
    masya "Давай посмотрим, что там!"
    hide neutral_cat
    jump third_task
    return

