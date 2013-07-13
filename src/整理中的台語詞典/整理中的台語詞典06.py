from 言語資料庫.公用資料 import 資料庫連線
from 文章音標解析器 import 文章音標解析器
from 言語資料庫.公用資料 import 字詞
from 言語資料庫.公用資料 import 加文字佮版本
from 教育部臺灣閩南語常用詞辭典.資料庫連線 import 加關係
from 言語資料庫.公用資料 import 義近
from 言語資料庫.公用資料 import 會當替換
from 通用拼音音標 import 通用拼音音標
from 整理中的台語詞典.詞六國語通用拼音轉注音符號表 import 通用佮注音聲韻轉換表
from 整理中的台語詞典.詞六國語通用拼音轉注音符號表 import 通用佮注音調轉換表

def 揣出全部組合(音陣列, 位置, 累積音, 全部結果):
	if 位置 == len(音陣列):
		全部結果.append(累積音[1:])
		return
	for 音 in 音陣列[位置]:
		揣出全部組合(音陣列, 位置 + 1, 累積音 + '-' + 音, 全部結果)
	return

# 通用佮注音聲韻轉換表.update()
# 通用佮注音調轉換表.update({'5':'ˊ'})
詞典06調整表 = [('5', '2'), ('chii', 'chih'), ('shii', 'shih'), ('zhii', 'jhih'), ('zii', 'zih'),
		('sii', 'sih'), ('rhii', 'rih'),
		('y', 'i'), ('ii', 'i'), ('zi', 'ji'), ('jih', 'zih'), ('w', 'u'), ('uu', 'u'), ('er', 'e'),
		('ung', 'ong'), ('ien', 'ian'), ('au', 'ao'), ('uo', 'o'),
		('rh', 'r'), ('zh', 'jh'), ('ung', 'uong'),
		('chng', 'cheng'), ('dng', 'deng'), ('fng', 'fong'), ('gng', 'geng'), ('hng', 'heng'),
		('mng', 'meng'), ('lng', 'leng'), ('png', 'peng'), ('rng', 'reng'), ('shng', 'sheng'),
		('nng', 'neng'), ('bng', 'beng'), ('sng', 'seng'), ('tng', 'teng'), ('zng', 'zeng'),
		('cng', 'ceng'), ('kng', 'keng'), ]
def 揣出全部組合順紲做國語處理(音陣列, 位置, 累積音, 全部結果):
	if 位置 == len(音陣列):
		全部結果.append(累積音[1:])
		return
	for 音 in 音陣列[位置]:
		原 = 音
		for 舊, 新 in 詞典06調整表:
			音 = 音.replace(舊, 新)
		if 音[:-1] in 通用佮注音聲韻轉換表 and 音[-1] in 通用佮注音調轉換表:
			揣出全部組合順紲做國語處理(音陣列, 位置 + 1,
				累積音 + ' ' + 通用佮注音聲韻轉換表[音[:-1]] + 通用佮注音調轉換表[音[-1]], 全部結果)
		else:
			print(原 + " →" + 音 + " 無法度轉")
	return

揣台華資料 = 資料庫連線.prepare('SELECT "識別碼","華語漢字","華語音標","台語漢字","台語音標" ' +
	'FROM "整理中的台語詞典"."整理中的台語詞典06" ORDER BY "識別碼"')

通用拼音解析器 = 文章音標解析器(通用拼音音標)
通用拼音解析器.標點符號 = {}
辭典名 = '整理中的台語詞典06'
臺員 = '臺員'
正常 = '正常'
for 識別碼, 華語漢字, 華語音標, 台語漢字, 台語音標 in 揣台華資料():
	print(識別碼)
	文字資料 = []
	# 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本
	台語音 = []
	for 音 in 台語音標.strip()[1:-1].split('-'):
		台語音.append(音[1:-1].split('/'))
	攏總音 = []
	揣出全部組合(台語音, 0, '', 攏總音)
# 	print(攏總音)
	for 台音 in 攏總音:
		音 = 台音.strip()
		if 音 != '':
			音解析結果, 音合法 = 通用拼音解析器.解析語句佮顯示毋著字元(音)
			# 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本
			文字資料.append((辭典名, 字詞, '漢語族閩方言閩南語', 臺員, 93, 台語漢字, 音解析結果, '正常'))
	國語音 = []
	for 音 in 華語音標.strip()[1:-1].split('-'):
		國語音.append(音[1:-1].split('/'))
# 	print(國語音)
	攏總國語音 = []
	揣出全部組合順紲做國語處理(國語音, 0, '', 攏總國語音)
	for 國音 in 攏總國語音:
		文字資料.append((辭典名, 字詞, '漢語族官話方言北京官話臺灣腔', 臺員, 93, 華語漢字, 國音, '正常'))

# 	print(文字資料)
	流水號 = []
	for 來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本 in 文字資料:
		流水號.append(加文字佮版本(來源, 種類, 腔口, 地區, 年代, 型體, 音標, 版本))
		
	for i in range(len(流水號)):
		for j in range(i + 1, len(流水號)):
			加關係(流水號[i], 流水號[j], 義近, 會當替換)
