run_tests:
	docker-compose up -d
	python -m pytest test_files/ --disable-warnings || docker-compose down
	docker-compose down
