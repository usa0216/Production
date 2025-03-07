def dentaku():
  print("簡易電卓アプリケーションです。\n終了するには「=」を入力してください")
  suu = float(input("数値："))
  while True:
    en = str(input("演算子（+,-,*,/,=）："))
    if en == "=":
      print("演算結果は" + str(suu) + "です。")
      break
    elif en == "+" or en == "-" or en == "*" or en == "/":
      suu1 = float(input("数値："))
      if en == "+":
        suu += suu1
      elif en == "-":
        suu -= suu1
      elif en == "*":
        suu *= suu1
      elif en == "/":
        suu /= suu1
    else:
      print("無効な操作です。\nもう一度入力してください")
dentaku()