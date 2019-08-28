from kolora import Kolora

txt = Kolora()\
    ('"kolora teksto"', fg='Maroon', bg="#d7af00")\
    (' is Esperanto, meaning ', reset=True)\
    ('"colored text."', fg='Silver', bg="#005fff").text

print(txt)