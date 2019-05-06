# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:12:56 2019

@author: 後藤　嶺
"""

import tkinter as tk
import tkinter.messagebox as tmsg

#位置決定のため
def ButtonClick_1():
    global x,y,dx,dy,editbox3,editbox4
    #テキストボックスに入力された文字を取得する
    x = float(editbox1.get())
    y = float(editbox2.get())
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width = 0)

    #速度ラベル
    label3 = tk.Label(root, text = "xの変位量を入力してください", font=("Helvetica",10))
    label3.place(x = 20, y = 135)
    label4 = tk.Label(root, text = "yの変位量を入力してください", font=("Helvetica",10))
    label4.place(x = 20, y = 175)
    #速度テキストエディタ
    editbox3 = tk.Entry(width = 4, font=("Helvetica",16))
    editbox3.place(x = 220, y = 130)
    editbox4 = tk.Entry(width = 4, font=("Helvetica",16))
    editbox4.place(x = 220, y = 170)
    #ボタン２を作る
    button2 = tk.Button(root, text = "実行", font=("Helvetica",10), command = ButtonClick_2)
    button2.place(x = 20, y = 200)
    
#速度決定のため
def ButtonClick_2():
    global dx,dy
    #テキストボックスに入力された文字を取得する
    dx = float(editbox3.get())
    dy = float(editbox4.get())
    return move()


def move():
    global x,y,dx,dy
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width = 0)
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="white",width=0)#whiteで円を消す
    x += dx  #座標変更
    y += dy
    canvas.create_oval(x-20,y-20,x+20,y+20,fill="red",width = 0)#redで円を描く
    
    if x >= canvas.winfo_width():
        dx = -dx
    if x <= 0:
        dx = -dx
    if y >= canvas.winfo_height():
        dy = -dy
    if y <= 0:
        dy = -dy
    
    root.after(15,move)  #do move method after 10ms only once
    
root = tk.Tk()
root.geometry("900x400")
root.title("円を動かす")

canvas = tk.Canvas(root,width = 600,height = 400,bg = "white")
canvas.place(x = 300,y = 0)


#ラベルを作る
label1 = tk.Label(root, text = "xの位置を入力してください", font=("Helvetica",10))
label1.place(x = 20, y = 20)
label2 = tk.Label(root, text = "yの位置を入力してください", font=("Helvetica",10))
label2.place(x = 20, y = 60)

#テキストボックスを作る
#位置
editbox1 = tk.Entry(width = 4, font=("Helvetica",16))
editbox1.place(x = 220, y = 15)
editbox2 = tk.Entry(width = 4, font=("Helvetica",16))
editbox2.place(x = 220, y = 55)


#ボタンを作る
button1 = tk.Button(root, text = "実行", font=("Helvetica",10), command = ButtonClick_1)
button1.place(x = 20, y = 100)


root.after(10,move)

root.mainloop()
    