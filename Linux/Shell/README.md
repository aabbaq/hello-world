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

---

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

---

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
- `ln -s SOURCE TARGET`：软链接（符号链接），类似于快捷方式或者指针的概念，但是依然是一种文件，颜色与普通文件也不一样；
  - **注意**，可以为文件夹创建链接，道理相同，但是目录下的文件并不是软连接文件，如果使用删除命令删除这些目录下文件，源文件也会消失

---

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