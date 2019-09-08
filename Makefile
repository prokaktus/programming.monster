.PHONY: deploy dump

dump:
	ansible-playbook deploy/ansible/play/dump_db.yml -i deploy/ansible/hosts

deploy:
	ansible-playbook deploy/ansible/play/deploy.yml -i deploy/ansible/hosts
