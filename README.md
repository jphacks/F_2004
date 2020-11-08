# Telework × Tech
[![表紙-1](https://user-images.githubusercontent.com/50434558/98461410-35e48080-21ef-11eb-9d0f-c75f851d83f8.jpg)](https://youtu.be/IdvRumHTEvc)


※ 画像をクリックすると紹介動画に移動します．
## 使用リポジトリ一覧

| Repository | Content |
| --- | --- |
| [F_2004](https://github.com/jphacks/F_2004) | バックエンド |
| [F_2004_1](https://github.com/jphacks/F_2004_1) | フロントエンド |
| [F_2004_2](https://github.com/jphacks/F_2004_2) | デバイス |
| [F_2004_3](https://github.com/jphacks/F_2004_3) | 予備 | 

※ どのリポジトリがどのように機能しているかは**製品説明**を，システム構成については**システム構成図**をご覧ください．

## 製品概要
### 背景(製品開発のきっかけ、課題等）
　2020年，新型コロナウイルスの影響で，テレワークが急速に広まった．テレワークはワークライフバランスが改善されるなどの良い面もある一方で，仕事とそれ以外を切り分けるのが難しく，同僚の存在を感じることがないため働くリズムを作りづらいといった特徴があり，その結果働きすぎてしまったり，逆に休み過ぎてしまい生産性が下がってしまうという面もある．この課題を解決するために，我々は，テレワーク中の集中力を測定・可視化し，職場内で共有することを可能にするだけでなく，作業効率アップのために休憩タイミングをサジェストしてくれるアプリを開発した．
 
### 製品説明（具体的な製品の説明）
　専用のデバイスを椅子に設置することで，ユーザーが着座しているかどうか，着座している場合，どの程度集中しているかを測定してサーバーにPOSTする．デバイスの詳細については，[F_2004_2](https://github.com/jphacks/F_2004_2) レポジトリを参照されたい．
 
 　サーバー側では，デバイスから受け取った集中力のデータを解析し，集中力が低下していると判断されたユーザーのslackに通知が飛ぶ．こうして，ユーザーが集中力を低下させた瞬間に適度な休憩と取らせることで，長期的に高い生産性を生み出すことができる．サーバー側の実装についてはこの**F_2004**のリポジトリを参照されたい．
  
 　また，デバイスから取得したデータはサーバーに保存されており，後から過去の集中力の遷移を確認することができる．これを見ることで，ユーザーは自分の集中力がどのような時に低下してしまうのか，またどのような時に高い集中力を継続できているのかを確認することができる．フロントエンドの実装については，[F_2004_1](https://github.com/jphacks/F_2004_1)を参照されたい．

### 特長
* 専用のデバイスによる集中力の測定
* 集中力の可視化・共有
* 休憩タイミングのサジェスト

### 解決出来ること
* テレワーク時の，働くリズムを作りづらく生産性が落ちてしまうという課題．

### 今後の展望
- 集中力まで人に見られたくないという意見もある．また，測定された集中力は椅子の形状などによりどうしても個人差が生じてしまう．共有するのは着座状態のみにし，集中力のデータは個人の作業効率を上げるためだけに利用するようにするなど，ユーザーへの配慮を行う．
- 蓄積したユーザーデータを可視化する機能をよりリッチにし、一覧表示、詳細表示、チーム内でのユーザーの検索などをできるようにする．
- ユーザーごとに蓄積した集中力のデータを分析し，そのユーザーにはどういう集中力の特性があり，どういうことを意識するとより効率よく仕事することができるかを知らせてアドバイスを行う．
- 休んだほうがいいとサジェストするだけではなく，「コーヒーを飲みませんか？」や「そろそろ運動するといいですよ！」というように，様々な観点から親しみやく効率アップのためのアドバイスを行えるようにする．
- 座りすぎによる健康被害を防止する，健康維持を手助けする，という観点でアドバイスできるような機能を拡充する．

### 注力したこと（こだわり等）
* 作業状況を可視化したり，他の人から見られてる感を出したいのなら，キーボードの打鍵数を計測したり，Webカメラを利用するなどの方法も考えられる．しかし，キーボードの打鍵数を指標とするとじっくり考えることに抵抗を感じてしまうようになる可能性もあり，また，webカメラを使用するのは監視されている感が強すぎる．そこで我々は，椅子にデバイスを取り付けるだけという，作業時にユーザーが意識する必要がなく，直接監視されている感も強くないが，ユーザーが努力していることを測定することができるエレガントな方法を採用したこと．
* デバイスが直接LANに接続し，サーバーにPOSTリクエストを送信できるようにしたこと．
* 構成要素をシンプルにし，利用を簡単にしたこと．
* バックエンドの構成にAWS(ALB,ECS,RDS等)を用い、リソースのスケーリングやデータのバックアップを簡単にできるようにしたこと。
* データの可視化をシンプルで見やすくするように心がけたこと

## 開発技術
### 活用した技術
- フロントエンド
    - React
    - ReCharts
- バックエンド
    - Flask
        - APIサーバーで動くプログラムに使用
- インフラ
    - uwsgi
        - APIを配信するサーバーとして利用
    - Nginx
        - クライアントからのリクエストをuwsgiに中継する用途で使用
    - Docker
        - APIを配信するためのサーバー環境構築に使用
    - AWS
        - ECS, EC2, ALB
            - APIのホスティングに使用
        - RDS(PostgreSQL)
            - ユーザー情報や集中力のデータの保管に使用 
    - CircleCI
        - フロントエンドの自動デプロイに使用
    - Firebase
        - フロントエンドのホスティングに使用


#### フレームワーク・ライブラリ・モジュール
* React
* Recharts
* Flask

#### デバイス
* ESP32 DevKitC ESP-WROOM-32 開発ボード　と　そのArduino IDEでの開発環境
* GY-521 MPU6050
* Shield2Go pressure DPS310 と　そのライブラリ

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 着座検知・集中力測定デバイス（ [F_2004_2](https://github.com/jphacks/F_2004_2)）
* Arduino IDEで開発したデバイスを制御するプログラム（[Arduino.ino](https://github.com/jphacks/F_2004_2/tree/main/Device)）
* ユーザー情報・集中力のデータを取得、登録する自作のAPI([F_2004](https://github.com/jphacks/F_2004))
* データベースに蓄積した集中力のデータをチャートにして表示するWebページ([F_2004_1](https://github.com/jphacks/F_2004_1))

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
[[1] 大久保　雅史，藤村　安那："加速度センサーを利用した集中度合い推定システムの提案"，WISS2008，2008](https://www.wiss.org/WISS2008Proceedings/posters/paper0038.pdf)

## システム構成図
![システム構成図](system_structure_diagram.png)

## このリポジトリについて
### 概要
ユーザー情報・集中力のデータを取得、登録する自作のAPIのソースコードを管理しているリポジトリ。システム構成図にも概略を示したが、主な用途として以下の三つが挙げられる。
- デバイスからのPOSTリクエストを受け取り、bodyに渡されたユーザーの集中力のデータをデータベースに保存する。
- ユーザーの集中力の遷移を監視し、集中力が低下したと思われるタイミングでそのユーザーのslackに通知を送る。
- 集中力の遷移をチャートにするWebページからGETリクエストを受け取り、ユーザーごとの集中力のデータをレスポンスとして返す。

以下にAPIのエンドポイントとデータベース(DB)の構造を示す。

### API Endpoint
| URL | Method | Parameters | description |
| --- | --- | --- | --- |
| /api/users | GET | | User list |
| /api/users | POST | id: int<br/>name: string | Add user |
| /api/concentration_values/<user_id>| GET | limit: int<br/>date: Datetime | Concentration_value list for specific user |
| /api/concentration_values| POST | user_id: int<br/>concentration_value:int<br/>is_sitting: boolean | Add concentration_value for specific user |


### DB Schema
#### usersテーブル
| Entity name | Data type | Nullable | Default| Primary key | Foreign key | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| id | Integer | No | | ○ | | |
| name | String(100) | No | | | | |
| is_watching| Boolean | No | False| | | |
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |


#### concentration_values
| Entity name | Data type | Nullable | Default| Primary key | Foreign key | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | Integer | No | | ○ | users.id | |
| concentration_value | Integer | No | | | |
| is_sitting | Integer | No | | | |
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |
