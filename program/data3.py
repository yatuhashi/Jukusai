from program.models import program, place, vote
from datetime import datetime, timedelta

placeData =[
    {
        "placeName":"B-ICHI",
        "room":"セブンイレブン前"
    },
    {
        "placeName":"3F",
        "room":"アーバンテックホール"
    },
    {
        "placeName":"5F",
        "room":"A-0511"
    },
    {
        "placeName":"5F",
        "room":"A0514"
    },
    {
        "placeName":"5F",
        "room":"A0542"
    },
    {
        "placeName":"5F",
        "room":"B0523"
    },
    {
        "placeName":"5F",
        "room":"B0526"
    },
    {
        "placeName":"5F",
        "room":"B0563"
    },
    {
        "placeName":"5F",
        "room":"B0567"
    },
    {
        "placeName":"6F",
        "room":"A0611"
    },
    {
        "placeName":"6F",
        "room":"A0615"
    },
    {
        "placeName":"6F",
        "room":"A0652"
    },
    {
        "placeName":"6F",
        "room":"A0656"
    },
    {
        "placeName":"6F",
        "room":"B0663"
    },
    {
        "placeName":"7F",
        "room":"食堂"
    },
    {
        "placeName":"10F",
        "room":"A1012"
    },
    {
        "placeName":"10F",
        "room":"A1015"
    },
    {
        "placeName":"STEC広場",
        "room":"STEC広場"
    },
    {
        "placeName":"1F",
        "room":"アトリウム"
    }
]

programData =[
    {
        "groupName":"K.P.F.R. OB会",
        "contentName":"Acoustic café",
        "contentData":"アコースティック演奏が聴けるカフェ",
        "category":2,
        "place":5,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部文化会吹奏楽部",
        "contentName":"アンサンブルステージ",
        "contentData":"少人数でも充実したサウンド！吹奏楽のアンサンブルの魅力をお届けします！",
        "category":1,
        "place":1,
        "firstFlag":False,
        "secondFlag":True,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"I.F.",
        "contentName":"イラスト展示",
        "contentData":"一次創作のイラスト活動を行っているI.F.です。部員たちの作品を展示しています！",
        "category":1,
        "place":6,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"アニメ放題サークル",
        "contentName":"カードゲームに触れてみよう",
        "contentData":"遊戯王、MTGなどのTCGで遊んでみませんか？カードを持っていない方でも遊べます！!",
        "category":1,
        "place":2,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部文化会SF研究会",
        "contentName":"映画評論+評論映画の上映",
        "contentData":"各部員が書いた映画の評論を冊子にして配布し、その冊子の中から数作品上映します。",
        "category":1,
        "place":10,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"文芸主体創作サークルink.",
        "contentName":"ブックカフェDrink.",
        "contentData":"昨年数百人以上を集客したブックカフェが再出店。飲み物、軽食や短編集を販売します！",
        "category":1,
        "place":7,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部文化会鉄道研究部",
        "contentName":"鉄道模型展示",
        "contentData":"首都圏の電車をはじめ、様々な鉄道車両の模型をジオラマの中で走行・展示します!",
        "category":1,
        "place":16,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"peace and humanity",
        "contentName":"教室展示(世界の政治、文化、歴史情勢アンケート)",
        "contentData":"世界の情勢を知り、日本との違いを認識して関心を深めて頂けるとうれしいです。",
        "category":1,
        "place":9,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部文化会マジシャンズソサエティ",
        "contentName":"クロースマジック",
        "contentData":"普段テレビで見ているようなマジックを目の前で見てみませんか？驚きの絵がを提供します！！",
        "category":1,
        "place":4,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"KFIP",
        "contentName":"教室企画",
        "contentData":"KFIPはプログラミングサークルです。様々な自作ゲームを展示しています！",
        "category":1,
        "place":3,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"自然科学研究部",
        "contentName":"自然科学研究部",
        "contentData":"気象・生物・天文・鉱物の分野で展示します。自然科学に興味が有りましたら、ぜひお立ち寄り下さい！",
        "category":1,
        "place":11,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部学科連合委員会",
        "contentName":"研究室公開",
        "contentData":"大学生ってどんなことを研究しているの？そんな疑問を抱いた方は是非お越し下さい！",
        "category":1,
        "place":13,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"SOL(Sound Of Liberty)",
        "contentName":"食堂ライブ",
        "contentData":"軽音サークルSOLが新宿祭を音楽で盛り上げる！！音楽好きは食堂に集まれ！！！",
        "category":1,
        "place":14,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"K.F.P.R. 部",
        "contentName":"K.P.F.R.新宿祭ライブ",
        "contentData":"新宿祭でのライブ、みんなで楽しみましょう！是非見に来てください！",
        "category":1,
        "place":5,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"電子技術研究部",
        "contentName":"電子技術研究部",
        "contentData":"部員が作製した電子工作を展示しております。興味がある方は気軽にお越しください。",
        "category":1,
        "place":15,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"研究室公開",
        "contentName":"研究室公開",
        "contentData":"研究室とは何かわからない人！！是非こちらにお越し下さい！！",
        "category":1,
        "place":12,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"研究室公開",
        "contentName":"研究室公開",
        "contentData":"研究室とは何かわからない人！！是非こちらにお越し下さい！！",
        "category":1,
        "place":13,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部文化会写真部",
        "contentName":"新宿祭展示会",
        "contentData":"自由展示と企画展示、ゆったりとした空間で皆様のご来場をお待ちしております…♪",
        "category":1,
        "place":0,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部新聞会",
        "contentName":"こぐテレ！新宿祭スペシャル！",
        "contentData":"新聞会が日曜日にお送りするネットテレビ！11～14時、17～20時には公開生放送も！",
        "category":1,
        "place":0,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部新聞会",
        "contentName":"新聞会Gallery",
        "contentData":"近年、幅広い活動を展開する新聞会。その製作物を余す所なくお見せします！",
        "category":1,
        "place":8,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部学科連合委員会",
        "contentName":"じゃがまがー",
        "contentData":"バターとマーガリンの違い知りたくないですか？(店頭にはマーガリンしかないです)",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"第Ⅱ部自治会、Ⅱ部合気道部",
        "contentName":"焼き鳥、豚汁",
        "contentData":"毎年大好評の焼き鳥、豚汁販売します！！皆様のご来店お待ちしております！！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"生協学生委員会",
        "contentName":"チュロス",
        "contentData":"シナモン味とココア味を用意しました！おいしいチュロスを味わってみませんか？",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"生協学生委員会",
        "contentName":"和風チュロス",
        "contentData":"和風チュロスでは抹茶味ときなこ味を用意しました！新しい和風チュロスを食べてみませんか？",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部学生自治会",
        "contentName":"水餃子－Water dumplings－",
        "contentData":"店長を中心とした愉快な仲間たちで研究に研究を重ねた水餃子をぜひご賞味ください！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"アニメ放題サークル",
        "contentName":"Kogakuin Fried Chicken",
        "contentData":"鶏と芋しかないじゃない！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"I.F.",
        "contentName":"キャラメルポップコーン",
        "contentData":"あの人気フレーバー、キャラメルポップコーン！お手頃な小さめサイズ♪",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"ケンタッキー・フライド・チキン",
        "contentName":"チキン販売",
        "contentData":"国産鶏肉を使用した他では真似のできないフライドチキンを販売します。",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部学生自治会",
        "contentName":"わたあめ",
        "contentData":"安くていろんな味のフワッフワのおいしいわたあめをご用意しています",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"DJサークル「KNOiSE」",
        "contentName":"焼きそば、ジュース",
        "contentData":"爽やかな特製ドリンクと濃厚なタラコクリーム焼きそばの熱いグルーヴをご堪能あれ！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"新宿祭実行委員会OB・OG",
        "contentName":"ラーメン・餃子",
        "contentData":"我は店長片岡アルよ！アイヤー？みんなは中華好きあるカ？我はね～...普通アルよ～！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"八王子祭実行委員会",
        "contentName":"ぷち爆弾焼き",
        "contentData":"たこ焼きをモチーフに数種類のフレーバーを展開してます！ぜひパクッと一口！",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"craft studio",
        "contentName":"手作り.com",
        "contentData":"手作りのアクセサリーを販売します。お気に入りの逸品探しに是非お立ち寄りください。",
        "category":2,
        "place":17,
        "firstFlag":False,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":True,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部新聞会",
        "contentName":"学生の注目している分野のプレゼンです！ちょっとだけ視野を広げてみませんか？",
        "contentData":"",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"Ⅰ部文化会",
        "contentName":"声優トークショー",
        "contentData":"超豪華声優陣によるトークショーを今年も開催決定！ご来場、お待ちしています！",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"工学院大学Ⅰ部学科連合委員会",
        "contentName":"THE TREASURE -隠されし秘宝-",
        "contentData":"工学院の秘宝が君を待っている。さぁ、新宿祭で大冒険に出かけよう！",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"DJサークル KNOiSE",
        "contentName":"Resonation of Music in Shinjuku",
        "contentData":"ステージ上のDJがガス音楽を大音量で楽しみましょう！♪",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"SOL(Sound Of Liberty)",
        "contentName":"ナイトライブ",
        "contentData":"",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"創価大学落語研究会",
        "contentName":"出張お笑いミニライブ",
        "contentData":"何だかんだ言って、皆んなお笑い好きでしょ？",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"SOL(Sound Of Liberty)",
        "contentName":"モーニングライブ",
        "contentData":"",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    },
    {
        "groupName":"喜楽屋",
        "contentName":"正しい便器の使い方",
        "contentData":"愛と涙あふれるハートフル・コメディ。ハンカチのご用意を忘れずに。",
        "category":3,
        "place":18,
        "firstFlag":True,
        "secondFlag":False,
        "thirdFlag":False,
        "allFlag":False,
        "start_at":datetime.now() + timedelta(hours=2),
        "end_at":datetime.now() + timedelta(hours=4)
    }

]

def createdata():
    for i in placeData:
        pl = place.objects.create(
            placeName  =i['placeName'],
            room       =i['room']
        )
    for i in programData:
        print(i['groupName'])
        print(i['place']+1)
        pl      = place.objects.get(pk=i['place']+1)
        print(pl.placeName)
        pro = program.objects.create(
            groupName  =i['groupName'],
            contentName=i['contentName'],
            contentData=i['contentData'],
            category   =i['category'],
            place      = place.objects.get(pk=i['place']+1),
            firstFlag  =i['firstFlag'],
            secondFlag =i['secondFlag'],
            thirdFlag  =i['thirdFlag'],
            allFlag    =i['allFlag'],
            start_at   =i['start_at'],
            end_at     =i['end_at']
        )
        vo = vote.objects.create(
            program = pro
        )

