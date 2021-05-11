import ciphers
import graph

user_input = ciphers.get_args()
if user_input.cipher_type_or_app.lower() == 'app':
    graph.window.mainloop()
else:
    print(ciphers.res(user_input))
