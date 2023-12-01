sentence = input('Enter two words: ')
w1, w2 = sentence.split()
w2, w1 = w1, w2
print(f'!{w1} ! {w2}!')
print('!{} ! {}!'.format(w1, w2))
print('!%s ! %s!' % (w1, w2))
