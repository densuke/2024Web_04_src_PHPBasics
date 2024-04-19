from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys

# リモートサーバーのアドレス
REMOTE_URL = 'http://selenium:4444/wd/hub'

class SampleTest(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())
            assert self.driver is not None

    def tearDown(self):
        self.driver.quit()

    def test_Hello(self):
        """pタグ取得のテスト
        最初のpタグの値を取得します。
        その値が"Hello,PHP"ならテストが通ります。
        """
        self.driver.get('http://web/hello.php')
        time.sleep(2)
        # pタグの最初のものを取得
        element = self.driver.find_element(By.TAG_NAME, "p")
        self.assertEqual('Hello,PHP', element.text)
        self.driver.get_screenshot_as_file(f"{sys.path[0]}/../results/hello.png")

    def test_Hello_using_PHP(self):
        """PHPを使っているかの確認
        直接PHPのファイルhello.phpを開き、
        `<?php`を含んでいるかをチェックします。

        ここ少しだけ解説: 実行する状況によりベースのパスが変わり得ます。
        (ベースディレクトリで動かすか、testsディレクトリで動かすかで変わります。)
        よって、sys.path[0]を使って、テストファイルの場所を取得しています。
        この値はスクリプトのあるパスになるため固定となります。
        """
        with open(f"{sys.path[0]}/../public/hello.php") as f:
            self.assertTrue('<?php' in f.read())

if __name__ == '__main__':
    unittest.main()
