# Apache Airflow IDE

Apache Airflow IDE with Kubernetes Operator capabilities.

Kubernetes can be painful for any untrained specialist. This is preconfigured local
development environment with full power of Kubernetes Operator, but with whole
bootstrapment automations. This repository just provide easy way to use Apache Airflow
and real Kubernetes cluster on the local. Dont use it in production! Deployment ready
to use by analists with python stack which have no any understanding about kubernetes :)

## Meet the Airflow

This is easy to welcome and almost full description about capabilities provided
by Airflow. Recommended to read before any action.

https://airflow.apache.org/docs/stable/concepts.html

## IDE

This is local bootstrapment of Apache Airflow service! It have fully-featured service
with API, web UI, scheduler, database server (required for service components), small
kubernetes cluster and some helpers which automate cluster routines.

Components:

- Web interface. Doesnt handle AAA-features, mean have no authorization.

- Scheduler. Defaulted to spawn workloads to kubernetes.

- Kubernetes. Simplified version, but fully-featured. Based on kubernetes-in-docker
(see [kind project](https://kind.sigs.k8s.io/)) tehnique (but all wrapped by docker-in-docker).

- Docker registry. Helps to use local builded airflow image to kubernetes-accessible
place.

## How to use

All what you need in Makefile. And you must neet to install Makefile resolver:
`brew install make` on MacOS or `apt-get install make || yum install make`
on Linux. This is required single time only. Actualy, this works on Windows, but
this manual doesnt cover how to install `make` into Windows.

For start your system, run this:

```bash
make start
```

After few-five minutes your system is ready to use: see `http://127.0.0.1:8080`
for Apache Airflow web interface. If you need, you can look for kubernetes
web interface: `http://127.0.0.1:8008`.

You can rebuild images for add supported packages to Apache Airflow. Just add
required libs to `docker/airflow/requirements.txt` file and start building
process:

```bash
# add libs to docker/airflow/requirements.txt
make rebuild
make restart
```

For stop (and release used resources), run this:

```bash
make stop
```

## Links

Airflow Docs: https://airflow.apache.org/docs

Kubernetes API Reference: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.19/

## License

Licensed by MIT.
