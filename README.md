# 練習問題: 「はじめてのPHP」

PHPの命令による出力練習です。

# 問題

`public`ディレクトリ以下に`hello.php`ファイルを作って下さい。
このファイルはPHPのテキストとなっています。

`hello.php` において、PHPの出力命令を用いて、ページとして `Hello,PHP` と返すようにプログラムを組んでください。
ただし条件があります。

1. PHPの出力命令を用いて出すこと
2. **最初の**「pタグ」の要素として出してください。
3. ズルして単純なHTMLで書かないこと(簡易的なチェックはします)

# 作業手順(コード取得と信頼)

今後のこともあるので手順について少し細かく記述します。

1. このリポジトリをcloneして、自身のマシン上で操作できるようにしてください
  1. 緑のCodeボタンのところでリポジトリアクセス用のリンクを取得しておきます ![](/images/get-link.png)
  2. vscodeを開く
  3. コマンドパレットを開きます(WindowsならCtrl-Shift-P、 macOSならCmd-Shift-P)
  4. `git clone` とタイプして、`Git: Clone`コマンドを呼び出します
    - 最初の `>` は消さないこと
    - 打ち込んでいると、途中でタイプした文字を含むコマンドが浮いてきます、 `Git: Clone` が見えてきたらカーソルキー下で選んでEnter
    - よく使うコマンドは早めに浮いてきたり、最初から見えることもあります(これもカーソルキー下で選べます)
    - ![](/images/git-clone.png)
  5. 取得したリポジトリアクセス用のリンクをペースト(貼り付け)します ※Ctrl-V(Command-V)してEnter ![](/images/paste-repo.png)
  6. 保存先の確認が出たら、事前に作っているディレクトリ(Windowsであれば `C:\web_app_dev` を選択する) ![](/images/select-output.png)
2. clone後のウィンドウで、以下の確認がでることがあります。この場合は **フォルダーを信頼して続行** を押してください、同様に作者の信頼が必要になるので、こちらも信頼するようにしてください。 ![](/images/user-authorize.png)
3. clone完了後、データをどのように開くかの確認が出ます。どちらでもかまいません(今のウィンドウを置き換えるか、追加でウィンドウを開くかの違いです) ![](/images/after-pull-select.png)

# 作業手順(開発環境の構築)

このままでも課題コードを書けますが、確認が全然できない状況ですので、開発環境に切り替えるための作業をおこないます。

1. コマンドパレットを開き(Ctrl-Shift-P もしくは  Cmd-Shift-P)、といれ、`rebuild`と入れてみてください、
   これで、 `Dev Container: Rebuild and Reopen in Container` が出てくるので選んでください ![](/images/type-rebuild.png)
2. 構成を読み取り、選択肢が出てきます、 **PHP開発環境** の側を選んでください。 ![](/images/select-phpdev.png)
3. しばらく構成処理が行われ(CPUパワーとネットワークに依存)、構成が行われます ![](/images/reconfiguring-window.png)
  - 気になる方はログを出すようにすると進行状況がわかります ![](/images/reconfigure-view-log.png)

![](/images/done.png)

あとは課題にあわせてファイルを作成し、コミットしてからpushしてください。

## おまけ

* Makefile tools拡張が入っている場合、 `Makefile`を検出して内容チェックをする旨が出ます、実害は無いので了解しておいてください。 ![](/images/makefile-tool.png)
* 同様に、入れている拡張によって追加のメッセージが出ることがありますので、適当にやっておいてください(こればかりはなにが出るかわからない)
