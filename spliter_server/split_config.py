
IP = '0.0.0.0'
PORT = 9001


SPLITERS = {
    "zh" : {
        "module" : "spliter.spliter_zh",
        "clazz"  : "SpliterZh",
        "args"   : {}
    },
    "en" : {
        "module" : "spliter.spliter_en",
        "clazz"  : "SpliterEn",
        "args"   : {}
    },
    "fr" : {
        "module" : "spliter.spliter_fr",
        "clazz"  : "SpliterFr",
        "args"   : {}
    },
    "de" : {
        "module" : "spliter.spliter_de",
        "clazz"  : "SpliterDe",
        "args"   : {}
    },
    "it" : {
        "module" : "spliter.spliter_it",
        "clazz"  : "SpliterIt",
        "args"   : {}
    },
    "es" : {
        "module" : "spliter.spliter_es",
        "clazz"  : "SpliterEs",
        "args"   : {}
    },
    "pt" : {
        "module" : "spliter.spliter_pt",
        "clazz"  : "SpliterPt",
        "args"   : {}
    },
    "com": {
        "module" : "spliter.spliter_com",
        "clazz"  : "SpliterCom",
        "args"   : {}
    }
}


STOPWORDS = {
    'zh': 'stopwords_zh.txt',
    'en': 'stopwords_en.txt',
    'fr': 'stopwords_fr.txt',
    'de': 'stopwords_de.txt',
    'pt': 'stopwords_pt.txt',
    'es': 'stopwords_es.txt',
    'it': 'stopwords_it.txt',
    'com': 'stopwords_zh.txt',
}
