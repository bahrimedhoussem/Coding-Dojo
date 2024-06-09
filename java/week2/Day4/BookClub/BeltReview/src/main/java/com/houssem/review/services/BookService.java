package com.houssem.review.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.houssem.review.models.Book;
import com.houssem.review.repositories.BookRepository;

@Service
public class BookService {
	@Autowired
	private BookRepository bookRepository;
	
//	Create 
	public Book createBook(Book book) {
		return bookRepository.save(book);
	}
//  READ ALL
	public Book findBookById(Long id) {
		Optional<Book> optBook= bookRepository.findById(id);
		if(optBook.isPresent()) {
			return optBook.get();
		}
		else {
		return null;
		}
	}
//	READ ALL
	public List<Book> allBooks(){
		return bookRepository.findAll();
	}
	//edit
    public Book updateBook(Book book) {
        return bookRepository.save(book);
    }

    //delete
    public void deleteBook(Long id) {
    	bookRepository.deleteById(id);
    }
}