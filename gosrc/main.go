package main

import (
	"fmt"
	"net/http"

	"github.com/gorilla/websocket" // go get github.com/gorilla/websocket
)

// 定义 WebSocket 升级器：把 HTTP 连接升级成 WebSocket
var upgrader = websocket.Upgrader{
	// 允许跨域（测试用）
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

// 处理 WebSocket 连接
func wsHandler(w http.ResponseWriter, r *http.Request) {
	// 1. 把 HTTP 连接升级为 WebSocket 连接
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		fmt.Println("升级失败：", err)
		return
	}
	defer conn.Close()

	fmt.Println("客户端已连接！")

	// 2. 循环接收/发送消息（长连接）
	for {
		// 读取客户端消息
		msgType, msg, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("客户端断开连接")
			break
		}

		fmt.Printf("收到消息：%s\n", string(msg))

		// 服务端主动回消息
		reply := "服务端收到：" + string(msg)
		conn.WriteMessage(msgType, []byte(reply))
	}
}

func main() {
	http.HandleFunc("/ws", wsHandler)
	fmt.Println("WebSocket 服务启动：ws://127.0.0.1:8080/ws")
	http.ListenAndServe(":8080", nil)
}
