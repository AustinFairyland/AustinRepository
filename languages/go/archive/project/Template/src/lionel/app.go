package main

import (
	"fmt"
	"lionel/api"
)

func main() {
	fmt.Println("Hello Go!")
	fmt.Println(Add(1, 2))
	fmt.Println(api.GoogleUrl())
	fmt.Println(api.BaiduUrl())
	fmt.Printf("aa%s\n", "a")

	aa := "1213"
	bb := 1.22

	aaa := "asd"

	fmt.Println(aa)
	fmt.Println(bb)
	fmt.Println(aaa)

	const (
		v1 = iota + 1
		_
		v2
		v3
	)
	v4 := v1 + v2
	fmt.Println(v1, v2, v3, v4)

	//var v5 int
	//var v6 string
	//count, err := fmt.Scan(&v5, &v6)
	//if err != nil {
	//	fmt.Println(err)
	//} else {
	//	fmt.Println(count)
	//}

	for i := 0; i < 10; i++ {
		fmt.Println("aaa")
	}

}
