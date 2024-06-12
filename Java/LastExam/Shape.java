package Java.LastExam;

public abstract class Shape
{
    public String name;
    protected int width;
    public int height;
    
    public String toString(){
        return name;
    }
    
    public abstract double getArea();
}
