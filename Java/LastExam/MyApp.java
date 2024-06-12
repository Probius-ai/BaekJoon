package Java.LastExam;

public class MyApp {
    public static void main(String[] args){
        Shape [] list =
        {
          new Rectangle("아빠 사각형",6,8),
          new Rectangle("엄마 사각형",5,21),
          new Rectangle("나의 사각형",4,22),
          new Triangle("이모 삼각형", 7),
          new Triangle("친구 삼각형", 11)
        };
        
        double result = computeArea(list);
        
        System.out.println("총 면적: "+result);
    }
    
    public static double computeArea(Shape[] shapeArray){
        double totalArea = 0.0;
        for(Shape shape : shapeArray){
            ((CanDraw)shape).draw();
            totalArea += shape.getArea();
        }
        return totalArea;
    }
}
