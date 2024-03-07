nric = input('Enter an NRIC number: ')

# Type your code below
valid1 = False
valid2 = False
valid3 = False


letter1 = nric[0].lower()



if letter1 == "s" or letter1 == "t" or letter1 == "f" or letter1 == "g":
  valid1 = True



nric_nums = nric[1:8]
all_num = nric_nums.isdigit()


if len(nric_nums) == 7 and all_num == True:
  valid2 = True


last_letter = nric[-1]
is_number = True

try:
  last_letter_check = int(last_letter)
except ValueError:
  is_number = False

if is_number == False:
  valid3 = True

# part 2
if valid1 == True and valid2 == True and valid3 == True:
  digits_valid = False
  
  nric_list1 = int(nric[1]) * 2
  nric_list2 = int(nric[2]) * 7
  nric_list3 = int(nric[3]) * 6
  nric_list4 = int(nric[4]) * 5
  nric_list5 = int(nric[5]) * 4
  nric_list6 = int(nric[6]) * 3
  nric_list7 = int(nric[7]) * 2
  
  nric_sum = nric_list1 + nric_list2 + nric_list3 + nric_list4 + nric_list5 + nric_list6 + nric_list7 
  
  if letter1 == "t" or letter1 == "g":
    nric_sum = nric_sum + 4
  
  check_digit = nric_sum % 11
  check_digit_valid = False
  s_or_t = "jzihgfedcba"
  f_or_g = "xwutrqpnmlk"
  if letter1 == "s" or letter1 == "t":
    if last_letter.lower() == s_or_t[check_digit]:
      check_digit_valid = True
  
  if letter1 == "f" or letter1 == "g":
    if last_letter.lower() == f_or_g[check_digit]:
      check_digit_valid = True

if valid1 == True and valid2 == True and valid3 == True and check_digit_valid == True:
  print("NRIC is valid.")

else:
  print("NRIC is invalid.")



          






  
  
