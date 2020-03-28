## REST APIs with Flask and Python
https://github.com/schoolofcode-me/rest-api-sections


#### 查看安裝項目 & 安裝 Flask
```bash
pip freeze

pip install flask
pip install Flask-RESTful
pip install Flask-JWT
```

## 使用 virtualenv
```bash
pip install virtualenv
```
#### 在當前的目錄，創建一個名為 venv的資料夾，並放入新的 python 安裝 
```bash
virtualenv venv --python=python3.7
```

#### 切換到 venv
可以利用 pip freeze 查看 為乾淨的 venv
```bash
source venv/bin/activate

./venv/Scripts/actvate.bat
```

#### 退出 venv
```bash
deactivate
```


## REST API 原則
ItemList resource
 * GET /items

Item resource

 * GET /item/chair

 * POST /item/chair


 #### section 4
 venv
 Flask-RESTful

 #### section 5
 SQL Database
