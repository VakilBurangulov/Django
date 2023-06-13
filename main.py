# import os
# current_path = os.path.abspath(__file__)
# parent_path = os.path.join(current_path, '..')
# def get_all_files(path):
#     for name in os.listdir(path):
#         new_path = os.path.join(path, name)
#         if os.path.isdir(new_path):
#             print('Папка', name)
#             get_all_files(new_path)
#         else:
#             print(' -', name)
# get_all_files(parent_path)







# from random import randint as rand
# file = open('file.txt', 'w')
# inter = rand(0,10)
# file.write(str(inter))
# if inter == 1 or inter == 2 or inter == 3 or inter == 4 or inter == 5:
#     file.write('\n' 'Плохо')
# else:
#     file.write('\n' 'Хорошо')
# file.close()





# import time
# start = time.time()
# for i in range(0, 1_000_001,):
#     print(i)
# end = time.time()
# print(end - start)












# def str(s):
#     for syn in set(s):
#         counter = 0
#         for sub_syn in s:
#             if syn == sub_syn:
#                 counter +=1
#
#         print(syn,counter)
# s = 'aaabc'
# str(s)




# def str(s):
#     sym_sym = {}
#     for sym in s:
#         sym_sym[sym] = sym_sym.get(sym, 0) + 1
#     print(sym_sym)
#
# str('aaabcabv')



