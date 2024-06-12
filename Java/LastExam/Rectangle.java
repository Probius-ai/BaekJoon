package Java.LastExam;

public class Rectangle extends Shape implements CanDraw
{
    public Rectangle(String name, int width, int height){
        this.name = name;
        this.width = width;
        this.height = height;
    }
    
    private double familyBonus(){
        return (double)height * 10;
    }
    
    public double getArea(){
        return width*height + familyBonus();
    }
    
    public void draw(){
        System.out.println("<사각형: "+super.toString()+" 사각형, 면적: "+this.getArea()+">");
    }
}