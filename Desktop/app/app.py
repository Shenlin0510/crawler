from flask import Flask
app=Flask(__name__) #__name__代表目前執行的模組
 
@app.route("/") #函式裝飾 (Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello Flask "
@app.route("/test")  #代表我們要處理的網路路徑
def test():
    return "test test"

if __name__ =="__main__": #如果以主程式執行
    app.run() 