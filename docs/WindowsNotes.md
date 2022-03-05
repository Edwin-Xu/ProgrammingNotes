# Windows Notes

## 命令行

### 添加右键管理员命令行

func.reg:

```sql
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\Directory\shell\runas]

[HKEY_CLASSES_ROOT\Directory\shell\runas]
@="Open cmd here as Admin"
"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\shell\runas\command]
@="cmd.exe /s /k pushd \"%V\""

[-HKEY_CLASSES_ROOT\Directory\Background\shell\runas]

[HKEY_CLASSES_ROOT\Directory\Background\shell\runas]
@="Open cmd here as Admin"
"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Directory\Background\shell\runas\command]
@="cmd.exe /s /k pushd \"%V\""

[-HKEY_CLASSES_ROOT\Drive\shell\runas]

[HKEY_CLASSES_ROOT\Drive\shell\runas]
@="Open cmd here as Admin"
"HasLUAShield"=""

[HKEY_CLASSES_ROOT\Drive\shell\runas\command]
@="cmd.exe /s /k pushd \"%V\""
```



### 查看端口占用进程并杀死

查找所有运行的端口：

> netstat -ano

查看对应端口占用：

> netstat -ano | findstr "8080"
>
>   TCP    0.0.0.0:8080           0.0.0.0:0              LISTENING       42620
>   TCP    2.0.0.1:49917          10.5.76.243:8080       ESTABLISHED     42620
>   TCP    2.0.0.1:50599          10.5.89.183:8080       ESTABLISHED     42620

最后一项即pid

查询pid对应的任务：

> tasklist | findstr "42620"

杀死进程

>  taskkil /T /F /PID 42620

