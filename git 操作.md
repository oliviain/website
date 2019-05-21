git 操作

cd 到想保存的目录 或者mkdir 目录

```
$ ssh-keygen -t rsa -C"109946****@qq.com" //生成一对密匙，""里是用户邮箱；输入保存密匙的文件名，输入密码，没有为空
$ cat ~/.ssh/id_rsa.pub//复制密匙粘贴到华为云保存

```



```
git init//本地初始化了git仓库，放了一些文件进去并进行了add操作和commit提交操作

git clone  git@codehub.devcloud.huaweicloud.com:ldrcglxtjxsl00001/ss_calen//克隆华为云最新文件

git add -A//这里出现插曲，见下图，因为是在.ssh文件夹作为根目录初始化的git，出现了一些密码文件被替换的警告
```

![1554896891167](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554896891167.png)

```
git status //查看 add commit 之后的文件状态
git log //查看最近操作
git branch -r //查看现在远程连接的仓库

git remote add [remote-name such as origin] https://github.com/tielemao/TielemaoMarkdown
//关联远程仓库，并给远程仓库起名为origin
```

![1554897192490](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554897192490.png)

图片操作，想从本地仓库master     push 到远程仓库origin 的dev 分支，报错

```
git checkout -b dev //因为本地没有dev分支，所以远程报错不匹配，本地新建dev分支
```

![1554897433527](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554897433527.png)

再次push,报错

```
git log//查看最近一次操作，是修改文件ss_calendar
```

重新关联远程仓库，重命名远程仓库为huawei

```
git remote add huawei https://codehub.devcloud.huaweicloud.com/ldrcglxtjxsl00001/ss_calendar.git
//git remote add [remote name] [url]
```

```
git push huawei dev//push到华为的dev分支，报错
```

![1554897706485](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554897706485.png)

在开始的搜索栏，搜索凭据管理器，找到windows下的华为记录，删除

![1554897730585](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554897730585.png)

![1554897813587](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554897813587.png)

重新git push huawei dev

弹出输入用户名密码的框

要到华为的代码托管-设置我的http密码-查看用户名-设置密码-找到用户名密码-输入



![1554898109584](C:\Users\goodluck\AppData\Roaming\Typora\typora-user-images\1554898109584.png)

```
git pull huawei dev
//因为远程有更新，所以本地要先合并，用pull
```

 出现refusing to merge unrelated histories

```
git pull huawei dev --allow-unrelated-histories//允许，这里还弹出框，出现黄字，要输入允许merge的信息，更改黄字,esc键，：wq就可以
```

```
 git push -u huawei dev//-u参数代表，下次就可以直接git push 默认推送到 huawei仓库的dec分支，成功！！！
```

```
git checkout//检出，是我们的常用命令。最为常用的两种情形是创建分支和切换分支。
git checkout dev//切换dev分支
git checkout -b temp //创建temp分支
```

git查看操作

```
git log //查看所有commit后提交的信息
git log--pretty=oneline//只会显示版本号和提交时的备注信息
git reflog//查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）
```

 

**git的撤销操作**

-------------------

修改提交

```
$ git commit -m 'initial commit'
$ git add forgotten_file
$ git commit --amend //三条命令最终只是产生一个提交，第二个提交命令修正了第一个的提交内容。
//上次commit提交完没有作任何改动，直接运行git commit --amend 的话，相当于有机会重新编辑提交说明，但将要提交的文件快照和之前的一样。
```

撤销add暂存

```
git reset HEAD benchmarks.rb//撤销add的文件benchmarks.rb

```

撤销commit

```
git log//记录由上至下出现的第二个commit_id（d1a65e9ac9a7c4396206f0072b7fbc9138a26c1f）
git reset --hard commit_id//也就是git reset --hard d1a65e9ac9a7c4396206f0072b7fbc9138a26c1f 
```

回退版本

```
git reset --hard HEAD~1//版本回退到上一个
git reset --hard <6位数版本号>//版本回退到版本号
```

![img](https://img-blog.csdn.net/20180507202521793)

```
git checkout -b mydev origin/dev

Branch 'mydev' set up to track remote branch 'dev' from 'origin'.git
```

```
删除raindow文件夹及其下所有的文件

git rm raindow -r -f  
```

```
* (no branch, rebasing mydev)
操作了半天数据，发现自己在* (no branch, rebasing mydev)分支

第一种情况是我们还没离开*(no branch)，这个时候，我们可以执行git checkout -b mybranch命令，这个时候会创建新分支mybranch，并将*(no branch)里面的数据都checkout到mybranch分支上，然后我们再在mybranch上开发，最终合并到master上。

第二种情况就不乐观了，我们已经离开*(no branch)了，然后发现用git log都找不到之前的提交了，当然了，在*(no branch)上提交的，在别的分支上怎么找的到在它上面提交的数据呢。不过也许还有救，如果git还没有执行git gc，那么我们可以通过执行git reflog找到在*(no branch)上提交的数据，然后根据找到的commit的id来恢复该数据，这也是最后唯一的希望了，如果git已经执行了git gc或者你手贱自己执行了git gc，那么就真的不能在一起愉快的玩耍了。

```

