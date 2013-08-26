from 教會系羅馬音標 import 教會系羅馬音標
from 方音符號吳守禮改良式 import 方音符號吳守禮改良式

臺灣閩南語羅馬字拼音聲母表 = {'p', 'ph', 'm', 'b', 't', 'th', 'n', 'l',
		'k', 'kh', 'ng', 'g', 'h', 'ts', 'tsh', 's', 'j', ''}
#臺灣閩南語羅馬字拼音方案使用手冊 + 臺灣語語音入門 + 教育部辭典的字
臺灣閩南語羅馬字拼音韻母表 = {'a', 'e', 'i', 'oo', 'o', 'u',
		'ai', 'au', 'ia', 'io', 'iu', 'ua', 'ue', 'ui', 'iau', 'uai',
		'ann', 'enn', 'inn', 'onn', 'm', 'ng', 'ainn', 'iann', 'iaunn', 'iunn', 'uann', 'uainn',
		'am', 'an', 'ang', 'im', 'in', 'ing', 'om', 'ong', 'iam', 'ian', 'iang', 'iong', 'un', 'uan',
		'ah', 'eh', 'ih', 'oh', 'uh', 'auh', 'iah', 'ioh', 'iuh', 'iauh', 'uah', 'ueh', 'ooh',
		'annh', 'ennh', 'innh', 'mh', 'iannh', 'ngh', 'ap', 'at', 'ak', 'op', 'ok', 'iok',
		'ip', 'it', 'ik', 'iap', 'iat', 'iak', 'ut', 'uat',
		'ioo', 'ir', 'ere', 'er', 'irinn', 'ee', 'uee', 'eeh', 'uinn', 'ionn', 'irm', 'irn', 'irng', 'eng', 'uang',
		'aih', 'ainnh', 'aunnh', 'erh', 'ereh', 'uih', 'irp', 'irt', 'irk', } | {
		'aunn', 'uenn','uaih', 'iunnh', 'iaunnh', 'uennh', 'uinnh', 'uainnh', 'iut', 'uak'} |{'onnh'}|{
		'or','orh','ior','iorh',}
臺灣閩南語羅馬字拼音聲調符號表 = dict(á = ('a', 2), à = ('a', 3), â = ('a', 5), ǎ = ('a', 6), ā = ('a', 7), a̍ = ('a', 8), a̋ = ('a', 9),
é = ('e', 2), è = ('e', 3), ê = ('e', 5), ě = ('e', 6), ē = ('e', 7), e̍ = ('e', 8), e̋ = ('e', 9),
í = ('i', 2), ì = ('i', 3), î = ('i', 5), ǐ = ('i', 6), ī = ('i', 7), i̍ = ('i', 8), i̋ = ('i', 9),
ó = ('o', 2), ò = ('o', 3), ô = ('o', 5), ǒ = ('o', 6), ō = ('o', 7), o̍ = ('o', 8), ő = ('o', 9),
ú = ('u', 2), ù = ('u', 3), û = ('u', 5), ǔ = ('u', 6), ū = ('u', 7), u̍ = ('u', 8), ű = ('u', 9),
ḿ = ('m', 2), m̀ = ('m', 3), m̂ = ('m', 5), m̌ = ('m', 6), m̄ = ('m', 7), m̍ = ('m', 8), m̋ = ('m', 9),
ń = ('n', 2), ǹ = ('n', 3), n̂ = ('n', 5), ň = ('n', 6), n̄ = ('n', 7), n̍ = ('n', 8), n̋ = ('n', 9),)

臺灣閩南語羅馬字拼音數字調轉閏號調表={('a', '2'):"á",('a', '3'):"à",('a', '5'):"â",('a', '6'):"ǎ",('a', '7'):"ā",('a', '8'):"a̍",('a', '9'):"a̋",
('e', '2'):"é",('e', '3'):"è",('e', '5'):"ê",('e', '6'):"ě",('e', '7'):"ē",('e', '8'):"e̍",('e', '9'):"e̋",
('ee', '2'):"ée",('ee', '3'):"èe",('ee', '5'):"êe",('ee', '6'):"ěe",('ee', '7'):"ēe",('ee', '8'):"e̍e",('ee', '9'):"e̋e",
('ere', '2'):"eré",('ere', '3'):"erè",('ere', '5'):"erê",('ere', '6'):"erě",('ere', '7'):"erē",('ere', '8'):"ere̍",('ere', '9'):"ere̋",
('i', '2'):"í",('i', '3'):"ì",('i', '5'):"î",('i', '6'):"ǐ",('i', '7'):"ī",('i', '8'):"i̍",('i', '9'):"i̋",
('iri', '2'):"irí",('iri', '3'):"irì",('iri', '5'):"irî",('iri', '6'):"irǐ",('iri', '7'):"irī",('iri', '8'):"iri̍",('iri', '9'):"iri̋",
('m', '2'):"ḿ",('m', '3'):"m̀",('m', '5'):"m̂",('m', '6'):"m̌",('m', '7'):"m̄",('m', '8'):"m̍",('m', '9'):"m̋",
('ng', '2'):"ńg",('ng', '3'):"ǹg",('ng', '5'):"n̂g",('ng', '6'):"ňg",('ng', '7'):"n̄g",('ng', '8'):"n̍g",('ng', '9'):"n̋g",
('o', '2'):"ó",('o', '3'):"ò",('o', '5'):"ô",('o', '6'):"ǒ",('o', '7'):"ō",('o', '8'):"o̍",('o', '9'):"ő",
('oo', '2'):"óo",('oo', '3'):"òo",('oo', '5'):"ôo",('oo', '6'):"ǒo",('oo', '7'):"ōo",('oo', '8'):"o̍o",('oo', '9'):"őo",
('u', '2'):"ú",('u', '3'):"ù",('u', '5'):"û",('u', '6'):"ǔ",('u', '7'):"ū",('u', '8'):"u̍",('u', '9'):"ű",
('ui', '2'):"uí",('ui', '3'):"uì",('ui', '5'):"uî",('ui', '6'):"uǐ",('ui', '7'):"uī",('ui', '8'):"ui̍",('ui', '9'):"ui̋",
('iu', '2'):"iú",('iu', '3'):"iù",('iu', '5'):"iû",('iu', '6'):"iǔ",('iu', '7'):"iū",('iu', '8'):"iu̍",('iu', '9'):"iű",}
class 臺灣閩南語羅馬字拼音(教會系羅馬音標):
	聲母表 = 臺灣閩南語羅馬字拼音聲母表
	韻母表 = 臺灣閩南語羅馬字拼音韻母表
	聲調符號表 = None
	數字調轉閏號調表=臺灣閩南語羅馬字拼音數字調轉閏號調表
	聲 = None
	韻 = None
	調 = 1
	輕 = False
	韻頭 = None
	韻腹 = None
	韻尾 = None
	音標 = None
	def __init__(self, 音標):
		self.分析聲韻調(音標)
#		if self.音標 != None:			
#			print('聲母=' + self.聲 + ' 韻母=' + self.韻 + ' 調＝' + str(self.調))
#		else:
#			print('不合法 原音標＝' + 音標)
	def 轉換到臺灣閩南語羅馬字拼音(self):
		return self.音標
	def 轉閏號調(self):		
		if self.音標==None:
			return None
		
		if (self.調!='2' and self.調!='3' and self.調!='5' and self.調!='6' 
			and self.調!='7' and self.調!='8' and self.調!='9'):# or 調!=10:
			return self.聲 + self.韻
				
		for 符號 in ['a','oo','o','ee','ere','e','iri','ui','iu','u','i','ng','m']:
			if 符號 in self.音標:
				替代符號=符號
				break
			
		return self.聲+self.韻.replace(替代符號,self.數字調轉閏號調表[(替代符號,self.調)])
	def 轉吳守禮方音(self):
		return 方音符號吳守禮改良式(self.音標).音標
	def 轉吳守禮方音組字式(self):
		return 方音符號吳守禮改良式(self.音標).產生音標組字式()
	def 轉通用拼音(self):
		return '　'
# 聲 介 韻 調，韻含元音跟韻尾

if __name__ == '__main__':
	print (len(臺灣閩南語羅馬字拼音韻母表))
	print(臺灣閩南語羅馬字拼音('@@').音標)
	print(臺灣閩南語羅馬字拼音('pI̋m').音標)
	print(臺灣閩南語羅馬字拼音('pe̍m').音標)
	print(臺灣閩南語羅馬字拼音('pi̍m').音標)
	print(臺灣閩南語羅馬字拼音('pîm').音標)
	print(臺灣閩南語羅馬字拼音('pǐN').音標)
	print(臺灣閩南語羅馬字拼音('pih').音標)
	print(臺灣閩南語羅馬字拼音('cat8').音標)
	print(臺灣閩南語羅馬字拼音('Pih8').音標)

	print(臺灣閩南語羅馬字拼音('nňg').音標)
	print(臺灣閩南語羅馬字拼音('tor').音標)
	print(臺灣閩南語羅馬字拼音('tsőo').音標)
	print(臺灣閩南語羅馬字拼音('tsňg').音標)
	print(臺灣閩南語羅馬字拼音('xxtsé--á').音標)
	print(臺灣閩南語羅馬字拼音('pňg').音標)
	print(臺灣閩南語羅馬字拼音('óonn').音標)
	
	print(臺灣閩南語羅馬字拼音('ainn7').音標)
	print(臺灣閩南語羅馬字拼音('ang3').音標)
	print(臺灣閩南語羅馬字拼音('au3').音標)
	print(臺灣閩南語羅馬字拼音('mng5').音標)
	print(臺灣閩南語羅馬字拼音('ainn7').轉閏號調())
	print(臺灣閩南語羅馬字拼音('ang3').轉閏號調())
	print(臺灣閩南語羅馬字拼音('au3').轉閏號調())
	print(臺灣閩南語羅馬字拼音('mng5').轉閏號調())
	print(臺灣閩南語羅馬字拼音('gio2').轉閏號調())
	print(臺灣閩南語羅馬字拼音('hiunnh8').轉閏號調())
	#for a,b in 臺灣閩南語羅馬字拼音聲調符號表.items():
	#	print(b,'=\"',a,'",',sep='')

	#a=