# Shell 命令

分为内嵌命令和外部命令，可以用 `type` 判断。例子如下：

`type pwd`：`pwd is a shell builtin`

下面是常用的一些基本命令：

- `help [command]`： 查看一个简单版本的内置命令

- `man [command]`： 查看外部命令的使用手册

- `command --help`：查看外部命令的命令

常用快捷键：

- `ctrl` + `c`：终止进程
- `ctrl` + `l`：控制台翻页至最下方，效果是清屏
  - `clear`：该命令和上述快捷键效果一致
  - `reset`：重置shell，真正的清屏



## 目录命令

- `cd [directory]`：切换目录，change directory
  - `cd`：回到当前用户主目录
  - `cd -`：回到上一个目录，用于反复切换目录时使用

- `pwd`：显示当前所在的**绝对路径**，print working directory
  - `pwd -P`：显示实际的路径（消除软链接等的影响）

- `ls [directory]`：列出某目录的文件
  - `ls `：列出当前目录的文件
  - `ls -a`：列出目录下所有文件，包括隐藏的，用这个命令可以显示 `.` 与 `..` 两种特殊文件
  - `ls -l`：列出目录下文件的详细信息，每行一个文件的信息
  - `ll`：同上，命令的别名

- `mkdir DIRECTORY`：创建目录
  - `mkdir DIRECTORY1 DIRECTORY2`：创建多个目录（需要合法）
  - `mkdir -p DIRECTORY`：创建多层级的嵌套目录
- `rmdir DIRECTORY`：删除目录
  - `rmdir DIRECTORY1 DIRECTORY2`：删除多个目录（需要合法）
  - `rmdir -p DIRECTORY`：嵌套删除多层级的目录



## 文件命令

- `touch FILE`：创建一个文件，可以指定文件路径
- `vim FILE`：用Vim编辑器打开一个文件，如果文件不存在，可以通过这种方式创建
- `cp SOURCE Destination `：复制源文件（文件夹）至目标处
  - `\cp SOURCE Destination ` ：如果需要覆盖（overwrite）文件，则不需要确认，`\`：表示使用原生命令
  - `cp -r SOURCE Destination `：递归复制源文件夹的所有内容至目标处
- `rm FILE`：删除一个文件，可指定文件路径
  - `rm -r DIRECTORY`：递归删除目录的所有内容
  - `rm -f FILE`：强制删除
- `mv SOURCE Destination ` ：移动，剪切文件，用法同 `cp` ，可以重命名文件

### 浏览文件

- `cat FILE`：查看文件， concatenate
  - `cat -n FILE`：查看文件并显示行号
- `more FILE`：查看文件，更丰富的查看文件支持（上下翻页）
  - `b` , `f`：向后，向前翻页
  - `=`：显示当前所在行行号
  - `q`：退出查看
- `less FILE`：动态查看文件，一次加载一部分，很多操作和`Vim`以及 `more` 的操作差不多
  - `/SEARCH`：向下搜索字符串
  - `?SEARCH`：向上搜索字符串
  - `n`，`N`：搜索后跳转到下一个（上一个）匹配项
- `head FILE`：查看文件开头十行的内容
  - `head -n NUMBER FILE` ：查看文件开头任意行的内容
- `tail FILE`：查看文件结尾十行的内容
  - `tail -n NUMBER FILE `：查看文件结尾任意行的内容
  - **`tail -f FILE`**：跟踪文件结尾的内容，随着文件更新而变化（相当于监控文件内容的更新，常用于查看日志文件）；
    - `ctrl` + `s`：暂停跟踪
    - `ctrl` + `q`：继续跟踪

### 链接文件

- `ln -s SOURCE TARGET`：软链接（符号链接），类似于快捷方式或者指针的概念，但是依然是一种文件，颜色与普通文件也不一样；
  - **注意**，可以为文件夹创建链接，道理相同，但是目录下的文件并不是软连接文件，如果使用删除命令删除这些目录下文件，源文件也会消失



## 输出命令

- `echo [option] STRING`：输出内容至控制台，字符串部分可以使用双引号 `"STRING"` 包裹以支持更多输出方式（例如，多个空格）
  - `echo -e STRING`：使字符串内的转义 `\` 生效
  - `echo $ENVI...`：可以使用该命令查看系统环境变量的值

- `>`  & `>>`：**输出内容的重定向**，用于将左侧的内容输出至右侧指定的文件内；当右侧文件**不存在**时，会创建指定的文件
  - `>`：表示覆盖式的输出（write）
  - `>>`：表示追加式的输出（append）
  - 左侧的命令可以使任何显示内容的命令，例如 `ls`， `echo`，`cat` 等等
- `history [number]`：查看指定数量的历史命令记录
  - `!COMMAND_NUM`：执行对应的历史命令
  - `history -c`：清空历史命令记录



## 时间命令

-  `date`：输出一般时间信息，可以添加很多 `flag`做不同操作，具体使用 `--help` 查看
  - `date +%Y` | `date +%y` ：输出当前年份，输出当前年份后两位
  - `date +%m`：输出当前月份
  - `date +%d `：输出当前的天数
  - `date +s`：输出当前的时间戳
  - `date +%Y-%m-%d-%H:%M:%S`：显示具体的当地时间信息，包括时分秒
  - `date "+%Y-%m-%d %H:%M:%S"`：如果想使用空格作为分隔，需要使用双引号
  - `date -d "NUM day ago"`：显示若干天前的时间（day也可以是days）
  - `date -d "-NUM day ago"`：显示若干天之后的时间
  - `date -s DATE_STRING`：设置系统时间为指定时间

- `cal`：显示一个好看的日历
  - `cal -3`：显示相邻两个月以及当前月的好看日历
  - `cal -s`：以Sunday周日为每周第一天
  - `cal -m`：以Monday周1为每周第一天
  - `cal -y`：显示当前年份的一整年的日历
  - `cal YEAR`：显示指定年的日历



## 权限命令

- `useradd`：添加新的系统用户，必须有root权限
  - `useradd USERNAME`： 添加一个任意名字的用户
  - `useradd -d DIRECTORY USERNAME`：添加用户，并修改其默认目录的名称
  - `useradd -g GROUP_NAME USERNAME`：添加用户，并指定其用户组
- `userdel`：删除一个用户
  - `userdel USERNAME`：删除一个指定用户
- `passwd`：修改一个用户的密码
  - `passwd USERNAME`：修改指定用户的密码，接下来会输入新的密码
- `who am i`：查询最初登录的用户（最外层）信息
  - `whoami`：查询当前登录的用户信息
- `id`：查询用户状态
  - `id USERNAME`：查看指定用户的权限和信息
- `/etc/passwd`：可以查看系统中所有的用户（敏感信息）的文件，在web security课上的常客了
- `su`：切换用户
  - `su USERNAME`：切换到指定用户，普通用户需要输入密码；root用户可以不需要
  - `exit`：如果在 `root`状态下嵌套切换到其他用户了，可以直接 `exit` 结束其他用户的会话，回到 `root` 用户
- `sudo`：在普通用户状态时，临时获得 `root` 的权限，需要输入普通用户的密码；（并且需要事先设置好配置文件 `/etc/sudoers`）

### 用户组相关

- `groupadd`：添加一个用户组
  - `groupadd GROUP_NAME`：添加指定名字的用户组
- `groupdel`：删除一个用户组
  - `groupdel GROUP_NAME`：删除指定的用户组
- `usermod`：更改用户的信息
  - `usermode -g GROUP_NAME USERNAME`：将用户移动至指定组内
- `groupmod`：更改用户组的信息
  - `groupmod -n NEW_NAME OLD_NAME`：更改一个组的名字

- `/etc/group`：可以查看系统中所有的组信息

### 文件属性

使用 `ll` 可以查看，第一串字符含义如下

```bash
drwxr-xr-x 2 root root  53 Nov 13 13:21 c
-rw-r--r-- 1 root root   0 Nov 25 12:23 e
drwxrwxrwx 5 root root 115 Mar  6  2022 k
drwxr-xr-x 3 root root  26 Mar  6  2022 kp
```

- 第 `0` 位，文件类型：

  - `d`：代表为目录

  - `c`：字符设备文件

  - `l`：链接文件

  - `-`：普通文件

- 第 `1~3` 位，属主（文件创建者）权限：对于创建者，一般为 `rwx`，表示可读，可写，可执行；

- 第 `4~6` 位，属组（文件属于的用户组）权限：对于组内成员，一般为 `r-x`，表示可读，不可写，可执行；

- 第 `7~9` 位，其他用户（不属于上述两种）权限：对于其他成员，一般为 `r-x`，表示可读，不可写，可执行；

第二个字符串数字表示该**文件**的**硬链接**数量 | 如果是**目录**，则为**子目录**数量

第三与第四分别指的是其**属主**以及**属组**，在上述例子中，都属于 `root` 用户以及 `root` 组

---

`rwx` 在不同情况下的解释：

- 普通文件
  - `r`：表示可读，可查看与浏览该文件
  - `w`：表示可以修改文件，但不一定可删除该文件
  - `x`：表示可以被系统执行该文件
- 目录文件
  - `r`：可以访问该目录，可以使用命令查看目录内容（如 `ll`）
  - `w`：可以修改目录，可以创建或删除目录内的内容，也可以重命名该目录
  - `x`：可以进入该目录（如 `cd`）

---

- `chmod`：变更权限
  - `chmod [ugoa] [+-=] [rwx] FILE_NAME`：通过字符形式来设置权限
    - `chmod g+w rua`：为文件 `rua` 增加属组的写权限
  - `chmod NUM FILE_NAME`：使用二进制编码设置权限
    - `chmod 774 rua`：对于 `rua` 文件，给予属组与属主所有权限，给予其他用户可读权限
    - `chmod -R NUM DIRECTORY`：递归赋予目录以及其子文件属性
- `chown`：变更所有者（属主）
  - `chown NEW_USER FILE_NAME`：变更指定文件的属主为指定用户
  - `chown -R NEW_USER DIRECTORY`：变更指定目录以及以下所有的文件属主为指定用户
- `chgrp`：变更所有组（属组）
  - `chgrp NEW_GROUP FILE_NAME`：变更指定文件的属组为指定用户组
  - `chgrp -R NEW_GROUP DIRECTORY`：变更指定目录以及以下所有的文件属主为指定用户组



## 搜索命令

- `find [range] [option] SEARCH` ：查找文件
  - `find -name NAME`：查找带有指定名称的文件
    - `find -name "*.css"`：查找后缀为 `.css` 的文件
  - `find -size SIZE`：查找指定文件大小的文件
    - `find -size +114M`：查找114MB大小以上的文件
- `locate SEARCH`：在内置文件系统数据库中查找文件（无序遍历整个文件系统）
  - `updatedb`：`locate` 可能保证不了一致性，因此首先写入数据库，再查找

- `which COMMAND`：查找指定命令的存储位置
- `whereis COMMAND`：查找指定命令的存储位置

---

