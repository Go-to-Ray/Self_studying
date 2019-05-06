#coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

#ボタンがクリックされた時の処理
def ButtonClick():
    #テキストボックスに入力された文字を取得する
    b = editbox1.get()

    #入力された文字が数字4桁か判定
    isok = False
    if len(b) != 4:
        tmsg.showerror("erroe","4桁の数字を入力してください>>>")
    else:
        kazuok = True
    for i in range(4):
        if (b[i] < "0") or (b[i] > "9"):
            tmsg.showerror("error","数字ではありません")
            kazuok = False
            break
        if kazuok:
            isok = True

    if isok:
        #4桁の数字であった時
        #ヒットを判定
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit += 1
        #ブローを判定                                
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j])==a[i])and(a[i]!=int(b[i]))and(a[j]!=int(b[j])):
                    #ブロー判定(要修正？)
                    if (j>i)and(b[j]==b[i]):
                        pass
                    else:
                        blow += 1

        global life
        #hit４で終了
        if hit == 4:
            tmsg.showinfo("WIN","当たり!君の勝ちだよ！")
            #終了
            root.destroy()
        else:
            life -= 1
            if life == 1:
                #ヒット数とブロー数、体力を表示
                rirekibox.insert(tk.END,b+"　　Hit:"+str(hit)+"/Blow:"+str(blow)+"\n")
                tmsg.showinfo("ライフ","君のライフは残り"+str(life)+"だ\nラストチャンスだ")
            elif life == 0:
                rirekibox.insert(tk.END,b+"　　Hit:"+str(hit)+"/Blow:"+str(blow)+"\n")
                tmsg.showinfo("LOSE","ゲームオーバー！君の負けだよ\n答えは"+str(a)+"だよ")
                #終了
                root.destroy()
            else:
                #ヒット数とブロー数、体力を表示
                rirekibox.insert(tk.END,b+"　　Hit:"+str(hit)+"/Blow:"+str(blow)+"\n")
                tmsg.showinfo("ライフ","君のライフは残り"+str(life)+"です")

#メインのプログラム
#最初にランダムな4桁の数字を作る
a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

#体力の設定
life = 10

#メインのプログラム
#ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("HIT & BROW game")

#履歴表示
rirekibox = tk.Text(root, font=("Helvetica",14))
rirekibox.place(x=400, y=0, width=200, height=400)

#ラベルを作る
label1 = tk.Label(root, text = "4桁の数を入力してください", font=("Helvetica",14))
label1.place(x = 20, y = 20)
"""確認用
label2 = tk.Label(root, text = a, font=("Helvetica",14))
label2.place(x = 280, y = 370)
"""
#テキストボックスを作る
editbox1 = tk.Entry(width = 4, font=("Helvetica",28))
editbox1.place(x = 120, y = 60)

#ボタンを作る
button1 = tk.Button(root, text = "チェック", font=("Helvetica",14), command = ButtonClick)
button1.place(x = 220, y = 60)

#ウィンドウを表示する
root.mainloop()

