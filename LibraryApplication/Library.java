package LibraryApplication;

import java.util.ArrayList;
import java.util.TreeSet;

public class Library {
    private TreeSet<Book> booksCollection;
    private ArrayList<Borrower> borrowersCollection;
    private ArrayList<Loan> loansCollection;
    
    public Library() { // 생성자
        booksCollection = new TreeSet<>();
        borrowersCollection = new ArrayList<>();
        loansCollection = new ArrayList<>();
    }
    
    // getter
    public TreeSet<Book> getBooks() { // 도서 목록 반환
        return booksCollection;
    }
    
    public ArrayList<Borrower> getBorrowers() { // 대출자 목록 반환
        return borrowersCollection;
    }
    
    public ArrayList<Loan> getLoans() { // 대출 목록 반환
        return loansCollection;
    }
    
    // 도서 관리 메소드
    public boolean addBook(Book book) { // 도서 추가
        return booksCollection.add(book);
    }
    
    public boolean removeBook(Book book) { // 도서 삭제
        return booksCollection.remove(book);
    }
    
    public Book findBookByCatalogueNumber(int catalogueNumber) { // 도서 찾기
        for (Book book : booksCollection) {
            if (book.getCatalogueNumber() == catalogueNumber) {
                return book;
            }
        }
        return null;
    }
    
    // 대출자 관리 메소드
    public boolean addBorrower(Borrower borrower) { // 대출자 추가
        return borrowersCollection.add(borrower);
    }
    
    public boolean removeBorrower(Borrower borrower) { // 대출자 삭제
        return borrowersCollection.remove(borrower);
    }
    
    public Borrower findBorrowerByName(String name) { // 대출자 찾기
        for (Borrower borrower : borrowersCollection) {
            if (borrower.getName().equals(name)) {
                return borrower;
            }
        }
        return null;
    }
    
    // 대출 관리 메소드
    public boolean addLoan(Loan loan) { // 대출 추가
        return loansCollection.add(loan);
    }
}
