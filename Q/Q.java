package Q;

public class Q {
    
}

interface Pencil {
    int getAmount();
    void setAmount(int amount);
    void write();
}

interface Pen {
    String getColor();
    void setColor(String color);
}

class SharpPencil implements Pencil{
    private int width;
    private int amount;
    public int getWidth() {
        return width;
    }
    public void setWidth(int width) {
        this.width = width;
    }
    @Override
    public int getAmount() {
        return amount;
    }
    @Override
    public void setAmount(int amount) {
        this.amount = amount;
    }
    @Override
    public void write() {
        System.out.println("0."+ width+"mm 샤프펜슬을 사용합니다.");
    }
}

class BallPen implements Pencil, Pen{
    private int amount;
    private String color;
    @Override
    public int getAmount() {
        return amount;
    }
    @Override
    public void setAmount(int amount) {
        this.amount = amount;
    }
    @Override
    public String getColor() {
        return color;
    }
    @Override
    public void setColor(String color) {
        this.color = color;
    }
    @Override
    public void write() {
        System.out.println(color + "색 볼펜을 사용합니다.");
    }
}

class FountainPen extends BallPen {
    public void refill(int n) {
        System.out.println("만년필에 잉크를 채웁니다.");
        setAmount(n);
    }
    @Override
    public void write() {
        System.out.println(getColor() + "색 만년필을 씁니다.");

    }
}

class Main{
    public static void main(String[] args) {
        SharpPencil sharpPencil = new SharpPencil();
        BallPen ballPen = new BallPen();
        FountainPen fountainPen = new FountainPen();
        
        sharpPencil.setWidth(5);
        sharpPencil.setAmount(100);
        ballPen.setColor("파랑");
        ballPen.setAmount(100);
        fountainPen.setColor("검정");
        fountainPen.setAmount(50);
        
        sharpPencil.write();
        System.out.println("남은 샤프심량: " + sharpPencil.getAmount());
        ballPen.write();
        System.out.println("남은 볼펜 량: " + ballPen.getAmount());
        System.out.println("볼펜의 색깔: " + ballPen.getColor());
        fountainPen.write();
        System.out.println("남은 만년필 량: " + fountainPen.getAmount());
        fountainPen.refill(100);
        System.out.println("남은 만년필 량: " + fountainPen.getAmount());
        System.out.println("만년필의 색깔: " + fountainPen.getColor());
    }
}