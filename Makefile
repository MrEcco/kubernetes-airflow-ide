AIRFLOW_IMAGE=local/airflow:local
KIND_IMAGE=local/kind:local

AIRFLOW_IMAGE_TARBALL=airflow.image.tar
LOCAL_REGISTRY=10.254.254.253

build:
	@cd docker/airflow && make build
	@cd docker/kind && make build

rebuild: build localupload

localupload:
	@echo 'Transfering image to kubernetes accessible registry (local operation)'
	@docker save $(AIRFLOW_IMAGE) > $(AIRFLOW_IMAGE_TARBALL)
	@docker cp $(AIRFLOW_IMAGE_TARBALL) airflow-kubernetes:/$(AIRFLOW_IMAGE_TARBALL)
	@rm $(AIRFLOW_IMAGE_TARBALL)
	@docker-compose exec kubernetes docker load --input /$(AIRFLOW_IMAGE_TARBALL)
	@docker-compose exec kubernetes rm /$(AIRFLOW_IMAGE_TARBALL)
	@docker-compose exec kubernetes docker tag $(AIRFLOW_IMAGE) $(LOCAL_REGISTRY)/$(AIRFLOW_IMAGE)
	@docker-compose exec kubernetes docker push $(LOCAL_REGISTRY)/$(AIRFLOW_IMAGE)
	@docker-compose exec kubernetes docker rmi $(AIRFLOW_IMAGE) $(LOCAL_REGISTRY)/$(AIRFLOW_IMAGE)

restart:
	@echo 'This restarts only web and scheduler, not kubernetes'
	@docker-compose stop web scheduler
	@docker-compose rm -f web scheduler
	@docker-compose up --no-start
	@docker-compose start web scheduler

start:
	@docker-compose up --no-start
	@docker-compose start kubernetes
	@docker-compose start postgres
	@docker-compose start dns
	@docker-compose start registry
	@docker-compose start web
	@docker-compose exec kubernetes routines.py create
	@docker-compose start
	@make localupload

stop:
	@docker-compose down
