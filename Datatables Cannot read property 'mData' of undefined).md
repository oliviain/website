[无法读取未定义的属性“mData”(Datatables: Cannot read property 'mData' of undefined)](http://www.it1352.com/545120.html)

FYI **dataTables** requires a well formed table. It must contain <thead> and <tbody> tags, otherwise it throws this error. Also check to make sure all your rows including header row have the same number of columns.  

The following will throw error (no <thead> and <tbody> tags)

![1555672684127](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1555672684127.png)

![1555672701240](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1555672701240.png)

dataTables必须包含< thead> 和< tbody> 标记，否则会抛出此错误。还要检查以确保所有的行，包括标题行具有相同的列数。

 以下将抛出错误（无< thead& 和< tbody> 标记）