# to build copy and paste
# docker build -f .\.devcontainer\app\base.Dockerfile --build-arg requirements_file=requirements_base.pip -t registry.gitlab.com/m.raesener/paper:base .
# docker push registry.gitlab.com/m.raesener/paper:base
FROM python:3.7-slim-buster 


ARG requirements_file

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

COPY ./.devcontainer/app/celery-init.d/celeryd /etc/init.d/celeryd
COPY ./.devcontainer/app/celery-init.d/celerybeat /etc/init.d/celerybeat
# copy and rename
COPY ./.devcontainer/app/celery-init.d/celeryd_config /etc/default/celeryd

## WAIT-TOOL FOR CHILD-CONTAINERS, USE IN DOCKER-COMPOSE
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.6.0/wait /wait

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    git \
    postgresql-server-dev-all \
    python3-psycopg2 \
    locales \
    gettext \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && locale-gen en_US.UTF-8 de_DE.UTF-8 \
    && useradd -r -s /bin/bash celery \
    && chmod +x /etc/init.d/celeryd /etc/init.d/celerybeat \
    && chmod 750 /etc/init.d/celeryd /etc/init.d/celerybeat \
    && chmod 640 /etc/default/celeryd \
    && chmod +x /wait

ENV DEBIAN_FRONTEND=

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

COPY ./ /app
COPY ./.devcontainer/app/idle.sh /idle.sh
COPY ./.devcontainer/app/startup_runserver.sh /startup_runserver.sh
COPY ./.devcontainer/app/startup_budgetapp.sh /startup_budgetapp.sh

WORKDIR /app/example
# RUN python3 -m pip install --disable-pip-version-check --no-cache-dir -r /app/example/requirements.txt \
#     && chmod +x /idle.sh /startup_runserver.sh /startup_budgetapp.sh
RUN python3 -m pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
RUN chmod +x /idle.sh /startup_runserver.sh /startup_budgetapp.sh
# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=