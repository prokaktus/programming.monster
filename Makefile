.PHONY: deploy dump deploy_config

dump:
	ansible-playbook deploy/ansible/play/dump_db.yml -i deploy/ansible/hosts

deploy:
	ansible-playbook deploy/ansible/play/deploy.yml -i deploy/ansible/hosts

deploy_config:
	ansible-playbook deploy/ansible/play/deploy_config.yml -i deploy/ansible/hosts
