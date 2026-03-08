package main

import (
	"fmt"
	"reflect"
)

type Calculator struct{}

func (c Calculator) Add(a, b int) int {
	return a + b
}

func main() {
	a := 10
	b := 20

	calc := Calculator{}
	v := reflect.ValueOf(calc)

	// 获取名为 "Add" 的方法
	method := v.MethodByName("Add")

	// 准备传入的参数（必须是 reflect.Value 的切片）
	args := []reflect.Value{
		reflect.ValueOf(a),
		reflect.ValueOf(b),
	}

	// 动态调用
	results := method.Call(args)

	// 获取返回值
	fmt.Printf("动态调用 Add 结果: %d\n", results[0].Int()) // 输出: 30
}
