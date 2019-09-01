
default tt = Tooltip("")
define maxBitchness = 560
define maxBitchness_EP1 = 560
default monicaBitch = False
define m = Character(_("Моника Бакфетт"), who_color=c_orange, what_color=c_white, what_italic=False) #Monica
define mt = Character(kind=m, what_color=c_blue, what_italic=True) #Monica thinking
#define narrator = Character(kind=m)

define help = Character(_("HELP"), who_color=c_blue) #helper in intro
define julia = Character(_("Юлия"), who_color=c_pink) #Julia Governess
define fred = Character(_("Водитель Фред"), who_color=c_blue) #Fred
define neighbor = Character(_("Сосед"), who_color=c_green) #Neighbor
define gray_mouse = Character(_("Серая мышь"), who_color=c_gray) #Gray Mouse
define secretary = Character(_("Секретарша"), who_color=c_pink) #Monica Secretary
define secretary_t = Character(_("Секретарша"), who_color=c_pink, what_color=c_blue, what_italic=True) #Monica Secretary thinking
define steve = Character(_("Партнер Стив"), who_color=c_blue) #Parthner Steve
define model1 = Character(_("Кастинг модель 1"), who_color=c_pink) #Casting Model 1
define model2 = Character(_("Кастинг модель 2"), who_color=c_pink) #Casting Model 2
define alex_photograph = Character(_("Фотограф Алекс"), who_color=c_green) #Alex Photograph
define melanie = Character(_("Модель Мелани"), who_color=c_pink) #Melanie Model
define dick = Character(_("Дик Адвокат"), who_color=c_green) #Dick The Lawyer
define dick2 = Character(_("Дик Адвокат"), who_color=c_red) #Dick The Lawyer
define saleswoman = Character(_("Кристина"), who_color=c_pink) #Saleswoman
define saleswoman_boss = Character(_("Босс"), who_color=c_orange) #Saleswoman Boss
define cashier = Character(_("Продавщица"), who_color=c_pink) #Clothing Shop Saler
define waitress = Character(_("Официантка"), who_color=c_green) #Waitress
define bartender = Character(_("Бармен"), who_color=c_blue) #Bartender
define fitness_instructor = Character(_("Фитнесс-инструктор"), who_color=c_blue) #Fitness Instructor
define rebecca = Character(_("Ребекка"), who_color=c_green) #Rebecca
define stephanie = Character(_("Стефани"), who_color=c_pink) #Stephanie
define bank_clerk = Character(_("Банковский Клерк"), who_color=c_pink) #Bank Clerk
define jane = Character(_("Секретарша Джейн"), who_color=c_pink) #Jane Secretary
define tiffany = Character(_("Тиффани"), who_color=c_pink) #Tiffany
define mommy = Character(_("Мамочка"), who_color=c_red) #Mommy
define shawarma = Character(_("Продавец шавермы"), who_color=c_green) #Kebab saler
define marcus = Character(_("Маркус"), who_color=c_red) #Marcus
define husband = Character(_("Супруг"), who_color=c_green) #Husband
define policewoman = Character(_("Полицейская"), who_color=c_red) #Policewoman
define policeman = Character(_("Полицейский"), who_color=c_red) #Policeman
define policeman1 = Character(_("Полицейский 1"), who_color=c_red) #Policeman
define policeman2 = Character(_("Полицейский 2"), who_color=c_red) #Policeman
define detective = Character(_("Детектив"), who_color=c_red) #Detective
define overseer = Character(_("Надзиратель"), who_color=c_red) #Overseer
define prisoner = Character(_("Заключенный"), who_color=c_blue) #Prisoner
define prisoner1 = Character(_("Заключенный 1"), who_color=c_red) #Prisoner
define prisoner2 = Character(_("Заключенный 2"), who_color=c_red) #Prisoner
define prisoner3 = Character(_("Заключенный 3"), who_color=c_red) #Prisoner
define prisoner4 = Character(_("Заключенный 4"), who_color=c_red) #Prisoner
define prisoner5 = Character(_("Заключенный 5"), who_color=c_red) #Prisoner
define prisoner6 = Character(_("Заключенный 6"), who_color=c_red) #Prisoner
define judge = Character(_("Судья"), who_color=c_blue) #Judge
define reception_secretary = Character(_("Секретарь на рецепшине"), who_color=c_pink) #Reception Secretary
define reception_secretary_t = Character(_("Секретарь на рецепшине"), who_color=c_pink, what_color=c_blue, what_italic=True) #Reception Secretary
define reception = Character(_("Рецепшин Администратор"), who_color=c_pink) #Reception Administrator
define reception_t = Character(_("Рецепшин Администратор"), who_color=c_pink) #Reception Administrator
define house_guard = Character(_("Охранник"), who_color=c_red) #Guard
define dick_secretary = Character(_("Секретарша Дика"), who_color=c_red) #Dick Secretary
define perry = Character(_("Перри"), who_color=c_green) #Perry
define ralph = Character(_("Ральф Робертс"), who_color=c_green) #Ralph Roberts
define biff = Character(_("Биф"), who_color=c_blue) #biff
define betty = Character(_("Бетти Робертс"), who_color=c_pink) #Betty Roberts
define bardie = Character(_("Барди"), who_color=c_blue) #Bardie
define bardie_t = Character(_("Барди"), who_color=c_blue, what_color=c_blue, what_italic=True) #Bardie
define gas_boyfriend = Character(_("Бойфренд"), who_color=c_blue) #бойфренд девушки с заправки
define hotel_staff = Character(_("Сотрудник Отеля"), who_color=c_blue) #сотрудник отеля
define philip = Character(_("Филипп"), who_color=c_blue) #Philip
define empty_name = Character("", who_color=c_blue) #empty name

define reporter1 = Character(_("Репортер 1"), who_color=c_blue) #Reporter1
define reporter2 = Character(_("Репортер 2"), who_color=c_orange) #Reporter2
define reporter3 = Character(_("Репортер 3"), who_color=c_pink) #Reporter3

define citizen = Character(_("Незнакомец"), who_color=c_pink) #Stranger
define citizen1 = Character(_("Том"), who_color=c_pink) #Stranger
define citizen2 = Character(_("Тим"), who_color=c_pink) #Stranger
define citizen3 = Character(_("Джек"), who_color=c_orange) #Stranger
define citizen4 = Character(_("Незнакомец"), who_color=c_blue) #Stranger
define citizen5 = Character(_("Акира Сан"), who_color=c_blue) #Stranger
define citizen6 = Character(_("Фил"), who_color=c_blue) #Stranger
define citizen7 = Character(_("Сальвадор"), who_color=c_pink) #Stranger
define citizen8 = Character(_("Хитрый Джонни"), who_color=c_blue) #Stranger
define citizen9 = Character(_("Найджел"), who_color=c_green) #Stranger
define citizen10 = Character(_("Реджинальд"), who_color=c_blue) #Stranger
define citizen11 = Character(_("Саймон"), who_color=c_blue) #Stranger
define citizen12 = Character(_("Незнакомец"), who_color=c_green) #Stranger
define citizen13 = Character(_("Анджело"), who_color=c_pink) #Stranger
define citizen14 = Character(_("Василий"), who_color=c_orange) #Stranger
define citizen15 = Character(_("Френк"), who_color=c_blue) #Stranger

define ashley = Character(_("Эшли"), who_color=c_pink) # Барменша
define joe = Character(_("Джо"), who_color=c_blue) # Бармен

define sound_from_side = Character(_("Звук"), who_color=c_blue)

define cit1 = Character(_("Покупатель"), who_color=c_blue)
define cit2 = Character(_("Покупатель"), who_color=c_blue)
define cit3 = Character(_("Покупатель"), who_color=c_blue)
define cit4 = Character(_("Покупательница"), who_color=c_pink)
define cit5 = Character(_("Покупательница"), who_color=c_pink)
define cit6 = Character(_("Покупательница"), who_color=c_pink)
define cit7 = Character(_("Покупательница"), who_color=c_pink)
define cit8 = Character(_("Покупательница"), who_color=c_pink)
define cit9 = Character(_("Покупательница"), who_color=c_pink)
define cit10 = Character(_("Покупательница"), who_color=c_pink)


define w1 = Character(_("Марта"), who_color=c_pink)
define w1t = Character(_("Марта"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w2 = Character(_("Системный Администратор"), who_color=c_blue)
define w2t = Character(_("Системный Администратор"), who_color=c_blue, what_color=c_blue, what_italic=True)
define w3 = Character(_("Эмма"), who_color=c_pink)
define w3t = Character(_("Эмма"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w4 = Character(_("Элла"), who_color=c_pink)
define w4t = Character(_("Элла"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w5 = Character(_("Джон"), who_color=c_blue)
define w5t = Character(_("Джон"), who_color=c_blue, what_color=c_blue, what_italic=True)
define w6 = Character(_("Грета"), who_color=c_pink)
define w6t = Character(_("Грета"), who_color=c_pink, what_color=c_blue, what_italic=True)
define w7 = Character(_("Лин"), who_color=c_pink)
define w7t = Character(_("Лин"), who_color=c_pink, what_color=c_blue, what_italic=True)

define customer1 = Character(_("Посетитель"), who_color=c_blue)
define customer1t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer2 = Character(_("Посетитель"), who_color=c_blue)
define customer2t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer3 = Character(_("Посетитель"), who_color=c_blue)
define customer3t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer4 = Character(_("Посетитель"), who_color=c_blue)
define customer4t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer5 = Character(_("Посетитель"), who_color=c_blue)
define customer5t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer6 = Character(_("Посетитель"), who_color=c_blue)
define customer6t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer7 = Character(_("Посетитель"), who_color=c_blue)
define customer7t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer8 = Character(_("Посетитель"), who_color=c_blue)
define customer8t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer9 = Character(_("Посетитель"), who_color=c_blue)
define customer9t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer10 = Character(_("Посетитель"), who_color=c_blue)
define customer10t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer11 = Character(_("Посетитель"), who_color=c_blue)
define customer11t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)
define customer12 = Character(_("Посетитель"), who_color=c_blue)
define customer12t = Character(_("Посетитель"), who_color=c_blue, what_color=c_blue, what_italic=True)


#
