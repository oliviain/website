phpd得到的post数据无法显示：

1. 找到php.ini 配置文件,查找enable_post_data_reading变量，确保其打开状态= on，语句前面的分号要去掉(有分号的语句是注释语句)：

    

   ![img]()

    

   ![img](https://img-blog.csdn.net/20161121204139905)

2. index.html 和 welcome.php不在同一个目录下 
   action="welcome.php" 表示的是[相对路径](https://www.baidu.com/s?wd=%E7%9B%B8%E5%AF%B9%E8%B7%AF%E5%BE%84&tn=SE_PcZhidaonwhc_ngpagmjz&rsv_dl=gh_pc_zhidao) 

3. 直接双击打开的index.html不生效，必须要在php集成环境下打开index.html 也就是url为localhost/newbird.html![1554690292141](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554690292141.png)

   