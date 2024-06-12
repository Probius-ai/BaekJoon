package Java.LastExam;

public class Triangle extends Shape implements CanDraw
{
    public Triangle(String name, int width){
        this.name = name;
        this.width = width;
        this.height = 10;
    }
    
    public double getArea(){
        return 0.5*width*height;
    }
    
    public void draw(){
        System.out.println("<삼각형: "+this.name+" 삼각형, 면적: "+this.getArea()+">");
    }
}
