package main

import (
	"embed"
	"fmt"
	"io/fs"
)

// 关键：用 //go:embed 指令把 static 目录下的所有文件嵌入程序
var embeddedFS embed.FS

func main() {
	// 用 fs 包的通用函数读取嵌入的文件
	data, err := fs.ReadFile(embeddedFS, "static/index.html")
	if err != nil {
		fmt.Println("读取嵌入文件失败：", err)
		return
	}
	fmt.Println("嵌入的 index.html 内容：", string(data))
}
