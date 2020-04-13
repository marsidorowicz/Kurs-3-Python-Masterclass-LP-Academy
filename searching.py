shopping_list = ["mleko", "makaron", "cukier", "dżem", "ryż", "chleb"]

item_to_find = "cukier"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
print("Znaleziono na pozycji {}".format(found_at))