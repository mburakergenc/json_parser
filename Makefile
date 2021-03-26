run-db:
	docker run --name retriever_postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=retriever -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres