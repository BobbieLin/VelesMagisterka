import velesresearch as vls
import anyascii

defaultOptions = {"hideNumber": True, "isRequired": False}


wstęp = vls.page(
    "wstęp",
    vls.info(
        "manipulacja",
        "<h2>Badanie magisterskie - grupa 1</h2>",
        visibleIf="{group} = 1",
    ),
    vls.info(
        "manipulacja",
        "<h2>Badanie magisterskie - grupa 2</h2>",
        visibleIf="{group} = 2",
    ),
    vls.info(
        "manipulacja",
        "<h2>Badanie magisterskie - grupa 3</h2>",
        visibleIf="{group} = 3",
    ),
    vls.info(
        "intro",
        "Dzień dobry, mam na imię Julia i jestem studentką V roku psychologii na Uniwersytecie Wrocławskim. \n\nPoniższy kwestionariusz powstał na potrzebę przeprowadzenia badania magisterskiego dotyczącego czynników wpływających na kreatywność. Nie jest to arkusz diagnostyczny, wyniki będą analizowane zbiorczo i nie świadczą o rzeczywistym poziomie kreatywności występującej u osoby wypełniającej badanie. \n\nAnkieta skierowana jest wyłącznie do <b>osób pełnoletnich.</b> Udział w badaniu jest w pełni <b>anonimowy</b> i <b>dobrowolny,</b> co oznacza, że <b>możliwa jest rezygnacja w dowolnym momencie,</b> a pozyskane dane zostaną wykorzystane tylko w celach naukowych. Czas potrzebny na wypełnienie kwestionariusza wynosi od 5 do 25 minut, w zależności od udzielonych odpowiedzi i losowo przypisanej grupy. \n\n<b>W przypadku rozwiązywania badania na telefonie</b> zachęcam do obrócenia urządzania do pozycji poziomej, ułatwi to odczytywanie zadań.  \n\nW razie pytań odnośnie badania proszę o kontakt pod adresem mailowym: 329808@uwr.edu.pl \n\nSerdecznie dziękuję za poświęcony czas!",
    ),
    vls.consent(
        "Wyrażam świadomą zgodę na udział w badaniu i zaświadczam, że jestem osobą pełnoletnią.",
        "Musisz wyrazić zgodę",
    ),
)


metryczka = vls.page(
    "metryczka",
    vls.info(
        "intro_metryczka",
        "<h2>Metryczka</h2>",
    ),
    vls.radio(
        "plec",
        "Płeć",
        "kobieta",
        "mężczyzna",
        "inna/wolę nie odpowiadać",
        **defaultOptions,
    ),
    vls.text(
        "wiek",
        "Wiek",
        inputType="number",
        min=18,
        max=99,
        **defaultOptions,
    ),
    vls.radio(
        "wyksztalcenie",
        "Wykształcenie",
        "podstawowe",
        "gimnazjalne",
        "średnie",
        "zasadnicze zawodowe",
        "w trakcie studiów",
        "wyższe",
        **defaultOptions,
    ),
    vls.radio(
        "zamieszkanie",
        "Miejsce zamieszkania",
        "wieś",
        "miasto do 50 tys. mieszkańców",
        "miasto od 50 tys. do 150 tys. mieszkańców",
        "miasto od 150 tys. do 500 tys. mieszkańców",
        "miasto powyżej 500 tys. mieszkańców",
        **defaultOptions,
    ),
    vls.radio(
        "stan_cywilny",
        "Stan cywilny",
        "kawaler/panna",
        "w związku nieformalnym",
        "żonaty/zamężna",
        "rozwiedziony/rozwiedziona lub w separacji",
        "wdowiec/wdowa",
        **defaultOptions,
    ),
)


instrukcja = vls.page(
    "instrukcja",
    vls.info(
        "uwaga",
        "<h2>Przeczytaj uważnie poniższą instrukcję:</h2>",
    ),
    vls.info(
        "intro_instrukcja",
        'W tej sekcji Twoim zadaniem będzie udzielenie kreatywnych, nietypowych odpowiedzi na pytanie: <b>"Jak można zastosować ten przedmiot?"</b>. Możesz udzielić dowolnej ilości odpowiedzi co do zastosowania każdego z przedmiotów. Nie musisz udzielać odpowiedzi na wszystkie pytania, postaraj się jednak odpowiedzieć na jak najwięcej z nich.',
        visibleIf="{group} = 1",
    ),
    vls.info(
        "intro_instrukcja",
        'W tej sekcji Twoim zadaniem będzie udzielenie kreatywnych, nietypowych odpowiedzi na pytanie: <b>"Jak można zastosować ten przedmiot?"</b>. Możesz udzielić dowolnej ilości odpowiedzi co do zastosowania każdego z przedmiotów. Nie musisz udzielać odpowiedzi na wszystkie pytania, postaraj się jednak odpowiedzieć na jak najwięcej z nich. \n\nPodczas badania towarzyszyć będzie Ci Miriam, badaczka twórczości. Będzie Cię wspierać, a czasami udzieli Ci wskazówek. <b>Postaraj się nie ignorować Miriam - ma wiele ciekawych rzeczy do powiedzenia.</b>',
        visibleIf="{group} = 2",
    ),
    vls.info(
        "intro_instrukcja",
        'W tej sekcji Twoim zadaniem będzie udzielenie kreatywnych, nietypowych odpowiedzi na pytanie: <b>"Jak można zastosować ten przedmiot?"</b>. Możesz udzielić dowolnej ilości odpowiedzi co do zastosowania każdego z przedmiotów. Nie musisz udzielać odpowiedzi na wszystkie pytania, postaraj się jednak odpowiedzieć na jak najwięcej z nich. \n\nPodczas badania towarzyszyć będzie Ci Miriam, badaczka twórczości. Będzie Cię wspierać, a czasami udzieli Ci wskazówek. <b>Postaraj się nie ignorować Miriam - ma wiele ciekawych rzeczy do powiedzenia.</b>',
        visibleIf="{group} = 3",
    ),
)

opowiadanie = vls.page(
    "opowiadanie",
    vls.info(
        "opowiadanie",
        "<h2>Przeczytaj poniższe krótkie opowiadanie o Miriam, po czym przejdź dalej:</h2>"
        'Miriam dorastała w tętniącym kolorami domu na obrzeżach Lizbony, gdzie poezja i polityka mieszały się z zapachem prażonych kasztanów i dźwiękami starego radia grającego fado. Jej matka prowadziła stare kino studyjne, a jej ojciec był zegarmistrzem. Dzięki rodzicom, Miriam już jako dziecko obserwowała, jak porządek i chaos są dwoma stronami tej samej monety. \n\nGdy dorosła, postanowiła studiować psychologię. Na uczelni szczególnie upodobała sobie psychologię twórczości. Wpadła na pomysł aby wieczorami organizować eksperymentalne, stymulujące kreatywność wydarzenia w kinie matki, na przykład spektakle, w których aktorzy dostawali zadanie zbudowania historii na podstawie losowo wyciągniętych przedmiotów. Dużym powodzeniem cieszyły się wymyślone przez nią "Wieczory Twórczego Ryzyka", gdzie widzowie losowali nieoczywiste tematy, a następnie artyści, naukowcy i zupełnie przypadkowe osoby musiały wspólnie wymyślić i przedstawić improwizowaną prezentację, instalację lub mini-spektakl. Miriam fascynowało, jak umysł tworzy sens z pozornego bezsensu i wysnuła tezę, że twórczość rodzi się z odwagi porzucenia kontroli. \n\nDziś prowadzi badania nad twórczością w warunkach niepewności — w jej laboratorium uczestnicy rozwiązują problemy bez instrukcji, reguł czy czasu. Jej najbardziej znany eksperyment to „5 minut w hałasie”, w którym ochotnicy musieli stworzyć opowieść podczas bombardowania bodźcami (szumami, migającymi światłami, absurdalnymi zadaniami).',
    ),
    visibleIf="{group} = 3",
)

AUT_items = """cegła
sznurek
beczka
butelka
długopis
grzebień
gumka recepturka
guzik
linijka
mop
opona
parasol
poduszka
puszka
spinacz
wieszak
zapalniczka
doniczka
pudełko
patyk""".splitlines()

AUT_pages = []
for item in AUT_items:
    item_a = anyascii.anyascii(item)
    p = vls.page(
        f"AUT_{item_a}",
        vls.info(
            f"AUT_intro_{item_a}",
            "<h2>Zadania AUT</h2> Twoim zadaniem w tej sekcji jest wymyślenie od jednego do trzech kreatywnych zastosowań danego przedmiotu. Możesz pomijać przedmioty. Możesz także w dowolnym momencie zakończyć zadanie klikając przycisk Zakończ AUT.",
        ),
        vls.panel(
            f"panel_AUT_{item_a}",
            vls.image(
                f"img_{item_a}",
                f"https://bobbielin.github.io/VelesMagisterka/images/{item_a}.png",
                visibleIf="{group}=2 or {group}=3",
            ),
            vls.multipleText(
                f"AUT_{item_a}",
                f"Wymyśl od jednego do trzech kreatywnych zastosowań dla: {item}",
                [{"name": f"{i+1}"} for i in range(3)],
            ),
        ),
    )
    AUT_pages.append(p)


epsi = vls.page(
    "epsi",
    vls.info(
        "epsi",
        "<h2>EPSI</h2>",
    ),
    vls.info(
        "epsi_instrukcja",
        "Odpowiedz na poniższe pytania:\n\n<b>Kiedy interaktowałem z Miriam, odniosłem wrażenie, że ona...</b>",
    ),
    vls.rating(
        "epsi",
        """była mnie świadoma.
wiedziała, że z nią jestem.
wiedziała, że jestem jej świadom.
wiedziała, że poświęcam jej uwagę.
wiedziała, że na nią reaguję.
reagowała na to co mówiłem lub robiłem.""".splitlines(),
        rateMin=1,
        rateMax=7,
        minRateDescription="Zdecydowanie się nie zgadzam",
        maxRateDescription="Zdecydowanie się zgadzam",
    ),
    visibleIf="{group} = 2 or 3",
    **defaultOptions,
)


mmpr = vls.page(
    "mmpr",
    vls.info(
        "mmpr_title",
        "<h2>MMPR</h2>",
    ),
    vls.info(
        "mmpr_instrukcja",
        "Kwestionariusz ten zawiera stwierdzenia na temat Twoich postaw, czyli myśli, uczuć i zachowań w odniesieniu do konkretnej postaci w mediach społecznościowych. <b>Zanim udzielisz odpowiedzi, pomyśl o konkretnej osobie z mediów społecznościowych, najlepiej tej, którą najczęściej obserwujesz.</b> Może to być influencer, youtuber, tiktoker lub postać z mediów społecznościowych, na przykład zajmująca się stylem życia, ćwiczeniami, sportem, grami, odżywianiem lub modą. Najważniejsze jest to, że nie masz z tą osobą relacji w prawdziwym życiu. Odpowiedz, w jakim stopniu zgadzasz się lub nie zgadzasz z poniższymi stwierdzeniami:",
    ),
    vls.rating(
        "question7",
        "Czuję więź z osobą medialną poprzez jego/jej posty w mediach społecznościowych.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question8",
        "Doświadczam, że angażuję się emocjonalnie, gdy osoba medialna dzieli się bardziej prywatnymi informacjami na swój temat.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question9",
        "Uważam, że osobiście nie utożsamiam się z treścią postów osoby medialnej.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question10",
        "Często czuję się zainspirowany postami publikowanymi przez osobę medialną.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question11",
        "Zawsze “lajkuję” posty osoby medialnej w mediach społecznościowych",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question12",
        "Często komentuję posty osoby medialnej w polu komentarzy.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question13",
        "Często przesyłam posty osoby medialnej moim znajomym lub udostępniam je na własnych kanałach internetowych.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question14",
        "Przeważnie sprawdzam tylko, co nowego opublikowała osoba medialna i nie jestem aż tak aktywny, jeżeli chodzi o klikanie “lubię to”, udostępnianie czy komentowanie.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question15",
        "Uważam, że osoba medialna reprezentuje wartości, które są dla mnie ważne.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question16",
        "Nie sądzę, aby osoba medialna przedstawiała się w autentyczny sposób w mediach społecznościowych.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question17",
        "Większość tego, co osoba medialna udostępnia w mediach społecznościowych, oceniam pozytywnie.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question18",
        "Osoba medialna wydaje się autentyczną osobą, z którą dogadałbym się w prawdziwym życiu.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question19",
        "Wolę rzeczy, które osoba medialna promuje (np. produkty, porady żywieniowe, porady dotyczące szkoleń itp.), niż podobne rzeczy reklamowane w innych miejscach.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question20",
        "Posty osoby medialnej często inspirują mnie do zmian we własnym życiu.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question21",
        "Nigdy nie kupuję produktów, które osoba medialna reklamuje lub poleca w mediach społecznościowych.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question22",
        "Chętnie stosuję się do różnych wskazówek i rad, którymi dzieli się osoba medialna, ponieważ czuję, że mogę zaufać jego wiedzy na ten temat.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question23",
        "Często zdarza się, że w rozmowach z innymi osobami na co dzień zwracam uwagę na rzeczy, o których osoba medialna wspomniała w swoich postach w mediach społecznościowych.",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
    vls.rating(
        "question24",
        "Zdarza się, że posty osoby medialnej przyczyniają się do tego, że w jakiś sposób zmieniam swoje przyzwyczajenia (np. ubiór, dietę, treningi, wygląd itp.).",
        rateMax=4,
        rateMin=1,
        **defaultOptions,
    ),
)


vls.survey(
    wstęp,
    metryczka,
    instrukcja,
    AUT_pages,
    epsi,
    mmpr,
    locale="pl",
    numberOfGroups=3,
    customCode=vls.getJS("./custom_buttons.js"),
)
