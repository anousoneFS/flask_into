from flask import Flask 

app = Flask(__name__)

def name(first_name, last_name):
    return first_name + last_name

if __name__ == "__main__":
    print("hahaha")
    print(name("anousone", "worlakoumman"))
    print(name("sone", "freestyle"))
    print(name("sone", "sonehaha"))
