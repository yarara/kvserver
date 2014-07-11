kvserver
========

key-value server

Запустить сервер и клиент. В клиенте для добавления значения нужно набрать команду:\n
add key value (Пример: add 1 hello)
Для удаления значения:
read key  (Пример: read 1)
Для вывода значения:
del key  (Пример: del 1)
Для вывода всех значений:
list 
Для завершения работы клиента:
exit
Для отправки команды/нескольких команд на сервер:
send

Пример работы:
>add 1 hello
>send
added 1 -> hello
>add 2 hello world
>send
added 2 -> hello
>add 3 hello_world
>read 1
>send
added 3 -> hello_world
1 -> hello
>list 
>del 2
>list
>send
1 -> hello
2 -> hello
3 -> hello_world
deleted 2
1 -> hello
3 -> hello_world
