# 作成物の概要
　私が今回作ったのは右側に配置したプレイヤーが左からくる敵を気弾で倒すゲームである（ドラゴンボールのゲームから着想を得た）。
ゲームの流れとしては、スペースバーを押してゲームが始まると左から敵（敵は強さが1～3まである）が登場し、<br>
その敵を気弾で倒す（sキーを押す）と左上に表示されるスコアに加算される。また敵を倒していくとその数に応じてオプションのボタンが表示される（攻撃力アップ、体力アップ、特殊攻撃）。<br>
特殊攻撃が敵に当たると画面の敵がすべて倒れるようになっている。
オプションのボタン使用すると（クリックする）ボタンは消える。またプレイヤーは敵に当たった時、敵がプレイヤーを超えて右側に行ったときにダメージを受ける。<br>
プレイヤーの体力が0になった時ゲームオーバーとなりゲームが終了する。なおプレイヤーの体力はスコアの下に表示される。
 
# 作った背景
 大学の授業で自由課題を作成する必要があったから。
 
# 使用技術
 Python（言語）、Pygame(ライブラリ）
 
# 意識した点
 オブジェクト指向の設計を心掛けた点。
 コメントを詳細に書くようにした点。　
  
# 苦労した点
 敵と気弾の衝突した時、敵とプレイヤーの衝突した時など様々なことを考慮した点。<br>
 エラーに対するデバッグ。

 
