#  Telework × Tech
[![表紙-1](https://user-images.githubusercontent.com/50434558/98461410-35e48080-21ef-11eb-9d0f-c75f851d83f8.jpg)](https://youtu.be/IdvRumHTEvc)

## 使用リポジトリ一覧

| Repository | Content |
| --- | --- |
| F_2004 |  |
| [F_2004_1](https://github.com/jphacks/F_2004_1) |  |
| [F_2004_2](https://github.com/jphacks/F_2004_2) | デバイス用 |
| [F_2004_3](https://github.com/jphacks/F_2004_3) | 予備 | 

*) 本アプリのシステムの全体像については**システム**の項をご覧ください．

## 製品概要
### 背景(製品開発のきっかけ、課題等）
　2020年，新型コロナウイルスの影響で，テレワークが急速に広まった．テレワークはワークライフバランスが改善されるなどの良い面もある一方で，仕事とそれ以外を切り分けるのが難しく，同僚の存在を感じることがないため働くリズムを作りづらいといった特徴があり，その結果働きすぎてしまったり，逆に休み過ぎてしまい生産性が下がってしまうという面もある．この課題を解決するために，我々は，テレワーク中の集中力を測定・可視化し，職場内で共有することを可能にするだけでなく，作業効率アップのために休憩タイミングをサジェストしてくれるアプリを開発した．
 
### 製品説明（具体的な製品の説明）
　専用のデバイスを椅子に設置することで，ユーザーが着座しているかどうか，着座している場合，どの程度集中しているかを測定してサーバーにPOSTする．デバイスの詳細については，[F_2004_2](https://github.com/jphacks/F_2004_2) レポジトリを参照されたい．
 
 //　デバイス以外の説明お願いします．

### 特長
* 専用のデバイスによる集中力の測定
* 集中力の可視化・共有
* 休憩タイミングのサジェスト

### 解決出来ること
* テレワーク時の，働くリズムを作りづらく生産性が落ちてしまうという課題．

### 今後の展望
### 注力したこと（こだわり等）
* デバイスが直接LANに接続し，サーバーにPOSTリクエストを送信できるようにしたこと．
* 構成要素をシンプルにし，利用を簡単にしたこと．

// 追記願います．

## 開発技術
### 活用した技術
- Arduino
    - デバイスの制御に利用
- Flask
    - APIサーバーで動くプログラムに使用
- PostgreSQL
    - データベースに使用
- uwsgi
    - APIを配信するサーバーとして利用
- Nginx
    - クライアントからのリクエストをuwsgiに中継する用途で使用
 
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* 
* 

#### デバイス
* Arduino IDE
* ESP32 DevKitC ESP-WROOM-32 開発ボード　とそのArduino IDEでの開発環境
* GY-521 MPU6050
* Shield2Go pressure DPS310 とそのライブラリ

### 独自技術
#### ハッカソンで開発した独自機能・技術
//独自で開発したものの内容をこちらに記載してください．特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

* 着座検知・集中力測定デバイス（ [F_2004_2](https://github.com/jphacks/F_2004_2)）
* Arduino IDEで開発したデバイスを制御するプログラム（[Arduino.ino](https://github.com/jphacks/F_2004_2/tree/main/Device)）

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
[[1] 大久保　雅史，藤村　安那："加速度センサーを利用した集中度合い推定システムの提案"，WISS2008，2008](https://www.wiss.org/WISS2008Proceedings/posters/paper0038.pdf)

## システム

// システム図とそれらがどのリポジトリのどこにあるか関係をまとめる．

## このリポジトリについて
### 概要

// 説明が少なすぎる気がするので追記願います

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
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |


#### concentration_values
| Entity name | Data type | Nullable | Default| Primary key | Foreign key | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | Integer | No | | ○ | users.id | |
| concentration_value | Integer | No | | | |
| is_sitting | Integer | No | | | |
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |
