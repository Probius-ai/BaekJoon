package LibraryApplication;

public class Borrower {
    private String name;
    
    // 생성자
    public Borrower(String name) {
        this.name = name;
    }
    
    // getter와 setter
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
}
