package main

import (
	"fmt"
	"log"
	"net/rpc"
)

// 客户端 需要定义一样的参数结构体
type Args struct {
	A, B int
}

func main() {
	// 1. 拨号连接 RPC 服务器
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("拨号失败:", err)
	}
	defer client.Close()

	// 2. 准备参数和接收结果的变量
	args := Args{A: 10, B: 20}
	var reply int

	// 3. 发起调用！ 第一个参数是 "结构体名.方法名"
	err = client.Call("MathService.Multiply", args, &reply)
	if err != nil {
		log.Fatal("调用失败:", err)
	}

	fmt.Printf("调用成功！结果是: %d\n", reply)
}
