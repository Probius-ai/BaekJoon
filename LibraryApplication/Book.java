package LibraryApplication;

class Book implements Comparable<Book> {
    private String title;
    private String author;
    private int catalogueNumber;
    
    public Book(String title, String author, int catalogueNumber) {
        this.title = title;
        this.author = author;
        this.catalogueNumber = catalogueNumber;
    }
    
    // Getters
    public String getTitle() {
        return title;
    }
    
    public String getAuthor() {
        return author;
    }
    
    public int getCatalogueNumber() {
        return catalogueNumber;
    }
    
    // Setters
    public void setTitle(String title) {
        this.title = title;
    }
    
    public void setAuthor(String author) {
        this.author = author;
    }
    
    public void setCatalogueNumber(int catalogueNumber) {
        this.catalogueNumber = catalogueNumber;
    }
    
    @Override
    public String toString() {
        return "책 제목: " + title + ", 저자: " + author + ", 카탈로그 번호: " + catalogueNumber;
    }
    
    @Override
    public int compareTo(Book other) {
        return this.catalogueNumber - other.catalogueNumber;
    }
}
