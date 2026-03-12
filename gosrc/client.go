package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
	"strings"
)

// 启动TCP客户端
func startTCPClient() {
	// 1. ResolveTCPAddr：解析服务端地址
	tcpAddr, err := net.ResolveTCPAddr("tcp", "127.0.0.1:8888")
	if err != nil {
		fmt.Printf("解析服务端地址失败：%v\n", err)
		return
	}

	// 2. DialTCP：连接服务端（对应思维导图的 DialTCP）
	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		fmt.Printf("连接服务端失败：%v\n", err)
		fmt.Println("请先启动服务端！")
		return
	}
	defer conn.Close() // 退出时关闭连接
	fmt.Println("成功连接到 TCP 服务端：127.0.0.1:8888")
	fmt.Println("输入任意文字发送（输入 exit 断开连接）：")

	// 读取用户输入
	reader := bufio.NewReader(os.Stdin)
	for {
		// 读取控制台输入
		fmt.Print("> ")
		input, err := reader.ReadString('\n')
		if err != nil {
			fmt.Printf("读取输入失败：%v\n", err)
			return
		}

		// 处理退出指令
		input = strings.TrimSpace(input)
		if input == "exit" {
			// 发送exit给服务端，然后断开
			conn.Write([]byte("exit\n"))
			fmt.Println("已断开与服务端的连接")
			return
		}

		// 3. WriteToConn：向服务端发送数据
		_, err = conn.Write([]byte(input + "\n")) // 加换行符（和服务端约定的分隔符）
		if err != nil {
			fmt.Printf("发送数据失败：%v\n", err)
			return
		}

		// 4. ReadFromConn：读取服务端响应
		response, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			fmt.Printf("读取服务端响应失败：%v\n", err)
			return
		}

		// 打印服务端响应
		fmt.Printf("服务端回复：%s", strings.TrimSpace(response))
	}
}
