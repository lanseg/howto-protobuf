package main

import (
	"fmt"
	"os"

	"google.golang.org/protobuf/proto"

	dpb "demo/proto"
)

func main() {
	swissBounds := &dpb.Area{
		AreaType: dpb.AreaType_PUBLIC,
		Polygons: []*dpb.Polygon{
			{
				Points: []*dpb.Polygon_Point{
					{X: 5.306396, Y: 45.660127},
					{X: 10.843506, Y: 45.660127},
					{X: 10.843506, Y: 47.798397},
					{X: 5.306396, Y: 47.798397},
					{X: 5.306396, Y: 45.660127},
				},
				Epsg: "2056",
			},
		},
	}

	target := "go_output.binarypb"
	out, err := proto.Marshal(swissBounds)
	if err != nil {
		fmt.Println(err)
		return
	}
	os.WriteFile(target, out, 0777)
	fmt.Printf("Message %s, saved to: %s\n", swissBounds, target)
}
