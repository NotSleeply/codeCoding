package main

import (
	"bufio"
	"fmt"
	"net"
	"strings"
)

// 启动TCP服务端
func startTCPServer() {
	// 1. ResolveTCPAddr：解析地址（对应思维导图的 ResolveTCPAddr）
	tcpAddr, err := net.ResolveTCPAddr("tcp", "127.0.0.1:8888")
	if err != nil {
		fmt.Printf("解析地址失败：%v\n", err)
		return
	}

	// 2. ListenTCP：监听端口（对应思维导图的 ListenTCP）
	listener, err := net.ListenTCP("tcp", tcpAddr)
	if err != nil {
		fmt.Printf("监听端口失败：%v\n", err)
		return
	}
	defer listener.Close() // 程序退出时关闭监听
	fmt.Println("TCP服务端已启动，监听地址：127.0.0.1:8888")
	fmt.Println("等待客户端连接...")

	// 3. 循环AcceptTCP：接受客户端连接（对应思维导图的 AcceptTCP + 循环监听）
	for {
		conn, err := listener.AcceptTCP() // 阻塞等待新连接
		if err != nil {
			fmt.Printf("接受连接失败：%v\n", err)
			continue
		}
		// 并发处理每个客户端连接（避免阻塞其他连接）
		go handleClientConn(conn)
	}
}

// handleClientConn：处理单个客户端连接（对应思维导图的回调函数）
func handleClientConn(conn *net.TCPConn) {
	clientAddr := conn.RemoteAddr().String() // 获取客户端地址
	fmt.Printf("客户端 [%s] 已连接\n", clientAddr)
	defer func() {
		conn.Close() // 处理完后关闭连接
		fmt.Printf("客户端 [%s] 已断开连接\n", clientAddr)
	}()

	// 创建缓冲区读取客户端数据
	reader := bufio.NewReader(conn)
	for {
		// 4. ReadFromConn：读取客户端发送的数据（对应思维导图的 ReadFromConn）
		msg, err := reader.ReadString('\n') // 按换行符分割消息（解决粘包）
		if err != nil {
			// 处理EOF（客户端断开）或其他错误
			if err.Error() == "EOF" {
				return
			}
			fmt.Printf("读取客户端 [%s] 数据失败：%v\n", clientAddr, err)
			return
		}

		// 去除换行符，处理退出指令
		msg = strings.TrimSpace(msg)
		if msg == "exit" {
			return
		}

		// 5. WriteToConn：向客户端发送响应（对应思维导图的 WriteToConn）
		response := fmt.Sprintf("【服务端回声】%s\n", msg)
		_, err = conn.Write([]byte(response))
		if err != nil {
			fmt.Printf("向客户端 [%s] 发送数据失败：%v\n", clientAddr, err)
			return
		}
		fmt.Printf("客户端 [%s] 发送：%s → 响应：%s", clientAddr, msg, strings.TrimSpace(response))
	}
}
