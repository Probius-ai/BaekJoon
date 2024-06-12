package Java;

import Java.LastExam.Shape;

class Shape{
    String name; //멤버 변수
    Shape(String name){ //생성자
        this.name = name;
    }
    //멤버 메서드
    void draw(){
        System.out.println(name+"Shape"); //도형의 이름과 클래스명 출력
    }
    double area(){ //도형의 면적 값 반환
        return 0;
    }
}

class Circle extends Shape{ //Shape클래스 상속받아 구현
    double radius; //멤버 변수
    Circle(String name, double radius){ //생성자
        super(name);
        this.radius = radius;
    }
    //draw()메서드 오버라이딩
    @Override
    void draw(){
        System.out.println("객체의 "+name+"Circle"); //"객체의 name Circle"을 출력
    }
    //area()메서드 오버라이딩
    @Override
    double area(){
        return 3.14*radius*radius; //원의 면적을 계산하고 반환
    }
    //메서드 오버라이딩
    void setRadius(int radius){
        this.radius = radius; //정수형 반지름 지정
    }
    void setRadius(double radius){
        this.radius = radius; //실수형 반지름 지정
    }
}

class Rectangle extends Shape{
    //멤버 변수
    double width;
    double height;
    Rectangle(String name, double width, double height){
        super(name);
        this.width = width;
        this.height = height;
    }
    @Override
    void draw(){
        System.out.println("객체의 "+name+"Rectangle");
    }
    @Override
    double area(){
        return width*height;
    }
}       