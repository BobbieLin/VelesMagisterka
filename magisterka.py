import os
import shutil
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
        "Dzień dobry, mam na imię Julia i jestem studentką V roku psychologii na Uniwersytecie Wrocławskim. \n\nPoniższy kwestionariusz powstał na potrzebę przeprowadzenia badania magisterskiego dotyczącego czynników wpływających na kreatywność. Nie jest to arkusz diagnostyczny, wyniki będą analizowane zbiorczo i nie świadczą o rzeczywistym poziomie kreatywności występującej u osoby wypełniającej badanie. \n\nAnkieta skierowana jest wyłącznie do <b>osób pełnoletnich.</b> Udział w badaniu jest w pełni <b>anonimowy</b> i <b>dobrowolny,</b> co oznacza, że <b>możliwa jest rezygnacja w dowolnym momencie,</b> a pozyskane dane zostaną wykorzystane tylko w celach naukowych. Czas potrzebny na wypełnienie kwestionariusza wynosi od 5 do 25 minut, w zależności od udzielonych odpowiedzi i losowo przypisanej grupy. \n\nW razie pytań odnośnie badania proszę o kontakt pod adresem mailowym: <a href='mailto:329808@uwr.edu.pl'>329808@uwr.edu.pl</a> \n\nSerdecznie dziękuję za poświęcony czas!",
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
        "rozwiedziony/rozwiedziona, w separacji lub wdowiec/wdowa",
        **defaultOptions,
    ),
)


opowiadanie = vls.page(
    "opowiadanie",
    vls.info(
        "opowiadanie",
        "<h2>Przeczytaj poniższe krótkie opowiadanie o Miriam, po czym przejdź dalej:</h2>",
        'Miriam dorastała w domu na obrzeżach Lizbony, gdzie poezja i polityka mieszały się z zapachem prażonych kasztanów i dźwiękami muzyki fado. Jej matka prowadziła małe kino studyjne, a jej ojciec był zegarmistrzem. Dzięki tak różnym rodzicom, Miriam już jako dziecko obserwowała, jak porządek i chaos są dwoma stronami tej samej monety. \n\nJako nastolatka, przeprowadziła się wraz z ojcem do Polski, jego ojczyzny, gdzie zdumiały ją różnice kulturowe. Polacy wyrażali siebie zupełnie inaczej niż portugalczycy. To zainspirowało ją do studiowania psychologii, gdzie szczególnie upodobała sobie psychologię twórczości. Okazało się, że wyjątkowo dobrze radzi sobie w środowisku naukowym. Pomimo początkowych problemów Miriam ze statystyką, jej praca magisterska zrobiła ogromne wrażenie. Po ukończeniu kierunku, zdecydowała się na doktorat z dziedziny psychologii twórczości w Portugalii. \n\n Po powrocie do domu, okazało się, że kino jej matki powoli upada z powodu braku funduszy i coraz mniejszego zainteresowania ludzi, którzy zaczęli preferować większe i tańsze kina. Miriam nie mogła patrzeć na smutek mamy, która od zawsze wkładała całą swoją duszę w to miejsce. Ona jednak kazała córce skupić się na doktoracie i przestać się o nią martwić. \n\n Miriam jednak nie po to badała kreatywność, aby samej jej nie wykorzystywać. Wpadła na pomysł, aby wieczorami w kinie studyjnym organizować eksperymentalne, stymulujące twórczość wydarzenia. Były to na przykład spektakle, w których aktorzy dostawali zadanie zbudowania historii na podstawie losowo wyciągniętych przedmiotów. Dużym powodzeniem cieszyły się wymyślone przez nią "Wieczory Twórczego Ryzyka", gdzie uczestnicy losowali nieoczywiste tematy, a następnie musieli wspólnie wymyślić i przedstawić improwizowany mini-spektakl. W ten sposób kino stało się równocześnie miejscem kreatywnych spotkań, które pozwalało Miriam na prowadzenie jej badań. \n\nDoktorantkę fascynowało, jak umysł tworzy sens z pozornego bezsensu i wysnuła tezę, że twórczość rodzi się z odwagi porzucenia kontroli. Dziś kontynuuje badania nad twórczością, a jedno z nich za chwilę będziesz wypełniać Ty.',
    ),
    visibleIf="{group} = 3",
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
            "<h2>Zadania AUT</h2> Twoim zadaniem w tej sekcji jest wymyślenie od jednego do trzech kreatywnych zastosowań danego przedmiotu. Możesz pomijać przedmioty. Po pierwszym przedmiocie możesz zakończyć zadanie klikając przycisk <i>Zakończ AUT</i>.",
        ),
        vls.panel(
            f"panel_AUT_{item_a}",
            vls.image(
                f"img_{item_a}",
                f"https://bobbielin.github.io/VelesMagisterka/images/{item_a}.png",
                visibleIf="{group}=2 or {group}=3",
                maxWidth="400px",
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
    visibleIf="{group}=2 or {group}=3",
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
        "mmpr",
        """Czuję więź z osobą medialną poprzez jego/jej posty w mediach społecznościowych.
Doświadczam, że angażuję się emocjonalnie, gdy osoba medialna dzieli się bardziej prywatnymi informacjami na swój temat.
Uważam, że osobiście nie utożsamiam się z treścią postów osoby medialnej.
Często czuję się zainspirowany postami publikowanymi przez osobę medialną.
Zawsze “lajkuję” posty osoby medialnej w mediach społecznościowych.
Często komentuję posty osoby medialnej w polu komentarzy.
Często przesyłam posty osoby medialnej moim znajomym lub udostępniam je na własnych kanałach internetowych.
Przeważnie sprawdzam tylko, co nowego opublikowała osoba medialna i nie jestem aż tak aktywny, jeżeli chodzi o klikanie “lubię to”, udostępnianie czy komentowanie.
Uważam, że osoba medialna reprezentuje wartości, które są dla mnie ważne.
Nie sądzę, aby osoba medialna przedstawiała się w autentyczny sposób w mediach społecznościowych.
Większość tego, co osoba medialna udostępnia w mediach społecznościowych, oceniam pozytywnie.
Osoba medialna wydaje się autentyczną osobą, z którą dogadałbym się w prawdziwym życiu.
Wolę rzeczy, które osoba medialna promuje (np. produkty, porady żywieniowe, porady dotyczące szkoleń itp.), niż podobne rzeczy reklamowane w innych miejscach.
Posty osoby medialnej często inspirują mnie do zmian we własnym życiu.
Nigdy nie kupuję produktów, które osoba medialna reklamuje lub poleca w mediach społecznościowych.
Chętnie stosuję się do różnych wskazówek i rad, którymi dzieli się osoba medialna, ponieważ czuję, że mogę zaufać jej wiedzy na ten temat.
Często zdarza się, że w rozmowach z innymi osobami na co dzień zwracam uwagę na rzeczy, o których osoba medialna wspomniała w swoich postach w mediach społecznościowych.
Zdarza się, że posty osoby medialnej przyczyniają się do tego, że w jakiś sposób zmieniam swoje przyzwyczajenia (np. ubiór, dietę, treningi, wygląd itp.).""".splitlines(),
        rateMax=4,
        rateMin=1,
        minRateDescription="Zdecydowanie się nie zgadzam",
        maxRateDescription="Zdecydowanie się zgadzam",
    ),
    **defaultOptions,
)

if os.path.exists("./survey/src"):
    shutil.copyfile("./index.css", "./survey/src/index.css")

vls.survey(
    wstęp,
    metryczka,
    opowiadanie,
    instrukcja,
    AUT_pages,
    epsi,
    mmpr,
    locale="pl",
    numberOfGroups=3,
    customCode=vls.getJS("./custom_buttons.js"),
)
