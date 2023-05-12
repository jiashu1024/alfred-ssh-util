#!/usr/bin/expect -f
# 从参数中获取ip、用户名和密码

set ip_username_password [lindex $argv 0]
set ip [lindex [split $ip_username_password " "] 0]
set username [lindex [split $ip_username_password " "] 1]
set password [lindex [split $ip_username_password " "] 2]

# 使用expect自动登录SSH
spawn ssh $username@$ip
expect {
    "*assword:" {
        send "$password\r"
        interact
    }
    "yes/no" {
        send "yes\r"
        expect "*assword:"
        send "$password\r"
        interact
    }
    timeout {
        puts "连接超时"
        exit 1
    }
    eof {
        exit 0
    }
}
