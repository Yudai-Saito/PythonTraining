import logging
import logging_lesson2


def loglevel_test():
    LOG_FORMAT = "%(levelname)s : %(asctime)s : %(name)s : %(message)s"

    """
    ログレベル：
    ログレベルを変更するには、basicConfigで設定可能。
    INFO : info以下表示、WARNING : warning以下表示といった具合。
    頭についてないと動作しなかった。既にログ吐いてからの設定は不可のよう。

    ファイル出力：
    filenameで指定可能。
    ログは毎回追記されていた。

    フォーマット：
    formatで指定可能。
    定数作って引数に与えてあげれば良さそう。
    時間のフォーマットはdatefmtで設定。"%Y-%m-%d %H:%M:%S"が日本人には見やすそう。
    その他、[関数名、PID、行番号]などもある。適したものを探して使おう。
    """
    logging.basicConfig(filename="../logs/test.log",format=LOG_FORMAT, 
                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.WARNING)

    """
    5つのログレベルが存在する。
    デフォルトのレベルがwarningなので、info以上は表示されない。
    どのレベルで、何を出力するのかは開発者次第。
    """
    logging.debug("動作の診断に関する詳細情報")
    logging.info("想定通りの動作の確認")
    logging.warning("想定外のことが発生、問題が起こりそう")
    logging.error("重大なエラーにより、機能の一部が停止")
    logging.critical("プログラム全体がダウン、重大なエラー")

    """
    ロガーを作成することで特定の処理だけのログ設定が可能になる。
    setLevelで、個別にログレベルを変えることも可能。
    getLogger()で名前変更ができる。"hoge"でhogeが、__name__で実行したファイル名が出力。
    実行元[__main__.pyは__main__に]、別ファイル(bar.py)は[bar]となるようだ。
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug("ロガーでのデバッグ")

    logging_lesson2.hoge()

if __name__ == "__main__":
    loglevel_test()