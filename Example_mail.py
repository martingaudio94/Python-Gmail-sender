from mail_script import Ge_mail


nuevo=Ge_mail("Usuario@gmail.com","Contraseña")
msg="""Hola este es un apartado de comentario multilinea adaptado a string. con el
cual podemos enviar un mensaje a cualquier direccion de gmail. Posiblemente tengamos que activar el acceso
a aplicaciones inseguras o potencialmente indeseables  de google para poder utilizar este metodo.
Este es una reduccion significativa de codigo en una clase.
saludos
Martin Gaudio
"""
nuevo.sendm("direccion de correo@gmail.com",msg)
nuevo.quit()
