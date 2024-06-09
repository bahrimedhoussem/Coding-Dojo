package com.houssem.review.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

import com.houssem.review.models.User;

public interface UserRepository extends CrudRepository<User, Long> {
	
	Optional<User> findByEmail(String email);
}
