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
	// 解析服务端地址
	tcpAddr, err := net.ResolveTCPAddr("tcp", ":8888")
	if err != nil {
		fmt.Printf("解析服务端地址失败：%v\n", err)
		return
	}

	// 连接服务端
	conn, err := net.DialTCP("tcp", nil, tcpAddr)
	if err != nil {
		fmt.Printf("连接服务端失败：%v\n", err)
		return
	}
	defer conn.Close()
	fmt.Println("输入任意文字发送（输入 exit 断开连接）：")

	// 读取用户输入
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Print("> ")
		input, err := reader.ReadString('\n')
		if err != nil {
			fmt.Printf("读取输入失败：%v\n", err)
			return
		}

		// 处理退出指令
		input = strings.TrimSpace(input)
		if input == "exit" {
			conn.Write([]byte("exit\n"))
			fmt.Println("已断开与服务端的连接")
			return
		}

		// 向服务端发送数据
		_, err = conn.Write([]byte(input + "\n"))
		if err != nil {
			fmt.Printf("发送数据失败：%v\n", err)
			return
		}

		// 读取服务端响应
		response, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			fmt.Printf("读取服务端响应失败：%v\n", err)
			return
		}

		fmt.Printf("服务端回复：%s", strings.TrimSpace(response))
	}
}

func main() {
	fmt.Println("启动客户端...")
	startTCPClient()
}
