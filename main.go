package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	// Println、Print、Printf 控制台
	fmt.Println("Hello, World!")
	fmt.Print("this is Print,so need add ?\n")
	fmt.Printf("this is Printf,so can %d\n", 123)

	// Sprint、Sprintf、Sprintln 字符串
	msg := fmt.Sprintf("id=%d name=%s", 10, "Tom")
	fmt.Println(msg)

	// Fprint、Fprintf、Fprintln 文件
	f, err := os.Create("out.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	fmt.Fprintln(f, "file log: ", 42)

}
