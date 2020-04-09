age = 24
print("Mam " + str(age) + " lat")
print("My age is {0} years".format(age))
print("Jest {0} dni w {1}, {2}, {3}, {4}, {5}, {6} i {7}"
      .format(31, "Sty", "Mar", "Maj", "Lip", "Sie", "Paź", "Gru"))
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))