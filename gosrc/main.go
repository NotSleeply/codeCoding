package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

// 中间件1
func middle() gin.HandlerFunc {
	return func(c *gin.Context) {
		fmt.Println("我在方法前，我是1")
		c.Next()
		fmt.Println("我在方法后，我是1")
	}
}

// 中间件2
func middle2() gin.HandlerFunc {
	return func(c *gin.Context) {
		fmt.Println("我在方法前，我是2")
		c.Next()
		fmt.Println("我在方法后，我是2")
	}
}

func main() {
	r := gin.Default()
	r.Use(middle()).Use(middle2())
	r.GET("/", func(c *gin.Context) {
		fmt.Println("我是方法内部")
		c.JSON(200, gin.H{"message": "Hello, World!"})
	})
	r.Run(":8080")
}

/*
输出结果：
我在方法前，我是1
我在方法前，我是2
我是方法内部
我在方法后，我是2
我在方法后，我是1
*/
