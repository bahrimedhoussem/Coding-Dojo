package com.houssem.review.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.houssem.review.models.Book;

public interface BookRepository extends CrudRepository<Book, Long> {
	
	List<Book> findAll();
}
