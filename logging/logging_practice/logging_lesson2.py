import logging

"""
main処理以外でのログ情報出力には、ハンドラを使用する。
ハンドラを組み合わせることにより、ロガー毎のログ出力が可能となる。
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#フォーマット形式作成
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(name)s : %(message)s")
#ファイルハンドラ(出力をファイルへ)
file_handler = logging.FileHandler("../logs/handler.log") 
#ファイルハンドラへフォーマットをセット
file_handler.setFormatter(formatter)

#ロガーへハンドラをセット
logger.addHandler(file_handler)#


def hoge():
    logger.info("logs from other file.")