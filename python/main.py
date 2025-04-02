import schema_pb2

# swissBounds := &dpb.Area{
# 	AreaType: dpb.AreaType_PUBLIC,
# 	Polygons: []*dpb.Polygon{
# 		{
# 			Points: []*dpb.Polygon_Point{
# 				{X: 5.306396, Y: 45.660127},
# 				{X: 10.843506, Y: 45.660127},
# 				{X: 10.843506, Y: 47.798397},
# 				{X: 5.306396, Y: 47.798397},
# 				{X: 5.306396, Y: 45.660127},
# 			},
# 			Epsg: "2056",
# 		},
# 	},
# }

if __name__ == "__main__":
    swissBounds = schema_pb2.Area(
        areaType=schema_pb2.PUBLIC,
        polygons=[
            schema_pb2.Polygon(
                points=[
                    schema_pb2.Polygon.Point(x=0, y=0),
                    schema_pb2.Polygon.Point(x=1, y=1),
                ],
                epsg="2056",
            ),
        ],
    )
    print(swissBounds)
