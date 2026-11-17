"""Pronunciación orientativa del inglés británico (England, no rótico) para hispanohablantes.

Convención de la guía (la misma que se explica en la clase 1 de A1):
  th  = «th» sorda (sin vibrar, lengua entre los dientes): think = thingk
  dh  = «th» sonora (vibrando): this = dhis
  sh  = «sh» rioplatense de «calle»; zh = «sh» sonora (television = TEL-i-vizh-ən)
  ch  = «ch» de «chico»; dj = «y» fuerte tipo «dj» (jam = djam)
  ng  = nasal de «sing»; h = aspirada suave; w = «u» + vocal (water, we)
  r   = solo suena delante de vocal; al final o antes de consonante se calla (car = kaa)
  ə   = vocal neutra (schwa), muy corta: about = ə-BAUT
  a   = «a» abierta de cat y también la «a» corta de cup (la de cat es más abierta)
  o   = «o» corta y redonda (lot = lot);  e = «e» de «perro»;  i = «i» corta
  u   = «u» corta (book = buk)
  ii  = «i» larga (see = sii);  uu = «u» larga (moon = muun)
  aa  = «a» larga y abierta (car = kaa, bath = baath)
  oo  = «o» larga (thought = thoot)
  əə  = vocal larga neutra (bird = bəəd)
  ei ai oi əu au iə eə uə = diptongos (day = dei, my = mai, boy = boi, go = gəu, now = nau)
  MAYÚSCULAS = sílaba tónica (solo en palabras de dos o más sílabas); los guiones separan sílabas.
"""

import re

# Palabras cuya pronunciación se escribe a mano (palabras gramaticales, irregulares, números…).
OVR = {
    # artículos, preposiciones, conjunciones
    "a": "ə", "an": "ən", "the": "dhə", "and": "and", "of": "ov", "to": "tuu", "in": "in",
    "on": "on", "at": "at", "for": "foo", "with": "widh", "from": "from", "by": "bai",
    "as": "az", "or": "oo", "but": "bat", "if": "if", "than": "dhan", "then": "dhen",
    "so": "səu", "because": "bi-KOZ", "about": "ə-BAUT", "after": "AAF-tə", "before": "bi-FOO",
    "into": "IN-tuu", "over": "ƏU-və", "under": "AN-də", "between": "bi-TWIIN", "through": "throo",
    "during": "DYUƏ-ring", "without": "widh-AUT", "until": "ən-TIL", "while": "wail",
    "up": "ap", "down": "daun", "out": "aut", "off": "of", "away": "ə-WEI",
    "near": "niə", "behind": "bi-HAIND", "next": "nekst", "across": "ə-KROS", "against": "ə-GENST",
    "along": "ə-LONG", "around": "ə-RAUND", "inside": "in-SAID", "outside": "aut-SAID",
    # pronombres y determinantes
    "i": "ai", "you": "yuu", "he": "hii", "she": "shii", "it": "it", "we": "wii", "they": "dhei",
    "me": "mii", "him": "him", "her": "həə", "us": "as", "them": "dhem", "my": "mai",
    "your": "yoo", "his": "hiz", "its": "its", "our": "auə", "their": "dheə", "mine": "main",
    "yours": "yooz", "this": "dhis", "that": "dhat", "these": "dhiiz", "those": "dhəuz",
    "what": "wot", "where": "weə", "when": "wen", "who": "huu", "whom": "huum", "why": "wai",
    "how": "hau", "which": "wich", "whose": "huuz", "there": "dheə", "here": "hiə",
    "some": "sam", "any": "E-ni", "all": "ool", "every": "EV-ri", "each": "iich", "both": "bəuth",
    "no": "nəu", "none": "nan", "other": "A-dhə", "another": "ə-NA-dhə", "much": "mach",
    "many": "ME-ni", "more": "moo", "most": "məust", "few": "fyuu", "little": "LI-təl",
    "own": "əun", "same": "seim", "such": "sach", "only": "ƏUN-li", "also": "OOL-səu",
    "very": "VE-ri", "too": "tuu", "just": "djast", "still": "stil", "already": "ool-RE-di",
    "yet": "yet", "even": "II-vən", "again": "ə-GEN", "ever": "E-və", "never": "NE-və",
    "always": "OOL-weiz", "often": "O-fən", "sometimes": "SAM-taimz", "usually": "YUU-zhuə-li",
    "not": "not", "yes": "yes", "ok": "əu-KEI", "okay": "əu-KEI", "please": "pliiz",
    "now": "nau", "soon": "suun", "today": "tə-DEI", "tonight": "tə-NAIT",
    # verbos auxiliares y muy comunes
    "be": "bii", "am": "am", "is": "iz", "are": "aa", "was": "woz", "were": "wəə",
    "been": "biin", "being": "BII-ing", "have": "hav", "has": "haz", "had": "had",
    "having": "HA-ving", "do": "duu", "does": "daz", "did": "did", "done": "dan",
    "doing": "DUU-ing", "will": "wil", "would": "wud", "shall": "shal", "should": "shud",
    "can": "kan", "could": "kud", "may": "mei", "might": "mait", "must": "mast",
    "go": "gəu", "goes": "gəuz", "going": "GƏU-ing", "went": "went", "gone": "gon",
    "come": "kam", "came": "keim", "comes": "kamz", "get": "get", "gets": "gets", "got": "got",
    "make": "meik", "makes": "meiks", "made": "meid", "take": "teik", "took": "tuk",
    "taken": "TEI-kən", "give": "giv", "gave": "geiv", "given": "GI-vən", "say": "sei",
    "said": "sed", "says": "sez", "see": "sii", "saw": "soo", "seen": "siin", "know": "nəu",
    "knew": "nyuu", "known": "nəun", "think": "thingk", "thought": "thoot", "want": "wont",
    "wants": "wonts", "need": "niid", "needs": "niidz", "like": "laik", "likes": "laiks",
    "love": "lav", "loves": "lavz", "look": "luk", "looks": "luks", "find": "faind",
    "found": "faund", "tell": "tel", "told": "təuld", "ask": "aask", "asked": "aaskt",
    "work": "wəək", "works": "wəəks", "worked": "wəəkt", "try": "trai", "leave": "liiv",
    "left": "left", "put": "put", "keep": "kiip", "let": "let", "begin": "bi-GIN",
    "seem": "siim", "help": "help", "show": "shəu", "hear": "hiə", "play": "plei",
    "run": "ran", "ran": "ran", "move": "muuv", "live": "liv", "lives": "livz",
    "lived": "livd", "believe": "bi-LIIV", "bring": "bring", "brought": "broot",
    "write": "rait", "wrote": "rəut", "written": "RI-tən", "sit": "sit", "sat": "sat",
    "stand": "stand", "stood": "stud", "lose": "luuz", "lost": "lost", "pay": "pei",
    "paid": "peid", "meet": "miit", "met": "met", "buy": "bai", "bought": "boot",
    "speak": "spiik", "spoke": "spəuk", "read": "riid", "eat": "iit", "ate": "et",
    "eaten": "II-tən", "drink": "dringk", "drank": "drangk", "sleep": "sliip",
    "slept": "slept", "wake": "weik", "woke": "wəuk", "stay": "stei", "stayed": "steid",
    "visit": "VI-zit", "visited": "VI-zi-tid", "call": "kool", "called": "koold",
    "start": "staat", "started": "STAA-tid", "stop": "stop", "stopped": "stopt",
    "open": "ƏU-pən", "close": "kləuz", "turn": "təən", "wait": "weit", "waited": "WEI-tid",
    "walk": "wook", "walked": "wookt", "wear": "weə", "wore": "woo", "worn": "woon",
    "cook": "kuk", "cooked": "kukt", "clean": "kliin", "cleaned": "kliind", "wash": "wosh",
    "washed": "wosht", "use": "yuuz", "used": "yuuzd", "feel": "fiil", "felt": "felt",
    "happen": "HA-pən", "happened": "HA-pənd", "learn": "ləən", "learned": "ləənd",
    "learnt": "ləənt", "study": "STA-di", "studied": "STA-did", "teach": "tiich",
    "taught": "toot", "decide": "di-SAID", "decided": "di-SAI-did", "remember": "ri-MEM-bə",
    "forget": "fə-GET", "forgot": "fə-GOT", "agree": "ə-GRII", "agreed": "ə-GRIID",
    "check": "chek", "pick": "pik", "enjoy": "in-DJOI", "enjoyed": "in-DJOID",
    "arrive": "ə-RAIV", "arrived": "ə-RAIVD", "travel": "TRA-vəl", "travelled": "TRA-vəld",
    "travelling": "TRA-və-ling", "organise": "OO-gə-naiz", "organised": "OO-gə-naizd",
    "organising": "OO-gə-nai-zing", "recognise": "RE-kəg-naiz", "apologise": "ə-PO-lə-djaiz",
    "realise": "RIƏ-laiz", "realised": "RIƏ-laizd", "favour": "FEI-və", "colour": "KA-lə",
    # sustantivos y adjetivos muy comunes
    "time": "taim", "year": "yiə", "years": "yiəz", "day": "dei", "days": "deiz",
    "week": "wiik", "weeks": "wiiks", "month": "manth", "morning": "MOO-ning",
    "afternoon": "aaf-tə-NUUN", "evening": "IIV-ning", "night": "nait", "way": "wei",
    "man": "man", "men": "men", "woman": "WU-mən", "women": "WI-min", "child": "chaild",
    "children": "CHIL-drən", "people": "PII-pəl", "person": "PƏƏ-sən", "thing": "thing",
    "things": "thingz", "life": "laif", "world": "wəəld", "country": "KAN-tri", "place": "pleis",
    "home": "həum", "house": "haus", "room": "ruum", "door": "doo", "water": "WOO-tə",
    "name": "neim", "friend": "frend", "friends": "frendz", "family": "FA-mə-li",
    "mum": "mam", "dad": "dad", "mother": "MA-dhə", "father": "FAA-dhə", "brother": "BRA-dhə",
    "sister": "SIS-tə", "wife": "waif", "husband": "HAZ-bənd", "girl": "gəəl", "boy": "boi",
    "money": "MA-ni", "pound": "paund", "pounds": "paundz",
    "job": "djob", "school": "skuul", "city": "SI-ti", "town": "taun", "street": "striit",
    "road": "rəud", "bus": "bas", "train": "trein", "car": "kaa", "shop": "shop",
    "food": "fuud", "tea": "tii", "coffee": "KO-fi", "milk": "milk", "bread": "bred",
    "good": "gud", "bad": "bad", "big": "big", "small": "smool", "new": "nyuu", "old": "əuld",
    "young": "yang", "long": "long", "short": "shoot", "high": "hai", "low": "ləu",
    "great": "greit", "nice": "nais", "beautiful": "BYUU-tə-fəl", "best": "best",
    "better": "BE-tə", "right": "rait", "wrong": "rong", "hot": "hot", "cold": "kəuld",
    "easy": "II-zi", "hard": "haad", "difficult": "DI-fi-kəlt", "happy": "HA-pi",
    "sad": "sad", "tired": "taiəd", "busy": "BI-zi", "free": "frii", "ready": "RE-di",
    "sure": "shoo", "late": "leit", "early": "ƏƏ-li", "first": "fəəst", "last": "laast",
    "two": "tuu", "three": "thrii", "four": "foo", "five": "faiv",
    "six": "siks", "seven": "SE-vən", "eight": "eit", "nine": "nain", "ten": "ten",
    "eleven": "i-LE-vən", "twelve": "twelv", "twenty": "TWEN-ti", "thirty": "THƏƏ-ti",
    "forty": "FOO-ti", "fifty": "FIF-ti", "hundred": "HAN-drəd", "thousand": "THAU-zənd",
    "one": "wan", "zero": "ZIƏ-rəu", "second": "SE-kənd",
    "monday": "MAN-dei", "tuesday": "TYUUZ-dei", "wednesday": "WENZ-dei",
    "thursday": "THƏƏZ-dei", "friday": "FRAI-dei", "saturday": "SA-tə-dei", "sunday": "SAN-dei",
    "january": "DJA-nyuə-ri", "february": "FE-bruə-ri", "march": "maach", "april": "EI-prəl",
    "june": "djuun", "july": "djuu-LAI", "august": "OO-gəst",
    "september": "sep-TEM-bə", "october": "ok-TƏU-bə", "november": "nəu-VEM-bə",
    "december": "di-SEM-bə",
    "england": "ING-glənd", "english": "ING-glish", "british": "BRI-tish", "britain": "BRI-tən",
    "london": "LAN-dən", "spanish": "SPA-nish", "argentina": "aa-djən-TII-nə",
    "scotland": "SKOT-lənd", "wales": "weilz", "ireland": "AIƏ-lənd", "uk": "yuu-KEI",
    "buenos": "BWE-nos", "aires": "AI-res", "spain": "spein", "america": "ə-ME-ri-kə",
    "mr": "MIS-tə", "mrs": "MI-siz", "ms": "miz", "miss": "mis", "sir": "səə",
    # contracciones
    "i'm": "aim", "i've": "aiv", "i'll": "ail", "i'd": "aid", "you're": "yoo", "you've": "yuuv",
    "you'll": "yuul", "you'd": "yuud", "he's": "hiiz", "she's": "shiiz", "it's": "its",
    "we're": "wiə", "we've": "wiiv", "we'll": "wiil", "we'd": "wiid", "they're": "dheə",
    "they've": "dheiv", "they'll": "dheil", "they'd": "dheid", "that's": "dhats",
    "there's": "dheəz", "here's": "hiəz", "what's": "wots", "who's": "huuz", "where's": "weəz",
    "how's": "hauz", "let's": "lets", "isn't": "IZ-ənt", "aren't": "aant", "wasn't": "WO-zənt",
    "weren't": "wəənt", "don't": "dəunt", "doesn't": "DA-zənt", "didn't": "DI-dənt",
    "won't": "wəunt", "wouldn't": "WU-dənt", "can't": "kaant", "couldn't": "KU-dənt",
    "shouldn't": "SHU-dənt", "haven't": "HA-vənt", "hasn't": "HA-zənt", "hadn't": "HA-dənt",
    "mustn't": "MA-sənt", "needn't": "NIID-ənt", "o'clock": "ə-KLOK", "what're": "WO-tə",
    "ain't": "eint", "ma'am": "mam", "y'all": "yool",
}

# Palabras de uso frecuente en los ejemplos y diálogos del curso (ortografía irregular).
OVR.update({
    "absent": "AB-sənt", "absolutely": "AB-sə-luut-li", "academic": "a-kə-DE-mik",
    "according": "ə-KOO-ding", "account": "ə-KAUNT", "actors": "AK-təz", "add": "ad",
    "addition": "ə-DI-shən", "addressed": "ə-DREST", "adds": "adz", "admitted": "əd-MI-tid",
    "afraid": "ə-FREID", "agent": "EI-djənt", "ahead": "ə-HED", "aims": "eimz", "alarm": "ə-LAAM",
    "almost": "OOL-məust", "among": "ə-MANG", "analysis": "ə-NA-lə-sis", "animal": "A-ni-məl",
    "anna": "A-nə", "announced": "ə-NAUNST", "answer": "AAN-sə", "apples": "A-pəlz",
    "apply": "ə-PLAI", "area": "EƏ-ri-ə", "argument": "AA-gyə-mənt", "arm": "aam",
    "arrange": "ə-REINDJ", "article": "AA-ti-kəl", "assistant": "ə-SIS-tənt",
    "attendance": "ə-TEN-dəns", "avoid": "ə-VOID", "awful": "OO-fəl", "back": "bak",
    "bags": "bagz", "balance": "BA-ləns", "ball": "bool", "bank": "bangk", "bar": "baa",
    "barking": "BAA-king", "bath": "baath", "beans": "biinz", "bed": "bed", "beef": "biif",
    "began": "bi-GAN", "belfast": "BEL-faast", "ben": "ben", "bit": "bit", "bite": "bait",
    "biting": "BAI-ting", "blocks": "bloks", "blood": "blad", "blow": "bləu",
    "bonfire": "BON-faiə", "book": "buk", "boxing": "BOK-sing", "break": "breik",
    "bridge": "bridj", "bright": "brait", "bristol": "BRI-stəl", "broke": "brəuk",
    "broken": "BRƏU-kən", "brown": "braun", "bullet": "BU-lit", "burns": "bəənz",
    "business": "BIZ-nis", "buyer": "BAI-ə", "bye": "bai", "cab": "kab", "cake": "keik",
    "capital": "KA-pi-təl", "cardiff": "KAA-dif", "careful": "KEƏ-fəl", "carry": "KA-ri",
    "case": "keis", "castle": "KAA-səl", "catch": "kach", "celebrate": "SE-lə-breit",
    "cent": "sent", "centre": "SEN-tə", "chain": "chein", "changed": "cheindjd",
    "cheaper": "CHII-pə", "cheek": "chiik", "chocolate": "CHOK-lit", "choose": "chuuz",
    "cities": "SI-tiz", "claims": "kleimz", "clapped": "klapt", "class": "klaas",
    "clear": "kliə", "clock": "klok", "closed": "kləuzd", "clothes": "kləudhz",
    "comfortable": "KAM-fə-tə-bəl", "coming": "KA-ming", "comment": "KO-ment",
    "common": "KO-mən", "completely": "kəm-PLIIT-li", "complex": "KOM-pleks",
    "compulsory": "kəm-PAL-sə-ri", "concern": "kən-SƏƏN", "confirm": "kən-FƏƏM",
    "corner": "KOO-nə", "cornwall": "KOON-wool", "cost": "kost", "countries": "KAN-triz",
    "course": "koos", "cream": "kriim", "cut": "kat", "damage": "DA-midj", "damp": "damp",
    "dance": "daans", "dark": "daak", "date": "deit", "dead": "ded", "debit": "DE-bit",
    "dearer": "DIƏ-rə", "declining": "di-KLAI-ning", "delicious": "di-LI-shəs",
    "delivery": "di-LI-və-ri", "depends": "di-PENDZ", "described": "di-SKRAIBD",
    "designer": "di-ZAI-nə", "developed": "di-VE-ləpt", "dickens": "DI-kinz", "died": "daid",
    "difference": "DI-frəns", "dispute": "di-SPYUUT", "double": "DA-bəl",
    "downstairs": "daun-STEƏZ", "drafted": "DRAAF-tid", "dressed": "drest",
    "driver": "DRAI-və", "driving": "DRAI-ving", "dry": "drai", "due": "dyuu",
    "effect": "i-FEKT", "eggs": "egz", "electric": "i-LEK-trik", "elephant": "E-li-fənt",
    "emphasis": "EM-fə-sis", "employed": "im-PLOID", "end": "end",
    "engineering": "en-dji-NIƏ-ring", "enough": "i-NAF", "equal": "II-kwəl",
    "error": "E-rə", "essay": "E-sei", "estate": "i-STEIT", "everyone": "EV-ri-wan",
    "everything": "EV-ri-thing", "example": "ig-ZAAM-pəl", "exams": "ig-ZAMZ",
    "excellent": "EK-sə-lənt", "excuse": "ik-SKYUUZ", "exit": "EK-sit",
    "expensive": "ik-SPEN-siv", "experience": "ik-SPIƏ-ri-əns", "explains": "ik-SPLEINZ",
    "extent": "ik-STENT", "fact": "fakt", "failed": "feild", "fair": "feə",
    "faithfully": "FEITH-fə-li", "fall": "fool", "false": "fools", "families": "FA-mə-liz",
    "famous": "FEI-məs", "fancy": "FAN-si", "farm": "faam", "fast": "faast",
    "favourite": "FEI-və-rit", "fed": "fed", "fell": "fel", "field": "fiild",
    "filling": "FI-ling", "fine": "fain", "finish": "FI-nish", "fireworks": "FAIƏ-wəəks",
    "flexible": "FLEK-sə-bəl", "flowers": "FLAUƏZ", "foot": "fut", "force": "foos",
    "formal": "FOO-məl", "forward": "FOO-wəd", "founded": "FAUN-did", "fresh": "fresh",
    "friendly": "FREND-li", "fruit": "fruut", "fry": "frai", "full": "ful", "fun": "fan",
    "future": "FYUU-chə", "glass": "glaas", "grandad": "GRAN-dad", "grandmother": "GRAN-ma-dhə",
    "grew": "gruu", "guests": "gests", "guilty": "GIL-ti", "guy": "gai", "haggis": "HA-gis",
    "half": "haaf", "hand": "hand", "hang": "hang", "head": "hed", "heavy": "HE-vi",
    "helped": "helpt", "henry": "HEN-ri", "history": "HIS-tə-ri", "hit": "hit",
    "holding": "HƏUL-ding", "hospitals": "HOS-pi-təlz", "hour": "auə", "housing": "HAU-zing",
    "huge": "hyuudj", "humour": "HYUU-mə", "hurry": "HA-ri", "ice": "ais", "idea": "ai-DIƏ",
    "important": "im-POO-tənt", "included": "in-KLUU-did", "industrial": "in-DA-stri-əl",
    "insisted": "in-SI-stid", "inspired": "in-SPAIƏD", "interrupt": "in-tə-RAPT",
    "introduce": "in-trə-DYUUS", "invest": "in-VEST", "invoice": "IN-vois", "island": "AI-lənd",
    "issue": "I-shuu", "jacket": "DJA-kit", "jam": "djam", "jobs": "djobz", "joke": "djəuk",
    "jury": "DJUƏ-ri", "kent": "kent", "kept": "kept", "kind": "kaind", "king": "king",
    "kingdom": "KING-dəm", "lager": "LAA-gə", "language": "LANG-gwidj", "large": "laadj",
    "later": "LEI-tə", "learning": "LƏƏ-ning", "leaves": "liivz", "leeds": "liidz",
    "leg": "leg", "lend": "lend", "licence": "LAI-səns", "light": "lait", "limit": "LI-mit",
    "line": "lain", "lip": "lip", "list": "list", "listen": "LI-sən", "lively": "LAIV-li",
    "living": "LI-ving", "lot": "lot", "lovely": "LAV-li", "magna": "MAG-nə", "main": "mein",
    "major": "MEI-djə", "market": "MAA-kit", "matter": "MA-tə", "meal": "miil",
    "mean": "miin", "medical": "ME-di-kəl", "middle": "MI-dəl", "mind": "maind",
    "minister": "MI-ni-stə", "minutes": "MI-nits", "modern": "MO-dən", "months": "manths",
    "morris": "MO-ris", "musical": "MYUU-zi-kəl", "myself": "mai-SELF", "nail": "neil",
    "nations": "NEI-shənz", "nearly": "NIƏ-li", "negative": "NE-gə-tiv", "net": "net",
    "news": "nyuuz", "noon": "nuun", "nurses": "NƏƏ-siz", "offence": "ə-FENS",
    "offer": "O-fə", "once": "wans", "online": "on-LAIN", "order": "OO-də",
    "outgoing": "aut-GƏU-ing", "owns": "əunz", "oxford": "OKS-fəd", "packed": "pakt",
    "park": "paak", "part": "paat", "passed": "paast", "past": "paast", "patience": "PEI-shəns",
    "pays": "peiz", "peer": "piə", "perfect": "PƏƏ-fikt", "perhaps": "pə-HAPS",
    "phone": "fəun", "photography": "fə-TO-grə-fi", "piece": "piis", "plan": "plan",
    "pleasure": "PLE-zhə", "point": "point", "policy": "PO-lə-si", "political": "pə-LI-ti-kəl",
    "politics": "PO-lə-tiks", "poppies": "PO-piz", "popular": "PO-pyə-lə",
    "positive": "PO-zi-tiv", "potato": "pə-TEI-təu", "prefer": "pri-FƏƏ",
    "present": "PRE-zənt", "pressure": "PRE-shə", "price": "prais", "prime": "praim",
    "priority": "prai-O-rə-ti", "problem": "PRO-bləm", "promises": "PRO-mi-siz",
    "protects": "prə-TEKTS", "public": "PA-blik", "pupils": "PYUU-pəlz",
    "question": "KWES-chən", "quick": "kwik", "quiz": "kwiz", "rained": "reind",
    "rate": "reit", "reading": "RII-ding", "really": "RIƏ-li", "reduce": "ri-DYUUS",
    "referee": "re-fə-RII", "refused": "ri-FYUUZD", "reliable": "ri-LAI-ə-bəl",
    "repeats": "ri-PIITS", "report": "ri-POOT", "resign": "ri-ZAIN", "respect": "ri-SPEKT",
    "result": "ri-ZALT", "return": "ri-TƏƏN", "revolution": "re-və-LUU-shən", "rings": "ringz",
    "rise": "raiz", "ritz": "rits", "river": "RI-və", "rules": "ruulz", "safety": "SEIF-ti",
    "save": "seiv", "scots": "skots", "season": "SII-zən", "seat": "siit", "seeing": "SII-ing",
    "send": "send", "serious": "SIƏ-ri-əs", "shareholders": "SHEƏ-həul-dəz",
    "shocking": "SHO-king", "showed": "shəud", "shy": "shai", "side": "said", "signed": "saind",
    "silence": "SAI-ləns", "simple": "SIM-pəl", "sincerely": "sin-SIƏ-li", "singing": "SING-ing",
    "sky": "skai", "sleeps": "sliips", "slow": "sləu", "snow": "snəu", "soap": "səup",
    "social": "SƏU-shəl", "solar": "SƏU-lə", "something": "SAM-thing", "sore": "soo",
    "sound": "saund", "soup": "suup", "spare": "speə", "species": "SPII-shiiz",
    "speech": "spiich", "speed": "spiid", "spend": "spend", "spill": "spil", "square": "skweə",
    "staff": "staaf", "state": "steit", "steak": "steik", "stick": "stik", "stiff": "stif",
    "storm": "stoom", "straight": "streit", "strange": "streindj", "strong": "strong",
    "stuck": "stak", "student": "STYUU-dənt", "success": "sək-SES", "sugar": "SHU-gə",
    "suppose": "sə-PƏUZ", "swim": "swim", "system": "SIS-təm", "table": "TEI-bəl",
    "task": "taask", "text": "tekst", "thank": "thangk", "thief": "thiif", "thou": "dhau",
    "threatens": "THRE-tənz", "throat": "thrəut", "tie": "tai", "toast": "təust", "tom": "tom",
    "tongue": "tang", "tower": "TAUƏ", "trade": "treid", "traffic": "TRA-fik", "tree": "trii",
    "tried": "traid", "twice": "twais", "typical": "TI-pi-kəl", "understood": "an-də-STUD",
    "united": "yuu-NAI-tid", "upper": "A-pə", "upstairs": "ap-STEƏZ", "values": "VAL-yuuz",
    "view": "vyuu", "villages": "VI-li-djiz", "viii": "eithth", "voice": "vois",
    "watch": "woch", "wearing": "WEƏ-ring", "welcome": "WEL-kəm", "well": "wel",
    "west": "west", "wet": "wet", "whole": "həul", "wind": "wind", "won": "wan",
    "word": "wəəd", "working": "WƏƏ-king", "worry": "WA-ri", "writing": "RAI-ting",
    "york": "yook", "yorkshire": "YOO-shə", "carta": "KAA-tə", "tuesdays": "TYUUZ-deiz",
    "sundays": "SAN-deiz", "e": "ii", "j": "djei", "fi": "fai", "wi": "wai",
})

OVR.update({
    "biscuits": "BIS-kits", "bedrooms": "BED-ruumz", "cambridge": "KEIM-bridj",
    "camden": "KAM-dən", "carefully": "KEƏ-fə-li", "colleagues": "KO-liigz",
    "deafening": "DE-fə-ning", "decker": "DE-kə", "denied": "di-NAID", "fawkes": "fooks",
    "gcses": "djii-sii-es-IIZ", "global": "GLƏU-bəl", "growing": "GRƏU-ing", "join": "djoin",
    "languages": "LANG-gwi-djiz", "liverpool": "LI-və-puul", "looking": "LU-king",
    "lucas": "LUU-kəs", "matches": "MA-chiz", "message": "ME-sidj", "mobility": "məu-BI-lə-ti",
    "monty": "MON-ti", "northern": "NOO-dhən", "operas": "O-prəz", "option": "OP-shən",
    "packet": "PA-kit", "pancake": "PAN-keik", "pancakes": "PAN-keiks", "passive": "PA-siv",
    "per": "pə", "persuaded": "pə-SWEI-did", "pleaded": "PLII-did", "post": "pəust",
    "pronunciation": "prə-nan-si-EI-shən", "provided": "prə-VAI-did", "pursuant": "pə-SYUU-ənt",
    "raining": "REI-ning", "received": "ri-SIIVD", "receives": "ri-SIIVZ", "reckon": "REK-ən",
    "redundancies": "ri-DAN-dən-siz", "remembers": "ri-MEM-bəz", "remembrance": "ri-MEM-brəns",
    "repetition": "re-pə-TI-shən", "represents": "re-pri-ZENTS", "resigned": "ri-ZAIND",
    "services": "SƏƏ-vi-siz", "shows": "shəuz", "slowly": "SLƏU-li", "smith": "smith",
    "sonnets": "SO-nits", "studies": "STA-diz", "studying": "STA-di-ing",
    "successful": "sək-SES-fəl", "suffers": "SA-fəz", "supply": "sə-PLAI", "support": "sə-POOT",
    "supports": "sə-POOTS", "tabloids": "TA-bloidz", "taxes": "TAK-siz", "teacup": "TII-kap",
    "terraced": "TE-rəst", "terrible": "TE-rə-bəl", "times": "taimz", "transport": "TRANS-poot",
    "trooping": "TRUU-ping", "understandable": "an-də-STAN-də-bəl", "update": "AP-deit",
    "voted": "VƏU-tid", "warming": "WOO-ming", "warned": "woond", "watched": "wocht",
    "westminster": "WEST-min-stə", "whales": "weilz", "wordsworth": "WƏƏDZ-wəəth",
    "writes": "raits", "visits": "VI-zits", "takes": "teiks", "rising": "RAI-zing",
    "risen": "RI-zən", "teaching": "TII-ching", "drivers": "DRAI-vəz", "exports": "EK-spoots",
    "imports": "IM-poots", "estates": "i-STEITS", "cakes": "keiks", "cars": "kaaz",
    "corners": "KOO-nəz", "brothers": "BRA-dhəz", "dancing": "DAAN-sing", "danced": "daanst",
    "ending": "EN-ding", "ended": "EN-did", "finishing": "FI-ni-shing", "finished": "FI-nisht",
    "falling": "FOO-ling", "footprint": "FUT-print", "handled": "HAN-dəld", "paying": "PEI-ing",
    "passing": "PAA-sing", "rush": "rash", "reached": "riicht", "raised": "reizd", "runs": "ranz",
    "sent": "sent", "self": "self", "semi": "SE-mi", "set": "set", "python": "PAI-thən",
    "quickly": "KWIK-li", "loudly": "LAUD-li", "clearly": "KLIƏ-li", "breaking": "BREI-king",
    "calling": "KOO-ling", "changing": "CHEIN-djing", "collects": "kə-LEKTS", "cooks": "kuks",
    "bits": "bits", "avoids": "ə-VOIDZ", "ends": "endz", "disrupted": "dis-RAP-tid",
    "devastating": "DE-və-stei-ting", "month's": "manths", "opens": "ƏU-pənz",
    "putting": "PU-ting", "sitting": "SI-ting", "shopping": "SHO-ping", "walking": "WOO-king",
    "waiting": "WEI-ting", "stronger": "STRONG-gə", "thanks": "thangks",
    "speaks": "spiiks", "starts": "staats", "teas": "tiiz", "trains": "treinz",
    "lights": "laits", "limits": "LI-mits", "plans": "planz", "rains": "reinz",
    "results": "ri-ZALTS", "nights": "naits", "levels": "LE-vəlz", "lasts": "laasts",
    "meets": "miits", "helps": "helps", "costs": "kosts", "dogs": "dogz", "cats": "kats",
    "scandals": "SKAN-dəlz", "spent": "spent",
})

# Palabras registradas desde el léxico del curso (se llena con register()).
_USER = {}

VOWELS = "aeiou"

# Marcadores privados para vocales largas del patrón «vocal + consonante + e».
_MAGIC = {"a": "\ue000", "i": "\ue001", "o": "\ue002", "u": "\ue003"}
_MAGIC_OUT = {"\ue000": "ei", "\ue001": "ai", "\ue002": "əu", "\ue003": "yuu"}

_RULES = [
    (r"tch", "ch"), (r"dge", "dj"), (r"ch", "ch"), (r"sh", "sh"), (r"ph", "f"), (r"th", "th"),
    (r"ck", "k"), (r"ng(?![a-z])", "ng"), (r"nk", "ngk"), (r"wh", "w"),
    (r"(?<![a-z])kn", "n"), (r"(?<![a-z])wr", "r"), (r"igh", "ai"),
    (r"tion(?![a-z])", "shən"), (r"sion(?![a-z])", "zhən"), (r"ture(?![a-z])", "chə"),
    (r"qu", "kw"), (r"x", "ks"), (r"c(?=[eiy])", "s"), (r"c", "k"), (r"j", "dj"),
    (r"ee", "ii"), (r"ea", "ii"), (r"oo", "uu"), (r"ou", "au"), (r"ow", "au"), (r"oa", "əu"),
    (r"ai", "ei"), (r"ay", "ei"), (r"oi", "oi"), (r"oy", "oi"), (r"au", "oo"), (r"aw", "oo"),
    (r"ie", "ii"), (r"ey(?![a-z])", "i"), (r"ey", "ei"),
    (r"er(?![a-z])", "ə"), (r"ar", "aa"), (r"or", "oo"), (r"(?:ur|ir|er)", "əə"),
    (r"(?<![a-z])y", "y"), (r"y(?![a-z])", "i"), (r"y", "i"),
    (r"(?<=[a-z]{2})ed(?![a-z])", "d"), (r"(?<=[a-z][^aeiou])e(?![a-z])", ""),
    (r"(?<=[aeioubdgvlmnrwyz])s(?![a-z])", "z"),
    (r"a", "a"), (r"e", "e"), (r"i", "i"), (r"o", "o"), (r"u", "a"),
]
_COMPILED = [(re.compile(p), r) for p, r in _RULES]


def register(word, pr):
    """Guarda la pronunciación de una palabra del léxico para usarla dentro de oraciones."""
    word = word.strip().lower()
    if word and " " not in word and pr:
        _USER.setdefault(word, pr)


def _guess(word):
    """Respelling aproximado de una palabra regular (sin sílaba tónica marcada)."""
    w = re.sub(r"([bdfgklmnprstvz])\1", r"\1", word)
    m = re.search(r"([aiou])([bcdfgklmnprstvz])e$", w)
    if m:
        w = w[: m.start()] + _MAGIC[m.group(1)] + m.group(2)
    else:
        m = re.search(r"([aiou])([bdgkpt])le$", w)
        if m:
            w = w[: m.start()] + _MAGIC[m.group(1)] + m.group(2) + "əl"
    out, i = [], 0
    while i < len(w):
        ch = w[i]
        if ch in _MAGIC_OUT:
            out.append(_MAGIC_OUT[ch])
            i += 1
            continue
        for pat, rep in _COMPILED:
            hit = pat.match(w, i)
            if hit and hit.end() > i:
                out.append(rep)
                i = hit.end()
                break
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def _known(key):
    return key in OVR or key in _USER


def _derived(key):
    """Pronunciación de formas con -s, -'s, -ing o -ed cuando la base ya está registrada."""
    if key.endswith("'s") and _known(key[:-2]):
        base = _word(key[:-2])
        return base + ("iz" if base[-1:] in "sz" else "z")
    if key.endswith("s") and len(key) > 3 and _known(key[:-1]):
        base = _word(key[:-1])
        if base[-1:] in "sz" or base.endswith(("sh", "ch", "dj")):
            return base + "iz"
        return base + ("s" if base[-1:] in "ptkf" or base.endswith("th") else "z")
    if key.endswith("ing") and len(key) > 5:
        stem = key[:-3]
        for cand in (stem, stem + "e", stem[:-1] if stem[-1:] == stem[-2:-1] else ""):
            if cand and _known(cand):
                return _word(cand) + "ing"
    if key.endswith("ed") and len(key) > 4:
        stem = key[:-2]
        for cand in (stem, stem + "e", stem[:-1] if stem[-1:] == stem[-2:-1] else ""):
            if cand and _known(cand):
                base = _word(cand)
                if base[-1:] in "td":
                    return base + "id"
                if base[-1:] in "pkfs" or base.endswith(("sh", "ch")):
                    return base + "t"
                return base + "d"
    return None


def _word(token):
    key = token.lower()
    if key in OVR:
        return OVR[key]
    if key in _USER:
        return _USER[key]
    derived = _derived(key)
    if derived:
        return derived
    return _guess(re.sub(r"[^a-z']", "", key).replace("'", ""))


def pron(text):
    """Guía de pronunciación de una palabra, frase u oración en inglés británico."""
    tokens = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*", text.replace("’", "'"))
    return " ".join(_word(t) for t in tokens)


def missing(text):
    """Palabras de un texto que no están en OVR ni registradas (para revisar a mano)."""
    tokens = re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*", text.replace("’", "'"))
    return [
        t.lower()
        for t in tokens
        if not _known(t.lower()) and not _derived(t.lower())
    ]
