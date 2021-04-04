import ciphers
import graph


while True:
    usr_i = ciphers.get_args()
    if usr_i[0].lower() == 'quit':
        break
    if usr_i[0].lower() == 'app':
        graph.window.mainloop()
        continue
    print(ciphers.res(usr_i))
