# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.geo_category import GeoCategory
from models.rus_total import RusTotal
from models.district import District
from models.territorial_unit import TerritorialUnit

engine = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

categories = [('Страна', 'Country'),
              ('Округ', 'District'),
              ('Республика', 'Republic'),
              ('Край', 'Territories'),
              ('Автономный округ', 'Autonomous Area '),
              ('Область', 'Region'),
              ('Автономная область', 'Autonomous Region'),
              ('Город федерального значения', 'City'),
              ]

# Добавляем виды территориального деления
for category in categories:
    gc = GeoCategory(category[0], category[1])
    session.add(gc)

# Добавляем РФ
session.add(RusTotal('Российская Федерация', 'Russian Federation', 1))

districts = [('Центральный федеральный округ', 'Central Federal District', 'ЦФО', 'CFD'),
             ('Северо-Западный федеральный округ', 'Northwestern Federal District', 'СЗФО', 'NW-FD'),
             ('Южный федеральный округ', 'Southern Federal District', 'ЮФО', 'SFD'),
             ('Северо-Кавказский федеральный округ', 'North Caucasus Federal District', 'СКФО', 'NCD'),
             ('Приволжский федеральный округ', 'Privolzhsky Federal District', 'ПФО', 'PFD'),
             ('Уральский федеральный округ', 'Urals Federal District', 'УФО', 'UFD'),
             ('Сибирский федеральный округ', 'Siberian Federal District', 'СФО', 'SibFD'),
             ('Дальневосточный федеральный округ', 'Fareast Federal District', 'ДФО', 'FED')]

# Добавляем округа
for district in districts:
    ds = District(district[0], district[1], district[2], district[3], 1, 2)
    session.add(ds)

territorial_units = [

    ("Белгородская область", "Belgorod Region", 1, 6),
    ("Брянская область", "Bryansk Region", 1, 6),
    ("Владимирская область", "Vladimir Region", 1, 6),
    ("Воронежская область", "Voronezh Region", 1, 6),
    ("Ивановская область", "Ivanovo Region", 1, 6),
    ("Калужская область", "Kaluga Region", 1, 6),
    ("Костромская область", "Kostroma Region", 1, 6),
    ("Курская область", "Kursk Region", 1, 6),
    ("Липецкая область", "Lipetsk Region", 1, 6),
    ("Московская область", "Moscow Region", 1, 6),
    ("Орловская область", "Orel Region", 1, 6),
    ("Рязанская область", "Ryazan Region", 1, 6),
    ("Смоленская область", "Smolensk Region", 1, 6),
    ("Тамбовская область", "Tambov Region", 1, 6),
    ("Тверская область", "Tver Region", 1, 6),
    ('Тверская область', "Tula Region", 1, 6),
    ("Ярославска область", "Yaroslavl Region", 1, 6),
    ("Москва", "Moscow", 1, 8),

    ('Республика Карелия', 'Republic of Karelia', 2, 3),
    ('Республика Коми', 'Kodi Republic', 2, 3),
    ('Архангельская область', 'Arkhangelsk Region', 2, 6),
    ('Ненецкий автономный округ', 'Nenets Autonomous Area', 2, 5),
    ('Вологодская область', 'Vologda Region', 2, 6),
    ('Калининградская область', 'Kaliningrad Region', 2, 6),
    ('Ленинградская область', 'Leningrad Region', 2, 6),
    ('Мурманская область', 'Murmansk Region', 2, 6),
    ('Новгородская область', 'Novgorod Region', 2, 6),
    ('Псковская область', 'Pskov Region', 2, 6),
    ('Санкт-Петербург', 'St Petersburg', 2, 8),

    ('Республика Адыгея', 'Republic of Adygea', 3, 3),
    ('Республика Калмыкия', 'Republic of Kalmykia', 3, 3),
    ('Республика Крым', 'Republic of Crimea', 3, 3),
    ('Краснодарский край', 'Krasnodar Territory', 3, 4),
    ('Астраханская область', 'Astrakhan Region', 3, 6),
    ('Волгоградская область', 'Volgograd Region', 3, 6),
    ('Ростовская область', 'Rostov Region', 3, 6),
    ('Севастополь', 'City of Sevastopol', 3, 8),

    ('Республика Дагестан', 'Republic of Dagestan', 4, 3),
    ('Республика Ингушетия', 'Republic of Ingushetia', 4, 3),
    ('Кабардино-Балкарская Республика', 'Kabardino-Balkarian Republic', 4, 3),
    ('Карачаево-Черкесская Республика', 'Karachayevo-Circassian Republic', 4, 3),
    ('Республика Северная Осетия — Алания', 'Republic of North Ossetia – Alania', 4, 3),
    ('Чеченская Республика', 'Chechen Republic', 4, 3),
    ('Ставропольский край', 'Stavropol Territory', 4, 4),

    ("Республика Башкортостан", "Republic of Bashkortostan", 5, 3),
    ("Республика Марий Эл", "Republic of Mari El", 5, 3),
    ("Республика Мордовия", "Republic of Mordovia", 5, 3),
    ("Республика Татарстан", "Republic of Tatarstan", 5, 3),
    ("Удмуртская Республика", "Republic of Udmurtia", 5, 3),
    ("Чувашская Республика", "Chuvash Republic", 5, 3),
    ("Пермский край", "Perm Territory", 5, 4),
    ("Кировская область", "Kirov Region", 5, 6),
    ("Нижегородская область", "Nizhny Novgorod Region", 5, 6),
    ("Оренбургская область", "Orenburg Region", 5, 6),
    ("Пензенская область", "Penza Region", 5, 6),
    ("Самарская область", "Samara Region", 5, 6),
    ("Саратовская область", "Saratov Region", 5, 6),
    ("Ульяновская область", "Ulyanovsk Region", 5, 6),

    ("Курганская область", "Kurgan Region", 6, 6),
    ("Свердловская область", "Sverdlovsk Region", 6, 6),
    ("Тюменская область", "Tyumen Region", 6, 6),
    ("Ханты-Мансийский автономный округ — Югра", "Khanty-Mansi Autonomous Area – Yugra", 6, 5),
    ("Ямало-Ненецкий автономный округ", "Yamalo-Nenets Autonomous Area", 6, 5),
    ("Челябинская область", "Chelyabinsk Region", 6, 6),

    ("Республика Алтай", "Altai Republic", 7, 3),
    ("Республика Тыва", "Tuva Republic", 7, 3),
    ("Республика Хакасия", "Khakassia Republic", 7, 3),
    ("Алтайский край", "Altai Territory", 7, 4),
    ("Красноярский край", "Krasnoyarsk Territory", 7, 4),
    ("Иркутская область", "Irkutsk Region", 7, 6),
    ("Кемеровская область", "Kemerovo Region", 7, 4),
    ("Новосибирская область", "Novosibirsk Region", 7, 6),
    ("Омская область", "Omsk Region", 7, 6),
    ("Томская область", "Tomsk Region", 7, 6),

    ("Республика Бурятия", "Republic of Buryatia", 8, 3),
    ("Республика Саха (Якутия)", "Republic of Sakha (Yakutia)", 8, 3),
    ("Забайкальский край", "Transbaikal Territory", 8, 4),
    ("Камчатский край", "Kamchatka Territory", 8, 4),
    ("Приморский край", "Primorsky Territory", 8, 4),
    ("Хабаровский край", "Khabarovsk Territory", 8, 4),
    ("Амурская область", "Amur Region", 8, 6),
    ("Магаданская область", "Magadan Region", 8, 6),
    ("Сахалинская область", "Sakhalin Region", 8, 6),
    ("Еврейская автономная область", "Jewish Autonomous Region", 8, 7),
    ("Чукотский автономный округ", "Chukotka Autonomous Area", 8, 5)
]

# Добавляем Регионы
for unit in territorial_units:
    ter = TerritorialUnit(unit[0], unit[1], unit[2], unit[3])
    session.add(ter)

session.commit()
session.close()
