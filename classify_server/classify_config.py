#coding: utf-8

IP = '0.0.0.0'
PORT = 11118



EN_EMOTIONS = {
    'good': ['good', 'sucess', 'enjoy', 'happy', 'strong', 'surprise'],
    'bad': ['bad', 'fail', 'disgust', 'sad', 'weak', 'terrify']
}

DE_EMOTIONS = {
    "Gut": ["gut", "Erfolg", "genießen", "glücklich", "stark", "Überraschung"],
    "Schlecht": ["schlecht", "nicht bestanden", "Ekel", "traurig", "schwach", 'schrecken ']
}

ZH_EMOTIONS = {
    '正面': ['正面', '成功', '享受', '高兴', '强壮', '惊喜'],
    '负面': ['负面', '失败', '恶心', '悲伤', '虚弱', '恐怖']
}

FR_EMOTIONS = {
    'Bon': ['bon', 'succès', 'profiter' 'heureux', 'fort', 'surprise',],
    'Mauvais': ['mauvais', 'échec', 'dégoût', 'triste', 'faible', 'terrifier']
}

RU_EMOTIONS = {
    'хороший': ['хороший', 'успех', 'наслаждаться', 'счастливый', 'сильный', 'сюрприз'],
    "плохой": ["плохой", "провал", "отвращение", "грустно", "слабый", "устрашить"]
}

ES_EMOTIONS = {
    "Bueno": ["bueno", "éxito", "disfrutar", "feliz", "fuerte", "sorpresa"],
    "Malo": ["malo", "prueba", "asco", "triste", "débil", 'aterrorizar ']
}

PT_EMOTIONS = {
    "Bom": ["bom", "sucesso", "aproveitar", "feliz", "forte", "surpresa"],
    "Mau": [ 'ruim', 'falhar', 'nojo', 'triste', 'fraco', 'aterrorizar']
}

FI_EMOTIONS = {
    "Hyvä": ["hyvä", "menestys", "nauttia", "happy", "vahva", "yllätys"],
    "Huonoja": ["huonoa", "hylätty", "inho", "surullinen", "heikko", "kauhu"]
}

DA_EMOTIONS = {
    "Gode": [ 'god', 'succes', 'nyde', 'lykkelig', 'stærk', 'overraskelse'],
    "Dårlige": [ 'dårlige', 'mislykkes', 'afsky', 'trist', 'svage', 'skræmme']
}

EL_EMOTIONS = {
    'Καλή': ['καλό', 'επιτυχία', 'απολαμβάνουν', 'ευτυχισμένος', 'ισχυρή', 'έκπληξη'],
    'Κακό': ['κακά', 'αποτυχία', 'αηδία', 'λυπημένος', 'ασθενές', 'τρομοκρατεί']
}

DEFAULT_EMOTIONS = {
    'zh': ZH_EMOTIONS,
    'en': EN_EMOTIONS,
    'fr': FR_EMOTIONS,
    'ru': RU_EMOTIONS,
    'es': ES_EMOTIONS,
    'pt': PT_EMOTIONS,
    'fi': FI_EMOTIONS,
    'da': DA_EMOTIONS,
    'el': EL_EMOTIONS,
    'de': DE_EMOTIONS,
}


EN_CLASS = {
    'politics':['politics'],
    'economy':['economy'],
    'technology':['technology'],
    'health':['health'],
    'education':['education'],
    'entertainment':['entertainment'],
    'sports':['sports'],
    'travel':['travel'],
}

ZH_CLASS = {
    '政治':['政治'],
    '经济':['经济'],
    '科技':['科技'],
    '健康':['健康'],
    '教育':['教育'],
    '体育':['体育'],
    '娱乐':['娱乐'],
    '旅游':['旅游'],
}

FR_CLASS = {
    'politique':['politique'],
    'économie':['économie'],
    'technologie':['technologie'],
    'santé':['santé'],
    'éducation':['éducation'],
    'sportif':['sportif'],
    'divertissement':['divertissement'],
    'tour':['tour'],
}

RU_CLASS = {
    'политическая':['политическая'],
    'экономика':['экономика'],
    'технологии':['технологии'],
    'здоровье':['здоровье'],
    'образование':['образование'],
    'спортивный':['спортивный'],
    'развлечения':['развлечения'],
    'тур':['тур'],
}

DA_CLASS = {
    'politisk':['politisk'],
    'økonomi':['økonomi'],
    'teknologi':['teknologi'],
    'sundhed':['sundhed'],
    'uddannelse':['uddannelse'],
    'sport':['sport'],
    'underholdning':['underholdning'],
    'tour':['tour'],
}

FI_CLASS = {
    'poliittinen':['poliittinen'],
    'talous':['talous'],
    'technology':['technology'],
    'terveys':['terveys'],
    'koulutus':['koulutus'],
    'urheilu':['urheilu'],
    'viihde':['viihde'],
    'kierros':['kierros'],
}

DE_CLASS = {
    'politisch':['politisch'],
    'Wirtschaft':['Wirtschaft'],
    'Technik':['Technik'],
    'Gesundheit':['Gesundheit'],
    'Bildung':['Bildung'],
    'Sport':['Sport'],
    'Unterhaltung':['Unterhaltung'],
    'Tour':['Tour'],
}

PT_CLASS = {
    'político':['político'],
    'economia':['economia'],
    'tecnologia':['tecnologia'],
    'saúde':['saúde'],
    'educação':['educação'],
    'esportes':['esportes'],
    'diversão':['diversão'],
    'excursão':['excursão'],
}

ES_CLASS = {
    'política': [ 'política'],
    'economía': [ 'económica'],
    'tecnología': [ 'tecnología'],
    'salud': ['salud'],
    'educación': [ 'educación'],
    'sport': [ 'sport'],
    'entretenimiento': ['entretenimiento'],
    'turismo': [ 'turismo']
}

EL_CLASS = {
    'πολιτική': ['πολιτική'],
    'οικονομική': ['οικονομική'],
    'τεχνολογία': ['τεχνολογία'],
    'υγεία': [ 'υγεία'],
    'εκπαίδευση': ['εκπαίδευση'],
    'sport': ['sport'],
    'ψυχαγωγία': ['ψυχαγωγία'],
    'περιοδεία': ['περιοδεία']
}

DEFAULT_CLASS = {
    'zh': ZH_CLASS,
    'en': EN_CLASS,
    'fr': FR_CLASS,
    'ru': RU_CLASS,
    'es': ES_CLASS,
    'pt': PT_CLASS,
    'fi': FI_CLASS,
    'da': DA_CLASS,
    'el': EL_CLASS,
    'de': DE_CLASS,
}
