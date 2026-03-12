package main

import (
	"bufio"
	"fmt"
	"net"
	"strings"
)

// 启动TCP服务端
func startTCPServer() {
	// 解析地址
	tcpAddr, err := net.ResolveTCPAddr("tcp", ":8888")
	if err != nil {
		fmt.Printf("解析地址失败：%v\n", err)
		return
	}

	// 监听端口
	listener, err := net.ListenTCP("tcp", tcpAddr)
	if err != nil {
		fmt.Printf("监听端口失败：%v\n", err)
		return
	}
	defer listener.Close()
	fmt.Println("等待客户端连接...")

	// 接受客户端连接
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

// 处理单个客户端连接
func handleClientConn(conn *net.TCPConn) {
	clientAddr := conn.RemoteAddr().String() // 获取客户端地址
	fmt.Printf("客户端 [%s] 已连接\n", clientAddr)
	defer func() {
		conn.Close()
		fmt.Printf("客户端 [%s] 已断开连接\n", clientAddr)
	}()

	// 创建缓冲区读取客户端数据
	reader := bufio.NewReader(conn)
	for {
		// 读取客户端发送的数据
		msg, err := reader.ReadString('\n')
		if err != nil {
			if err.Error() == "EOF" {
				return
			}
			fmt.Printf("读取客户端 [%s] 数据失败：%v\n", clientAddr, err)
			return
		}

		msg = strings.TrimSpace(msg)
		if msg == "exit" {
			return
		}

		// special command: return client address
		var response string
		if msg == "ip" {
			response = clientAddr + "\n"
		} else {
			// 普通回声响应
			response = fmt.Sprintf("【服务端回声】%s\n", msg)
		}

		_, err = conn.Write([]byte(response))
		if err != nil {
			fmt.Printf("向客户端 [%s] 发送数据失败：%v\n", clientAddr, err)
			return
		}
		fmt.Printf("客户端 [%s] 发送：%s → 响应：%s", clientAddr, msg, strings.TrimSpace(response))
	}
}

func main() {
	fmt.Println("启动服务...")
	startTCPServer()
}
