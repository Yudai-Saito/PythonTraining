import logging


def loglevel_test():

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


if __name__ == "__main__":
    loglevel_test()