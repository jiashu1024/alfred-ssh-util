#!/usr/bin/expect -f

spawn ssh #username@#ip
expect {
    "*assword:" {
        send "#password\r"
        interact
    }
    "yes/no" {
        send "yes\r"
        expect "*assword:"
        send "#password\r"
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
