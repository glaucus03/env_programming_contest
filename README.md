# programming contest環境
atcoderでonline-judge-toolsを使ってサンプルのダウンロード、テスト、提出などを行う

vscodeでの環境を想定。task runnerを使ってワンクリックで一連の流れを実行できるよう

## 導入
このリポジトリをcloneして、あとはvscodeのremote containerで開けば自動で構築までしてくれるはず

提出にはid,passwordの認証が必要

```
$oj login https://atcoder.jp/
```

などで対象のサイトのログインをしておく

コードの頭に
```
"""
URL:https://atcoder.jp/contests/typical90/tasks/typical90_bl
DATE:2021/09/24
"""
```

のように問題のURLを記載しておけば、自動で実行できる

## todo:
- README.mdの充実
- libraryの整理