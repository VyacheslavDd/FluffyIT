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
    hide screen show_image
    show neutral at front_transform
    
    menu:
        "И что же мне ответить?"
        "Конечно, я с радостью помогу тебе!":
            jump do_help
        "Ой... Как-то мне лень...":
            jump refuse_help
        "Может, лучше поступим наоборот? Я постараюсь доделать твои сайты, а ты поможешь нашему клиенту.":
            jump think_twice

    return

label do_help:
    call change_skill(1, True)
    hide neutral
    show happy_cat at front_transform
    masya "Спасибо. Ты настоящий друг. Тогда за работу!"
    call change_mood(1, True)
    hide happy_cat
    show happy at front_transform
    main_character "Уже начинаю!"
    hide happy
    jump start_work
    return

label refuse_help:
    call change_skill(-1, False)
    hide neutral
    show serious_cat at front_transform with vpunch
    masya "Хэй, тут не место лентяям. Мы должны ответственно относиться к своей работе!"
    masya "Прости, но тебе все же придется сделать это."
    call change_mood(-1, False)
    hide serious_cat
    show sad at front_transform
    main_character "Видимо у меня изначально не было выбора..."
    hide sad
    jump start_work
    return

label think_twice:
    hide neutral
    show what_cat at front_transform
    masya "Хм, подумай хорошо. Дорабатывать сайты, созданные с нуля, довольно непростая работа."

    menu:
        "И всё же, чем я займусь..."
        "Найти доставку на сайте заказчика.":
            jump start_work
        "Доделать работы Маси":
            pass
    return

label start_work:
    show emwhat at front_transform
    main_character "Хм, с какого бы раздела сайта начать?"
    return