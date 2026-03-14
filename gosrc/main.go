package main

import (
	"fmt"
	"net/http"
	"sync"

	"github.com/gorilla/websocket" // go get github.com/gorilla/websocket
)

// 全局连接管理
var clients = make(map[*websocket.Conn]bool)
var clientsMutex sync.Mutex
var clientNames = make(map[*websocket.Conn]string)

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
	// 新连接加入 clients
	clientsMutex.Lock()
	clients[conn] = true
	clientsMutex.Unlock()
	fmt.Println("客户端已连接！")
	defer func() {
		// 断开时移除
		clientsMutex.Lock()
		delete(clients, conn)
		name := clientNames[conn]
		for c := range clients {
			c.WriteMessage(websocket.TextMessage, []byte("系统: "+name+" 离开了聊天室"))
		}
		delete(clientNames, conn)
		clientsMutex.Unlock()
		conn.Close()
		fmt.Println(name + "已断开！")
	}()
	conn.WriteMessage(websocket.TextMessage, []byte("欢迎连接 WebSocket 服务器！你叫什么名字？"))
	_, msg, err := conn.ReadMessage()
	if err != nil {
		fmt.Println("连接失败：", err)
		return
	}
	name := string(msg)
	clientNames[conn] = name
	clientsMutex.Lock()
	for c := range clients {
		c.WriteMessage(websocket.TextMessage, []byte("系统: "+name+" 进入了聊天室"))
	}
	clientsMutex.Unlock()

	// 循环接收/广播消息
	for {
		msgType, msg, err := conn.ReadMessage()
		if err != nil {
			fmt.Println("读取消息失败：", err)
			break
		}
		sender := clientNames[conn]
		broadcastMsg := sender + ": " + string(msg)
		fmt.Printf(broadcastMsg)

		// 广播给所有连接
		clientsMutex.Lock()
		for c := range clients {
			c.WriteMessage(msgType, []byte(broadcastMsg))
		}
		clientsMutex.Unlock()
	}
}

func main() {
	http.HandleFunc("/ws", wsHandler)
	fmt.Println("WebSocket 服务启动：ws://127.0.0.1:8081/ws")
	http.ListenAndServe(":8081", nil)
	// 测试： wscat -c ws://127.0.0.1:8081/ws
}
