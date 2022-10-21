1 задача
а = ввод ()
b=[int(x) для x в a.split()]
печать (макс (б))

3 задача
а = целое (ввод ())
б=ввод()
b_list=[int(x) для x в b.split()]
b_list.sort()
с=0
b_sum=[]
для i в диапазоне (len (b_list)):
  если c+b_list[i]<a:
    c+=b_list[i]
    b_sum.append(b_list[i])
печать (b_sum)
