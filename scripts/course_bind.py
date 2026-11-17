"""Clases de C1 y C2 y el ensamblado de los niveles A2 a C2 del curso de inglés británico."""

from course_upper import A2_SPECS, B1_SPECS, B2_SPECS, D, L, Q, bind

# --- C1 ---------------------------------------------------------------------

C1_SPECS = [
    L(
        "Conectores formales",
        "Nonetheless, notwithstanding, whereas y la precisión del registro escrito.",
        [
            "En el registro escrito y en el debate, but y so se quedan cortos. Nonetheless y notwithstanding marcan oposición con peso formal: Nonetheless, the plan succeeded. Notwithstanding se usa antes de un sustantivo: notwithstanding the cost. Hence significa «de ahí que» y suele ir sin verbo conjugado: Hence the delay.",
            "Whereas contrasta dos hechos en la misma frase: Jack likes tea, whereas Anna prefers coffee. Albeit es «aunque» en estilo elevado: a small, albeit significant, change. Moreover y furthermore suman argumentos con tono académico. Thereby indica el resultado de una acción: He signed the contract, thereby accepting the terms.",
            "En un texto formal británico se evita sobrecargar de conectores. Uno bien puesto vale más que cinco mal elegidos. Leé la prensa seria, como The Guardian o The Times, y vas a ver cómo se usan.",
        ],
        [
            ("nonetheless", "no obstante; sin embargo", "The task was hard; nonetheless, we finished.", "La tarea era difícil; no obstante, la terminamos.", "na-nə-DHES"),
            ("notwithstanding", "a pesar de", "Notwithstanding the weather, the match went ahead.", "A pesar del clima, el partido se jugó.", "not-wi-DHSTAN-ding"),
            ("hence", "de ahí que; por eso", "The road was closed, hence the delay.", "La ruta estaba cortada, de ahí la demora.", "hens"),
            ("whereas", "mientras que", "He is shy, whereas she is outgoing.", "Él es tímido, mientras que ella es extrovertida.", "weər-AZ"),
            ("albeit", "aunque; si bien", "It was a success, albeit a small one.", "Fue un éxito, aunque pequeño.", "ool-BII-it"),
            ("moreover", "además; es más", "Moreover, the price is very fair.", "Además, el precio es muy justo.", "moor-ƏU-və"),
            ("furthermore", "asimismo; por otra parte", "Furthermore, the results are reliable.", "Asimismo, los resultados son fiables.", "fəə-dhə-MOO"),
            ("thereby", "con lo cual; de ese modo", "He resigned, thereby ending the dispute.", "Renunció, con lo cual terminó la disputa.", "dheə-BAI"),
        ],
        quiz=[
            Q("Whereas introduce…", "un contraste", "una causa", "un ejemplo", "una pregunta"),
            Q("Notwithstanding significa…", "a pesar de", "gracias a", "durante", "después de"),
            Q("Moreover equivale a…", "además", "mientras", "sin embargo", "por lo tanto"),
            Q("Albeit es un sinónimo formal de…", "although", "because", "unless", "perhaps"),
            Q("Thereby indica…", "el resultado de una acción", "un deseo", "una condición", "un lugar"),
        ],
    ),
    L(
        "Lenguaje jurídico",
        "Contract, clause, solicitor, barrister y el sistema legal inglés.",
        [
            "Un contract tiene clauses, cláusulas, y se firma ante un solicitor, el abogado que asesora a clientes y prepara documentos. El barrister es el abogado que litiga ante los tribunales superiores; usa peluca y toga en las audiencias. La distinción entre solicitor y barrister no existe en América Latina.",
            "Si hay un conflicto, se va al tribunal. En el proceso hay un defendant (acusado) y se llega a un verdict, la decisión del jurado. Cuando alguien es liable, es legalmente responsable. La legislation es el conjunto de leyes que sanciona el Parlamento. Un tribunal laboral es un employment tribunal.",
            "El lenguaje legal inglés conserva fórmulas muy antiguas, pero hay un movimiento por simplificarlo, el «Plain English». Una cláusula típica de contrato: «The tenant shall pay the rent monthly in advance».",
        ],
        [
            ("contract", "contrato", "I signed the contract yesterday.", "Firmé el contrato ayer.", "KON-trakt"),
            ("clause", "cláusula", "Read clause five carefully.", "Leé con cuidado la cláusula cinco.", "klooz"),
            ("tribunal", "tribunal", "The tribunal will decide next month.", "El tribunal decidirá el mes próximo.", "trai-BYUU-nəl"),
            ("solicitor", "abogado (asesor)", "My solicitor drafted the contract.", "Mi abogado redactó el contrato.", "sə-LI-si-tə"),
            ("barrister", "abogado litigante", "The barrister addressed the court.", "El abogado litigante se dirigió al tribunal.", "BA-ri-stə"),
            ("verdict", "veredicto", "The jury reached a verdict.", "El jurado llegó a un veredicto.", "VƏƏ-dikt"),
            ("liable", "responsable legalmente", "The company is liable for the damage.", "La empresa es responsable por el daño.", "LAI-ə-bəl"),
            ("legislation", "legislación", "New legislation comes into force in April.", "Una nueva legislación entra en vigor en abril.", "le-dji-SLEI-shən"),
            ("defendant", "acusado; demandado", "The defendant pleaded not guilty.", "El acusado se declaró inocente.", "di-FEN-dənt"),
        ],
    ),
    L(
        "Economía avanzada",
        "Austerity, deficit, fiscal, GDP y el lenguaje de los mercados.",
        [
            "Un país puede tener deficit o surplus en su presupuesto. La austerity es una política de recorte del gasto público; en Gran Bretaña se aplicó con fuerza tras la crisis de 2008. La política fiscal (fiscal) se refiere a impuestos y gasto del Estado. El GDP, o PBI, mide la riqueza producida en un año.",
            "La moneda se llama sterling, la libra esterlina. Cuando los diarios hablan de «the pound» en los mercados, se refieren a ella. El interest rate es la tasa de interés, fijada por el Bank of England. Un tariff es un arancel, el impuesto que se cobra por las importaciones.",
            "Un ejemplo de titular: «Sterling falls as GDP figures disappoint». Aprender este lenguaje te permite leer el Financial Times y seguir debates económicos con seguridad.",
        ],
        [
            ("austerity", "austeridad", "Austerity cut many public services.", "La austeridad recortó muchos servicios públicos.", "o-STE-rə-ti"),
            ("deficit", "déficit", "The country has a large deficit.", "El país tiene un déficit grande.", "DE-fi-sit"),
            ("surplus", "superávit; excedente", "They announced a budget surplus.", "Anunciaron un superávit presupuestario.", "SƏƏ-pləs"),
            ("fiscal", "fiscal", "The government changed its fiscal policy.", "El gobierno cambió su política fiscal.", "FIS-kəl"),
            ("GDP", "PBI; producto bruto", "GDP grew by one per cent.", "El PBI creció un uno por ciento.", "djii-dii-PII"),
            ("interest rate", "tasa de interés", "The interest rate is now five per cent.", "La tasa de interés es ahora del cinco por ciento.", "IN-trəst reit"),
            ("sterling", "libra esterlina", "Sterling is stronger today.", "La libra esterlina está más fuerte hoy.", "STƏƏ-ling"),
            ("tariff", "arancel", "The tariff makes imports dearer.", "El arancel encarece las importaciones.", "TA-rif"),
        ],
    ),
    L(
        "Ideas y filosofía",
        "Ethics, liberty, justice y la tradición empirista británica.",
        [
            "La ethics orienta la decisión sobre qué está bien o mal. La liberty y la justice son valores que se discuten sin fin. La conscience es lo que sabe que algo está bien o mal; también existe el sentido de «conciencia» como estar enterado, que se dice consciousness. Una notion es una idea vaga o general.",
            "Los filósofos británicos fundaron una tradición importante: el empiricism de Locke, Hume y Berkeley sostiene que el conocimiento viene de la experiencia. El scepticism (escrito con «c» en inglés británico; en Estados Unidos, skepticism) es la actitud de dudar de lo que no se puede probar. Una virtue es una cualidad moral.",
            "Una frase típica de un ensayo: «Hume's scepticism undermines the notion of causality». Este vocabulario te sirve para leer a los pensadores británicos en su idioma original.",
        ],
        [
            ("ethics", "ética", "Medical ethics is a complex field.", "La ética médica es un campo complejo.", "E-thiks"),
            ("liberty", "libertad", "Liberty has limits.", "La libertad tiene límites.", "LI-bə-ti"),
            ("justice", "justicia", "Justice must be equal for all.", "La justicia debe ser igual para todos.", "DJA-stis"),
            ("conscience", "conciencia moral", "He has a clear conscience.", "Tiene la conciencia tranquila.", "KON-shəns"),
            ("notion", "noción; idea", "It's a strange notion.", "Es una idea extraña.", "NƏU-shən"),
            ("virtue", "virtud", "Patience is a virtue.", "La paciencia es una virtud.", "VƏƏ-chuu"),
            ("scepticism", "escepticismo", "Her scepticism was understandable.", "Su escepticismo era comprensible.", "SKEP-ti-si-zəm"),
            ("empiricism", "empirismo", "Empiricism values experience.", "El empirismo valora la experiencia.", "em-PI-ri-si-zəm"),
        ],
        quiz=[
            Q("Scepticism con «c» es la ortografía…", "británica", "norteamericana", "alemana", "francesa"),
            Q("Empiricism sostiene que el conocimiento viene de…", "la experiencia", "la razón pura", "la fe", "la tradición"),
            Q("Conscience es…", "la conciencia moral", "la ciencia", "la consciencia física", "la conferencia"),
            Q("Virtue significa…", "virtud", "virus", "viaje", "valor monetario"),
            Q("Liberty es…", "libertad", "libro", "libertinaje", "librería"),
        ],
    ),
    L(
        "Matices del discurso",
        "Nuance, connotation, understatement y el arte de decir sin decir.",
        [
            "En C1 se espera que captés los matices. Una nuance es una diferencia sutil. Subtle significa sutil, delicado. La connotation es el sentido adicional que una palabra carga además de su significado literal: «home» y «house» denotan lo mismo pero connotan cosas distintas. Un euphemism es una forma suave de decir algo duro: «passed away» en vez de «died».",
            "El humor británico se apoya en el understatement, quitarle importancia a algo importante: «It's a bit damp» para una tormenta. El estilo tongue-in-cheek es dicho en broma, sin que se note, y el deadpan es contar un chiste con cara seria. Una inference es lo que deducís de lo que se dice, sin que se diga.",
            "El peligro para un hispanohablante es tomar todo literal. Si un inglés dice «That's an interesting idea», puede significar «No me convence». Aprender a leer entre líneas es parte esencial del nivel C1.",
        ],
        [
            ("subtle", "sutil", "There is a subtle difference.", "Hay una diferencia sutil.", "SA-təl"),
            ("nuance", "matiz", "She understood every nuance.", "Entendió cada matiz.", "NYUU-aans"),
            ("connotation", "connotación", "The word has a negative connotation.", "La palabra tiene una connotación negativa.", "ko-nə-TEI-shən"),
            ("euphemism", "eufemismo", "'Passed away' is a euphemism for 'died'.", "'Passed away' es un eufemismo de 'died'.", "YUU-fə-mi-zəm"),
            ("understatement", "subestimación deliberada", "'A bit damp' is a typical understatement.", "'Un poco húmedo' es una subestimación típica.", "an-də-STEIT-mənt"),
            ("tongue-in-cheek", "en broma; con ironía", "It was a tongue-in-cheek comment.", "Fue un comentario en tono de broma.", "tang-in-CHIIK"),
            ("deadpan", "inexpresivo (humor)", "He told the joke completely deadpan.", "Contó el chiste con total seriedad.", "DED-pan"),
            ("inference", "inferencia; deducción", "That's a fair inference.", "Es una deducción razonable.", "IN-fə-rəns"),
        ],
    ),
    L(
        "Escritura académica",
        "Thesis, dissertation, footnote y el estilo de un trabajo universitario.",
        [
            "Escribir en un entorno universitario británico sigue convenciones precisas. Un trabajo final de grado se llama dissertation, y una tesis doctoral es una thesis. Cada uno incluye un abstract, el resumen inicial. Al final aparece la bibliography, la lista de fuentes consultadas, y en el cuerpo se agregan footnotes, notas a pie de página.",
            "La methodology explica cómo se hizo la investigación. Antes de entregar hay que proofread, es decir, releer buscando errores. Y hay una falta grave: el plagiarism, copiar sin citar, que puede llevar a la expulsión.",
            "El estilo académico británico es impersonal: se prefiere «It can be argued that…» a «I think that…». Un ejemplo: «This dissertation examines the impact of austerity on local services».",
        ],
        [
            ("thesis", "tesis", "She is writing her thesis.", "Está escribiendo su tesis.", "THII-sis"),
            ("abstract", "resumen (de un trabajo)", "Write a short abstract first.", "Primero escribí un resumen breve.", "AB-strakt"),
            ("dissertation", "trabajo final; tesina", "My dissertation is due in May.", "Mi trabajo final es para mayo.", "di-sə-TEI-shən"),
            ("bibliography", "bibliografía", "Add the book to your bibliography.", "Agregá el libro a tu bibliografía.", "bi-bli-O-grə-fi"),
            ("footnote", "nota al pie", "The footnote explains the date.", "La nota al pie explica la fecha.", "FUT-nəut"),
            ("methodology", "metodología", "The methodology is clearly described.", "La metodología está claramente descrita.", "me-thə-DO-lə-dji"),
            ("proofread", "revisar; corregir pruebas", "Please proofread your essay.", "Por favor, corregí tu ensayo.", "PRUUF-riid"),
            ("plagiarism", "plagio", "Plagiarism is a serious offence.", "El plagio es una falta grave.", "PLEI-djə-ri-zəm"),
        ],
        quiz=[
            Q("Plagiarism es…", "copiar sin citar", "una forma de citar", "un tipo de tesis", "una nota al pie"),
            Q("Bibliography es…", "la lista de fuentes", "un libro de ficción", "un resumen", "un índice"),
            Q("Abstract en un trabajo es…", "el resumen inicial", "la conclusión", "el título", "un apéndice"),
            Q("Footnote es…", "una nota a pie de página", "un pie de foto", "una huella", "un apéndice"),
            Q("Dissertation en el Reino Unido es…", "un trabajo final", "una conferencia", "un debate", "una clase"),
        ],
    ),
    L(
        "Modismos útiles",
        "Piece of cake, under the weather, break the ice y las expresiones del día a día.",
        [
            "Los idioms son expresiones cuyo significado no se deduce de las palabras. Si alguien dice «It's a piece of cake», no habla de torta: significa que es muy fácil. «I'm under the weather» no es sobre el clima: dice que te sentís mal. Hay que aprenderlos como frases completas.",
            "Otros ejemplos con equivalente en español: bite the bullet (hacer algo difícil sin quejarse), spill the beans (contar un secreto), break the ice (romper el hielo en una situación incómoda), once in a blue moon (muy de vez en cuando), hit the nail on the head (dar en el clavo) y cost an arm and a leg (costar un ojo de la cara).",
            "Los británicos usan los idioms con naturalidad, a menudo con humor. Prestá atención a cómo se los usa en series como Fawlty Towers o The Office. Usarlos bien te hace sonar fluido; usarlos mal puede resultar cómico.",
        ],
        [
            ("a piece of cake", "pan comido; muy fácil", "The exam was a piece of cake.", "El examen fue pan comido.", "ə piis əv KEIK"),
            ("under the weather", "indispuesto; mal", "I'm a bit under the weather today.", "Hoy ando un poco indispuesto.", "AN-də dhə WE-dhə"),
            ("bite the bullet", "tragarse el orgullo; hacer lo difícil", "I just had to bite the bullet.", "Tuve que hacer de tripas corazón.", "bait dhə BU-lit"),
            ("spill the beans", "contar un secreto", "Don't spill the beans about the party.", "No cuentes el secreto de la fiesta.", "spil dhə BIINZ"),
            ("break the ice", "romper el hielo", "A joke helped to break the ice.", "Un chiste ayudó a romper el hielo.", "breik dhi AIS"),
            ("once in a blue moon", "muy de vez en cuando", "We go out once in a blue moon.", "Salimos muy de vez en cuando.", "wans in ə bluu MUUN"),
            ("hit the nail on the head", "dar en el clavo", "You hit the nail on the head.", "Diste en el clavo.", "hit dhə NEIL on dhə HED"),
            ("cost an arm and a leg", "costar un ojo de la cara", "That watch cost an arm and a leg.", "Ese reloj costó un ojo de la cara.", "kost ən AAM ənd ə LEG"),
        ],
        dialogue=D(
            ("How was the interview?", "¿Cómo fue la entrevista?"),
            ("A piece of cake! I think I hit the nail on the head.", "¡Pan comido! Creo que di en el clavo."),
            ("Well done! Don't spill the beans yet.", "¡Bien hecho! No cuentes el secreto todavía."),
            ("I won't. I'm still a bit under the weather.", "No voy a contarlo. Todavía ando algo indispuesto."),
            ("Take it easy. Let's celebrate once in a blue moon.", "Tomátelo con calma. Celebremos de vez en cuando."),
        ),
    ),
    L(
        "Historia británica",
        "Empire, Victorian, Tudor, the Blitz y los períodos que marcaron al país.",
        [
            "La historia británica tiene capítulos reconocidos. El período medieval, medieval, vio la firma de la Magna Carta en 1215, que limitó el poder del rey. La dinastía Tudor, con Enrique VIII e Isabel I, dejó una época de esplendor cultural. Una dynasty es una familia que gobierna durante varias generaciones.",
            "El empire británico llegó a ser el más grande de la historia, con colonias en todos los continentes. La era Victorian, durante el reinado de la reina Victoria (1837-1901), coincidió con la Industrial Revolution, que transformó la economía y la sociedad. Esa herencia imperial sigue siendo tema de debate hoy, en museos, escuelas y medios.",
            "En el siglo XX, el Blitz fue la campaña de bombardeos alemanes sobre Londres durante la Segunda Guerra Mundial. Es una época que los británicos recuerdan con orgullo y emoción. Una frase típica: «Keep calm and carry on», el lema de 1939.",
        ],
        [
            ("empire", "imperio", "The British Empire was huge.", "El Imperio Británico fue enorme.", "EM-paiə"),
            ("Victorian", "victoriano", "It's a lovely Victorian house.", "Es una hermosa casa victoriana.", "vik-TOO-ri-ən"),
            ("medieval", "medieval", "The castle is medieval.", "El castillo es medieval.", "me-DII-vəl"),
            ("Tudor", "Tudor (dinastía)", "Henry VIII was a Tudor king.", "Enrique VIII fue un rey Tudor.", "TYUU-də"),
            ("Industrial Revolution", "Revolución Industrial", "The Industrial Revolution began in Britain.", "La Revolución Industrial empezó en Gran Bretaña.", "in-DA-stri-əl re-və-LUU-shən"),
            ("Magna Carta", "Carta Magna", "Magna Carta was signed in 1215.", "La Carta Magna se firmó en 1215.", "MAG-nə KAA-tə"),
            ("Blitz", "bombardeo de Londres (1940-41)", "My grandmother remembers the Blitz.", "Mi abuela recuerda el Blitz.", "blits"),
            ("dynasty", "dinastía", "The Tudor dynasty ended in 1603.", "La dinastía Tudor terminó en 1603.", "DI-nə-sti"),
        ],
        quiz=[
            Q("Victorian se refiere a…", "la era de la reina Victoria", "una victoria militar", "una ciudad", "una calle"),
            Q("Magna Carta limitó…", "el poder del rey", "los impuestos locales", "la libertad religiosa", "el comercio"),
            Q("Blitz fue…", "una campaña de bombardeos sobre Londres", "una batalla naval", "una invasión", "una epidemia"),
            Q("Tudor es…", "una dinastía", "una ciudad", "un puente", "una universidad"),
            Q("Industrial Revolution empezó en…", "Gran Bretaña", "Francia", "Alemania", "España"),
        ],
    ),
    L(
        "Psicología y emociones",
        "Resilience, anxiety, empathy, burnout y el vocabulario del bienestar.",
        [
            "La salud mental ocupa mucho espacio en la conversación británica actual. La resilience es la capacidad de sobreponerse a las dificultades. La anxiety es la ansiedad, un problema muy frecuente. El burnout es el agotamiento extremo por exceso de trabajo y estrés.",
            "La empathy es ponerse en el lugar del otro. La motivation es lo que te mueve a actuar. Un mindset es una mentalidad, una forma habitual de pensar: growth mindset es la actitud de aprender de los errores. El wellbeing (bienestar) es la salud física y emocional en conjunto. Cope with significa afrontar un problema.",
            "En las empresas británicas se habla mucho de wellbeing: hay días de salud mental y espacios de descanso. Una frase útil: «I'm finding it hard to cope with the pressure», «Me cuesta afrontar la presión».",
        ],
        [
            ("resilience", "resiliencia", "Resilience helps in hard times.", "La resiliencia ayuda en tiempos difíciles.", "ri-ZI-li-əns"),
            ("anxiety", "ansiedad", "She suffers from anxiety.", "Sufre de ansiedad.", "ang-ZAI-ə-ti"),
            ("empathy", "empatía", "Empathy is key in teaching.", "La empatía es clave en la enseñanza.", "EM-pə-thi"),
            ("motivation", "motivación", "He lost his motivation.", "Perdió la motivación.", "məu-ti-VEI-shən"),
            ("burnout", "agotamiento extremo", "Burnout is common among nurses.", "El agotamiento extremo es común entre los enfermeros.", "BƏƏN-aut"),
            ("wellbeing", "bienestar", "Staff wellbeing is a priority.", "El bienestar del personal es una prioridad.", "wel-BII-ing"),
            ("mindset", "mentalidad", "A positive mindset helps.", "Una mentalidad positiva ayuda.", "MAIND-set"),
            ("cope", "afrontar; arreglárselas", "I can't cope with this pressure.", "No puedo afrontar esta presión.", "kəup"),
        ],
    ),
    L(
        "Sostenibilidad y ecología",
        "Biodiversity, net zero, emissions y el futuro del planeta.",
        [
            "El vocabulario ecológico avanza rápido. La biodiversity es la variedad de formas de vida, y la deforestation es la tala masiva de bosques. Las emissions son los gases que se liberan a la atmósfera, y un carbon footprint es la huella de carbono que deja cada persona o empresa.",
            "Las energías renewable (solar, eólica) reemplazan al carbón y al petróleo. El Reino Unido se comprometió a alcanzar net zero (cero emisiones netas) en 2050. La conservation busca proteger los espacios naturales. Y el landfill es el vertedero de basura, algo que se intenta reducir con el reciclaje.",
            "Son temas políticos de primer orden. Una frase típica de un informe: «We must reduce emissions to protect biodiversity». Seguir este vocabulario es indispensable para leer la prensa británica actual.",
        ],
        [
            ("biodiversity", "biodiversidad", "Biodiversity is declining fast.", "La biodiversidad está disminuyendo rápido.", "bai-əu-dai-VƏƏ-sə-ti"),
            ("deforestation", "deforestación", "Deforestation threatens many species.", "La deforestación amenaza a muchas especies.", "dii-fo-ri-STEI-shən"),
            ("emissions", "emisiones", "We must cut emissions.", "Tenemos que reducir las emisiones.", "i-MI-shənz"),
            ("renewable", "renovable", "Wind is a renewable energy.", "El viento es una energía renovable.", "ri-NYUU-ə-bəl"),
            ("net zero", "cero emisiones netas", "Britain aims for net zero by 2050.", "Gran Bretaña apunta a cero emisiones netas en 2050.", "net ZIƏ-rəu"),
            ("conservation", "conservación", "Conservation protects wildlife.", "La conservación protege la fauna.", "kon-sə-VEI-shən"),
            ("landfill", "vertedero", "Too much rubbish goes to landfill.", "Demasiada basura va al vertedero.", "LAND-fil"),
            ("carbon footprint", "huella de carbono", "Reduce your carbon footprint.", "Reducí tu huella de carbono.", "KAA-bən FUT-print"),
        ],
        quiz=[
            Q("Net zero significa…", "cero emisiones netas", "cero residuos", "cero impuestos", "cero población"),
            Q("Landfill es…", "un vertedero", "un tipo de energía", "una selva", "un río"),
            Q("Deforestation es…", "tala masiva de bosques", "reforestación", "contaminación del aire", "sequía"),
            Q("Renewable se dice de…", "energías que se renuevan", "cosas caras", "productos viejos", "residuos"),
            Q("Biodiversity es…", "la variedad de vida", "una enfermedad", "un tipo de combustible", "un parque"),
        ],
    ),
    L(
        "Cortesía y etiqueta",
        "Polite, tact, stiff upper lip y las reglas no escritas de la sociedad británica.",
        [
            "Ser polite es esencial en la vida británica. Courteous es más formal: «a courteous reply». El etiquette son las normas sociales. Un buen británico tiene tact, la habilidad de decir las cosas sin herir. Se pide perdón con apologise (ortografía británica con «s»), incluso cuando no es necesario.",
            "La stiff upper lip es una expresión que describe la contención emocional: no mostrar los sentimientos en público. Muchos ingleses son reserved, es decir, reservados; hablan poco de sí mismos con extraños. Ser blunt, es decir, muy directo, puede considerarse maleducado. Una situación awkward es incómoda, y los británicos hacen casi cualquier cosa para evitarla.",
            "Consejo cultural: si un inglés te dice «Perhaps you could…», puede significar «Hacelo ya». La cortesía británica es indirecta y vale la pena aprender a leerla.",
        ],
        [
            ("polite", "educado; cortés", "He is always very polite.", "Siempre es muy educado.", "pə-LAIT"),
            ("courteous", "cortés; atento", "The staff were courteous.", "El personal fue cortés.", "KƏƏ-ti-əs"),
            ("tact", "tacto", "She handled it with great tact.", "Lo manejó con mucho tacto.", "takt"),
            ("etiquette", "etiqueta; normas sociales", "It's bad etiquette to interrupt.", "Es mala educación interrumpir.", "E-ti-ket"),
            ("stiff upper lip", "contención emocional", "He kept a stiff upper lip.", "Mantuvo la compostura.", "stif A-pə LIP"),
            ("apologise", "disculparse; pedir perdón", "I must apologise for the delay.", "Debo disculparme por la demora.", "ə-PO-lə-djaiz"),
            ("awkward", "incómodo; torpe", "It was an awkward silence.", "Fue un silencio incómodo.", "OO-kwəd"),
            ("reserved", "reservado", "The English can be quite reserved.", "Los ingleses pueden ser bastante reservados.", "ri-ZƏƏVD"),
            ("blunt", "directo; brusco", "Don't be so blunt.", "No seas tan directo.", "blant"),
        ],
    ),
    L(
        "Retórica y oratoria",
        "Eloquent, rhetoric, rebuttal y cómo hablar en público con eficacia.",
        [
            "Hablar bien en público es una tradición muy respetada en Gran Bretaña, desde Churchill hasta el debate parlamentario. La rhetoric es el arte de persuadir con las palabras. Alguien eloquent habla con fluidez y fuerza. Alguien articulate expresa sus ideas con claridad.",
            "Un discurso eficaz es concise, es decir, breve y sin relleno, y coherent, con ideas ordenadas. Un argumento persuasive convence al público. Para destacar un punto se usa emphasise (con «s»). En un debate, el rebuttal es la respuesta que refuta al rival.",
            "Una técnica clásica de Churchill: la repetición. «We shall fight on the beaches, we shall fight on the landing grounds». Practicá en voz alta: la oratoria se aprende hablando.",
        ],
        [
            ("eloquent", "elocuente", "She gave an eloquent speech.", "Dio un discurso elocuente.", "E-lə-kwənt"),
            ("rhetoric", "retórica", "His rhetoric inspired many.", "Su retórica inspiró a muchos.", "RE-tə-rik"),
            ("concise", "conciso", "Please be concise.", "Por favor, sé conciso.", "kən-SAIS"),
            ("articulate", "que se expresa con claridad", "She is very articulate.", "Se expresa con mucha claridad.", "aa-TI-kyə-lət"),
            ("persuasive", "persuasivo", "It was a persuasive argument.", "Fue un argumento persuasivo.", "pə-SWEI-siv"),
            ("emphasise", "destacar; enfatizar", "I want to emphasise this point.", "Quiero destacar este punto.", "EM-fə-saiz"),
            ("rebuttal", "refutación", "His rebuttal was devastating.", "Su refutación fue devastadora.", "ri-BA-təl"),
            ("coherent", "coherente", "Make your argument coherent.", "Hacé que tu argumento sea coherente.", "kəu-HIƏ-rənt"),
        ],
        quiz=[
            Q("Concise significa…", "breve y claro", "largo y detallado", "confuso", "ruidoso"),
            Q("Rebuttal es…", "una refutación", "una promesa", "una felicitación", "un aplauso"),
            Q("Eloquent describe a alguien que…", "habla con fluidez y fuerza", "habla poco", "grita mucho", "habla despacio"),
            Q("Persuasive es…", "persuasivo", "persistente", "persona", "pesimista"),
            Q("Rhetoric es…", "el arte de persuadir", "una forma de bailar", "un tipo de poema", "una asignatura de matemática"),
        ],
    ),
]


# --- C2 ---------------------------------------------------------------------

C2_SPECS = [
    L(
        "Humor británico",
        "Irony, banter, wit, satire y la comedia como forma de vida.",
        [
            "El humor es el corazón de la cultura británica. La irony consiste en decir lo contrario de lo que se piensa, con un tono que deja ver la verdad. El sarcasm es más hiriente y directo. El banter es el intercambio de bromas entre amigos, que a veces suena a insulto pero es una muestra de afecto. Si un inglés te burla con cariño, es buena señal.",
            "El wit es el ingenio rápido, la gracia aguda. La satire se burla de la política y la sociedad con humor; programas como Have I Got News for You la practican desde hace décadas. Un pun es un juego de palabras, que los ingleses adoran aunque digan que es terrible. El dry humour es un humor seco, sin gestos, y los Monty Python son su máxima expresión absurda.",
            "Si no entendés una broma, no te preocupes: suele ser a propósito. Para el hispanohablante, la clave está en el tono, no en las palabras. Escuchá cómo se dicen las cosas más que lo que se dice.",
        ],
        [
            ("irony", "ironía", "There is a lot of irony in his speech.", "Hay mucha ironía en su discurso.", "AI-rə-ni"),
            ("sarcasm", "sarcasmo", "Her sarcasm was quite biting.", "Su sarcasmo era bastante mordaz.", "SAA-ka-zəm"),
            ("banter", "bromas entre amigos", "We enjoy a bit of banter at work.", "Nos gusta un poco de chanza en el trabajo.", "BAN-tə"),
            ("wit", "ingenio", "He is known for his quick wit.", "Es conocido por su ingenio rápido.", "wit"),
            ("satire", "sátira", "The show is a satire of politics.", "El programa es una sátira de la política.", "SA-taiə"),
            ("pun", "juego de palabras", "That was a terrible pun.", "Fue un juego de palabras terrible.", "pan"),
            ("dry humour", "humor seco", "She has a very dry humour.", "Tiene un humor muy seco.", "drai HYUU-mə"),
            ("Monty Python", "Monty Python (grupo de humor)", "We watched a Monty Python film.", "Vimos una película de Monty Python.", "MON-ti PAI-thən"),
        ],
        quiz=[
            Q("Banter es…", "bromas entre amigos", "una pelea seria", "un discurso formal", "un tipo de té"),
            Q("Satire se burla de…", "la política y la sociedad", "los animales", "los niños", "la comida"),
            Q("Pun es…", "un juego de palabras", "una pelea", "una poesía", "un golpe"),
            Q("Dry humour es…", "un humor seco, sin gestos", "un humor soso", "un humor infantil", "un humor ácido"),
            Q("Wit significa…", "ingenio", "oscuridad", "agua", "ruido"),
        ],
    ),
    L(
        "Subestimación y cortesía indirecta",
        "Not bad, I'm afraid, with respect y el arte de decir poco para decir mucho.",
        [
            "El understatement es la figura favorita del inglés: se dice menos de lo que se piensa. «Not bad» para una cosa excelente; «a bit of a problem» para un desastre; «quite good» para algo muy bueno, aunque en otros contextos quite puede significar «completamente». Hay que prestar atención al tono.",
            "Con I'm afraid se da una mala noticia sin sonar brusco: «I'm afraid I can't come». With respect abre un desacuerdo en un tono muy cortés, y a menudo significa «con todo respeto, estás equivocado». If you don't mind es un pedido suave. I suppose, dicho con duda, muchas veces significa «no, pero no te lo quiero decir».",
            "Rather es «bastante» y a menudo es un suavizador: «It's rather late». Y a bit es «un poco». Todo este sistema indirecto es la trampa más grande para un hispanohablante, acostumbrado a la franqueza. El truco: cuando un inglés es muy educado, a menudo está en desacuerdo.",
        ],
        [
            ("not bad", "bastante bien; muy bien", "'How was the film?' 'Not bad.'", "'¿Cómo estuvo la película?' 'No estuvo mal.'", "not BAD"),
            ("rather", "bastante; más bien", "It's rather cold today.", "Hoy hace bastante frío.", "RAA-dhə"),
            ("I'm afraid", "lamentablemente; me temo que", "I'm afraid I can't help.", "Me temo que no puedo ayudar.", "aim ə-FREID"),
            ("with respect", "con todo respeto", "With respect, I think you're wrong.", "Con todo respeto, creo que te equivocás.", "widh ri-SPEKT"),
            ("if you don't mind", "si no te molesta", "If you don't mind, I'll sit here.", "Si no te molesta, me siento acá.", "if yuu dəunt MAIND"),
            ("a bit", "un poco", "I'm a bit tired.", "Estoy un poco cansado.", "ə BIT"),
            ("I suppose", "supongo", "I suppose we could go.", "Supongo que podríamos ir.", "ai sə-PƏUZ"),
            ("quite", "bastante; completamente", "It was quite brilliant.", "Fue realmente brillante.", "kwait"),
        ],
    ),
    L(
        "Modismos de nivel avanzado",
        "Raining cats and dogs, back to square one y las expresiones que hay que saber.",
        [
            "Además de los idioms de C1, hay un segundo grupo muy usado. «It's raining cats and dogs» significa que llueve a cántaros. Una storm in a teacup es una tormenta en un vaso de agua, un alboroto por una tontería. «The ball is in your court» quiere decir que ahora te toca a vos decidir.",
            "Si alguien está barking up the wrong tree, está buscando donde no es: se equivocó de camino. Cut corners es hacer un trabajo mal, ahorrando esfuerzo. Get the wrong end of the stick es malinterpretar algo. Back to square one es empezar de nuevo, y the elephant in the room es un problema obvio que nadie nombra.",
            "Estos modismos conviene usarlos con medida: uno por conversación suena natural; cinco juntos, forzado. Escuchá cómo los usan los presentadores de la BBC y tomá nota.",
        ],
        [
            ("raining cats and dogs", "llover a cántaros", "It's raining cats and dogs outside.", "Afuera llueve a cántaros.", "REI-ning kats ənd DOGZ"),
            ("a storm in a teacup", "tormenta en un vaso de agua", "It was just a storm in a teacup.", "Fue solo una tormenta en un vaso de agua.", "ə stoom in ə TII-kap"),
            ("the ball is in your court", "ahora te toca a vos", "I've made my offer; the ball is in your court.", "Hice mi oferta; ahora te toca a vos.", "dhə bool iz in yoo KOOT"),
            ("barking up the wrong tree", "equivocarse de camino", "You're barking up the wrong tree.", "Estás buscando por donde no es.", "BAA-king ap dhə rong TRII"),
            ("cut corners", "hacer algo a medias", "Don't cut corners on safety.", "No hagas las cosas a medias con la seguridad.", "kat KOO-nəz"),
            ("get the wrong end of the stick", "malinterpretar", "I think you got the wrong end of the stick.", "Creo que entendiste mal.", "get dhə rong end əv dhə STIK"),
            ("back to square one", "volver a empezar", "We're back to square one.", "Estamos otra vez en el punto de partida.", "bak tə skweə WAN"),
            ("the elephant in the room", "el problema evidente que nadie nombra", "Money is the elephant in the room.", "La plata es el elefante en la habitación.", "dhi E-li-fənt in dhə RUUM"),
        ],
        dialogue=D(
            ("Did you finish the report?", "¿Terminaste el informe?"),
            ("I'm afraid we're back to square one.", "Me temo que estamos otra vez en el punto de partida."),
            ("I think you got the wrong end of the stick.", "Creo que entendiste mal."),
            ("Perhaps. But the ball is in your court now.", "Quizás. Pero ahora te toca a vos."),
            ("Fair enough. Let's not make a storm in a teacup.", "Está bien. No hagamos una tormenta en un vaso de agua."),
        ),
    ),
    L(
        "Registro formal",
        "Hereby, pursuant, kindly y la correspondencia oficial británica.",
        [
            "El inglés formal escrito tiene fórmulas fijas. En una carta de trabajo se usa kindly para pedir algo con cortesía: «Kindly confirm receipt». Regarding significa «con respecto a», y enclosed indica que se adjunta un documento: «Please find enclosed my CV».",
            "En contratos y documentos legales aparecen hereby (por la presente), aforementioned (antes mencionado) y pursuant to (conforme a). Para cerrar una carta británica hay una regla clara: si empezás con el nombre del destinatario (Dear Mr Smith), cerrás con Yours sincerely; si empezás con Dear Sir or Madam, cerrás con Yours faithfully. Y para una carta general se usa To whom it may concern.",
            "Esta regla distingue a los que dominan el inglés formal británico. En correos electrónicos de trabajo se usan fórmulas menos rígidas, como «Best wishes» o «Kind regards».",
        ],
        [
            ("hereby", "por la presente", "I hereby resign from my post.", "Por la presente renuncio a mi cargo.", "hiə-BAI"),
            ("aforementioned", "antes mencionado", "The aforementioned person is absent.", "La persona antes mencionada está ausente.", "ə-FOO-men-shənd"),
            ("pursuant to", "conforme a", "Pursuant to the contract, you must pay.", "Conforme al contrato, debe pagar.", "pə-SYUU-ənt tuu"),
            ("kindly", "amablemente; tenga a bien", "Kindly confirm your attendance.", "Tenga a bien confirmar su asistencia.", "KAIND-li"),
            ("regarding", "con respecto a", "I'm writing regarding your invoice.", "Escribo con respecto a su factura.", "ri-GAA-ding"),
            ("enclosed", "adjunto; incluido", "Please find enclosed my CV.", "Encontrará adjunto mi currículum.", "in-KLƏUZD"),
            ("yours sincerely", "atentamente (cuando se nombra al destinatario)", "Yours sincerely, Anna Brown.", "Atentamente, Anna Brown.", "yooz sin-SIƏ-li"),
            ("yours faithfully", "atentamente (carta a «Sir or Madam»)", "Yours faithfully, J. Green.", "Atentamente, J. Green.", "yooz FEIDH-fə-li"),
            ("to whom it may concern", "a quien corresponda", "To whom it may concern, I am writing to apply.", "A quien corresponda, escribo para postularme.", "tə huum it mei kən-SƏƏN"),
        ],
        quiz=[
            Q("¿Cómo cerrás una carta que empieza con «Dear Mr Smith»?", "Yours sincerely", "Yours faithfully", "Best of luck", "Dear friend"),
            Q("Hereby significa…", "por la presente", "por favor", "de aquí a allá", "hacia atrás"),
            Q("Enclosed indica…", "que se adjunta algo", "que se cierra la carta", "que está prohibido", "que es secreto"),
            Q("To whom it may concern es…", "a quien corresponda", "para quien quiera", "a mi amigo", "con mucho gusto"),
            Q("Kindly en una carta formal es…", "tenga a bien", "un tipo de persona", "por amabilidad solamente", "una despedida"),
        ],
    ),
    L(
        "Cultura gastronómica",
        "Scone, crumpet, Marmite, afternoon tea y los sabores de la tradición británica.",
        [
            "La comida es una ventana a la cultura. El afternoon tea es una tradición del siglo XIX: té con sándwiches pequeños, scones con crema y mermelada, y pasteles, servido alrededor de las cuatro de la tarde. Un scone se come con jam y clotted cream, y hay una eterna discusión sobre qué va primero. En Devon, la crema; en Cornwall, la mermelada.",
            "Una crumpet es una torta esponjosa que se tuesta y se come con manteca. El Marmite es una pasta salada de levadura, que se unta en el pan: la gente lo adora o lo odia, tanto que la marca hizo un eslogan con eso. El Sunday roast es la comida del domingo, con carne asada y Yorkshire pudding, una masa que se hornea alta y vacía por dentro.",
            "El trifle es un postre en capas, con bizcocho, fruta, natilla y crema; es el favorito en Navidad. El Full English es el desayuno completo. Si te invitan a una de estas comidas, es un honor y una forma de entrar de verdad en la cultura inglesa.",
        ],
        [
            ("scone", "scone (panecillo dulce)", "I'd like a scone with jam and cream.", "Quisiera un scone con mermelada y crema.", "skon"),
            ("crumpet", "panqueque esponjoso", "A crumpet with butter is delicious.", "Un crumpet con manteca es delicioso.", "KRAM-pit"),
            ("Marmite", "Marmite (pasta de levadura)", "I love Marmite on toast.", "Me encanta el Marmite en tostadas.", "MAA-mait"),
            ("Yorkshire pudding", "masa horneada de Yorkshire", "Yorkshire pudding goes with roast beef.", "El Yorkshire pudding va con el rosbif.", "YOO-shə PU-ding"),
            ("trifle", "postre en capas (trifle)", "We always have trifle at Christmas.", "Siempre comemos trifle en Navidad.", "TRAI-fəl"),
            ("afternoon tea", "té de la tarde", "We had afternoon tea at the Ritz.", "Tomamos el té de la tarde en el Ritz.", "aaf-tə-NUUN TII"),
            ("Sunday roast", "asado dominical", "Sunday roast is my favourite meal.", "El asado dominical es mi comida favorita.", "SAN-dei RƏUST"),
            ("Full English", "desayuno inglés completo", "I'll have the Full English, please.", "Voy a pedir el desayuno inglés completo, por favor.", "ful ING-glish"),
        ],
    ),
    L(
        "Estilo y figuras literarias",
        "Sonnet, metaphor, alliteration y el análisis de un texto.",
        [
            "Leer literatura inglesa en su idioma es una de las grandes recompensas. Un sonnet es un poema de catorce versos, y Shakespeare escribió 154. La prose es el texto sin forma poética, y el verse es el lenguaje en verso. La alliteration repite sonidos al comienzo de palabras cercanas: «Peter Piper picked a peck of pickled peppers».",
            "Una metaphor identifica una cosa con otra («Time is a thief»), mientras que una allegory es una historia entera cuyo sentido profundo es otro: Animal Farm, de George Orwell, es una alegoría política. Un oxymoron junta dos términos opuestos: «deafening silence». Un idiom es una expresión fija cuyo sentido no se deduce de las palabras.",
            "Una tarea de análisis literario: «Identify the metaphors in the first stanza». Conocer estos términos te permite estudiar literatura británica con profundidad y participar en un taller de lectura crítica.",
        ],
        [
            ("sonnet", "soneto", "Shakespeare wrote 154 sonnets.", "Shakespeare escribió 154 sonetos.", "SO-nit"),
            ("prose", "prosa", "The novel is written in simple prose.", "La novela está escrita en prosa sencilla.", "prəuz"),
            ("verse", "verso; poesía", "She writes verse in her spare time.", "Escribe versos en su tiempo libre.", "vəəs"),
            ("metaphor", "metáfora", "'Time is a thief' is a metaphor.", "'El tiempo es un ladrón' es una metáfora.", "ME-tə-faa"),
            ("allegory", "alegoría", "Animal Farm is a political allegory.", "Rebelión en la granja es una alegoría política.", "A-lə-gə-ri"),
            ("idiom", "modismo", "'Piece of cake' is an idiom.", "'Piece of cake' es un modismo.", "I-di-əm"),
            ("alliteration", "aliteración", "Alliteration repeats the same sound.", "La aliteración repite el mismo sonido.", "ə-li-tə-REI-shən"),
            ("oxymoron", "oxímoron", "'Deafening silence' is an oxymoron.", "'Silencio ensordecedor' es un oxímoron.", "ok-si-MOO-ron"),
        ],
        quiz=[
            Q("Un sonnet tiene…", "catorce versos", "doce versos", "cuatro versos", "veinte versos"),
            Q("Un oxymoron junta…", "dos términos opuestos", "dos sinónimos", "dos números", "dos colores"),
            Q("Alliteration es…", "la repetición de sonidos iniciales", "una rima final", "un verso suelto", "un tipo de prosa"),
            Q("Allegory es…", "una historia con otro sentido profundo", "un cuento de hadas", "una novela larga", "una canción"),
            Q("Prose es…", "texto sin forma poética", "poesía rimada", "una obra teatral", "una carta"),
        ],
    ),
    L(
        "Clase y sociedad",
        "Posh, working class, toff y la huella de las clases sociales.",
        [
            "Pocos temas son tan británicos como la clase social. La sociedad se describe como working class (clase trabajadora), middle class (clase media) y upper class (clase alta). El acento, la escuela y hasta lo que se come revelan la clase de origen. Alguien posh habla con acento de elite y tiene modales refinados. Un toff es un aristócrata, a menudo dicho con cierta ironía.",
            "Una public school es un colegio privado de elite, como Eton o Harrow; los egresados pasan a Oxford o Cambridge y forman redes que se conocen como the old school tie. La social mobility es la posibilidad de subir de clase. Es una promesa política que, según los críticos, funciona poco.",
            "Hablar de clase con un inglés exige cuidado. La mayoría dirá «I'm just ordinary» y preferirá no hablar de dinero ni de origen. Pero entender este sistema te ayuda a comprender muchas actitudes y chistes que de otro modo parecerían raros.",
        ],
        [
            ("posh", "elegante; de clase alta", "She speaks in a very posh accent.", "Habla con un acento muy elegante.", "posh"),
            ("working class", "clase trabajadora", "He comes from a working class family.", "Viene de una familia de clase trabajadora.", "WƏƏ-king klaas"),
            ("middle class", "clase media", "They are a middle class family.", "Son una familia de clase media.", "MI-dəl klaas"),
            ("upper class", "clase alta", "The upper class owns large estates.", "La clase alta posee grandes propiedades.", "A-pə klaas"),
            ("toff", "aristócrata (coloquial)", "He's a bit of a toff.", "Es un poco aristócrata.", "tof"),
            ("social mobility", "movilidad social", "Social mobility is a key political issue.", "La movilidad social es un tema político central.", "SƏU-shəl məu-BI-lə-ti"),
            ("public school", "colegio privado de elite", "He went to a public school.", "Fue a un colegio privado de elite.", "PA-blik skuul"),
            ("old school tie", "red de contactos de colegio de elite", "The old school tie helps in business.", "La red de contactos del colegio ayuda en los negocios.", "əuld skuul TAI"),
        ],
    ),
    L(
        "Jerga británica",
        "Innit, knackered, cheeky, bloke y el inglés de la calle.",
        [
            "El inglés informal británico es tan rico que conviene tener una guía. Innit es la contracción de «isn't it» y se usa al final de una frase, a veces sin sentido literal. Knackered es estar muy cansado. Cheeky describe a alguien descarado de manera simpática, y daft es tonto, bobo, sin ser un insulto grave.",
            "Un bloke es un tipo, un hombre. Dos palabras sobre dinero: fiver es un billete de cinco libras y tenner, uno de diez. Skint es estar sin un peso, y dodgy, algo sospechoso o de mala calidad. Gobsmacked es estar boquiabierto por la sorpresa.",
            "Estas palabras son informales: usalas con amigos, no en una entrevista de trabajo. Saberlas, sin embargo, te permite entender mucho mejor a los británicos cuando hablan entre ellos, en series, programas y canciones.",
        ],
        [
            ("innit", "¿no? (isn't it)", "Nice day, innit?", "Lindo día, ¿no?", "I-nit"),
            ("knackered", "agotado; muerto de cansancio", "I'm absolutely knackered.", "Estoy agotadísimo.", "NA-kəd"),
            ("cheeky", "descarado (simpático)", "That's a cheeky question.", "Es una pregunta descarada.", "CHII-ki"),
            ("daft", "tonto; bobo", "Don't be daft!", "¡No seas bobo!", "daaft"),
            ("bloke", "tipo; hombre", "He's a nice bloke.", "Es un buen tipo.", "bləuk"),
            ("fiver", "billete de cinco libras", "Can you lend me a fiver?", "¿Me prestás cinco libras?", "FAI-və"),
            ("tenner", "billete de diez libras", "It costs a tenner.", "Cuesta diez libras.", "TE-nə"),
            ("skint", "sin plata; pelado", "I'm skint until Friday.", "Estoy pelado hasta el viernes.", "skint"),
            ("dodgy", "sospechoso; dudoso", "That looks a bit dodgy.", "Eso se ve un poco sospechoso.", "DO-dji"),
            ("gobsmacked", "boquiabierto", "I was completely gobsmacked.", "Me quedé completamente boquiabierto.", "GOB-smakt"),
        ],
        quiz=[
            Q("Knackered significa…", "muy cansado", "enojado", "contento", "hambriento"),
            Q("Un fiver es…", "un billete de cinco libras", "un billete de cincuenta", "una moneda", "un cheque"),
            Q("Skint es…", "no tener plata", "tener mucha plata", "estar enfermo", "estar apurado"),
            Q("Bloke es…", "un tipo; un hombre", "un tipo de queso", "un bloque", "un auto"),
            Q("Cheeky describe a alguien…", "descarado, de forma simpática", "muy educado", "muy callado", "muy enojado"),
        ],
    ),
    L(
        "Fiestas y tradiciones",
        "Hogmanay, Burns Night, Guy Fawkes y el calendario folclórico.",
        [
            "Fuera de las fiestas conocidas, el Reino Unido guarda tradiciones antiguas. El Hogmanay es la Nochevieja escocesa, una fiesta enorme con música y fuego. El 25 de enero, los escoceses celebran la Burns Night en honor al poeta Robert Burns, con un banquete de haggis y versos recitados.",
            "El Remembrance Day (11 de noviembre) honra a los caídos en las guerras, con dos minutos de silencio y amapolas rojas en las solapas. Al comienzo de mayo, el May Day se celebra con un maypole, un palo adornado con cintas alrededor del cual se baila. Y el morris dancing es una danza folclórica con campanillas y pañuelos que se hace en pueblos y festivales.",
            "El Guy Fawkes recuerda al conspirador que intentó volar el Parlamento en 1605; sus muñecos se queman en hogueras. Otra ceremonia famosa es el Trooping the Colour, el desfile con que se celebra el cumpleaños oficial del monarca, en junio. Cada una cuenta una parte de la historia y de la identidad británica.",
        ],
        [
            ("Hogmanay", "Nochevieja escocesa", "We spent Hogmanay in Edinburgh.", "Pasamos el Hogmanay en Edimburgo.", "HOG-mə-nei"),
            ("Burns Night", "Noche de Burns (25 de enero)", "We eat haggis on Burns Night.", "Comemos haggis en la Noche de Burns.", "bəənz NAIT"),
            ("Remembrance Day", "Día del Recuerdo (11 de noviembre)", "People wear poppies for Remembrance Day.", "La gente usa amapolas por el Día del Recuerdo.", "ri-MEM-brəns DEI"),
            ("Guy Fawkes", "Guy Fawkes (conspirador de 1605)", "Guy Fawkes tried to blow up Parliament.", "Guy Fawkes intentó volar el Parlamento.", "GAI FOOKS"),
            ("May Day", "Primero de Mayo; fiesta de la primavera", "Villages dance on May Day.", "Los pueblos bailan el Primero de Mayo.", "MEI dei"),
            ("maypole", "palo de mayo (con cintas)", "The children danced around the maypole.", "Los chicos bailaron alrededor del palo de mayo.", "MEI-pəul"),
            ("morris dancing", "danza folclórica inglesa", "Morris dancing is very old.", "La danza morris es muy antigua.", "MO-ris DAAN-sing"),
            ("Trooping the Colour", "desfile del cumpleaños oficial del monarca", "Trooping the Colour takes place in June.", "El Trooping the Colour se hace en junio.", "TRUU-ping dhə KA-lə"),
        ],
    ),
    L(
        "Gramática y estilo avanzado",
        "Subjunctive, inversion, hedging y las sutilezas del inglés escrito.",
        [
            "En C2 la gramática se vuelve estilo. El subjunctive es raro en inglés pero existe: «I suggest that he be present» (con be, no is). La inversion cambia el orden de sujeto y verbo para dar énfasis: «Never have I seen such a thing», en lugar de «I have never seen…». Es típica de los textos formales y literarios.",
            "La ellipsis omite palabras que se sobreentienden: «She went to Paris; he, to Rome». El hedging es suavizar una afirmación con expresiones como «it seems that» o «perhaps»: muy propio del texto académico. La nominalisation convierte verbos en sustantivos («decide → decision») y le da un tono impersonal. La passive voice (la voz pasiva) quita el foco del agente: «Mistakes were made».",
            "Un buen escritor domina el register, es decir, el nivel de formalidad de cada situación. Un texto puede ser colloquial (coloquial) o, al contrario, tener palabras archaic (arcaicas) como «thou» y «hath». Saber cuándo usar cada nivel es lo que distingue al hablante avanzado.",
        ],
        [
            ("subjunctive", "subjuntivo", "I suggest that he be present.", "Sugiero que esté presente.", "səb-DJANK-tiv"),
            ("inversion", "inversión (gramatical)", "Inversion adds emphasis.", "La inversión añade énfasis.", "in-VƏƏ-shən"),
            ("ellipsis", "elipsis", "Ellipsis avoids repetition.", "La elipsis evita la repetición.", "i-LIP-sis"),
            ("hedging", "atenuación (en el discurso)", "Hedging is typical of academic writing.", "La atenuación es típica de la escritura académica.", "HE-djing"),
            ("nominalisation", "nominalización", "Nominalisation makes a text more formal.", "La nominalización hace un texto más formal.", "no-mi-nə-lai-ZEI-shən"),
            ("passive voice", "voz pasiva", "Use the passive voice here.", "Usá la voz pasiva acá.", "PA-siv VOIS"),
            ("register", "registro (nivel de formalidad)", "Choose the right register.", "Elegí el registro adecuado.", "RE-dji-stə"),
            ("colloquial", "coloquial", "That word is quite colloquial.", "Esa palabra es bastante coloquial.", "kə-LƏU-kwi-əl"),
            ("archaic", "arcaico", "'Thou' is an archaic word.", "'Thou' es una palabra arcaica.", "aa-KEI-ik"),
        ],
        quiz=[
            Q("Inversion en gramática es…", "cambiar el orden de sujeto y verbo", "una pregunta", "un error", "un sinónimo"),
            Q("Hedging es…", "suavizar una afirmación", "afirmar con fuerza", "negar una idea", "repetir una frase"),
            Q("Archaic significa…", "arcaico", "arqueológico", "artístico", "autoritario"),
            Q("Register es…", "el nivel de formalidad", "un listado", "un archivo", "una caja registradora"),
            Q("Passive voice es…", "la voz pasiva", "una voz muda", "un tipo de acento", "un silencio"),
        ],
    ),
    L(
        "Pensamiento crítico",
        "Fallacy, premise, bias, scrutiny y cómo analizar un argumento.",
        [
            "Pensar con claridad es una destreza de C2. Una premise es la base de un argumento: si la premisa es falsa, la conclusión también lo es. Una fallacy es un error de razonamiento que parece válido pero no lo es. Un counterargument es el argumento opuesto, y refutarlo con rigor da fuerza a tu postura.",
            "El bias, el sesgo, es una inclinación que nos impide juzgar con equidad. Un buen razonamiento resiste el scrutiny, el examen minucioso, y es rigorous, riguroso. Una opinión nuanced es matizada, no blanco o negro. Y una critique es un análisis crítico, que no significa solo criticar sino evaluar con criterio.",
            "Los universitarios británicos aprenden desde jóvenes a cuestionar. Una pregunta típica en un seminario: «What assumptions underlie your argument?». Si podés responderla con calma y precisión, estás hablando como un hablante nativo culto.",
        ],
        [
            ("fallacy", "falacia", "That argument is a fallacy.", "Ese argumento es una falacia.", "FA-lə-si"),
            ("premise", "premisa", "The premise is false.", "La premisa es falsa.", "PRE-mis"),
            ("counterargument", "contraargumento", "She raised a strong counterargument.", "Presentó un contraargumento sólido.", "KAUN-tə-aa-gyə-mənt"),
            ("bias", "sesgo", "The study shows a clear bias.", "El estudio muestra un sesgo claro.", "BAI-əs"),
            ("scrutiny", "escrutinio", "The plan is under scrutiny.", "El plan está bajo escrutinio.", "SKRUU-tə-ni"),
            ("rigorous", "riguroso", "The analysis is rigorous.", "El análisis es riguroso.", "RI-gə-rəs"),
            ("nuanced", "matizado", "It was a nuanced debate.", "Fue un debate matizado.", "NYUU-aanst"),
            ("critique", "análisis crítico", "Write a critique of the article.", "Escribí un análisis crítico del artículo.", "kri-TIIK"),
        ],
    ),
    L(
        "Cierre del curso",
        "Congratulations, well done, cheerio y las palabras para seguir.",
        [
            "Llegaste al final. Congratulations: completaste un recorrido enorme, desde el cat y el cup de la primera clase hasta el estilo y la crítica de C2. Fue un largo journey y un gran achievement que te abre puertas en el trabajo, en los estudios y en los viajes.",
            "Un milestone es un hito, un punto importante en el camino, y este curso es uno de ellos. Ser fluent, es decir, fluido, no significa no cometer errores sino poder comunicarte sin trabarte. Los británicos te dirán «Well done!» cuando aciertes y «Keep going!» para animarte. Y en la despedida, muy cálida, se dice cheerio o farewell, según el contexto.",
            "El camino sigue: leer The Guardian, escuchar a la BBC, mirar series británicas con subtítulos en inglés y, sobre todo, hablar con ingleses cada vez que puedas. Escuchá, repetí, equivocate sin miedo. Con estas palabras y las que ya sumaste, tenés el nivel para vivir en inglés británico. Good luck, and cheerio!",
        ],
        [
            ("congratulations", "felicitaciones", "Congratulations on passing the exam!", "¡Felicitaciones por aprobar el examen!", "kən-gra-chə-LEI-shənz"),
            ("milestone", "hito; logro importante", "Today is an important milestone.", "Hoy es un hito importante.", "MAIL-stəun"),
            ("journey", "viaje; recorrido", "Learning a language is a long journey.", "Aprender un idioma es un largo recorrido.", "DJƏƏ-ni"),
            ("achievement", "logro", "Finishing the course is a great achievement.", "Terminar el curso es un gran logro.", "ə-CHIIV-mənt"),
            ("fluent", "fluido; con fluidez", "She is fluent in three languages.", "Habla con fluidez tres idiomas.", "FLUU-ənt"),
            ("keep going", "seguí adelante", "Keep going, you're nearly there.", "Seguí adelante, ya casi llegás.", "kiip GƏU-ing"),
            ("well done", "bien hecho", "Well done! That was perfect.", "¡Bien hecho! Estuvo perfecto.", "wel DAN"),
            ("cheerio", "chau; hasta luego (informal británico)", "Cheerio! See you next week.", "¡Chau! Nos vemos la semana próxima.", "chiə-ri-ƏU"),
            ("farewell", "adiós; despedida", "They said a warm farewell.", "Se dieron una cálida despedida.", "feə-WEL"),
        ],
        dialogue=D(
            ("I've finished the whole course!", "¡Terminé todo el curso!"),
            ("Congratulations! That's a great achievement.", "¡Felicitaciones! Es un gran logro."),
            ("Thank you. It was a long journey.", "Gracias. Fue un largo recorrido."),
            ("Keep going. Soon you'll be fluent.", "Seguí adelante. Pronto vas a hablar con fluidez."),
            ("Cheers! And farewell for now.", "¡Gracias! Y hasta pronto."),
        ),
        quiz=[
            Q("Well done significa…", "bien hecho", "bien cocido", "hecho a mano", "muy hecho"),
            Q("Milestone es…", "un hito", "una piedra de molino", "una milla", "un mojón de ruta"),
            Q("Fluent describe a quien…", "habla con fluidez", "habla poco", "habla muy fuerte", "habla de forma antigua"),
            Q("Cheerio es una forma informal de…", "despedirse", "saludar", "agradecer", "pedir perdón"),
            Q("Achievement significa…", "logro", "llegada", "pérdida", "trabajo"),
        ],
    ),
]

_COURSE = None


def _course():
    global _COURSE
    if _COURSE is None:
        _COURSE = {
            2: bind(A2_SPECS, 2),
            3: bind(B1_SPECS, 3),
            4: bind(B2_SPECS, 4),
            5: bind(C1_SPECS, 5),
            6: bind(C2_SPECS, 6),
        }
    return _COURSE


def extra_words():
    """Filas de léxico de A2 a C2, por nivel."""
    return {level: rows for level, (rows, _) in _course().items()}


def extra_lessons():
    """Clases de A2 a C2, por nivel."""
    return {level: lessons for level, (_, lessons) in _course().items()}
