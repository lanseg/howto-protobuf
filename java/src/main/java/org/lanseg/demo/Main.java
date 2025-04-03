package org.lanseg.demo;

import java.io.FileOutputStream;

import org.lanseg.demo.proto.Schema;
import org.lanseg.demo.proto.Schema.Polygon;
import org.lanseg.demo.proto.Schema.Polygon.Point;

public class Main {
  public static void main(String[] args) throws Exception {
    var swissBounds = Schema.Area.newBuilder()
        .setAreaType(Schema.AreaType.PUBLIC)
        .addPolygons(
            Polygon.newBuilder()
                .setEpsg("2056")
                .addPoints(Point.newBuilder().setX(5.306396).setY(45.660127))
                .addPoints(Point.newBuilder().setX(10.843506).setY(45.660127))
                .addPoints(Point.newBuilder().setX(10.843506).setY(47.798397))
                .addPoints(Point.newBuilder().setX(5.306396).setY(47.798397))
                .addPoints(Point.newBuilder().setX(5.306396).setY(45.660127)))
        .build();

    System.out.printf("Message: %s\n", swissBounds);
    try (var out = new FileOutputStream("java_output.binarypb")) {
      swissBounds.writeTo(out);
    }
  }
}
