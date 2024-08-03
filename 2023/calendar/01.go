package calendar

var Day01Example = []string{
	"1abc2",
	"pqr3stu8vwx",
	"a1b2c3d4e5f",
	"treb7uchet",
}


func Day01(input []string) int {
    return 0
}

func sum(m uint64) uint64 {
	var x uint64
	for i := range make([]any, m+1) {
		x += uint64(i)
	}
	return x
}
