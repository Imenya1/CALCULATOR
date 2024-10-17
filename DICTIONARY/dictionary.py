print('ENTER LIST ONE VARIABLE''\n')
_list_1 = input('Enter elements for the first list with spacing from each variable'"\n").split()
_y = "yes"
_n = "no"
done = input('are you through? Enter yes of no''\n')

while done == _n:
    print('enter list again' '\n')
    _list_1 = input('Enter elements for the first list with spacing from each variable'"\n").split()
    input('are you through yes or no' '\n')
    if done == _y:
        break

print('ENTER LIST TWO VARIABLE')
_list_2 = input('Enter elements for the second list with spacing from each variable'"\n").split()
done = input('are you through? Enter yes of no''\n')
while done == _n:
    print('enter list again''\n')
    _list_2 = input('Enter elements for the second list with spacing from each variable'"\n").split()
    input('are you through yes or no''\n')
    if done == _y:
        break

if (len(_list_1) == len(_list_2)):
    _my_dict = dict(zip(_list_1,_list_2))
    print('KEY:',  _list_1)
    print('VALUE:', _list_2,'\n')
    print("My Dictionary:", _my_dict)
else:
    print("try again length of lists did not match")