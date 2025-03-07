import random

def zyanken():
  kobusi = {"1":"グー","2":"チョキ","3":"パー"}

  play = kobusi["1"]
  cpu = kobusi["1"]
  print("最初はグー\nじゃんけんぽん！")
  while play == cpu:
    play = input("1（グー）、2（チョキ）、3（パー）のどれかを入力")
    play1 = play.isdigit()
    if play1 == True:
      if play == "1" or play == "2" or play == "3":
        play = str(kobusi[play])
      else:
        play = "false"
        print("もう一度入力してください")
    elif play1 == False:
      if play == "グー" or play == "チョキ" or play == "パー":
        play = str(play)
      else:
        play = "false"
        print("もう一度入力してください")
    cpu = random.choice(list(kobusi.values()))
    if play == "グー" or play == "チョキ" or play == "パー":
      print("あなた：" + play + "、CPU：" + str(cpu))
      if play != cpu:
        if play == "グー" and cpu == "パー":
          print("\n結果：あなたの負け...")
          break
        elif play == "チョキ" and cpu == "グー":
          print("\n結果：あなたの負け...")
          break
        elif play == "パー" and cpu == "チョキ":
          print("\n結果：あなたの負け...")
          break
        else :
          print("\n結果：あなたの勝ち！")
      else:
        print("\nあいこでしょ！")
    elif play == "false":
      play = kobusi["1"]
      cpu = kobusi["1"]

zyanken()