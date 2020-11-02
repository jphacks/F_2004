#  Telework × Tech (Backend)
[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
### 製品説明（具体的な製品の説明）
### 特長
####1. 特長1
####2. 特長2
####3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
* 
* 

## 開発技術
### 活用した技術
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
* 
* 

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 
* 


## API Endpoint
| URL | Method | Parameters |
| --- | --- | --- |
| /api/users | GET | |
| /api/users | POST | id: int<br/>name: string |
| /api/concentration_values/<user_id>| GET | |
| /api/concentration_values| POST | user_id: int<br/>concentration_value:int<br/>is_sitting: boolean |


## DB Schema
### usersテーブル
| Entity name | Data type | Nullable | Default| Primary key | Foreign key | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| id | Integer | No | | ○ | | |
| name | String(100) | No | | | | |
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |


### concentration_values
| Entity name | Data type | Nullable | Default| Primary key | Foreign key | Extra |
| --- | --- | --- | --- | --- | --- | --- |
| user_id | Integer | No | | ○ | users.id | |
| concentration_value | Integer | No | | | |
| is_sitting | Integer | No | | | |
| created_at | Timestamp | No | CURRENT_TIMESTAMP | ○ |
