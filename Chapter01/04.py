text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
split = text.split()

first_letter = [1, 5, 6, 7, 8, 9, 15, 16, 19]
num = 1
result = {}

for i in split:
    if num in first_letter:
        result[i[0]] = num

    else:
        result[i[0] + i[1]] = num
    
    num += 2
    
  print(result)
