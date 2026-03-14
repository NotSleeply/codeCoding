package main

import (
	"fmt"
	"net"
	"net/rpc"
)

// 1. 定义传入的参数结构体
type Args struct {
	A, B int
}

// 2. 定义服务结构体
type MathService struct{}

// 3. 实现服务方法（严格遵守 5 条规则）
func (m *MathService) Multiply(args Args, reply *int) error {
	*reply = args.A * args.B
	fmt.Printf("服务端执行：计算 %d * %d\n", args.A, args.B)
	return nil
}

func main() {
	// 实例化服务
	math := new(MathService)

	// 注册 RPC 服务，客户端就可以通过 "MathService.Multiply" 来调用了
	rpc.Register(math)

	// 启动 TCP 监听
	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		panic(err)
	}
	fmt.Println("RPC 服务端已启动，监听端口 1234...")

	// 接收请求并处理
	rpc.Accept(listener)
}
