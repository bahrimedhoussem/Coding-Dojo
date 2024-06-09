package com.alaa.springfullcrud.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.alaa.springfullcrud.models.Book;

public interface BookRepository extends CrudRepository<Book, Long> {

	// Find ALL BOOKS
	List<Book> findAll();
}
