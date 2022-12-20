init python:
    def check_if_appropriate_value(current_value, min_value, max_value):
        if current_value > max_value:
            current_value = max_value
        if current_value < min_value:
            current_value = min_value
        return current_value

    def update_mood(mood_level, value):
        mood_level += value
        mood_level = check_if_appropriate_value(mood_level, 0, 10)
        return ("red_left" if mood_level < 5 else ("yellow_left" if mood_level < 8 else "green_left"), mood_level)

    def update_skill(skill_level, value):
        skill_level += value
        return check_if_appropriate_value(skill_level, 0, 10)

    def change_variants(variants, ind):
        del variants[int(ind)]
        for i, elem in enumerate(variants):
            elem[1] = elem[1][:-1] + str(i)
        return variants


screen the_ending(ending_description):
    frame:
        xsize 1280
        ysize 720
        add Solid("#000000", xsize=1280, ysize=720)
        background None
        text "Конец.":
            color "#0fb8db"
            size 60
            xalign 0.5
            yalign 0.5
        text '"ПУШИСТЫЕ IT"':
            color "#ede115"
            size 50
            xalign 0.5
            yalign 0.1
        text "[ending_description]":
            color "#b5c9cd"
            size 35
            xalign 0.5
            yalign 0.8


screen title_screen():
    frame:
        xalign 0.5
        yalign 0.3
        background None
        text "{b}Выберите пол главного героя{/b}:":
            color "#3b3e03"
            slow_cps 25
            bold True
            italic True
            size 30

screen virus1(is_interaction):
    use virus("virus1", is_interaction, 150, 10)

screen virus2(is_interaction):
    use virus("virus2", is_interaction, 550, 280)

screen virus3(is_interaction):
    use virus("virus3", is_interaction, 900, 550)

screen virus4(is_interaction):
    use virus("virus4", is_interaction, 0, 400)

screen virus5(is_interaction):
    use virus("virus5", is_interaction, 950, 100)

screen virus(parent_name, is_interaction, x_align, y_align):
    default n = 5
    frame:
        xpos x_align
        ypos y_align
        background None

        imagebutton:
            idle "sized_virus"
            if is_interaction:
                if n - 1 == 0:
                    action [Hide(parent_name), SetVariable("killed", killed + 1), Show("dead_virus", None, x_align, y_align), Notify("Ликвидирован!")]
                if n - 1 > 0:
                    action [SetLocalVariable("n", n - 1), Notify("Осталось нанести {0} {1}!".format(n - 1, "удара" if n - 1 != 1 else "удар"))]
            else:
                action None

screen dead_virus(x_align, y_align):
    if killed == 5:
        timer 1.0 action [Hide(), Jump("continue_after_cleaning")]
    else:
        timer 1.0 action Hide()
    frame:
        xpos x_align
        ypos y_align
        background None
        add "images/virus/virusdead_sized.png"

screen remained_answers():
    frame:
        xalign 0.0
        yalign 0.0
        background None
        text "Осталось правильных ответов: [correct_variants]":
            size 30
            color "#10ceec"

screen choose_character():
    use title_screen()
    use character(0, "boy_neutral", "boy_happy", "boy")
    use character(0.95, "girl_neutral", "girl_happy", "girl")

screen character(row_align, image_idle, image_hover, move_to_label):
    frame:
        xalign row_align
        yalign 0.95
        background None

        imagebutton:
            idle image_idle
            hover image_hover
            action Jump(move_to_label)


screen mood():
    timer 3.0 action Hide("mood")
    frame:
        xalign 0
        yalign 0
        xsize 100
        background "#282828"
        bar:
            left_bar "gui/bar/[bar_part].png"
            right_bar "gui/bar/right.png"
            value VariableValue("mood_level", 10)


screen skill():
    timer 3.0 action Hide("skill")
    frame:
        xpos 1180 
        ypos 0
        xsize 100
        background "#980795"
        bar:
            left_bar "gui/bar/purple_left.png"
            right_bar "gui/bar/right.png"
            value VariableValue("skill_level", 10)


screen viewport_ex(x_pos, y_pos, _id, scene_pic_name):
    side "c":
        area(x_pos, y_pos, 640, 720)
        viewport id _id:
            draggable False
            add "images/scenes/[scene_pic_name].png"


screen show_image(scene_pic_name):
    add "images/scenes/[scene_pic_name].png"


screen first_customer_talk():
    use viewport_ex(0, 0, "one", "kinden")
    use viewport_ex(640, 0, "two", "class")


screen second_customer_talk():
    use viewport_ex(0, 0, "one", "rest")
    use viewport_ex(640, 0, "two", "class")

screen third_customer_talk():
    use viewport_ex(0, 0, "one", "laboratory")
    use viewport_ex(640, 0, "two", "class")

screen last_customer_talk():
    use viewport_ex(0, 0, "one", "Anon_bg")
    use viewport_ex(640, 0, "two", "class")

screen phone_screen():
    imagemap:
        ground "images/scenes/phone_main.png"
        idle "images/scenes/phone_main.png"
        hover "images/scenes/phone_main.png"
        hotspot(550, 327, 71, 71):
            action Jump("playing_phone")


screen customer_notification(picture, customer_name, customer_color):
    timer 4.0 action Hide("customer_notification")
    frame:
        xsize 1280
        ysize 720
        add "[picture]"
        background None

        text "Новый заказчик:":
            color "#9ee2de"
            size 50
            xalign 0.5
            yalign 0.1

        text customer_name:
            color customer_color
            size 70
            yalign 0.5
            xalign 0.5

transform front_transform:
    xalign 0.5
    yalign 0.4

transform left_transform:
    xalign 0.2
    yalign 0.4

transform right_transform:
    xalign 0.8
    yalign 0.4

transform very_left_transform:
    xalign 0.05
    yalign 0.4

transform touching_left_transform:
    xalign 0
    yalign 0.4

transform very_right_transform:
    xalign 0.95
    yalign 0.4
  
define main_character_name = "Денис"
define img_prefix = "boy"
define slowdissolve = Dissolve(1.5)
define very_slow_dissolve = Dissolve(3.5)
define main_character = Character("[main_character_name]", color="#b406de")
define mum = Character("Мама", color="#0a30f0")
define boss_cat = Character("Василий Мяукович", color="#597e0e")
define murka = Character("Мурка", color="#c30f8a")
define masya = Character("Мася", color="#b2c601")
define masya_nvl = Character(None, color="#8e450c", kind=nvl)
define kindegarten_cat = Character("Садовод", color="#149e09")
define restaurant_cat = Character("Ресторатор", color="#ec043d")
define science_cat = Character("Учёный", color="#4f3fe2")
define anonymous_cat = Character("Аноним", color="#4b5457")
define mood_level = 5
define skill_level = 2
define bar_part = "yellow_left"
define is_boy = True
define bv = ["определился", "сынок", "Такой", "большой стал", "стал", "нервным", "сделал", "попал", "такой", "пришёл", "новенький", "оказался", "видел", "сделал", "нашёл",
"выбрал", "Уверен", "помог", "понял", "огромный"]
define gv = ["определилась", "дочка", "Такая", "большая стала", "стала", "нервной", "сделала", "попала", "такая", "пришла", "новенькая", "оказалась", "видела", "сделала", "нашла",
"выбрала", "Уверена", "помогла", "поняла", "огромная"]

define audio.bad_sound = "sounds/smh_bad.mp3"
define audio.punch_door = "sounds/door_punch.mp3"
define audio.t1 = "sounds/t1.mp3"
define audio.t2 = "sounds/t2.mp3"
define audio.t3 = "sounds/t3.mp3"
define audio.t4 = "sounds/t4.mp3"
define audio.t5 = "sounds/t5.mp3"
define audio.t6 = "sounds/t6.mp3"
define audio.info_type = "sounds/info_type.mp3"

image neutral = "[img_prefix]_neutral"
image cat_kindegarten = "kindegarten"
image cat_boss = "boss"
image cat_restaurant = "restaurant"
image cat_secretary = "secretary"
image cat_science = "scientist"
image cat_anon = "anon_cat"
image angry = "[img_prefix]_angry"
image emwhat = "[img_prefix]_emwhat"
image happy = "[img_prefix]_happy"
image sad = "[img_prefix]_sad"
image wow = "[img_prefix]_wow"
image oh_my_gosh = "[img_prefix]_omg"
image sunny_street = "street"
image lab = "lab_full"
image anon_room = "anon_bg"
image restaurant_f = "rest_full"
image kinden_f = "kind_full"
image pretty_kitchen = "kitchen"
image class_room = "class"
image room = "[img_prefix]sroom"
image dream_office = "office"
image neutral_cat = "cat_neutral"
image serious_cat = "cat_serious"
image happy_cat = "cat_happy"
image mur_cat = "cat_mur"
image oneeye_cat = "cat_oneeye"
image sad_cat = "cat_sad"
image what_cat = "cat_what"
image mom = "mom([img_prefix])"
image black = "#000000"