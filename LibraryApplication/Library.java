package LibraryApplication;

import java.util.ArrayList;
import java.util.TreeSet;

public class Library {
    private TreeSet<Book> books;
    private ArrayList<Borrower> borrowers;
    private ArrayList<Loan> loans;
    
    public Library() {
        books = new TreeSet<>();
        borrowers = new ArrayList<>();
        loans = new ArrayList<>();
    }
    
    public TreeSet<Book> getBooks() {
        return books;
    }
    
    public ArrayList<Borrower> getBorrowers() {
        return borrowers;
    }
    
    public ArrayList<Loan> getLoans() {
        return loans;
    }
    
    // 도서 관리 메소드
    public boolean addBook(Book book) {
        return books.add(book);
    }
    
    public boolean removeBook(Book book) {
        return books.remove(book);
    }
    
    public Book findBookByCatalogueNumber(int catalogueNumber) {
        for (Book book : books) {
            if (book.getCatalogueNumber() == catalogueNumber) {
                return book;
            }
        }
        return null;
    }
    
    // 대출자 관리 메소드
    public boolean addBorrower(Borrower borrower) {
        return borrowers.add(borrower);
    }
    
    public boolean removeBorrower(Borrower borrower) {
        return borrowers.remove(borrower);
    }
    
    public Borrower findBorrowerByName(String name) {
        for (Borrower borrower : borrowers) {
            if (borrower.getName().equals(name)) {
                return borrower;
            }
        }
        return null;
    }
    
    // 대출 관리 메소드
    public boolean addLoan(Loan loan) {
        return loans.add(loan);
    }
}
