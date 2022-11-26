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
        return check_if_appropriate_value(skill_level, 0, 5)

screen title_screen():
    frame:
        xalign 0.5
        yalign 0.3
        background None
        text "{b}Выберите пол главного героя{/b}:":
            slow_cps 20
            underline True
            bold True
            italic True
            size 30

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
            value VariableValue("skill_level", 5)


screen phone_screen():
    imagemap:
        ground "images/scenes/hall.png"
        idle "images/scenes/hall.png"
        hover "images/scenes/hall.png"
        hotspot(0, 0, 1280, 720):
            action Jump("playing_phone")


screen playing_screen():
    frame:
        xsize 1280
        ysize 720
        add "images/scenes/nighthall.png"
        background None


screen unfinished_flower_website():
    frame:
        xsize 1280
        ysize 720
        add "images/scenes/bosscabinet.png"


screen finished_flower_website():
    frame:
        xsize 1280
        ysize 720
        add "images/scenes/schoolhall.png"


screen first_customer():
    timer 4.0 action Hide("first_customer")
    frame:
        xsize 1280
        ysize 720
        add "gui/nvl.png"
        background None

        text "Новый заказчик:":
            color "#9ee2de"
            size 50
            xalign 0.5
            yalign 0.1

        text "Котик-Садовод":
            color "#2ea40d"
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
define kindegarten_cat = Character("Садовод", color="#149e09")
define mood_level = 5
define skill_level = 2
define bar_part = "yellow_left"
define is_boy = True
define bv = ["определился", "сынок", "Такой", "большой стал", "стал", "нервным", "сделал", "попал", "такой", "пришёл", "новенький", "оказался", "видел"]
define gv = ["определилась", "дочка", "Такая", "большая стала", "стала", "нервной", "сделала", "попала", "такая", "пришла", "новенькая", "оказалась", "видела"]


image neutral = "[img_prefix]_neutral"
image angry = "[img_prefix]_angry"
image emwhat = "[img_prefix]_emwhat"
image happy = "[img_prefix]_happy"
image sad = "[img_prefix]_sad"
image wow = "[img_prefix]_wow"
image oh_my_gosh = "[img_prefix]_omg"
image sunny_street = "street"
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