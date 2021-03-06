from unittest.case import TestCase
from unittest.mock import patch
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.解析整理.解析錯誤 import 解析錯誤
from 臺灣言語工具.解析整理.型態錯誤 import 型態錯誤
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音


class 集單元試驗(TestCase):

    def test_集烏白傳(self):
        self.assertRaises(型態錯誤, 集, None)
        self.assertRaises(型態錯誤, 集, [None])
        self.assertRaises(型態錯誤, 集, ['sui2'])

    def test_看集(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = 拆文分析器.對齊集物件(型, 音)
        self.assertEqual(集物件.看型(), 型)
        self.assertEqual(集物件.看音(), 音)
        分詞 = '恁｜lin1 老｜lau3 母｜bu2 ti3｜ti3 佗｜to1 位｜ui7'
        self.assertEqual(集物件.看分詞(), 分詞)

    def test_看集內底有兩組以上(self):
        型 = '恁老母ti3佗位'
        音 = 'lin1 lau3 bu2 ti3 to1 ui7'
        集物件 = 集([拆文分析器.對齊組物件(型, 音), 拆文分析器.對齊組物件(型, 音)])
        self.assertRaises(解析錯誤, 集物件.看型)
        self.assertRaises(解析錯誤, 集物件.看音)
        self.assertRaises(解析錯誤, 集物件.看分詞)

    @patch('臺灣言語工具.基本物件.組.組.綜合標音')
    def test_綜合標音用組的結果(self, 組綜合標音mock):
        集物件 = 拆文分析器.對齊集物件('美女', 'mi2-lu2')
        self.assertEqual(集物件.綜合標音(閩南語綜合標音), 組綜合標音mock.return_value)

    def test_綜合標音愛用頭一組(self):
        # 因為攏用佇輸出，愛檢查就佇程式別位檢查
        媠某 = 拆文分析器.對齊組物件('美女', 'sui2-boo2')
        美女 = 拆文分析器.對齊組物件('美女', 'mi2-lu2')
        self.assertEqual(
            集([媠某, 美女]).綜合標音(閩南語綜合標音),
            集([媠某]).綜合標音(閩南語綜合標音)
        )

    def test_空集綜合標音莫例外(self):
        # 因為攏用佇輸出，愛檢查空愛佇程式別位檢查
        集物件 = 集()
        self.assertEqual(集物件.綜合標音(閩南語綜合標音), [
            {}
        ])
