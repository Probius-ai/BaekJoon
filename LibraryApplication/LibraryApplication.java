package LibraryApplication;

// import java.time.LocalDate;
// import java.time.format.DateTimeFormatter;

public class LibraryApplication {
    private Library library;
    
    public LibraryApplication() {
        this.library = new Library();
    }
    
    // 도서 등록
    public boolean registerBook(String title, String author, int catalogueNumber) {
        Book newBook = new Book(title, author, catalogueNumber);
        return library.addBook(newBook);
    }
    
    // 대출자 등록
    public boolean registerBorrower(String name) {
        Borrower newBorrower = new Borrower(name);
        return library.addBorrower(newBorrower);
    }
    
    // 도서 대출
    public boolean borrowBook(Book book, Borrower borrower) {
        if (!library.getBooks().contains(book)) {
            return false;
        }
        
        // 추후 구현 예정: 날짜 관련 기능
        // 현재 날짜와 반납 예정일(2주 후) 설정
        // LocalDate now = LocalDate.now();
        // LocalDate dueDate = now.plusWeeks(2);
        // DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        
        // 추후 구현 예정: 날짜 정보는 임시로 null 처리
        Loan loan = new Loan(book, borrower, null, null);
        
        library.getLoans().add(loan);
        return true;
    }
    
    // 도서 반납
    public boolean returnBook(Book book) {
        for (Loan loan : library.getLoans()) {
            if (loan.getBook().equals(book) && !loan.isReturned()) {
                loan.setReturned(true);
                return true;
            }
        }
        return false;
    }
    
    // 대출 가능한 도서 목록 표시
    public void displayAvailableBooks() {
        for (Book book : library.getBooks()) {
            boolean isAvailable = true;
            for (Loan loan : library.getLoans()) {
                if (loan.getBook().equals(book) && !loan.isReturned()) {
                    isAvailable = false;
                    break;
                }
            }
            if (isAvailable) {
                System.out.println(book.toString());
            }
        }
    }
}
