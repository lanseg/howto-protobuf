import schema_pb2


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
