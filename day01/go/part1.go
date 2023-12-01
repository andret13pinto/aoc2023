package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func check(e error) {
	if e != nil {
		fmt.Println("Error:", e)
		os.Exit(1)
	}
}

func main() {
	file, err := os.Open("files/input.txt")
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	sum := 0
	for scanner.Scan() {
		curr := ""
		var line = scanner.Text()
		for _, char := range line {
			if !unicode.IsLetter(char) {
				curr += string(char)
				break
			}
		}
		var line_rune = []rune(line)
		for i := len(line_rune) - 1; i >= 0; i-- {
			char := line_rune[i]
			if !unicode.IsLetter(char) {
				curr += string(char)
				break
			}
		}
		curr_int, _ := strconv.Atoi(curr)
		sum += curr_int
	}
	fmt.Println(sum)
}
