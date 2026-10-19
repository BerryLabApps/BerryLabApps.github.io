import pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "berrylab.app@gmail.com"

FIREBASE_LINK = ("Firebase", "Firebase", "https://firebase.google.com/support/privacy", "https://firebase.google.com/support/privacy")
RUSSIAN_AD_PARTNERS = [
    {"en": "Yandex Mobile Ads and Yandex AppMetrica", "ru": "Yandex Mobile Ads и Яндекс AppMetrica",
     "link": ("Yandex", "Яндекс", "https://yandex.com/legal/confidential/", "https://yandex.ru/legal/confidential/")},
    {"en": "VK Ads (myTarget and myTracker)", "ru": "VK Реклама (myTarget и myTracker)",
     "link": ("VK Ads", "VK Реклама", "https://help.mail.ru/legal/terms/adsvk/euprivacy/", "https://help.mail.ru/legal/terms/adsvk/privacy/")},
]
ADMOB = {"en": "Google AdMob", "ru": "Google AdMob",
         "link": ("Google", "Google", "https://policies.google.com/technologies/partner-sites", "https://policies.google.com/technologies/partner-sites?hl=ru")}
MINTEGRAL = {"en": "Mintegral", "ru": "Mintegral",
             "link": ("Mintegral", "Mintegral", "https://www.mintegral.com/en/privacy", "https://www.mintegral.com/en/privacy")}
APPLOVIN = {"en": "AppLovin", "ru": "AppLovin",
            "link": ("AppLovin", "AppLovin", "https://legal.applovin.com/privacy/", "https://legal.applovin.com/privacy/")}
UNITY_ADS = {"en": "Unity Ads", "ru": "Unity Ads",
             "link": ("Unity", "Unity", "https://unity.com/legal/game-player-and-app-user-privacy-policy", "https://unity.com/legal/game-player-and-app-user-privacy-policy")}

LOCAL_ONLY_EN = "Game data, including everything you type, is stored only on your device and is not sent to us or anyone else."
LOCAL_ONLY_RU = "Данные игры, включая всё, что вы вводите, хранятся только на устройстве и не передаются ни нам, ни кому-либо ещё."

APPS = [
    {
        "slug": "hatgame", "icon": "hat-icon.webp", "name_en": "Hat Game", "name_ru": "Шляпа",
        "intro_en": "Hat Game (“the app”) is developed by BerryLab.",
        "intro_ru": "Игру «Шляпа» (далее — приложение) разрабатывает BerryLab.",
        "local_en": LOCAL_ONLY_EN, "local_ru": LOCAL_ONLY_RU,
        "remote_config": True, "consent": True, "ios": False,
        "ad_partners": [ADMOB, MINTEGRAL, APPLOVIN],
    },
    {
        "slug": "alias", "icon": "alias-icon.webp", "name_en": "Alias", "name_ru": "Alias",
        "intro_en": "Alias for Android and iOS (“the app”) is developed by BerryLab.",
        "intro_ru": "Игру Alias для Android и iOS (далее — приложение) разрабатывает BerryLab.",
        "local_en": LOCAL_ONLY_EN, "local_ru": LOCAL_ONLY_RU,
        "remote_config": True, "consent": False, "ios": True,
        "ad_partners": [ADMOB, MINTEGRAL, APPLOVIN, UNITY_ADS],
    },
    {
        "slug": "quizbattle", "icon": "quizbattle-icon.webp", "name_en": "Quiz Battle", "name_ru": "Quiz Battle",
        "intro_en": "Quiz Battle (“the app”) is developed by BerryLab.",
        "intro_ru": "Игру Quiz Battle (далее — приложение) разрабатывает BerryLab.",
        "local_en": "Game data is stored on your device and, if backup is turned on in your device settings, in your own Android backup in your Google account. It is not sent to us.",
        "local_ru": "Данные игры хранятся на устройстве и, если в его настройках включено резервное копирование, в вашей собственной резервной копии Android в аккаунте Google. Нам они не передаются.",
        "remote_config": False, "consent": False, "ios": False,
        "ad_partners": [ADMOB, MINTEGRAL, APPLOVIN],
    },
    {
        "slug": "aliaspremium", "icon": "alias-icon.webp", "name_en": "Alias Premium", "name_ru": "Alias Premium",
        "intro_en": "Alias Premium for iOS (“the app”) is developed by BerryLab.",
        "intro_ru": "Игру Alias Premium для iOS (далее — приложение) разрабатывает BerryLab.",
        "collects": False,
    },
]


def links(items, lang):
    name, url = (0, 2) if lang == "en" else (1, 3)
    return ", ".join(f'<a href="{link[url]}">{link[name]}</a>' for link in items)


def app_ad_partners(app, lang):
    return app["ad_partners"] + RUSSIAN_AD_PARTNERS if lang == "en" else RUSSIAN_AD_PARTNERS + app["ad_partners"]


def ad_partners(app, lang):
    return ", ".join(partner[lang] for partner in app_ad_partners(app, lang))


def policy_links(app, lang):
    return links([FIREBASE_LINK] + [partner["link"] for partner in app_ad_partners(app, lang)], lang)


def bullets(items):
    return chr(10).join(f"    <li>{item}</li>" for item in items)


def head(app, lang):
    title = f"{app['name_en']} — Privacy Policy" if lang == "en" else f"{app['name_ru']} — политика конфиденциальности"
    return f"""  <div class="doc__head">
    <img src="../../assets/img/{app['icon']}" alt="" width="56" height="56">
    <h1>{title}</h1>
  </div>"""


def english_no_data(app):
    return f"""
<section lang="en">
{head(app, 'en')}

  <h2>Contact us</h2>
  <p>{app['intro_en']} If you have questions about this policy, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2>The data we collect</h2>
  <p>The app does not collect any data: it has no analytics and no ads, and it sends nothing to us or to third parties. Game data, including everything you type, is stored only on your device and is deleted when you uninstall the app.</p>
</section>"""


def russian_no_data(app):
    return f"""
<section lang="ru">
{head(app, 'ru')}

  <h2>Контактная информация</h2>
  <p>{app['intro_ru']} Вопросы об этой политике присылайте на <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2>Какие данные мы собираем</h2>
  <p>Приложение не собирает никаких данных: в нём нет аналитики и рекламы, и оно ничего не передаёт ни нам, ни третьим лицам. Данные игры, включая всё, что вы вводите, хранятся только на устройстве и удаляются вместе с приложением.</p>
</section>"""


def english(app):
    if not app.get("collects", True):
        return english_no_data(app)
    ad_id = "advertising ID (on iPhone and iPad the IDFA, only if you allow tracking)" if app["ios"] else "advertising ID"
    collected = [
        "<b>Game usage:</b> screens opened, games played and their settings.",
        "<b>Device and app information:</b> device model, OS and app version, language and region.",
        f"<b>Identifiers:</b> app instance and installation IDs, {ad_id}, app set ID.",
        "<b>IP address</b> and the approximate location derived from it.",
        "<b>Crash and error reports.</b>",
        "<b>Interactions with ads.</b>",
    ]
    why = [
        "<b>To keep the app working:</b> find and fix bugs" + ("; configure the app without an update." if app["remote_config"] else "."),
        "<b>To improve the game:</b> analyse how it is used.",
        "<b>To show ads:</b> show ads, measure their performance and prevent fraud.",
    ]
    basis = ("For users in the EEA, UK and Switzerland, the legal basis is our legitimate interests in keeping a free game working and improving it"
             + ("; for personalised ads, it is your consent." if app["consent"] else "."))
    firebase = "Google Analytics for Firebase, Firebase Crashlytics" + (" and Firebase Remote Config" if app["remote_config"] else "")
    recipients = [
        f"<b>Analytics and crash reporting:</b> {firebase} (Google).",
        f"<b>Advertising partners:</b> {ad_partners(app, 'en')}.",
    ]
    protection_promise = "These services are required to protect the data they receive from the app at least as well as this policy describes. " if app["ios"] else ""
    options = []
    if app["consent"]:
        options.append("<p>In the EEA, UK and Switzerland, the app shows Google’s consent form when you first open it. You can change your choice at any time in the app’s settings.</p>")
    if app["ios"]:
        options.append("<p>On iPhone and iPad, the app asks your permission before your activity may be tracked across other companies’ apps and websites. You can change this in Settings → Privacy &amp; Security → Tracking.</p>")
    keep = ["On your device: until you uninstall the app or clear its data.", "Google Analytics for Firebase: up to 14 months.", "Crashlytics: 90 days.",
            "Other services: as set out in their policies."]
    return f"""
<section lang="en">
{head(app, 'en')}

  <h2>Contact us</h2>
  <p>{app['intro_en']} If you have questions about this policy or your data, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2>The data we collect</h2>
  <p>When you use the app, the following data is collected automatically:</p>
  <ul>
{bullets(collected)}
  </ul>
  <p>{app['local_en']}</p>

  <h2>Why we collect your data</h2>
  <ul>
{bullets(why)}
  </ul>
  <p>{basis}</p>

  <h2>Who can see your data</h2>
  <p>The data is collected and processed by third-party services built into the app, each under its own privacy policy:</p>
  <ul>
{bullets(recipients)}
  </ul>
  <p>{protection_promise}Privacy policies: {policy_links(app, 'en')}.</p>

  <h2>International data transfers</h2>
  <p>Third-party services may process data outside your country in accordance with their own privacy policies.</p>

  <h2>How long we keep your data</h2>
  <ul>
{bullets(keep)}
  </ul>

  <h2>How we protect your data</h2>
  <p>We do not run servers of our own: the data from the app goes directly to the third-party services listed above over encrypted connections.</p>

  <h2>Your rights and options</h2>
  {chr(10).join(options)}
  <p>Depending on where you live, you can:</p>
  <ul>
    <li>access your personal data and get a copy of it;</li>
    <li>have it corrected or deleted;</li>
    <li>restrict its processing;</li>
    <li>object to processing based on legitimate interests;</li>
    <li>withdraw consent at any time.</li>
  </ul>
  <p>Write to <a href="mailto:{EMAIL}">{EMAIL}</a> — we will respond within the data we have access to. For data held by the ad services, you can contact them directly using the links above. In the EEA, UK and Switzerland you can also complain to your data protection authority.</p>
</section>"""


def russian(app):
    if not app.get("collects", True):
        return russian_no_data(app)
    ad_id = "рекламный идентификатор (на iPhone и iPad — IDFA, только если вы разрешили отслеживание)" if app["ios"] else "рекламный идентификатор"
    collected = [
        "<b>Использование игры:</b> открытые экраны, партии и их настройки.",
        "<b>Сведения об устройстве и приложении:</b> модель устройства, версии ОС и приложения, язык и регион.",
        f"<b>Идентификаторы:</b> идентификаторы экземпляра приложения и установки, {ad_id}, идентификатор набора приложений (app set ID).",
        "<b>IP-адрес</b> и примерное местоположение по нему.",
        "<b>Отчёты о сбоях и ошибках.</b>",
        "<b>Взаимодействие с рекламой.</b>",
    ]
    why = [
        "<b>Обеспечение работы приложения:</b> находить и исправлять ошибки" + ("; настраивать работу приложения без его обновления." if app["remote_config"] else "."),
        "<b>Улучшение игры:</b> анализировать использование игры.",
        "<b>Показ рекламы:</b> показывать рекламу, оценивать её эффективность и предотвращать мошенничество.",
    ]
    basis = ("Для пользователей из Европейской экономической зоны, Великобритании и Швейцарии правовое основание — наши законные интересы: чтобы бесплатная игра работала и улучшалась"
             + ("; для персонализированной рекламы — ваше согласие." if app["consent"] else "."))
    firebase = "Google Analytics for Firebase, Firebase Crashlytics" + (" и Firebase Remote Config" if app["remote_config"] else "")
    recipients = [
        f"<b>Аналитика и отчёты о сбоях:</b> {firebase} (Google).",
        f"<b>Партнёры по рекламе:</b> {ad_partners(app, 'ru')}.",
    ]
    protection_promise = "Эти сервисы обязаны защищать данные, которые получают из приложения, не хуже, чем описано в этой политике. " if app["ios"] else ""
    options = []
    if app["consent"]:
        options.append("<p>В Европейской экономической зоне, Великобритании и Швейцарии при первом запуске приложение показывает форму согласия Google. Изменить выбор можно в любой момент в настройках приложения.</p>")
    if app["ios"]:
        options.append("<p>На iPhone и iPad приложение спрашивает разрешение, прежде чем ваши действия могут отслеживаться в приложениях и на сайтах других компаний. Изменить его можно в «Настройки» → «Конфиденциальность и безопасность» → «Отслеживание».</p>")
    keep = ["На устройстве — пока вы не удалите приложение или его данные.", "Google Analytics for Firebase — не дольше 14 месяцев.", "Crashlytics — 90 дней.",
            "Остальные сервисы — по их политикам."]
    return f"""
<section lang="ru">
{head(app, 'ru')}

  <h2>Контактная информация</h2>
  <p>{app['intro_ru']} Вопросы об этой политике и ваших данных присылайте на <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2>Какие данные мы собираем</h2>
  <p>Во время использования приложения автоматически собираются:</p>
  <ul>
{bullets(collected)}
  </ul>
  <p>{app['local_ru']}</p>

  <h2>Зачем мы собираем ваши данные</h2>
  <ul>
{bullets(why)}
  </ul>
  <p>{basis}</p>

  <h2>Кто имеет доступ к вашим данным</h2>
  <p>Данные собирают и обрабатывают сторонние сервисы, встроенные в приложение, — каждый по своей политике конфиденциальности:</p>
  <ul>
{bullets(recipients)}
  </ul>
  <p>{protection_promise}Политики конфиденциальности: {policy_links(app, 'ru')}.</p>

  <h2>Международная передача данных</h2>
  <p>Сторонние сервисы могут обрабатывать данные за пределами вашей страны в соответствии со своими политиками конфиденциальности.</p>

  <h2>Сколько мы храним данные</h2>
  <ul>
{bullets(keep)}
  </ul>

  <h2>Как мы защищаем ваши данные</h2>
  <p>Своих серверов у нас нет: данные из приложения по зашифрованному соединению напрямую получают сторонние сервисы, перечисленные выше.</p>

  <h2>Ваши права и возможности</h2>
  {chr(10).join(options)}
  <p>В зависимости от страны вы можете:</p>
  <ul>
    <li>получить доступ к своим персональным данным и их копию;</li>
    <li>исправить или удалить их;</li>
    <li>ограничить их обработку;</li>
    <li>возразить против обработки на основании законных интересов;</li>
    <li>в любой момент отозвать согласие.</li>
  </ul>
  <p>Пишите на <a href="mailto:{EMAIL}">{EMAIL}</a> — мы ответим в пределах данных, к которым у нас есть доступ. По данным рекламных сервисов можно обратиться к ним напрямую: ссылки на их политики — выше. В Европейской экономической зоне, Великобритании и Швейцарии можно также пожаловаться в надзорный орган по защите данных.</p>
</section>"""


def page(app):
    title_en = f"{app['name_en']} — Privacy Policy · BerryLab"
    title_ru = f"{app['name_ru']} — политика конфиденциальности · BerryLab"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title_en}</title>
  <meta name="title-en" content="{title_en}">
  <meta name="title-ru" content="{title_ru}">
  <link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="../../assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Unbounded:wght@600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/site.css">
  <script src="../../assets/site.js"></script>
</head>
<body>

<header class="wrap top">
  <a class="brand" href="../../index.html" aria-label="BerryLab">
    <img class="brand__mark" src="../../assets/favicon.svg" alt="" width="36" height="36">
    <img class="brand__word" src="../../assets/img/berrylab-logo.webp" alt="BerryLab" width="170" height="30">
  </a>
  <nav class="lang" aria-label="Language">
    <button type="button" data-set-lang="en">EN</button>
    <button type="button" data-set-lang="ru">RU</button>
  </nav>
</header>

<main class="doc">
  <a class="back" href="../../index.html"><span lang="en">← All games</span><span lang="ru">← Все игры</span></a>
  <article class="doc__card">
{english(app)}
{russian(app)}
  </article>
</main>

<footer class="foot">
  <div class="wrap">
    <span>© 2026 BerryLab · <span lang="en">Support:</span><span lang="ru">Поддержка:</span> <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>

</body>
</html>
"""


for app in APPS:
    target = SITE / app["slug"] / "privacy" / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page(app), encoding="utf-8", newline="\n")
    print(target.relative_to(SITE))
