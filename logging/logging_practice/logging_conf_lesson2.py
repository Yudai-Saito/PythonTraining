import logging

def hoge():
    logger = logging.getLogger("conf_test")
    
    logger.debug("動作の診断に関する詳細情報")
    logger.info("想定通りの動作の確認")
    logger.warning("想定外のことが発生、問題が起こりそう")
    logger.error("重大なエラーにより、機能の一部が停止")
    logger.critical("プログラム全体がダウン、重大なエラー")