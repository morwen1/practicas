package main

import (
	"fmt"
	"math/rand"
	"time"
)

func intercambia(x int, y int) (int, int) {
	temp := 0
	temp = x
	x = y
	y = temp
	return x, y
}
func lista(x int) []int {
	arraytest := make([]int, 0, x*2)

	for i := 0; i < x; i++ {
		arraytest = append(arraytest, rand.Intn(x))

	}
	return arraytest
}

func burbuja(arraytest []int) {
	start := time.Now()

	for i := 0; i < len(arraytest)-1; i++ {

		for j := i + 1; j < len(arraytest); j++ {
			if arraytest[j] < arraytest[j-1] {

				arraytest[j], arraytest[j-1] = intercambia(arraytest[j], arraytest[j-1])

			}

		}
	}
	t := time.Now()
	fmt.Println(t.Sub(start))

}

func busqueda(array []int, item int) {
	for i := 0; i < len(array); i++ {
		if array[i] == item {
			fmt.Printf("encontrado")

		}
	}

}

func main() {
	arraytest := lista()

	busqueda(arraytest, arraytest[len(arraytest)-1])
	burbuja(arraytest)
}
