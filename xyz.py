from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_cors import cross_origin
import pandas as pd
import pyodbc

#connection to database
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=DESKTOP-RJP28KB;'
                      'Database=Inventory;'
                      'Trusted_Connection=yes;');

app = Flask(__name__)

@app.route("/")             #This is a decorator.
@cross_origin()
def home():
    return render_template("index1.html")


@app.route("/Stock", methods = ["GET", "POST"])
@cross_origin()
def Stock():
    data1 = pd.read_sql("SELECT * FROM Stock", conn)
    result1=data1.to_html()
    return result1


@app.route("/Purchase History", methods = ["GET", "POST"])
@cross_origin()
def P_H():
    data1 = pd.read_sql("SELECT * FROM Purchase", conn)
    result1=data1.to_html()
    return result1


@app.route("/Login User Details", methods = ["GET", "POST"])
@cross_origin()
def L_U_D():
    data1 = pd.read_sql("SELECT * FROM User_", conn)
    result1=data1.to_html()
    return result1


@app.route("/Customer Details", methods = ["GET", "POST"])
@cross_origin()
def C_D():
    data1 = pd.read_sql("SELECT * FROM Customer", conn)
    result1=data1.to_html()
    return result1


@app.route("/Inventory", methods = ["GET", "POST"])
@cross_origin()
def Inv():
    data1 = pd.read_sql("SELECT * FROM Inventory", conn)
    result1=data1.to_html()
    return result1


@app.route("/Supplier Details", methods = ["GET", "POST"])
@cross_origin()
def S_D():
    data1 = pd.read_sql("SELECT * FROM Supplier", conn)
    result1=data1.to_html()
    return result1
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7532, debug = True) 