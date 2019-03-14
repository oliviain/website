# [如何用命令将本地项目夹上传到git](https://www.cnblogs.com/eedc/p/6168430.html) 		

  预备：

(首先进入到我们需要上传的项目文件夹里。建立本地仓库，我在整个项目工程的最外层使用git init进行初始化。)

```
cd C:/Project/C++/OpencvLearn
```

![在这里插入图片描述](https://img-blog.csdn.net/2018101121503242?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3h1X2Z1X3lvbmc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)



### 传项目文件夹

1、（先进入项目文件夹）通过命令 git init 把这个目录变成git可以管理的仓库

```
git init
```

2、

把文件添加到版本库中，使用命令 git add .添加到暂存区里面去，不要忘记后面的小数点“.”，意为添加文件夹下的所有文件，

如果是某个文件1.txt，先转入特定文件夹，比如C:/Project/C++/OpencvLearn/Chaper3，再添加

```
git add .
```

```
cd C:/Project/C++/OpencvLearn/Chaper3

git add  1.text
```

3、用命令 git commit告诉Git，把文件提交到仓库。引号内为提交说明

```
git commit -m 'first commit'
```

4、关联到远程库

```
git remote add origin 你的远程库地址
```

如：

```
git remote add origin https://github.com/githubusername/demo.git
```

> 如果出现fatal: remote origin already exists，那么
>
> git remote rm origin
>
> git remote add origin https://你的库址

5、获取远程库与本地同步合并（如果远程库不为空必须做这一步，否则后面的提交会失败）

```
git pull --rebase origin master
```

6、把本地库的内容推送到远程，使用 git push命令，实际上是把当前分支master推送到远程。执行此命令后会要求输入用户名、密码，验证通过后即开始上传。

```
git push -u origin master
```

*、状态查询命令

```
git status
```

