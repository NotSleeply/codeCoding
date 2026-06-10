package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	args := os.Args[1:]

	// 如果没有传文件名，就从标准输入读取
	if len(args) == 0 {
		_, err := io.Copy(os.Stdout, os.Stdin)
		if err != nil {
			fmt.Fprintln(os.Stderr, "cat: read stdin:", err)
			os.Exit(1)
		}
		return
	}

	// 依次读取每个文件
	for _, filename := range args {
		err := printFile(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "cat: %s: %v\n", filename, err)
		}
	}
}

func printFile(filename string) error {
	file, err := os.Open(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = io.Copy(os.Stdout, file)
	return err
}
