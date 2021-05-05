import ciphers
import graph

usr_i = ciphers.get_args()
if usr_i.cipher_type_or_app.lower() == 'app':
    graph.window.mainloop()
else:
    print(ciphers.res(usr_i))
